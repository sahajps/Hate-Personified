import os
import pandas as pd
import torch
import torch.nn as nn
from datasets import load_dataset
from tqdm import tqdm
import time
from timeout_decorator import timeout
import openai
openai.api_key = "Your OpenAI API"

@timeout(15)
def chatGPT(prompt):
    res = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                    {"role": "system", "content": prompt},
                    ],
                    temperature=0,
                    max_tokens=5)

    return res

###########################################################
f = 'Enter file path from respective */ChatGPT/ folder'

df = pd.read_excel(f)

"""The below code should be commented only when reproducing the results
This was written to take the dataset (prompt injected) from respective files of open-source models
So this drops the aditional outputs of open-source models and keep only the text, gold labels & ChatGPT's output"""
# df = df[df.columns[:8]] # choose this based on the dataset (CREHate)
# df = df[df.columns[:2]] # choose this based on the dataset (HateXplain)
# df = df.sample(n=500, random_state=42).reset_index(drop=True)

dft = df.text

anno = []
for i in tqdm(range(df.shape[0])):
    # if file is in */ChatGPT/ folder (prompt in English language)
    prompt = dft.iloc[i]+" Answer in one word only."
    # if file is in ML/ChatGPT_SL/ folder (prompt in same language) beacause in case of same language
    # "Answer in one word only." is already in the translated prompt
    prompt = dft.iloc[i]

    try:
        response = chatGPT(prompt)
    except:
        print('Sleep')
        time.sleep(30)
        print('& here we go...')
        try:
            response = chatGPT(prompt)
        except:
            print('Sleep')
            time.sleep(30)
            print('& here we go...')
            response = chatGPT(prompt)
                    
    anno += [response["choices"][0]["message"]["content"].lower()]


df["cgpt"] = anno
df.to_excel(f, index=False)