import streamlit as st
import pandas as pd
import altair as alt

st.title("ROLEViA 🚀")

menu = st.sidebar.radio("Navigate", ["Home", "Career Explorer", "Skill Explorer"])

# Load datasets
content = pd.read_csv("content_model_refrence.csv")
skills = pd.read_csv("essential_skills.csv")

# Pages
if menu == "Home":
    st.subheader("Content Model Reference")
    st.dataframe(content.head())

    st.subheader("Essential Skills")
    st.dataframe(skills.head())

elif menu == "Career Explorer":
    st.subheader("Career Explorer")
    job_title = st.text_input("Enter a Job Title (e.g., Chief Executives)")

    if job_title:
        filtered = skills[skills["Title"].str.contains(job_title, case=False, na=False)]
        st.dataframe(filtered)

        if not filtered.empty:
            chart = alt.Chart(filtered).mark_bar().encode(
                x="Element Name",
                y="Data",
                color="Scale Name",
                column="Scale Name"
            ).properties(width=150, height=300)

            st.altair_chart(chart, use_container_width=True)

elif menu == "Skill Explorer":
    st.subheader("Skill Explorer")
    skill_name = st.text_input("Enter a Skill Name (e.g., Active Listening)")

    if skill_name:
        filtered = skills[skills["Element Name"].str.contains(skill_name, case=False, na=False)]
        st.dataframe(filtered)

        if not filtered.empty:
            chart = alt.Chart(filtered).mark_bar().encode(
                x="Title",
                y="Data",
                color="Scale Name",
                column="Scale Name"
            ).properties(width=150, height=300)

            st.altair_chart(chart, use_container_width=True)



