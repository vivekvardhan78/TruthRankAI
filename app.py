import streamlit as st
import pandas as pd

st.title("TruthRank AI")

uploaded = st.file_uploader(
    "Upload Candidate CSV",
    type=["csv"]
)

if uploaded:

    df = pd.read_csv(uploaded)

    st.write(df.head())

    st.success(
        "TruthRank AI Demo Running"
    )