# xai-dashboard

Code is structured into frontend code (VUE JS) and Backend Code (Python with Flask). 


### Start Frontend  

Install VUE JS with NPM first. Then run:

```
cd frontend/

npm run serve
```

### Start Backend 

Deploy Python environment installing the packages in requirements.txt. Then run:

``` 
python main_backend.py
```


## Workflows:

### 1) Initialization & Training & Inference:
- Clean data folders (not 01_data_raw)
- Split the data into training and testing, prepare data (02_data_preprocessed) 
- Some small data preparation
- Training of different models on the training set (04_trained_models)
- Inference

### 2) Global Explanation
- main_global: plot and create data for the global explanations, save in 03_outputs
- Show data and plots
    - Shapley Values (Global)


### 3) Local Explanations & Inference
- main_local: plot and create data for the local explanations, save in 03_outputs
    - Shapley Values (Local)
    - Lime 

