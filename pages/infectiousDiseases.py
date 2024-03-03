import pandas as pd
import streamlit as st
from streamlit_extras.stoggle import stoggle

def main():
    url='https://data.humdata.org/dataset/b239ef6c-910d-4347-ba87-2d21a23f03fa/resource/15a69fd8-71a0-43e0-b116-1f8def1c2d79/download/infectious_diseases_indicators_ken.csv'
    data= pd.read_csv(url)
    df= pd.DataFrame(data)
    #Cleaning data
    df2 = df.dropna(axis=1, how='all')
    df2 = df2.drop(['GHO (URL)',
                'PUBLISHSTATE (CODE)',
                'PUBLISHSTATE (DISPLAY)',
                'REGION (CODE)',
                'REGION (DISPLAY)',
                'COUNTRY (CODE)',
                'YEAR (CODE)',
                'STARTYEAR',
                'ENDYEAR',
                'COUNTRY (CODE)',
                'COUNTRY (DISPLAY)'], axis=1)

    #Cholera
    cholera_mortality = df2[df2['GHO (CODE)'] == 'CHOLERA_0000000002']
    cholera_reported_cases = df2[df2['GHO (CODE)'] == 'CHOLERA_0000000001']
    cholera_fatality_rate= df2[df2['GHO (CODE)'] == 'CHOLERA_0000000003']

    #Meningitis
    mening_suspected_deaths =df2[df2['GHO (CODE)'] == 'MENING_1']

    #Polio
    polio_reported_cases =df2[df2['GHO (CODE)'] == 'WHS3_49']

    #Diptheria
    diptheria_reported_cases = df2[df2['GHO (CODE)'] == 'WHS3_41']

    #Pertussis
    pertussis_reported_cases = df2[df2['GHO (CODE)'] == 'WHS3_43']

    #Tetanus
    tetanus_reported_cases = df2[df2['GHO (CODE)'] == 'WHS3_46']

    #Yellow Fever
    yellow_reported_cases = df2[df2['GHO (CODE)'] == 'WHS3_50']

    #Mumps
    mumps_reported_cases = df2[df2['GHO (CODE)'] == 'WHS3_53']

    #NeoTetanus
    neotetanus_reported_cases = df2[df2['GHO (CODE)'] == 'WHS3_56']

    #Rubella
    rubella_reported_cases = df2[df2['GHO (CODE)'] == 'WHS3_57']

    #Measles
    measles_reported_cases = df2[df2['GHO (CODE)'] == 'WHS3_62']

    ##
    diseases =['Cholera',
            'Meningitis',
            'Polio',
            'Diptheria',
            'Pertussis',
            'Tetanus',
            'Yellow Fever',
            'Mumps',
            'Neonatal Tetanus',
            'Rubella',
            'Measles']
    
    st.title('Infectious Diseases')
    st.header('Definition', divider='gray')
    st.write('Infectious Diseases are diseases caused by pathogenic microorganisms, such as bacteria, viruses, parasites or fungi; the diseases can be transimitted, directly or indirectly, from one person to another')
    stoggle("Source","https://www.emro.who.int/health-topics/infectious-diseases/index.html")
    st.header('Infectious Diseases', divider='gray')
    st.write('Infectious diseases continue to pose significant health challenges in Kenya, affecting individuals, communities, and the nation\'s healthcare system. Aside from Malaria and Tuberculosi, there are numerous more diseases that continue to be prevalent in the Kenya.')
    selected_disease = st.selectbox("Select Disease", diseases)

    if selected_disease == 'Cholera':
        st.header('Cholera', divider='blue')
        st.subheader('Key Facts')
        st.write('Cholera is an acute diarrhoeal disease that can kill within hours if left untreatedCholera is an acute diarrhoeal infection caused by ingestion of food or water contaminated with the bacterium Vibrio cholerae.')
        st.markdown("""
            ### Symptoms
                    -Severe Acute Watery Diarrhoea
                    -Fatigue due to dehydration
                    -Vomiting
                    """)
st.set_page_config(
    page_title= "Infectious Diseases",
)

if __name__ == "__main__":
   main()