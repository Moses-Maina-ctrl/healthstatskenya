import pandas as pd
import streamlit as st
import altair as alt
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
    
    df_2 = df2[['GHO (CODE)','YEAR (DISPLAY)','Display Value']]
 

    #Cholera
    cholera_mortality = df_2[df_2['GHO (CODE)'] == 'CHOLERA_0000000002']
    cholera_reported_cases = df_2[df_2['GHO (CODE)'] == 'CHOLERA_0000000001']
    cholera_fatality_rate= df_2[df_2['GHO (CODE)'] == 'CHOLERA_0000000003']

    #Meningitis
    mening_suspected_deaths =df_2[df_2['GHO (CODE)'] == 'MENING_1']

    #Polio
    polio_reported_cases =df_2[df_2['GHO (CODE)'] == 'WHS3_49']

    #Diptheria
    diptheria_reported_cases = df_2[df_2['GHO (CODE)'] == 'WHS3_41']

    #Pertussis
    pertussis_reported_cases = df_2[df_2['GHO (CODE)'] == 'WHS3_43']

    #Tetanus
    tetanus_reported_cases = df_2[df_2['GHO (CODE)'] == 'WHS3_46']

    #Yellow Fever
    yellow_reported_cases = df_2[df_2['GHO (CODE)'] == 'WHS3_50']

    #Mumps
    mumps_reported_cases = df_2[df_2['GHO (CODE)'] == 'WHS3_53']

    #NeoTetanus
    neotetanus_reported_cases = df_2[df_2['GHO (CODE)'] == 'WHS3_56']

    #Rubella
    rubella_reported_cases = df_2[df_2['GHO (CODE)'] == 'WHS3_57']

    #Measles
    measles_reported_cases = df_2[df_2['GHO (CODE)'] == 'WHS3_62']

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
    st.write('Infectious diseases continue to pose significant health challenges in Kenya, affecting individuals, communities, and the nation\'s healthcare system. Aside from Malaria and Tuberculosis, there are numerous more diseases that continue to be prevalent in the Kenya.')
    selected_disease = st.selectbox("Select Disease", diseases)

    if selected_disease == 'Cholera':
        st.header('Cholera', divider='blue')
        st.subheader('Key Facts')
        st.write('Cholera is an acute diarrhoeal infection caused by ingestion of food or water contaminated with the bacterium Vibrio cholerae.')
        st.markdown("""
            ### Symptoms:
                    - Severe Acute Watery Diarrhoea
                    - Fatigue due to dehydration
                    - Vomiting
                    """)
        st.markdown("""
            Sources: [CDC](https://www.cdc.gov/cholera/general/index.html) , [WHO](https://www.who.int/news-room/fact-sheets/detail/cholera)
                    """)
    
        st.subheader('Trends',divider='blue')
        #Charts
        
        cholera_mortality_val = cholera_mortality.rename(columns={'YEAR (DISPLAY)':'Years', 'Display Value':'Number of Deaths'})
        chol_mort_chart = alt.Chart(cholera_mortality_val).mark_line().encode(
              x = 'Years',
              y = 'Number of Deaths'
        ).properties(
              width=600,
              height= 400,
              title= 'Number of Reported Deaths'
        )
        st.write(chol_mort_chart)
        stoggle("Source","Humanitarian Data Exchange")
        st.markdown("""
            [HDX Kenya-Health Indicators](https://data.humdata.org/dataset/who-data-for-kenya?) 
                    """)
 

    elif selected_disease == 'Meningitis':
        st.header('Meningitis', divider='violet')
        st.subheader('Key Facts')
        st.write('Meningitis is the inflammation of the tissues surrounding the brain and spinal cord. It is usually caused by infection. It can be fatal and requires immediate medical care. Meningitis can be caused by several species of bacteria, viruses, fungi and parasites. Most infections can be transmitted from person to person.')

        st.markdown("""
            ### Symptoms:
                    - Neck Stiffness
                    - Fever
                    - Nausea
                    """)
        st.markdown("""
            Sources:  [WHO](https://www.who.int/news-room/fact-sheets/detail/meningitis)
                    """)
    
        st.subheader('Trends',divider='violet')
    elif selected_disease == 'Polio':
        st.header('Polio', divider='red')
        st.subheader('Key Facts')
        st.write('Polio, or poliomyelitis, is a disabling and life-threatening disease caused by the poliovirus. The virus spreads from person to person and can infect a person’s spinal cord, causing paralysis (can’t move parts of the body).')
        
        st.markdown("""
            ### Symptoms:
                    - Most people who get infected with poliovirus will not have any visible symptoms
                    - About 1 out of 4 people (or 25 out of 100) with poliovirus infection will have flu-like symptoms that can include:
                    - A smaller proportion of people with poliovirus infection will develop other, more serious symptoms that affect the brain and spinal cord leading to paralysis.
                    """)
        st.markdown("""
            Sources: [CDC](https://www.cdc.gov/polio/what-is-polio/index.htm)  
                    """)
    
        st.subheader('Trends',divider='red')
    elif selected_disease == 'Diptheria':
            st.header('Diptheria', divider='grey')
            st.subheader('Key Facts')
            st.write('Diphtheria is a serious infection caused by strains of bacteria called Corynebacterium diphtheriae. Diphtheria bacteria spread from person to person, usually through respiratory droplets, like from coughing or sneezing. ')
            
            st.markdown("""
                ### Symptoms:
                        - Swollen glands in the neck 
                        - Sore throat 
                        - Mild Fever 
                        """)
            st.markdown("""
                Sources: [CDC](https://www.cdc.gov/diphtheria/about/symptoms.html)  
                        """)
        
            st.subheader('Trends',divider='gray')
    elif selected_disease == 'Pertussis':
            st.header('Pertussis', divider='green')
            st.subheader('Key Facts')
            st.write('Pertussis, also known as whooping cough, is a highly contagious respiratory infection caused by the bacterium Bordetella pertussis.')
            
            st.markdown("""
                ### Symptoms:
                        - Fever
                        - Dry and Peristent Cough 
                        - Breathing Difficulties 
                        """)
            st.markdown("""
                Sources: [CDC](https://www.cdc.gov/diphtheria/about/symptoms.html)  
                        """)
        
            st.subheader('Trends',divider='green')
    
    elif selected_disease == 'Tetanus':
            st.header('Tetanus', divider='orange')
            st.subheader('Key Facts')
            st.write('Tetanus is an infection caused by bacteria called Clostridium tetani. When these bacteria enter the body, they produce a toxin that causes painful muscle contractions.')
            
            st.markdown("""
                ### Symptoms:
                        - Jaw cramping
                        - Sudden, involuntary muscle spasms 
                        - Painful muscle stiffness all over the body 
                        - Seizures
                        """)
            st.markdown("""
                Sources: [CDC](https://www.cdc.gov/tetanus/index.html)  
                        """)
        
            st.subheader('Trends',divider='orange')
    elif selected_disease == 'Yellow Fever':
            st.header('Yellow Fever', divider='gray')
            st.subheader('Key Facts')
            st.write('Yellow fever is a viral disease that is transmitted to humans by the bites of infected mosquitoes. It is prone to epidemics and is preventable with a vaccine.')
            
            st.markdown("""
                ### Symptoms:
                        - Fever
                        - Muscle Pain
                        - Nausea
                        """)
            st.markdown("""
                Sources: [WHO](https://www.who.int/health-topics/yellow-fever#tab=tab_1)  
                        """)
        
            st.subheader('Trends',divider='gray')
 
    elif selected_disease == 'Mumps':
            st.header('Mumps', divider='green')
            st.subheader('Key Facts')
            st.write('Mumps is an acute disease of children and young adults, caused by a paramyxovirus of which there is only a single serotype. Humans are the only known host for mumps virus, which is spread via direct contact or by airborne droplets from the upper respiratory tract of infected individuals.')
            
            st.markdown("""
                ### Symptoms:
                        - Discomfort in the salivary glands
                        - Pain and tenderness of the testicles
                        - Fever
                        """)
            st.markdown("""
                Sources: [WHO](https://www.who.int/teams/health-product-policy-and-standards/standards-and-specifications/vaccine-standardization/mumps)  
                        """)
        
            st.subheader('Trends',divider='gray')
 
    elif selected_disease == 'Neonatal Tetanus':
            st.header('Neonatal Tetanus', divider='orange')
            st.subheader('Key Facts')
            st.write('Neonatal tetanus (trismus nascentium) is a form of generalised tetanus that occurs in newborns. Infants who have not acquired passive immunity from an immunized mother are at risk.')
            
            st.markdown("""
                ### Symptoms:
                        - Symptoms usually appear from 4 to 14 days after birth, averaging about 7 days.
                        - The fatality rate for infants has been estimated as 70% to 100%; death usually occurs by the age of 2 weeks
                        - Fever
                        """)
            st.markdown("""
                Sources: [WHO](https://www.who.int/news-room/fact-sheets/detail/tetanus)  
                        """)
        
            st.subheader('Trends',divider='orange')
 
    elif selected_disease == 'Rubella':
            st.header('Pink', divider='violet')
            st.subheader('Key Facts')
            st.write('Rubella is an acute, contagious viral infection. While rubella virus infection usually causes a mild fever and rash in children and adults, infection during pregnancy, especially during the first trimester, can result in miscarriage, fetal death, stillbirth, or infants with congenital malformations, known as congenital rubella syndrome (CRS)')
            
            st.markdown("""
                ### Symptoms:
                        - Low Fever
                        - Mild Conjuctivits
                        - Nausea
                        """)
            st.markdown("""
                Sources: [WHO](https://www.who.int/news-room/fact-sheets/detail/rubella)  
                        """)
        
            st.subheader('Trends',divider='orange')
    elif selected_disease == 'Measles':
            st.header('Measles', divider='red')
            st.subheader('Key Facts')
            st.write('Measles is a highly contagious disease caused by a virus. It spreads easily when an infected person breathes, coughs or sneezes. It can cause severe disease, complications, and even death.')
            
            st.markdown("""
                ### Symptoms:
                        - Running Nose
                        - Cough
                        - Red and Watery eyes
                        """)
            st.markdown("""
                Sources: [WHO](https://www.who.int/news-room/fact-sheets/detail/measles)  
                        """)
        
            st.subheader('Trends',divider='red')
            
 

st.set_page_config(
    page_title= "Infectious Diseases",
)

if __name__ == "__main__":
   main()