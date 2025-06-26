import streamlit as st
from PIL import Image

# --- Page config ---
st.set_page_config(
    page_title="NZ Indoor Air Quality Checker",
    page_icon="🏠",
    layout="wide",  # Ensures full width layout
    initial_sidebar_state="expanded"  # Makes sidebar open by default
)

# --- Sidebar Layout ---
with st.sidebar:
    # Optional logo (comment out if not used)
    # st.image("your_logo.png", width=150)

    st.title("IAQ Survey")
    st.markdown("Answer the questions below to get an IAQ risk assessment for your room.")

    # Expanded input options
    room = st.selectbox("Which room are you assessing?", ["Bedroom", "Living Room", "Kitchen", "Bathroom", "Other"])
    building_age = st.slider("Age of building (years)", 0, 120, 30)
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

st.write("This tool helps you assess your room's indoor air quality and offers recommendations aligned with New Zealand conditions.")

# --- Scoring Logic ---
score = 0

# Risk scoring
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
    st.markdown("- Clean mold promptly and reduce moisture with a dehumidifier or better ventilation.")
if drying != "Never":
    st.markdown("- Avoid drying clothes indoors or ensure strong airflow while doing so.")
if cooking == "Yes":
    st.markdown("- Ventilate while cooking, especially with gas. Use a rangehood or open a window.")
if heating == "Portable gas heater":
    st.markdown("- Avoid unflued gas heaters; they release moisture and CO. Switch to a dry heat source like a heat pump.")
if insulation in ["Poor", "Unknown"]:
    st.markdown("- Check your home’s insulation. Poor insulation leads to cold, damp conditions.")
if humidity >= 65:
    st.markdown("- Keep humidity below 60% using ventilation or a dehumidifier.")
if is_renter == "Yes":
    st.markdown("- You may be protected under the [Healthy Homes Standards](https://www.tenancy.govt.nz/healthy-homes/). Talk to your landlord if your home is damp or moldy.")

st.markdown("---")
st.caption("This tool is educational and does not replace professional IAQ or building inspections.")
