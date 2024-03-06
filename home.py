import streamlit as st
from streamlit_extras.metric_cards import style_metric_cards
from streamlit_extras.stoggle import stoggle
from st_pages import Page, Section, show_pages, add_page_title


kenyan_flag = "\U0001F1F0\U0001F1EA"

def main():
    st.title(f'Health Stats {kenyan_flag}')
    st.markdown(
        """
        Welcome to Health Stats Kenya, 

        A data visualization site that explores the spread and impact of infectious diseases in different regions of Kenya.



        """
    )

    st.subheader('General Facts about Kenya')
    st.write('Population')
    st.metric('Population', '> 54.9 million', '1.9%')
    st.write('Life Expectancy')
    col1_1, col1_2 =st.columns(2)
    col1_1.metric('Female','64 years')
    col1_2.metric('Male','59 years')
    st.write('Infant Mortality rate')
    st.metric('Infant Mortality Rate','30/1000 live births')
    stoggle('Source','https://www.cdc.gov/globalhealth/countries/kenya')
    style_metric_cards(background_color="#0e1117")
    st.link_button("Get Informed About Infectious Diseases",url="/1_infectiousDiseases.py") 
        

st.set_page_config(
    page_title ="HealthStats",
    page_icon="HS"
)

if __name__ == "__main__":
    main()

show_pages(
    [
        Page("home.py", "Home", "🏠"),
        Section("Infectious Diseases"),
        Page("pages/1_infectiousDiseases.py", "Infectious Diseases")
    ]
) 