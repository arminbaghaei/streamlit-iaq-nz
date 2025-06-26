import streamlit as st
from PIL import Image

# --- Page config ---
st.set_page_config(
    page_title="NZ Indoor Air Quality Checker",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Sidebar Layout ---
with st.sidebar:
    # Optional logo (comment this line if you don't have a logo file)
    # st.image("your_logo.png", width=150)

    st.title("IAQ Survey")
    st.markdown("Answer the questions below to get an IAQ risk assessment for your room.")

    room = st.selectbox("Which room are you assessing?", ["Bedroom", "Living Room", "Kitchen", "Bathroom", "Other"])
    building_age = st.slider("Age of building (years)", 0, 120, 30)
    number_of_occupants = st.number_input("Number of people using this room", min_value=1, max_value=12, value=2)
    ventilation = st.selectbox("How is this room ventilated?", [
        "No ventilation", "Window only", "Fan", "Mechanical system", "HRV/ERV unit"
    ])
    mold = st.radio("Visible mold or musty smell?", ["Yes", "No"])
    drying = st.selectbox("Do you dry clothes inside?", ["Never", "Sometimes", "Often"])
    cooking = st.selectbox("Do you cook with gas appliances here?", ["No", "Yes"])
    heating = st.selectbox("Primary heating type", [
        "None", "Portable gas heater", "Heat pump", "Electric heater", "Wood burner"
    ])
    insulation = st.selectbox("Wall and ceiling insulation status", [
        "Good", "Partial", "Poor", "Unknown"
    ])
    humidity = st.slider("Estimated indoor humidity (%)", 20, 90, 60)
    is_renter = st.radio("Are you renting this property?", ["Yes", "No"])

# --- Header Banner ---
st.markdown("""
    <div style='background-color:#009688;padding:15px;border-radius:8px'>
        <h2 style='color:white;text-align:center;'>NZ Indoor Air Quality Checker</h2>
    </div>
""", unsafe_allow_html=True)

st.write("This tool helps you assess your room's indoor air quality and offers recommendations aligned with New Zealand housing conditions.")

# --- Scoring Logic ---
score = 0

# Risk scoring based on inputs
if ventilation == "No ventilation":
    score += 2
elif ventilation == "Window only":
    score += 1

if mold == "Yes":
    score += 2

if drying == "Often":
    score += 2
elif drying == "Sometimes":
    score += 1

if cooking == "Yes":
    score += 1

if heating == "Portable gas heater":
    score += 2
elif heating == "None":
    score += 1

if insulation in ["Poor", "Unknown"]:
    score += 1

if humidity >= 65:
    score += 1

if building_age > 60:
    score += 1

if number_of_occupants >= 4:
    score += 2
elif number_of_occupants == 3:
    score += 1

# --- Output Results ---
st.subheader("🔍 IAQ Risk Assessment")

if score >= 7:
    st.error("❌ High IAQ Risk: Immediate action recommended.")
elif score >= 4:
    st.warning("⚠️ Moderate IAQ Risk: Some improvements needed.")
else:
    st.success("✅ Low IAQ Risk: Conditions seem acceptable.")

# --- Personalized Recommendations ---
st.markdown("### 💡 Recommendations")

if ventilation == "No ventilation":
    st.markdown("- Improve airflow: open windows daily or consider installing fans or mechanical ventilation.")
if mold == "Yes":
    st.markdown("- Clean mold using safe methods. Identify and fix sources of excess moisture.")
if drying != "Never":
    st.markdown("- Avoid drying clothes indoors, or increase ventilation if you must.")
if cooking == "Yes":
    st.markdown("- Always ventilate during cooking, especially with gas stoves.")
if heating == "Portable gas heater":
    st.markdown("- Avoid unflued gas heaters. They release water vapor and pollutants. Use dry heat sources like heat pumps.")
if insulation in ["Poor", "Unknown"]:
    st.markdown("- Poor insulation contributes to dampness. Consider improving thermal performance.")
if humidity >= 65:
    st.markdown("- Use a dehumidifier or increase airflow. Try to keep indoor RH below 60%.")
if number_of_occupants >= 4:
    st.markdown("- With many people in a room, CO₂ and humidity rise quickly. Ensure consistent ventilation.")
if is_renter == "Yes":
    st.markdown("- Learn about your rights under the [Healthy Homes Standards](https://www.tenancy.govt.nz/healthy-homes/). Request improvements if needed.")

# --- Footer ---
st.markdown("---")
st.caption("This tool provides general guidance and should not replace professional building or health assessments.")
