# Importing the required packages

import streamlit as st
import pandas as pd
import joblib

# Loading the prebuilt model

model= joblib.load("fraud_detection_model.pkl")

# Setting up the UI

st.set_page_config(page_title="Fraudulent Transaction Detector", layout="wide")

option= st.sidebar.radio("Select an Option", ['Dataset Overview', 'Prediction'])
st.title("Fraud Detection Prediction App")


# Overview

if option == "Dataset Overview":
    st.subheader("Dataset Overview")
    st.info(
        "This section explains the meaning of each column in the dataset "
        "to help users understand the data they are interacting with."
    )

    st.divider()

    # -------------------------------
    st.subheader("Transaction Details")

    st.markdown("""
    **Transaction Type (`Transaction Type`)**  
    Describes the nature of the transaction and how money flows between accounts.

    ---

    ### PAYMENT
    - Used for paying merchants or services  
    - Money flows from **customer → merchant**
    - Usually small to medium amounts  
    - **Fraud Risk:**  Very Low  
    - Common for daily expenses like bills and shopping

    ---

    ### TRANSFER
    - Used to move money between customer accounts  
    - Often an intermediate step before cash withdrawal  
    - Can involve large amounts  
    - **Fraud Risk:** High  
    - Frequently associated with fraudulent activity

    ---

    ### CASH_OUT
    - Used to withdraw money from the system  
    - Often follows a `TRANSFER` transaction  
    - Large and sudden withdrawals are common  
    - **Fraud Risk:** Very High  
    - Represents the final step in many fraud cases

    ---

    ### CASH_IN
    - Used to deposit money into an account  
    - Increases the account balance  
    - Typically legitimate transactions  
    - **Fraud Risk:** Very Low  
    - Common for salary credits and deposits

    ---

    ### DEBIT
    - System-generated bank debits or service charges  
    - Low transaction amounts  
    - Predictable transaction pattern  
    - **Fraud Risk:** Very Low  
    - Rarely associated with fraudulent behavior

    ---

    **Transaction Amount (`Amount`)**  
    Represents the monetary value involved in the transaction.  
    Large and unusual amounts may indicate suspicious activity.
    """)

    # -------------------------------
    st.subheader("Origin Account (Sender)")

    st.markdown("""
    **Sender Balance Before Transaction (`Old Balance(Sender)`)**  
    Account balance of the sender before the transaction.

    **Sender Balance After Transaction (`New Balance(Sender)`)**  
    Account balance of the sender after the transaction.
    """)
    # -------------------------------
    st.subheader("Destination Account (Receiver)")

    st.markdown("""
    **Receiver Balance Before Transaction (`Old Balance(Receiver)`)**  
    Account balance of the receiver before the transaction.

    **Receiver Balance After Transaction (`New Balance(Receiver)`)**  
    Account balance of the receiver after the transaction.
    """)
    # -------------------------------
    st.subheader("Fraud Indicators")

    st.markdown("""
    **Fraud Label (`Fraud`)**  
    Indicates whether the transaction is fraudulent:
    - `1` → Fraud  
    - `0` → Legitimate  
    """)

    st.info("Now you can proceed to the Prediction section "
            "THANK YOU!")



# Final Prediction


if option == "Prediction":
    st.markdown("Please Enter the Transaction Details")
    st.divider()

    transaction_type= st.selectbox("Transaction Type", ['PAYMENT','TRANSFER','CASH_OUT','DEPOSITE'])
    amount= st.number_input("Amount", min_value=0.0, value= 1000.0)
    oldbalanceOrg= st.number_input('Old Balance(Sender)', min_value= 0.0, value= 10000.0)
    newbalanceOrig= st.number_input("New Balance(Sender)", min_value= 0.0, value= 9000.0)
    oldbalanceDest= st.number_input("Old Balance(Receiver)", min_value= 0.0, value= 0.0)
    newbalanceDest= st.number_input("New Balance(Receiver)", min_value= 0.0, value= 0.0)

    if st.button("Predict"):
        input_data= pd.DataFrame([{
            'type':transaction_type,
            'amount':amount,
            'oldbalanceOrg':oldbalanceOrg,
            'newbalanceOrig':newbalanceOrig,
            'oldbalanceDest':oldbalanceDest,
            'newbalanceDest':newbalanceDest
        }])

        prediction= model.predict(input_data)[0]

        st.subheader(f"Prediction : '{int(prediction)}'")

        if prediction == 1:
            st.error("This is a Fraudulent Transaction")

        else:
            st.success("This is a Legit Transaction")



















