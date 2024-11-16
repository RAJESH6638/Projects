import streamlit as st
st.title("✉️Cold Mail Generator")
url_input = st.text_input("Enter a url: ", value= "https://jobs.nike.com/job/R-44993?from=job%20search%20funnel")
submit_button = st.button("Submit")

if submit_button:
    st.code("Hello Hiring Manager , I am from AtliQ", language = 'markdown')

