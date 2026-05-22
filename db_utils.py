import streamlit as st
import pandas as pd
import snowflake.connector
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

def get_snowflake_connection():
    return snowflake.connector.connect(
        user=os.getenv("user"),
        password=os.getenv("SNOWFLAKE_PASSWORD"),
        account=os.getenv("account"),
        warehouse=os.getenv("warehouse"),
        database=os.getenv("database"),
        schema=os.getenv("schema")
    )

@st.cache_data(ttl=600)
def load_snowflake_data():
    conn = get_snowflake_connection()
    query = "SELECT * FROM MART.V_FACT_FLAT"
    df = pd.read_sql(query, conn)
    conn.close()
    return df

def get_mongodb_connection():
    client = MongoClient(os.getenv("MONGO_URI"))
    return client["terminals"]

@st.cache_data(ttl=600)
def load_mongodb_data():
    db = get_mongodb_connection()
    collection = db["terminals_desc"]

    data = list(collection.find())
    df = pd.DataFrame(list(data))

    if '_id' in df.columns:
        df.drop(columns=['_id'], inplace=True)
    return df

