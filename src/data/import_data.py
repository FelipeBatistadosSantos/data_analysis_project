import pandas as pd

def import_data():
    file = (r'C:\Users\User\Downloads\produtos_IM.xlsx').replace('\\', '/')
    df = pd.read_csv(file)
    print(df)

import_data()    