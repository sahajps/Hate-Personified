<h1 align="center">Hate Personified: Investigating the role of LLMs in content moderation</h1>

For subjective tasks such as hate detection, where people of different socio-cultural backgrounds perceive hate differently, the Large Language Model's (LLM) ability to represent diverse groups is unclear. By including additional context in prompts, we comprehensively analyze LLM's sensitivity to geographical priming, persona attributes, and numerical information to assess how well the needs of various groups are reflected. Our findings on two LLMs, five languages, and six datasets reveal that mimicking persona-based attributes leads to annotation variability. Meanwhile, incorporating geographical signals leads to better regional alignment. We also find that the LLMs are sensitive to numerical anchors, indicating the ability to leverage community-based flagging efforts and exposure to adversaries. Our work provides preliminary guidelines and highlights the nuances of applying LLMs in culturally sensitive cases.

# Repo Overview
- **Original_Datasets**
    - `CREHate`(En), `HateXplain`(En), `MLMA`(Ar, Fr) & `HASOC`(De, Hi) dataset files
    - `Dataset_stats.ipynb`

- **Graphs**
    - GC, NC & ML 
    - `GC.ipynb`, `NC.ipynb` & `ML.ipynb`

- **RQ1_GC: Geographical Cues**
    - Analysis
        - `All_models_performance.ipynb`
        - `PerformanceOS_LLMs.csv`
        - `PerformanceChatGPT.csv`
    - OS_LLMs
    - ChatGPT
- **RQ2_PC: Persona Cues**
    - Analysis
        - `All_models_performance.ipynb`
        - `PerformanceOS_LLMs_HA.csv`
        - `PerformanceOS_LLMs_N.csv`
        - `PerformanceChatGPT_HA.csv`
        - `PerformanceChatGPT_N.csv`
    - OS_LLMs
    - ChatGPT
- **RQ3_NC: Numerical Cues**
    - Analysis
        - `All_models_performance.ipynb`
        - `PerformanceOS_LLMs_H.csv`
        - `PerformanceOS_LLMs_N.csv`
        - `PerformanceChatGPT_H.csv`
        - `PerformanceChatGPT_N.csv`
    - OS_LLMs
    - ChatGPT
    - Temp_Variations
- **RQ_ML: Multi-lingual**
    - Analysis
        - `All_models_performance.ipynb`
        - `All_models_performance_SL.ipynb`
        - `All_models_performance_LocalLLMs.ipynb`
        - `Performance.csv`
        - `Performance_SL.csv`
        - `Performance_LocalLLMs.csv`
    - OS_LLMs
    - ChatGPT

- `Prompt_Files_Guide.xlsx`
- `Prompt_files_generator.ipynb`
- `English_to_same_language_convertor.ipynb`
- `Inference_OS_LLMs.py`
- `Inference_ChatGPT.py`
- `Inference_temp_variation.py`
- `requirements.txt`
- `README.md`


# Cite
```sh
To be appear in EMNLP (main) conference in Miami, USA (Dec 2024)
```