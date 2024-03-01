import streamlit as st

kenyan_flag = "\U0001F1F0\U0001F1EA"

def main():
    st.title(f'Health Stats {kenyan_flag}')
    st.markdown(
        """
        Welcome to Health Stats Kenya, 

        A data visualization site that explores the spread and impact of infectious diseases in different regions of Kenya.



        """
    )

    col1, col2 = st.columns(2)
    with col1:
        st.subheader('General Facts about Kenya')
        st.write('Population')
        st.metric('Population', '> 54.9 million', '1.9%')
        st.write('Life Expectancy')
        col1_1, col1_2 =st.columns(2)
        col1_1.metric('Female','64 years')
        col1_2.metric('Male','59 years')
        st.write('Infant Mortality rate: 30/1000 live births')
    with col2:
        st.subheader('Health Facts about Kenya')
        

st.set_page_config(
    page_title ="HealthStats",
    page_icon="HS"
)

if __name__ == "__main__":
    main()