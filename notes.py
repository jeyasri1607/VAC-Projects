import streamlit as st
import pandas as pd
from supabase import create_client
from dotenv import load_dotenv
import os

# ----------------------------
# Load Environment Variables
# ----------------------------
load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase = create_client(
    SUPABASE_URL,
    SUPABASE_KEY
)

# ----------------------------
# UI
# ----------------------------
st.title("📝 AI Notes Taker")

menu = st.sidebar.selectbox(
    "Select Option",
    ["Create", "View", "Update", "Delete"]
)

# ----------------------------
# CREATE
# ----------------------------
if menu == "Create":

    st.subheader("Create New Note")

    title = st.text_input("Title")
    note = st.text_area("Notes")

    if st.button("Save"):

        if title and note:

            supabase.table("notes").insert(
                {
                    "title": title,
                    "note": note
                }
            ).execute()

            st.success("Note Saved Successfully")

        else:
            st.warning("Enter Title and Notes")

# ----------------------------
# VIEW
# ----------------------------
elif menu == "View":

    st.subheader("All Notes")

    response = (
        supabase
        .table("notes")
        .select("*")
        .execute()
    )

    data = response.data

    if data:

        df = pd.DataFrame(data)
        st.dataframe(df, use_container_width=True)

    else:
        st.info("No Notes Found")

# ----------------------------
# UPDATE
# ----------------------------
elif menu == "Update":

    st.subheader("Update Note")

    response = (
        supabase
        .table("notes")
        .select("*")
        .execute()
    )

    data = response.data

    if data:

        df = pd.DataFrame(data)

        note_id = st.selectbox(
            "Select Note ID",
            df["id"]
        )

        selected = df[df["id"] == note_id]

        title = st.text_input(
            "Title",
            selected.iloc[0]["title"]
        )

        note = st.text_area(
            "Notes",
            selected.iloc[0]["note"]
        )

        if st.button("Update"):

            supabase.table("notes").update(
                {
                    "title": title,
                    "note": note
                }
            ).eq(
                "id",
                int(note_id)
            ).execute()

            st.success(
                "Note Updated Successfully"
            )

    else:
        st.info("No Notes Available")

# ----------------------------
# DELETE
# ----------------------------
elif menu == "Delete":

    st.subheader("Delete Note")

    response = (
        supabase
        .table("notes")
        .select("*")
        .execute()
    )

    data = response.data

    if data:

        df = pd.DataFrame(data)

        st.dataframe(
            df,
            use_container_width=True
        )

        note_id = st.selectbox(
            "Select Note ID",
            df["id"]
        )

        if st.button("Delete"):

            supabase.table("notes").delete().eq(
                "id",
                int(note_id)
            ).execute()

            st.success(
                "Note Deleted Successfully"
            )

    else:
        st.info("No Notes Available")