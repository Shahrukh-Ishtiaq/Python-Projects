import pandas as pd 
import streamlit as st
from io import BytesIO


st.set_page_config(page_title="Fle Convertor & Cleaner", page_icon="📊", layout="wide")
st.title("Fle Convertor & Cleaner")
st.write("This app allows you to convert and clean your CSV files. You can upload a CSV file, and the app will provide options to convert it to Excel or JSON format. Additionally, you can clean the data by removing duplicates and filling missing values.")

files = st.file_uploader("Upload a CSV or Excel file", type=["csv","xlsx"], accept_multiple_files=True)

if files:
    for file in files:
        ext = file.name.split('.')[-1]
        df = pd.read_csv(file) if ext == 'csv' else pd.read_excel(file)

        st.write(f"### Data from {file.name}")
        st.dataframe(df.head()) 
        if st.checkbox(f"File Missing Values - {file.name}"):
            df.fillna(df.select_dtypes(include="number").mean(), inplace=True)
            st.write("### Missing Values Filled")
            st.dataframe(df.head())

            selected_columns = st.multiselect(f"Select columns to clean, {file.name}", df.columns, default=df.columns)
            df = df[selected_columns]
            st.dataframe(df.head())

            if st.checkbox(f"Show Chart - {file.name}") and not df.select_dtypes(include="number").empty:
              st.bar_chart(df.select_dtypes(include="number").iloc[:, :2])
              
            format = st.radio(f"Convert {file.name} to:", ["Excel", "CSV"], key=file.name)

            if st.button(f"Download {file.name} as {format}"):
                output = BytesIO()
                if format == "CSV":
                     df.to_csv(output, index=False)
                     mime = "text/csv"
                     new_name = file.name.replace(ext, 'csv')
                else:
                    df.to_excel(output, index=False)
                    mime = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                    new_name = file.name.replace(ext, 'xlsx')   
                    output.seek(0)
                st.download_button("Download File", file_name=new_name, data=output, mime=mime)
                st.success(f"File {new_name} downloaded successfully!")