import streamlit as st
import pandas as pd
import snowflake.connector
from pymongo import MongoClient
from dotenv import load_dotenv
import os
from db_utils import load_snowflake_data, load_mongodb_data, get_snowflake_connection, get_mongodb_connection

load_dotenv()


st.set_page_config(page_title="Intermodal Data Platform", layout="wide")
st.title("Intermodal Data Platform")


st.subheader("Snowflake Data")
try:
    snowflake_data = load_snowflake_data()
    st.dataframe(snowflake_data)    
except Exception as e:
    st.error(f"Error loading Snowflake data: {e}")


st.subheader("MongoDB Data")
try:
    df_mongo = load_mongodb_data()
    st.dataframe(df_mongo)
except Exception as e:
    st.error(f"Error loading MongoDB data: {e}")

st.subheader("Data Visualization")  

try:
    df_snowflake = load_snowflake_data()
    df_snowflake.columns = df_snowflake.columns.str.upper()

    if "REPORT_YEAR" in df_snowflake.columns and "VALUE" in df_snowflake.columns:
        chart_data = df_snowflake.groupby("REPORT_YEAR")["VALUE"].sum().reset_index()

        st.bar_chart(
            chart_data,
            x="REPORT_YEAR",
            y="VALUE"
        )
    else:
        st.warning("Columns 'REPORT_YEAR' and 'VALUE' not found in Snowflake data for visualization.")

except Exception as e:
    st.error(f"Error creating visualization: {e}")