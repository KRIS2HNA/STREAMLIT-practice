import streamlit as st 
import datetime
from streamlit_option_menu import option_menu

with st.sidebar:
    menu = option_menu(
        menu_title = "Main Menu",
        options = ["Home", "About", "Contact"],
        icons = ["house", "info-circle", "envelope"],
        default_index = 0,
        orientation = "horizontal"
    )

st.title("Hello Streamlit")
st.write("Welcome to your first Streamlit app!")

st.header("user input")
st.subheader("Enter your name")

st.text("This is a simple text input example")
st.markdown(" this is **markdown** example with _italic_ and **bold** text")

v = st.slider('Select a value', 0, 100, 25)
st.write('you selected:', v)
 
n = st.number_input("insert a number")
st.write("The number you inserted is:", n)


t= st.text_area("enter name")
st.write("Hello,", t)


option = st.selectbox('Select your favorite fruit:', 
    ['Apple', 'Banana', 'Orange', 'Grapes'])


if st.button("This is a button"):
    st.write("Buton Clicked!") 
    st.write("you selected:", option)
    
    
st.info("This is an info message")
st.success("This is a success message")
st.warning("This is a warning message")
st.error("This is an error message")

st.exception("this is an exception message")

st.help("this is a help message")

with st.echo():
    st.write("This code is inside the st.echo() context manager.")
  
with st.sidebar:
    st.title("sidebar title")
    st.write("this is sidebar content")
    
    option = st.selectbox('Select your favorite fruit:', 
    ['Apple', 'Banana', 'Orange', 'Grapes'])
    
    if st.button("sidebar button"):
        st.write("you selected:", option)
        st.write("sidebar button clicked!" )
        st.write(f"selected option: {option}")
        
    agree = st.checkbox("I agree")
    if agree:
        st.write("Thank you for agreeing!")
    else:
        st.write("You haven't agreed yet.")
        
choice = st.radio("Choose an option:", ('Option 1', 'Option 2', 'Option 3'))
if st.button("Submit Choice"):
    st.write(f"Slected choice: {choice}")

st.date_input("Select a date")
st.time_input("Select a time")

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    st.write("File uploaded:", uploaded_file.name)
    
  
st.file_uploader("Upload an image", type = ["png", "jpg", "jpeg"])
