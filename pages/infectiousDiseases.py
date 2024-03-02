import pandas as pd
import streamlit as st

url='https://data.humdata.org/dataset/b239ef6c-910d-4347-ba87-2d21a23f03fa/resource/15a69fd8-71a0-43e0-b116-1f8def1c2d79/download/infectious_diseases_indicators_ken.csv'
data= pd.read_csv(url)
df= pd.DataFrame(data)
df2 = df.dropna(axis=1, how='all')
print(df2)