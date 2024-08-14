import streamlit as st

def main():
    st.title("Welcome to the Loan Application")
    st.header("Please enter your details to proceed with your loan application")

    Gender = st.selectbox("Gender" , ("Male","Female"))
    Married = st.selectbox("Married" , ("Yes","No"))
    Dependents = st.selectbox("Dependents" , ("0","1","2","3+"))
    Education = st.selectbox("Education" , ('Graduate' , 'Not Graduate'))
    Self_Employed = st.selectbox("Self Employed" , ('No' ,'Yes'))
    Applicant_income = st.number_input("Applicant Income")
    CoApplicant_income = st.number_input("Co Applicant Income")
    LoanAmount = st.number_input("Loan Amount")
    LoanAmountTerm = st.number_input("Loan Amount Term")
    CreditHistory = st.number_input("Credit History")
    PropertyArea = st.selectbox("Property Area" , ('Urban' , 'Rural', 'Semiurban'))

    st.button("Predict")

if __name__ == "__main__":
    main()