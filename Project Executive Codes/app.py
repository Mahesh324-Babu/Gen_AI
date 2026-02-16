import streamlit as st
from file_handler import read_file_content
from report_generator import generate_report
from visualization import create_visualizations

def main():
    st.set_page_config(page_title="Financial Data Pro", page_icon="💰")

    st.title("💰 Financial Data Pro")
    st.subheader("Gemini-powered Financial Analysis")

    uploaded_file = st.file_uploader(
        "Upload Financial Data",
        type=['csv', 'txt', 'xlsx', 'xls']
    )

    if uploaded_file:
        file_content = read_file_content(uploaded_file)

        st.subheader("Data Preview")
        st.text_area("", file_content[:1500], height=200)

        if st.button("Generate Report"):
            report = generate_report(file_content)
            st.markdown(report)

        if st.button("Generate Visualizations"):
            code = create_visualizations(file_content)
            st.code(code, language="python")

if __name__ == "__main__":
    main()
