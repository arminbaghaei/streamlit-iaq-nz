import streamlit as st
from PIL import Image

# Set page config
st.set_page_config(
    page_title="NZ Indoor Air Quality Checker",
    page_icon="🏠",
    layout="wide"
)

# Optional: Add logo in the sidebar
with st.sidebar:
    st.image("logo_placeholder.png", width=150)  # Replace with your logo file
    st.title("IAQ Checker NZ")
    st.markdown("---")
    st.markdown("### 🧭 Room Info")

    room = st.selectbox("Which room are you assessing?", [
        "Bedroom", "Living Room", "Kitchen", "Bathroom", "Other"
    ])
    building_age = st.slider("Approximate age of building (years)", 0, 100, 20)
    ventilation = st.selectbox("How is this room ventilated?", [
        "No ventilation", "Window only", "Fan", "Mechanical ventilation system"
    ])
    mold = st.radio("Have you seen any visible mold or smelled mustiness?", ["Yes", "No"])
    drying = st.selectbox("Do you dry clothes inside this room?", ["Never", "Sometimes", "Often"])
    cooking = st.selectbox("Do you cook with gas appliances in this room?", ["No", "Yes"])
    is_renter = st.radio("Are you renting this property?", ["Yes", "No"])

# Banner header
st.markdown("""
    <div style='background-color:#009688;padding:15px;border-radius:8px'>
        <h2 style='color:white;text-align:center;'>NZ Indoor Air Quality Checker</h2>
    </div>
""", unsafe_allow_html=True)

st.write("Use this tool to assess your indoor air quality and receive tips aligned with common housing challenges in New Zealand.")

# IAQ Score Calculation
score = 0
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
if building_age > 50:
    score += 1

# Results
st.subheader("🔍 IAQ Risk Assessment")

if score >= 6:
    st.error("❌ High IAQ Risk: Immediate attention recommended.")
elif score >= 3:
    st.warning("⚠️ Moderate IAQ Risk: Room for improvement.")
else:
    st.success("✅ Low IAQ Risk: Looks good!")

# Explanation section
st.markdown("### 💡 Personalized Recommendations")

if ventilation == "No ventilation":
    st.markdown("- Improve airflow by opening windows or using extractor fans.")
if mold == "Yes":
    st.markdown("- Clean mold using safe products. Investigate possible moisture sources.")
if drying != "Never":
    st.markdown("- Avoid indoor drying. Ventilate well if necessary.")
if cooking == "Yes":
    st.markdown("- Use a rangehood or keep a window open while cooking.")
if building_age > 50:
    st.markdown("- Older homes are prone to dampness. Check insulation, seals, and ventilation.")
if is_renter == "Yes":
    st.markdown("- You may be covered by the [Healthy Homes Standards](https://www.tenancy.govt.nz/healthy-homes/) for insulation, heating, and ventilation.")

# Footer
st.markdown("---")
st.caption("This tool provides general guidance only and is not a replacement for professional IAQ evaluation.")
