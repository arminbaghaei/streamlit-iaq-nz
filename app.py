# app.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

# Page setup
st.set_page_config(page_title="NZ Indoor Air Quality Tool", page_icon="🏡", layout="wide", initial_sidebar_state="expanded")

# Sidebar - Input
with st.sidebar:
    st.title("📅 IAQ Evaluation Form")

    room_name = st.text_input("Room name/label", value="Living Room")
    num_occupants = st.number_input("Number of people using the room", 1, 12, 2)
    ventilation = st.selectbox("Ventilation type", ["No ventilation", "Window only", "Fan", "Mechanical ventilation", "HRV/ERV system"])
    mold_presence = st.radio("Visible mold or musty smell?", ["Yes", "No"])
    drying_clothes = st.selectbox("Do you dry clothes indoors?", ["Never", "Sometimes", "Often"])
    cooking_type = st.selectbox("Cooking method (if applicable)", ["None", "Electric stove", "Gas stove"])
    heating_type = st.selectbox("Primary heating type", ["None", "Portable gas heater", "Heat pump", "Electric heater", "Wood burner"])
    insulation_status = st.selectbox("Wall/Ceiling insulation", ["Good", "Partial", "Poor", "Unknown"])
    humidity_level = st.slider("Estimated indoor humidity (%)", 20, 90, 60)
    building_age = st.slider("Building age (years)", 0, 120, 30)
    is_renter = st.radio("Are you renting this property?", ["Yes", "No"])

# Scoring model
iaq_factors = {
    "Ventilation": 2 if ventilation == "No ventilation" else 1 if ventilation == "Window only" else 0,
    "Mold/Moisture": 2 if mold_presence == "Yes" else 0,
    "Drying habits": 2 if drying_clothes == "Often" else 1 if drying_clothes == "Sometimes" else 0,
    "Cooking source": 1 if cooking_type == "Gas stove" else 0,
    "Heating type": 2 if heating_type == "Portable gas heater" else 1 if heating_type == "None" else 0,
    "Insulation": 1 if insulation_status in ["Poor", "Unknown"] else 0,
    "Humidity": 1 if humidity_level >= 65 else 0,
    "Building age": 1 if building_age >= 60 else 0,
    "Occupants": 2 if num_occupants >= 4 else 1 if num_occupants == 3 else 0
}

iaq_score = sum(iaq_factors.values())

# Header & Radar Chart
st.markdown("""
    <div style='background-color:#00695c;padding:15px;border-radius:10px'>
        <h2 style='color:white;text-align:center;'>🏡 NZ Indoor Air Quality Assessment</h2>
    </div>
""", unsafe_allow_html=True)

st.write("Use this tool to evaluate and improve indoor air quality, tailored for NZ homes and rental conditions.")

# Radar chart to visualize score components
st.subheader("🔄 IAQ Risk Breakdown")
categories = list(iaq_factors.keys())
values = list(iaq_factors.values()) + [list(iaq_factors.values())[0]]
angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
ax.fill(angles, values, color='#26a69a', alpha=0.25)
ax.plot(angles, values, color='#00796b', linewidth=2)
ax.set_yticks([0, 1, 2])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories)
st.pyplot(fig)

# Score interpretation
st.subheader("🔍 Overall IAQ Risk")
if iaq_score >= 9:
    st.error("❌ High IAQ Risk: Immediate intervention recommended.")
elif iaq_score >= 5:
    st.warning("⚠️ Moderate IAQ Risk: Improvement needed.")
else:
    st.success("✅ Low IAQ Risk: No urgent concerns.")

# Recommendations
st.subheader("💡 Recommendations")
if ventilation == "No ventilation":
    st.markdown("- Install a fan or open windows daily for air exchange.")
if mold_presence == "Yes":
    st.markdown("- Identify and clean mold sources; use a dehumidifier.")
if drying_clothes != "Never":
    st.markdown("- Dry clothes outside or use a ventilated space.")
if cooking_type == "Gas stove":
    st.markdown("- Use a rangehood or ventilate while cooking.")
if heating_type == "Portable gas heater":
    st.markdown("- Avoid unflued gas heaters. Switch to dry heat sources.")
if insulation_status in ["Poor", "Unknown"]:
    st.markdown("- Improve insulation to reduce damp and heat loss.")
if humidity_level >= 65:
    st.markdown("- Maintain indoor RH below 60% with ventilation or dehumidifier.")
if num_occupants >= 4:
    st.markdown("- Higher occupancy needs more ventilation to control CO₂ and moisture.")
if is_renter == "Yes":
    st.markdown("- Check [Healthy Homes Standards](https://www.tenancy.govt.nz/healthy-homes/) for landlord responsibilities.")

# Footer
st.markdown("---")
st.caption("Developed as a demonstration IAQ tool. Not a substitute for professional indoor air assessments.")
