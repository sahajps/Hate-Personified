import pandas as pd
import numpy as np
import torch
import torch.nn as nn
from datasets import load_dataset
from tqdm import tqdm
from transformers import T5Tokenizer, T5ForConditionalGeneration

tokenizer = T5Tokenizer.from_pretrained("google/flan-t5-xxl")
model = T5ForConditionalGeneration.from_pretrained("google/flan-t5-xxl", torch_dtype=torch.float16)
model = model.to('cuda')

files = [] #'LIST of paths of different prompt files'

for f in tqdm(files):
    df = pd.read_excel(f+'.xlsx')
    for t in tqdm(np.linspace(0.1, 1.9, num=100)):
        anno = []
        bs = 128
        for i in range(0,df.shape[0],bs):
            prompt = []
            for j in range(i,i+bs):
                try:
                    prompt.append(df.iloc[j].text)
                except:
                    break
            
            inputs = tokenizer(prompt, padding=True, return_tensors="pt").to('cuda')
            with torch.no_grad():
                outputs = model.generate(**inputs, do_sample=True, temperature=t, max_new_tokens=5)
            anno += tokenizer.batch_decode(outputs, skip_special_tokens=True)

            del inputs
            torch.cuda.empty_cache()

        df["Temp: "+str(t)] = anno
        
    df.to_excel(f+'.xlsx', index=False)

del model
torch.cuda.empty_cache()