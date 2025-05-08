"""Creatinine Clearance Calculator using Cockcroft-Gault formula."""
import streamlit as st
import math

st.set_page_config(
    page_title="Creatinine Clearance Calculator",
    page_icon="💊",
)

st.title("Creatinine Clearance Calculator")
st.divider()

st.markdown(
    """
    This calculator uses the Cockcroft-Gault formula to estimate creatinine clearance (CrCl).
    The formula takes into account age, weight, gender, and serum creatinine levels.
    """
)

# Input fields
age = st.number_input("Age (years)", min_value=18, max_value=120, value=50)
weight = st.number_input("Weight (kg)", min_value=20.0, max_value=300.0, value=70.0)
gender = st.radio("Gender", ["Male", "Female"])
serum_creatinine = st.number_input("Serum Creatinine (mg/dL)", min_value=0.1, max_value=20.0, value=1.0, step=0.1)

# Calculate button
if st.button("Calculate Creatinine Clearance"):
    # Cockcroft-Gault formula
    # CrCl = [(140 - age) × weight] / (72 × SCr) × (0.85 if female)
    
    crcl = ((140 - age) * weight) / (72 * serum_creatinine)
    
    # Adjust for gender
    if gender == "Female":
        crcl *= 0.85
    
    # Round to 2 decimal places
    crcl = round(crcl, 2)
    
    # Display result
    st.subheader("Results")
    st.metric("Estimated Creatinine Clearance", f"{crcl} mL/min")
    
    # Interpretation
    st.subheader("Interpretation")
    if crcl >= 90:
        st.info("Normal kidney function")
    elif crcl >= 60:
        st.info("Mildly reduced kidney function")
    elif crcl >= 30:
        st.warning("Moderately reduced kidney function")
    elif crcl >= 15:
        st.warning("Severely reduced kidney function")
    else:
        st.error("Kidney failure")

st.divider()
st.markdown(
    """
    ### About the Cockcroft-Gault Formula
    
    The Cockcroft-Gault formula is a widely used method to estimate creatinine clearance.
    It's important to note that this is an estimate and may not be accurate for all patients,
    particularly those with:
    - Extremely high or low muscle mass
    - Severe malnutrition
    - Amputation
    - Ascites
    - Pregnancy
    
    Always consult with a healthcare professional for proper medical assessment.
    """
) 