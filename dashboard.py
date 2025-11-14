import streamlit as st 

st.set_page_config(
    page_title="Dashboard Example", 
    page_icon="📊",
    layout="wide",
    )

st.title("Dashboard Example")

with st.sidebar:
    st.header("configuration")
    data_type = st.selectbox("Select Data Type", ["variables and datatypes", "control flow and loops", "Functions and modules", "Data handling and file operations", "Error handling and exceptions", "Object-oriented programming", "Libraries and frameworks", "Advanced topics"])
    
if data_type == "variables and datatypes":
    st.subheader("Variables and Data Types")
    st.write("This section covers the basics of variables and data types in programming.")
    var_name = st.text_input("Enter a variable name:", value="my_string")
    var_value = st.text_input("Enter a value for the variable:", value="Hello, Streamlit!")
    
    if var_name and var_value:
        st.write(f"You have created a variable named `{var_name}` with the value: `{var_value}`")
        st.code(f"{var_name} = '{var_value}'", language="python")
        
        
    data_obj = {"string" : "hello world", "integer" : 422, "Float" : 3.33}
    st.subheader("Data Types Examples")
    for name , value in data_obj.items():
        st.write(f"**{name.capitalize()}**: `{value}` of type `{type(value).__name__}`")    
        st.markdown("---")
    