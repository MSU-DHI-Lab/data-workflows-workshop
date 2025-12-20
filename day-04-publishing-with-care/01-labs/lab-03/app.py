import pandas as pd
import streamlit as st
from pathlib import Path

st.title("Day 04 Handoff Dashboard")
st.write("A lightweight view for stakeholders to browse the curated dataset and see quality status.")

data_path = Path("../lab-01/outputs/dataset-package/data/curated_collection.csv")
report_path = Path("../lab-03/validation_report.md")

if data_path.exists():
    df = pd.read_csv(data_path)
    st.subheader("Data Preview")
    st.dataframe(df.head())

    st.subheader("Filters")
    rights = st.multiselect("Rights", sorted(df["rights"].unique()))
    place = st.multiselect("Place", sorted(df["place"].unique()))
    filtered = df
    if rights:
        filtered = filtered[filtered["rights"].isin(rights)]
    if place:
        filtered = filtered[filtered["place"].isin(place)]
    st.write(f"Rows after filter: {len(filtered)}")
    st.dataframe(filtered)
else:
    st.warning("Curated dataset not found. Please run Lab 01 and place the CSV in dataset-package/data/.")

st.subheader("Data Quality Status")
if report_path.exists():
    st.markdown(report_path.read_text())
else:
    st.info("No validation report found yet. Run Lab 03 to generate one and place it as validation_report.md in this folder.")

st.caption("Why this app: quick, low-friction way for non-technical stakeholders to browse and see quality signals without opening notebooks.")
