import pandas as pd 
df = pd.DataFrame({
    "Name": [
        "sai",
        "ram",
        "raj",
    ],
    "Age":[

        "16",
        "infinity",
        "undefined"


    ],

    "hobby": [
        "coding","hello", "art"
    ]
}, index=['a', 'b', 'c'])

print(df)