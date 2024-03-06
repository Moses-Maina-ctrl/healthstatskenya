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
            'Malaria',
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
        cholera_reported_cases_val =cholera_reported_cases.rename(columns={'YEAR (DISPLAY)':'Years', 'Display Value':'Number of Cases'})
        chol_cases_chart = alt.Chart(cholera_reported_cases_val).mark_line().encode(
              x = 'Years',
              y = 'Number of Cases'
        ).properties(
              width=600,
              height= 400,
              title= 'Number of Reported Cases of Cholera'
        )
        st.write(chol_cases_chart)
        cholera_mortality_val = cholera_mortality.rename(columns={'YEAR (DISPLAY)':'Years', 'Display Value':'Number of Deaths'})
        chol_mort_chart = alt.Chart(cholera_mortality_val).mark_line().encode(
              x = 'Years',
              y = 'Number of Deaths'
        ).properties(
              width=600,
              height= 400,
              title= 'Number of Reported Deaths from Cholera'
        )
        st.write(chol_mort_chart)

        cholera_fatal_val = cholera_fatality_rate.rename(columns={'YEAR (DISPLAY)':'Years', 'Display Value':'Fatality Rate'})
        chol_fatal_chart = alt.Chart(cholera_fatal_val).mark_line().encode(
              x = 'Years',
              y = 'Fatality Rate'
        ).properties(
              width=600,
              height= 400,
              title= 'Cholera Case Fatality Rate'
        )
        st.write(chol_fatal_chart)
        stoggle("Source","Humanitarian Data Exchange")
        st.markdown("""
            [HDX Kenya-Health Indicators](https://data.humdata.org/dataset/who-data-for-kenya?) 
                    """)
 
    elif selected_disease == 'Malaria':
           malaria()
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
        mening_reported= mening_suspected_deaths.rename(columns={'YEAR (DISPLAY)':'Years', 'Display Value':'Number of Suspected Meningitis Deaths Reported'})
        mening_chart= alt.Chart(mening_reported).mark_line().encode(
              x = 'Years',
              y = 'Number of Suspected Meningitis Deaths Reported'
        ).properties(
              width=600,
              height= 400,
              title= 'Suspected Meningitis Deaths Reported Annually'
        )
        st.write(mening_chart)
        stoggle("Source","Humanitarian Data Exchange")
        st.markdown("""
            [HDX Kenya-Health Indicators](https://data.humdata.org/dataset/who-data-for-kenya?) 
                    """)
 
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
        polio_val= polio_reported_cases.rename(columns={'YEAR (DISPLAY)':'Years', 'Display Value':'Number of Reported Polio Cases'})
        polio_chart= alt.Chart(polio_val).mark_line().encode(
              x = 'Years',
              y = 'Number of Reported Polio Cases'
        ).properties(
              width=600,
              height= 400,
              title= 'Number of Reported Polio Cases Annually'

        )
        st.write(polio_chart)
        stoggle("Source","Humanitarian Data Exchange")
        st.markdown("""
            [HDX Kenya-Health Indicators](https://data.humdata.org/dataset/who-data-for-kenya?) 
                    """)
 
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
            diptheria_val= diptheria_reported_cases.rename(columns={'YEAR (DISPLAY)':'Years', 'Display Value':'Number of Reported Diptheria Cases'})
            diptheria_chart= alt.Chart(diptheria_val).mark_line().encode(
              x = 'Years',
              y = 'Number of Reported Diptheria Cases'
            ).properties(
              width=600,
              height= 400,
              title= 'Number of Reported Diptheria Cases Annually'

            )
            st.write(diptheria_chart)
            stoggle("Source","Humanitarian Data Exchange")
            st.markdown("""
                 [HDX Kenya-Health Indicators](https://data.humdata.org/dataset/who-data-for-kenya?) 
                    """)
 
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
            pertussis_val= pertussis_reported_cases.rename(columns={'YEAR (DISPLAY)':'Years', 'Display Value':'Number of Reported Pertussis Cases'})
            pertussis_chart= alt.Chart(pertussis_val).mark_line().encode(
              x = 'Years',
              y = 'Number of Reported Pertussis Cases'
            ).properties(
              width=600,
              height= 400,
              title= 'Number of Reported Pertussis Cases Annually'

            )
            st.write(pertussis_chart)
            stoggle("Source","Humanitarian Data Exchange")
            st.markdown("""
                 [HDX Kenya-Health Indicators](https://data.humdata.org/dataset/who-data-for-kenya?) 
                    """)
    
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
            tetanus_val= tetanus_reported_cases.rename(columns={'YEAR (DISPLAY)':'Years', 'Display Value':'Number of Reported Tetanus Cases'})
            tetanus_chart= alt.Chart(tetanus_val).mark_line().encode(
              x = 'Years',
              y = 'Number of Reported Tetanus Cases'
            ).properties(
              width=600,
              height= 400,
              title= 'Number of Reported Tetanus Cases Annually'

            )
            st.write(tetanus_chart)
            stoggle("Source","Humanitarian Data Exchange")
            st.markdown("""
                 [HDX Kenya-Health Indicators](https://data.humdata.org/dataset/who-data-for-kenya?) 
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
            yellow_val= yellow_reported_cases.rename(columns={'YEAR (DISPLAY)':'Years', 'Display Value':'Number of Reported Yellow Fever Cases'})
            yellow_chart= alt.Chart(yellow_val).mark_line().encode(
              x = 'Years',
              y = 'Number of Reported Yellow Fever Cases'
            ).properties(
              width=600,
              height= 400,
              title= 'Number of Reported Yellow Fever Cases Annually'

            )
            st.write(yellow_chart)
            stoggle("Source","Humanitarian Data Exchange")
            st.markdown("""
                 [HDX Kenya-Health Indicators](https://data.humdata.org/dataset/who-data-for-kenya?) 
                    """)

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
            mumps_val= mumps_reported_cases.rename(columns={'YEAR (DISPLAY)':'Years', 'Display Value':'Number of Reported Mumps Cases'})
            mumps_chart= alt.Chart(mumps_val).mark_line().encode(
              x = 'Years',
              y = 'Number of Reported Mumps Cases'
            ).properties(
              width=600,
              height= 400,
              title= 'Number of Reported Mumps Cases Annually'

            )
            st.write(mumps_chart)
            stoggle("Source","Humanitarian Data Exchange")
            st.markdown("""
                 [HDX Kenya-Health Indicators](https://data.humdata.org/dataset/who-data-for-kenya?) 
                    """)

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
            neo_val= neotetanus_reported_cases.rename(columns={'YEAR (DISPLAY)':'Years', 'Display Value':'Number of Reported Neonatal Tetanus Cases'})
            neo_chart= alt.Chart(neo_val).mark_line().encode(
              x = 'Years',
              y = 'Number of Reported Neonatal Tetanus Cases'
            ).properties(
              width=600,
              height= 400,
              title= 'Number of Reported Neonatal Tetanus Cases Annually'

            )
            st.write(neo_chart)
            stoggle("Source","Humanitarian Data Exchange")
            st.markdown("""
                 [HDX Kenya-Health Indicators](https://data.humdata.org/dataset/who-data-for-kenya?) 
                    """)


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

            rubella_val= rubella_reported_cases.rename(columns={'YEAR (DISPLAY)':'Years', 'Display Value':'Number of Reported Rubella Cases'})
            rubella_chart= alt.Chart(rubella_val).mark_line().encode(
              x = 'Years',
              y = 'Number of Reported Rubella Cases'
            ).properties(
              width=600,
              height= 400,
              title= 'Number of Reported Rubella Cases Annually'

            )
            st.write(rubella_chart)
            stoggle("Source","Humanitarian Data Exchange")
            st.markdown("""
                 [HDX Kenya-Health Indicators](https://data.humdata.org/dataset/who-data-for-kenya?) 
                    """)

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
            
            measles_val= measles_reported_cases.rename(columns={'YEAR (DISPLAY)':'Years', 'Display Value':'Number of Reported Measles Cases'})
            measles_chart= alt.Chart(measles_val).mark_line().encode(
              x = 'Years',
              y = 'Number of Reported Measles Cases'
            ).properties(
              width=600,
              height= 400,
              title= 'Number of Reported Measles Cases Annually'

            )
            st.write(measles_chart)
            stoggle("Source","Humanitarian Data Exchange")
            st.markdown("""
                 [HDX Kenya-Health Indicators](https://data.humdata.org/dataset/who-data-for-kenya?) 
                    """)

def malaria():
        malariaUrl='https://data.humdata.org/dataset/b239ef6c-910d-4347-ba87-2d21a23f03fa/resource/71904d91-8e70-4f87-844b-88a0648a8bad/download/malaria_indicators_ken.csv'
        malaria_data = pd.read_csv(malariaUrl)
        malaria_df= pd.DataFrame(malaria_data)
        #Cleaning data
        malaria_df2 =malaria_df.dropna(axis=1, how='all')
        malaria_df2 = malaria_df2[['GHO (CODE)','YEAR (DISPLAY)','Numeric']]
       #malaria
        estimated_cases = malaria_df2[malaria_df2['GHO (CODE)'] == 'MALARIA_EST_CASES']
        confirmed_cases = malaria_df2[malaria_df2['GHO (CODE)'] == 'MALARIA_CONF_CASES']
        estimated_death = malaria_df2[malaria_df2['GHO (CODE)'] == 'MALARIA_EST_DEATHS']
        estimated_mortality_rate = malaria_df2[malaria_df2['GHO (CODE)'] == 'MALARIA_EST_MORTALITY']
        st.header('Malaria', divider='blue')
        st.subheader('Key Facts')
        st.write('Malaria is a life-threatening disease caused by parasites that are transmitted to people through the bites of infected female Anopheles mosquitoes')
        st.markdown("""
            ### Symptoms:
                    - Fever
                    - Chills 
                    - Muscle or joint pain
                    - Abdominal pain
                    """)
        st.markdown("""
            Sources:  , [WHO](https://www.who.int/news-room/fact-sheets/detail/malaria)
                    """)
    
        st.subheader('Trends',divider='blue')
        
        #Charts
        mal_est =estimated_cases.rename(columns={'YEAR (DISPLAY)':'Years', 'Numeric':'Estimated Number of Malaria Cases'})
        mal_est_chart = alt.Chart(mal_est).mark_line().encode(
              x = 'Years',
              y = 'Estimated Number of Malaria Cases'
        ).properties(
              width=600,
              height= 400,
              title= 'Estimated Number of Malaria Cases'
        )
        st.write(mal_est_chart)
        conf_cases = confirmed_cases.rename(columns={'YEAR (DISPLAY)':'Years', 'Numeric':'Number of confirmed malaria cases'})
        conf_chart = alt.Chart(conf_cases).mark_line().encode(
              x = 'Years',
              y = 'Number of confirmed malaria cases'
        ).properties(
              width=600,
              height= 400,
              title= 'Number of confirmed malaria cases Annually'
        )
        st.write(conf_chart)
        est_death =estimated_death.rename(columns={'YEAR (DISPLAY)':'Years', 'Numeric':'Estimated Number of Deaths caused by Malaria'})
        est_death_chart = alt.Chart(est_death).mark_line().encode(
              x = 'Years',
              y = 'Estimated Number of Deaths caused by Malaria'
        ).properties(
              width=600,
              height= 400,
              title= 'Estimated Number of Deaths caused by Malaria'
        )
        st.write(est_death_chart)
        est_rate = estimated_mortality_rate.rename(columns={'YEAR (DISPLAY)':'Years', 'Numeric':'Estimated malaria incidence (per 1000 population at risk)'})
        rate_chart = alt.Chart(est_rate).mark_line().encode(
              x = 'Years',
              y = 'Estimated malaria incidence (per 1000 population at risk)'
        ).properties(
              width=600,
              height= 400,
              title= 'Estimated malaria incidence (per 1000 population at risk)'
        )
        st.write(rate_chart)
        



st.set_page_config(
    page_title= "Infectious Diseases",
)

if __name__ == "__main__":
   main()
