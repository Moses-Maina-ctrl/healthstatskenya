import streamlit as st
from st_pages import Page, show_pages, add_page_title

kenyan_flag = "\U0001F1F0\U0001F1EA"

def main():
    st.title(f'Health Stats {kenyan_flag}')
    st.markdown(
        """
        Welcome to Health Stats Kenya, a Data Visualization  Site that explores the spread and impact of diseases in different regions of Kenya.



        """
    )

st.set_page_config(
    page_title ="HealthStats",
    page_icon="HS"
)

if __name__ == "__main__":
    main()