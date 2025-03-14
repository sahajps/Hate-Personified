import pandas as pd
import torch
import torch.nn as nn
from datasets import load_dataset
from tqdm import tqdm
from transformers import T5Tokenizer, T5ForConditionalGeneration, AutoTokenizer, AutoModelForCausalLM

model_names = ['flan-t5-small', 'flan-t5-base', 'flan-t5-large', 'flan-t5-xl', 'flan-t5-xxl', 'mistralai/Mistral-7B-Instruct-v0.1', 'HuggingFaceH4/zephyr-7b-alpha', 'meta-llama/Meta-Llama-3-8B-Instruct', 'ai4bharat/Airavata', 'malhajar/Mistral-7B-v0.1-arabic']

model_names = [] #'LIST of models names (can be choosen from the list above)'
files = [] #'LIST of paths of different prompt files'

for m in model_names:
    if(m[0]=='f'):
        tokenizer = T5Tokenizer.from_pretrained("google/"+m)
        model = T5ForConditionalGeneration.from_pretrained("google/"+m, torch_dtype=torch.float16)
    else:
        tokenizer = AutoTokenizer.from_pretrained(m, padding_side='left')
        model = AutoModelForCausalLM.from_pretrained(m, torch_dtype=torch.float16)
        tokenizer.pad_token = tokenizer.eos_token

    model = model.to('cuda')
    print(m," loaded for inference")
    for f in files:
        df = pd.read_excel(f+'.xlsx')
        #df = df[df.columns[:2]] # For RQ_NC, ML
        #df = df[df.columns[:8]] # For RQ_GC, RQ_PC
        
        anno = []
        bs = 8
        for i in tqdm(range(0,df.shape[0],bs)):
            prompt = []
            for j in range(i,i+bs):
                try:
                    if(m in ['mistralai/Mistral-7B-Instruct-v0.1', 'HuggingFaceH4/zephyr-7b-alpha', 'meta-llama/Meta-Llama-3-8B-Instruct']):
                        # only for mistral, zephyr, llama3
                        prompt.append(df.text.iloc[j]+" Answer in one word only.")
                    else:
                        prompt.append(df.text.iloc[j])        
                except:
                    break
            
            inputs = tokenizer(prompt, padding=True, return_tensors="pt").to('cuda')
            with torch.no_grad():
                outputs = model.generate(**inputs, max_new_tokens=5)
            outputs = tokenizer.batch_decode(outputs, skip_special_tokens=True)

            # Except FlanT5 models: outputs= input + new generated tokens
            if(m[0]!='f'):
                for j in range(len(outputs)):
                    outputs[j] = outputs[j][len(prompt[j]):]
            
            anno += outputs
            del inputs, outputs
            torch.cuda.empty_cache()

        df[m] = anno
        df.to_excel(f+'.xlsx', index=False)

    del model
    torch.cuda.empty_cache()