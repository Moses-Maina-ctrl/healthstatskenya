import pandas as pd
import streamlit as st

url='https://data.humdata.org/dataset/b239ef6c-910d-4347-ba87-2d21a23f03fa/resource/71904d91-8e70-4f87-844b-88a0648a8bad/download/malaria_indicators_ken.csv'
data = pd.read_csv(url)
df= pd.DataFrame(data)
#Cleaning data
df =df.dropna(axis=1, how='all')
df2 = df.drop(['GHO (URL)',
               'PUBLISHSTATE (CODE)',
               'PUBLISHSTATE (DISPLAY)',
               'REGION (CODE)',
               'REGION (DISPLAY)',
               'COUNTRY (CODE)',
               'COUNTRY (CODE)',
               'COUNTRY (DISPLAY)'], axis=1)
#malaria
estimated_cases = df2[df2['GHO (CODE)'] == 'MALARIA_EST_CASES']
confirmed_cases = df2[df2['GHO (CODE)'] == 'MALARIA_CONF_CASES']
estimated_death = df2[df2['GHO (CODE)'] == 'MALARIA_EST_DEATHS']
estimated_mortality_rate = df2[df2['GHO (CODE)'] == 'MALARIA_EST_MORTALITY']


print(df2)
