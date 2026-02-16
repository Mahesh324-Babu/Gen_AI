import pandas as pd
from io import StringIO
import streamlit as st

@st.cache_data
def read_file_content(uploaded_file):
    try:
        if uploaded_file.name.endswith(('.xlsx', '.xls')):
            df = pd.read_excel(uploaded_file)
            return df.to_csv(index=False)
    except:
        pass

    try:
        return StringIO(uploaded_file.getvalue().decode()).read()
    except Exception as e:
        return f"Error reading file: {str(e)}"
