#Write a simple app that reads the user input and display the output
import numpy as np
import pandas as pd
import streamlit as st
import altair as alt

# Define the Streamlit app
def app():
    st.header("Welcome to Streamlit GUI Demo")
    st.subheader("Louie F. Cervantes M.Eng. \n(c) 2023 WVSU College of ICT")
    
    st.title("Handy reference for GUI Elements")
    st.text('This is some plain text')
    name = st.text_input('Enter your name')
    age = st.number_input('Enter your age', min_value=0, max_value=150)
    gender = st.selectbox('Select your gender', ('Male', 'Female', 'Other'))

    if st.button('Click me'):
        st.write('You clicked the button')
    
    if st.checkbox('Show/hide'):
        st.write('You checked the box')
    
    if st.radio('Choose one', ('Option 1', 'Option 2')):
        st.write('You selected an option')
    
    if st.selectbox('Choose one', ('Option 1', 'Option 2')):
        st.write('You selected an option')    
    
# Run the app
if __name__ == "__main__":
    app()
