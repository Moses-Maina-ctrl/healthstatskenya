import pandas as pd 
import streamlit as st
import plotly.graph_objs as go

url = "https://data.humdata.org/dataset/accb9f02-ed55-460b-b7a2-534b59b5f27b/resource/573f09bd-084f-4e51-8936-8a40048b7c94/download/kenya-tuberculosis-prevalence-per-county.csv"
data = pd.read_csv(url)
df= pd.DataFrame(data)
df2=df.dropna()
print(df2)