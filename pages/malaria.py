import pandas as pd
import streamlit as st

url='https://data.humdata.org/dataset/b239ef6c-910d-4347-ba87-2d21a23f03fa/resource/71904d91-8e70-4f87-844b-88a0648a8bad/download/malaria_indicators_ken.csv'
data = pd.read_csv(url)
df= pd.DataFrame(data)
df2 = df.dropna(axis=1, how='all')
print(df2)