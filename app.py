import streamlit as st
from classifier import classify_ticket

st.title("AI Support Ticket Classifier")

st.write("Enter a support ticket below to classify the issue.")

ticket = st.text_area("Support Ticket")

if st.button("Analyze Ticket"):

    if ticket:

        result = classify_ticket(ticket)

        st.subheader("Analysis Result")
        st.write(result)

    else:
        st.warning("Please enter a ticket first.")
