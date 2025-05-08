"""Contains the `Home` page contents of the app."""
import streamlit as st

st.set_page_config(
    page_title="Home",
    page_icon="🏠",
)

st.title("Creatinine Clearance Calculator 📊")
st.divider()
st.markdown(
    """
    Welcome to the Creatinine Clearance Calculator! This application helps healthcare professionals
    estimate a patient's kidney function using the Cockcroft-Gault formula.

    ### Features
    - Calculate estimated creatinine clearance (CrCl)
    - Input validation for age, weight, and serum creatinine
    - Gender-specific calculations
    - Clear interpretation of results
    - Educational information about the formula

    Navigate to the Creatinine Clearance Calculator page to get started!
    """
)

st.subheader("About the Calculator")

st.markdown(
    """
    The calculator uses the Cockcroft-Gault formula, which is one of the most widely used methods
    to estimate creatinine clearance. This estimation is crucial for:
    - Determining appropriate drug dosages
    - Assessing kidney function
    - Monitoring renal impairment
    - Making clinical decisions

    The formula takes into account:
    - Age
    - Weight
    - Gender
    - Serum creatinine levels
    """
)

st.divider()
st.markdown(
    """
    ### Important Note
    This calculator provides estimates and should be used as a clinical decision support tool.
    Always verify results and consult with healthcare professionals for proper medical assessment.
    """
)
