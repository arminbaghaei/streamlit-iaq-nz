import streamlit as st
import pandas as pd

# Set up the page
st.set_page_config(page_title="IAQ Checker NZ", layout="centered")

# Title and intro
st.title("🏠 Indoor Air Quality Checker (NZ)")
st.markdown("This tool helps you quickly assess the indoor air quality (IAQ) of a room in your house and gives you simple, science-based recommendations.")

# Step 1: User inputs
st.header("📝 Room Information")
room = st.selectbox("Which room are you assessing?", ["Bedroom", "Living Room", "Kitchen", "Bathroom", "Other"])
building_age = st.slider("Approximate age of building (years)", 0, 100, 20)
ventilation = st.selectbox("How is this room ventilated?", [
    "No ventilation", "Window only", "Fan", "Mechanical ventilation system"
])
mold = st.radio("Have you seen any visible mold or smelled mustiness?", ["Yes", "No"])
drying = st.selectbox("Do you dry clothes inside this room?", ["Never", "Sometimes", "Often"])
cooking = st.selectbox("Do you cook with gas appliances in this room?", ["No", "Yes"])

# Step 2: Scoring
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

# Step 3: Show result
st.header("🔍 IAQ Risk Assessment")
if score >= 6:
    st.error("❌ High IAQ Risk: Immediate action recommended.")
elif score >= 3:
    st.warning("⚠️ Moderate IAQ Risk: Some improvement needed.")
else:
    st.success("✅ Low IAQ Risk: Conditions seem acceptable.")

# Step 4: Recommendations
st.header("💡 Recommendations")

if ventilation == "No ventilation":
    st.markdown("- Improve ventilation: open windows regularly or install a fan.")
if mold == "Yes":
    st.markdown("- Clean moldy areas safely. Use a dehumidifier to reduce moisture.")
if drying != "Never":
    st.markdown("- Avoid drying clothes indoors. It increases indoor humidity.")
if cooking == "Yes":
    st.markdown("- Ensure proper ventilation while cooking. Use a range hood or open a window.")
if building_age > 50:
    st.markdown("- Older homes may have poor insulation and hidden leaks. Consider professional assessment.")

# Footer
st.markdown("---")
st.caption("Note: This tool provides a basic screening for educational purposes only. For serious concerns, consult a qualified building or health professional.")
