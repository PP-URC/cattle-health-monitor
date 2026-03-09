import pandas as pd
import numpy as np

n_healthy = 100
n_mastitis = n_healthy // 20
n_anaplasmosis = n_healthy // 20

metrics = {
    "healthy": {
        "activity": (0.7, 0.1), 
        "temp": (38.5, 0.2), 
        "milk_yield": (26, 3)
    },
    "mastitis":{
        "activity": (0.45, 0.1), 
        "temp": (39, 0.3), 
        "milk_yield": (18, 3)
    },
    "anaplasmosis":{
        "activity": (0.3, 0.1), 
        "temp": (39.5, 0.4), 
        "milk_yield": (20, 3)
    }
}

def gen_disease_df(n, disease):
    return pd.DataFrame({
        "activity": np.random.normal(*metrics[disease]["activity"], n),
        "temp":  np.random.normal(*metrics[disease]["temp"], n),
        "milk_yield": np.random.normal(*metrics[disease]["temp"], n),
        "disease": disease
        })



def gen_df():

    healthy_df = gen_disease_df(n_healthy, "healthy")
    mastitis_df = gen_disease_df(n_mastitis, "mastitis")
    anaplasmosis_df = gen_disease_df(n_mastitis, "anaplasmosis")

    df = pd.concat([healthy_df, mastitis_df, anaplasmosis_df])
    df = df.sample(frac=1).reset_index(drop=True)

