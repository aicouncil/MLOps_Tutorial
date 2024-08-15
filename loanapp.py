import streamlit as st
import numpy as np
import joblib

#Loading our artifacts
loaded_model = joblib.load("loan_model.pkl")
scaling = joblib.load("scaler.pkl")

def prediction(Gender,Married,Dependents,Education,Self_Employed,Applicant_income,CoApplicant_income,LoanAmount,LoanAmountTerm,CreditHistory,PropertyArea):
    #Encode categorical features
    gender_encode = lambda x : 0 if x == 'Female' else 1
    married_encode = lambda x : 0 if x == 'No' else 1
    dependents_encode = lambda x : 0 if x == '0' else 1 if x == '1' else 2 if x == '2' else 3
    education_encode = lambda x : 0 if x == 'Graduate' else 1
    self_employed_encode = lambda x : 0 if x == 'No' else 1
    property_area_encode = lambda x : 0 if x == 'Rural' else 1 if x == 'Semiurban' else 2


    gender = gender_encode(Gender)
    married = married_encode(Married)
    dependents = dependents_encode(Dependents)
    education = education_encode(Education)
    self_employed = self_employed_encode(Self_Employed)
    property_area = property_area_encode(PropertyArea)

    #numerical features
    applicantincome = Applicant_income + CoApplicant_income
    applicantincome_log = np.log(applicantincome)
    loanamount_log = np.log(LoanAmount)
    loanamountterm_log = np.log(LoanAmountTerm)

    #Combine all features into a single array as input data
    input_data = np.array([[gender,married,dependents,education,self_employed,applicantincome_log,loanamount_log,loanamountterm_log,CreditHistory,property_area]])
    input_data_scaled = scaling.transform(input_data)
    predicted_value = loaded_model.predict(input_data_scaled)[0]
    #print(predicted_value)
    return predicted_value

#prediction('Female','No','1','Graduate','No',30000,10000,20000,360,1.0,'Semiurban')


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

    if st.button("Predict"):
        result = prediction(Gender,Married,Dependents,Education,Self_Employed,Applicant_income,CoApplicant_income,LoanAmount,LoanAmountTerm,CreditHistory,PropertyArea)
        if result == 0: 
            st.error("Your loan application is rejected")
        else:
            st.success("Your loan application is approved")


if __name__ == "__main__":
    main()

