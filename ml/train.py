import matplotlib.pyplot as plt
#import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

colors = {
    "healthy": "green",
    "mastitis": "blue",
    "anaplasmosis": "red"
}

df1 = gen_df()

plt.figure()
for disease, group in df1.groupby("disease"):
    plt.scatter(
        group["temp"],
        group["milk_yield"],
        label=disease
    )

plt.xlabel("Temp")
plt.ylabel("Milk yield")
plt.legend()
plt.show()
