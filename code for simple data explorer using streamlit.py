import streamlit as st
import pandas as pd
import matplotlib as plt

st.title("Simple Data Dashboard")

uploaded_file = st.file_uploader("Choose a CSV file",type="csv")

if (uploaded_file is not None):
    dataf= pd.read_csv(uploaded_file)

    st.subheader("Data preview")
    st.write(dataf.head())

    st.subheader("Data Summary")
    st.write(dataf.describe())

    st.subheader("Filter Data")
    columns = dataf.columns.tolist()
    selected_column = st.selectbox("Select column to filter by", columns)
    unique_values = dataf[selected_column].unique()
    selected_values = st.selectbox("Select Value", unique_values)

    filtered_dataf = dataf[dataf[selected_column] == selected_values]
    st.write(filtered_dataf)

    st.subheader("Plot Header")
    x_column = st.selectbox("Select x-axis column", columns)
    y_column = st.selectbox("Select y-axis column", columns)

    if(st.button("Generate Plot")):
        st.line_chart(filtered_dataf.set_index(x_column)[y_column])

else:
    st.write("Please upload a file....")

