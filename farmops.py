import streamlit as st
import pandas as pd
import datetime
from PIL import Image

# Optional: For weather API, image recognition, or file storage
# import requests
# import tensorflow as tf
# import os

st.set_page_config(page_title="FarmOps App", layout="wide")

# App Header
st.markdown("## 🌾 FarmOps – Smart Integrated Farm Management System")
st.markdown("> Empowering Farmers with AI, Sustainability, and Simplicity.")
# --------------------------------------------
# 🚜 Farm Dashboard Input Section
# --------------------------------------------
# 🚜 Farm Dashboard Section
st.header("🌱 Farm Dashboard")

farm_name = st.text_input("Farm Name")
farm_size = st.number_input("Farm Size (in hectares)", min_value=0.1, step=0.1)
farm_location = st.text_input("Farm Location")

cropping_season = st.selectbox("Cropping Season", ["Wet Season", "Dry Season", "Year-round"])
season_phase = st.selectbox("Phase", ["Land Preparation", "Planting", "Growing", "Harvesting", "Post-Harvest"])

# Key metrics input
col1, col2, col3 = st.columns(3)
with col1:
    yield_estimate = st.number_input("Expected Yield (tons)", min_value=0.0, step=0.1)
with col2:
    labor_count = st.number_input("Labor Used", min_value=0, step=1)
with col3:
    budget_alloc = st.number_input("Budget (PHP)", min_value=0.0, step=100.0)

# Optional metrics
col4, col5 = st.columns(2)
with col4:
    soil_status = st.selectbox("Soil Condition", ["Good", "Moderate", "Poor"])
with col5:
    weather_snapshot = st.selectbox("Weather Today", ["Sunny", "Cloudy", "Rainy", "Storm", "Dry"])

# Show Alert (Demo Purpose)
if soil_status == "Poor":
    st.warning("⚠️ Soil condition is poor. Consider applying organic compost.")
if weather_snapshot == "Storm":
    st.error("🌩️ Severe weather warning. Delay field operations today.")

st.markdown("### 🧭 Farm Dashboard: Basic Farm Information")

# Farm Details Input
farm_name = st.text_input("Farm Name", "AgriVigor Demo Farm")
farm_size = st.number_input("Farm Size (in sq.m)", min_value=1, value=1000)
farm_location = st.text_input("Farm Location", "Suriname")

# Cropping Season Tracker
st.markdown("#### 🌱 Cropping Season")
season_start = st.date_input("Season Start Date", datetime.date.today())
season_end = st.date_input("Season End Date", datetime.date.today())

# Key Farm Metrics (Placeholder visuals)
st.markdown("#### 📊 Key Metrics")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Estimated Yield", "2,000 kg", "↑ 10%")
col2.metric("Budget Usage", "$1,200", "- 5%")
col3.metric("Labor Hours", "320 hrs", "↑ 2%")
col4.metric("ESG Score", "75 / 100")

# Weather Snapshot (Static Placeholder)
st.info("🌤️ Weather Snapshot: 29°C, Humid, Cloudy – Ideal for field prep.")

# Soil Condition (Placeholder)
st.success("🧪 Soil Condition: Sandy Loam, pH 6.5, Good drainage")
# --- Smart Crop Calendar ---
import datetime

st.header("📆 Smart Crop Calendar")

crop_list = [
    "Turmeric", "Annatto", "Butterfly Pea", "Hibiscus", "Neem", "Moringa",
    "Aloe Vera", "Ginger", "Ashwagandha", "Lemongrass", "Purple Sweet Potato",
    "Cassava", "Yellow Malanga", "Groundnuts", "Bitter Gourd",
    "Tomato", "Eggplant", "Bell Pepper", "Chili Pepper", "Soursop", "Watermelon"
]

# User Input
crop = st.selectbox("Select Crop", sorted(crop_list))
planting_date = st.date_input("Select Planting Date", datetime.date.today())

# Crop durations (in days)
crop_durations = {
    "Turmeric": 240, "Annatto": 180, "Butterfly Pea": 90, "Hibiscus": 100,
    "Neem": 365, "Moringa": 90, "Aloe Vera": 150, "Ginger": 210, "Ashwagandha": 180,
    "Lemongrass": 120, "Purple Sweet Potato": 120, "Cassava": 300,
    "Yellow Malanga": 270, "Groundnuts": 110, "Bitter Gourd": 70,
    "Tomato": 90, "Eggplant": 100, "Bell Pepper": 90, "Chili Pepper": 120,
    "Soursop": 365, "Watermelon": 90
}

# Compute harvest date
duration = crop_durations.get(crop, 90)
harvest_date = planting_date + datetime.timedelta(days=duration)

# Companion planting tips
companions = {
    "Tomato": ["Basil", "Carrot"],
    "Cassava": ["Lemongrass", "Groundnuts"],
    "Moringa": ["Sweet Potato", "Legumes"],
    "Ginger": ["Turmeric", "Chili Pepper"],
    "Turmeric": ["Ginger", "Lemongrass"],
    "Eggplant": ["Beans", "Basil"],
    "Watermelon": ["Corn", "Radish"]
}
companion_suggestions = companions.get(crop, ["No known companion crops."])

# Display Calendar Summary
st.subheader("📋 Crop Calendar Summary")
st.write(f"**Crop:** {crop}")
st.write(f"**Planting Date:** {planting_date.strftime('%B %d, %Y')}")
st.write(f"**Expected Harvest:** {harvest_date.strftime('%B %d, %Y')}")
st.write(f"**Growing Duration:** {duration} days")

# Weather warning
if planting_date.month in [7, 8, 9]:
    st.warning("⚠️ July–September is typhoon season. Consider using raised beds or rain shields.")

# Companion suggestion
st.success(f"🌿 Suggested Companions for {crop}: {', '.join(companion_suggestions)}")

# Field Operation Reminders
st.markdown("### ✅ Field Operations Reminder")
st.markdown("""
- **Land Preparation:** 7 days before planting  
- **Fertilizer Application:** 2–3 weeks after planting  
- **Pest & Disease Scouting:** Every 7–10 days  
- **Harvest Planning:** 1 week before harvest date  
""")
st.header("📅 Smart Crop Calendar")

# Crop master list
crop_list = [
    "Turmeric", "Annatto", "Butterfly Pea", "Hibiscus", "Neem", "Moringa", "Aloe Vera", "Ginger", "Ashwagandha", "Lemongrass",
    "Purple Sweet Potato", "Cassava", "Yellow Malanga", "Groundnuts",
    "Bitter Gourd", "Tomato", "Eggplant", "Bell Pepper", "Chili Pepper",
    "Soursop", "Watermelon"
]

# Crop selection
crop = st.selectbox("🌱 Select your crop:", crop_list)

# Planting date
planting_date = st.date_input("📆 Select planting date:")

# Optional crop growth duration (you can later adjust this with AI)
growth_durations = {
    "Turmeric": 240,
    "Moringa": 90,
    "Tomato": 100,
    "Cassava": 300,
    "Butterfly Pea": 75,
    "Eggplant": 120,
    "Watermelon": 80,
    "Ginger": 180,
    "Bitter Gourd": 100,
    "Bell Pepper": 120,
    "Chili Pepper": 120,
    "Groundnuts": 110,
    "Lemongrass": 150,
    "Aloe Vera": 365,
    "Soursop": 540,
    "Neem": 730,
    "Annatto": 360,
    "Yellow Malanga": 210,
    "Ashwagandha": 150,
    "Hibiscus": 120
}

# Calculate expected harvest
days_to_harvest = growth_durations.get(crop, 100)  # Default to 100 days
harvest_date = planting_date + datetime.timedelta(days=days_to_harvest)

# Display Calendar Summary
st.subheader("📌 Crop Calendar Summary")
st.write(f"**Crop:** {crop}")
st.write(f"**Planting Date:** {planting_date.strftime('%B %d, %Y')}")
st.write(f"**Expected Harvest:** {harvest_date.strftime('%B %d, %Y')}")
st.write(f"**Growing Duration:** {days_to_harvest} days")
# 🌱 Smart Crop Calendar – AI-Powered Planner
st.markdown("## 📅 Smart Crop Calendar")

# Final crop master list
crop_list = [
    "Turmeric", "Annatto", "Butterfly Pea", "Hibiscus", "Neem", "Moringa", "Aloe Vera", "Ginger",
    "Ashwagandha", "Lemongrass", "Purple Sweet Potato", "Cassava", "Yellow Malanga", "Groundnuts",
    "Bitter Gourd", "Tomato", "Eggplant", "Bell Pepper", "Chili Pepper", "Soursop", "Watermelon"
]

crop = st.selectbox("🌾 Select your crop:", crop_list)
planting_date = st.date_input("📆 Select planting date:", datetime.date.today())

# Simple maturity lookup table
maturity_days = {
    "Turmeric": 240, "Annatto": 180, "Butterfly Pea": 75, "Hibiscus": 100, "Neem": 365,
    "Moringa": 90, "Aloe Vera": 240, "Ginger": 210, "Ashwagandha": 150, "Lemongrass": 120,
    "Purple Sweet Potato": 120, "Cassava": 300, "Yellow Malanga": 270, "Groundnuts": 110,
    "Bitter Gourd": 90, "Tomato": 90, "Eggplant": 100, "Bell Pepper": 90, "Chili Pepper": 120,
    "Soursop": 365, "Watermelon": 80
}

harvest_date = planting_date + datetime.timedelta(days=maturity_days.get(crop, 90))
duration = (harvest_date - planting_date).days

st.success(f"🗓️ Expected Harvest Date: **{harvest_date.strftime('%B %d, %Y')}**")
st.info(f"🌱 Growing Duration: **{duration} days**")
# 🤖 AI-Based Decision Support
st.markdown("## 🤖 AI-Based Decision Support")

st.write("Get smart suggestions for your selected crop.")

soil_type = st.selectbox("🧪 Select Soil Type", ["Loamy", "Sandy", "Clayey", "Silty"])
location = st.selectbox("📍 Select Location", ["Suriname – Lowland", "Suriname – Highlands"])
elevation = st.slider("🗻 Farm Elevation (meters above sea level)", 0, 1000, 200)

# AI logic (simplified rule-based system)
best_months = {
    "Turmeric": "May–June", "Cassava": "March–May", "Moringa": "June–July",
    "Ginger": "April–June", "Hibiscus": "July–August", "Aloe Vera": "Anytime",
    "Bitter Gourd": "June–July", "Watermelon": "April–May"
}

fertilizer_tips = {
    "Loamy": "Compost + Vermicast", "Sandy": "Chicken manure + Biochar",
    "Clayey": "Decomposed FYM + Lime", "Silty": "Compost + Seaweed extract"
}

st.success(f"🌿 Best Planting Period for {crop}: **{best_months.get(crop, 'Data not available')}**")
st.info(f"🌱 Recommended Organic Inputs: **{fertilizer_tips.get(soil_type, 'Use compost')}**")

# Crop mismatch logic
if crop in ["Cassava", "Tomato", "Eggplant"] and soil_type == "Clayey":
    st.warning("⚠️ Clayey soil may cause poor root development for this crop.")
# Section: Smart Crop Calendar - Step 1
st.markdown("### 🌱 Smart Crop Calendar")
st.markdown("Create an AI-guided calendar for your organic crops.")

# Crop selection
crops = [
    "Turmeric (Curcuma longa)", "Annatto (Bixa orellana)", "Butterfly Pea (Clitoria ternatea)",
    "Hibiscus (Hibiscus sabdariffa)", "Neem", "Moringa", "Aloe Vera", "Ginger", "Ashwagandha",
    "Lemongrass", "Purple Sweet Potato", "Cassava", "Yellow Malanga", "Groundnuts",
    "Bitter Gourd", "Tomato", "Eggplant", "Bell Pepper", "Chili Pepper", "Soursop", "Watermelon"
]

crop = st.selectbox("🌿 Select Crop", crops)
planting_date = st.date_input("📅 Select Planting Date", datetime.date.today())
harvest_date = st.date_input("🌾 Select Expected Harvest Date", datetime.date.today())
field_location = st.text_input("📍 Field Location (e.g., Plot A, GPS)", "")
field_size = st.number_input("🌾 Field Size (hectares)", min_value=0.1, step=0.1)

# Save data to DataFrame
if 'calendar_data' not in st.session_state:
    st.session_state['calendar_data'] = []

if st.button("➕ Add to Calendar"):
    st.session_state['calendar_data'].append({
        "Crop": crop,
        "Planting Date": planting_date,
        "Harvest Date": harvest_date,
        "Location": field_location,
        "Size (ha)": field_size
    })
    st.success(f"{crop} added to your smart crop calendar!")

# Display the crop calendar
if st.session_state['calendar_data']:
    df = pd.DataFrame(st.session_state['calendar_data'])
    st.dataframe(df)
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import datetime

# Page Setup
st.set_page_config(page_title="FarmOps – Smart Crop Calendar", layout="wide")
st.title("🌾 Smart Crop Calendar & AI Recommendations")

# Crop Master List
crop_data = [
    {"Crop": "Turmeric", "Planting": "2025-07-01", "Harvest": "2026-01-01"},
    {"Crop": "Moringa", "Planting": "2025-07-05", "Harvest": "2025-10-05"},
    {"Crop": "Aloe Vera", "Planting": "2025-08-01", "Harvest": "2026-02-01"},
    {"Crop": "Cassava", "Planting": "2025-07-20", "Harvest": "2026-01-20"},
    {"Crop": "Hibiscus", "Planting": "2025-09-01", "Harvest": "2026-01-01"},
    {"Crop": "Neem", "Planting": "2025-07-15", "Harvest": "2026-01-15"},
    {"Crop": "Groundnuts", "Planting": "2025-08-10", "Harvest": "2025-12-10"},
    {"Crop": "Watermelon", "Planting": "2025-07-10", "Harvest": "2025-10-10"},
]

df = pd.DataFrame(crop_data)
df["Planting"] = pd.to_datetime(df["Planting"])
df["Harvest"] = pd.to_datetime(df["Harvest"])

# Crop Calendar Visualization
st.subheader("📅 Crop Calendar Timeline")
fig, ax = plt.subplots(figsize=(10, 5))
for i, row in df.iterrows():
    ax.barh(row["Crop"], (row["Harvest"] - row["Planting"]).days, left=row["Planting"])
ax.set_xlabel("Date")
ax.set_ylabel("Crop")
plt.tight_layout()
st.pyplot(fig)

# AI Recommendations
st.subheader("🤖 AI Recommendations")

def get_recommendation(crop):
    match crop:
        case "Turmeric":
            return "Best in July. Companion: Ginger. Avoid Cassava."
        case "Moringa":
            return "Best in June–August. Companion: Lemongrass. Avoid Annatto."
        case "Aloe Vera":
            return "Best in June–September. Companion: Neem. Avoid Soursop."
        case "Cassava":
            return "Best in May–July. Companion: Groundnuts. Avoid Turmeric."
        case "Hibiscus":
            return "Best in July–August. Companion: Butterfly Pea."
        case "Neem":
            return "Best in Rainy Season. Companion: Aloe Vera. Avoid Watermelon."
        case "Groundnuts":
            return "Best in May–August. Companion: Cassava."
        case "Watermelon":
            return "Best in April–July. Avoid Neem nearby."
        case _:
            return "No specific data available."

selected_crop = st.selectbox("🔍 Select a crop to get AI recommendations:", df["Crop"].unique())
if selected_crop:
    st.info(get_recommendation(selected_crop))
# Organic input suggestions
def suggest_inputs(crop, soil):
    if crop == "Turmeric":
        return {"Fertilizer": "Vermicompost + Indigenous Microorganisms (IMO)", "Rate": "5 tons/ha"}
    elif crop == "Moringa":
        return {"Fertilizer": "Decomposed Animal Manure + Seaweed Extract", "Rate": "4 tons/ha"}
    elif crop == "Cassava":
        return {"Fertilizer": "Composted Poultry Manure + Biochar", "Rate": "6 tons/ha"}
    elif crop == "Aloe Vera":
        return {"Fertilizer": "Cocopeat + Vermicast", "Rate": "4 tons/ha"}
    elif crop == "Neem":
        return {"Fertilizer": "Neem Cake + Trichoderma-enriched compost", "Rate": "3 tons/ha"}
    else:
        return {"Fertilizer": "Fermented Plant Juice (FPJ) + Bokashi", "Rate": "3-5 tons/ha"}
import pandas as pd
import streamlit as st
from datetime import datetime

# --- FARM MAPPING & LOGBOOK ---
st.header("🌍 Farm Mapping & Field Logbook")

# Initialize field data if not present
if "field_data" not in st.session_state:
    st.session_state.field_data = []

# Input Form
with st.form("field_mapping_form"):
    st.subheader("📝 Add New Field")
    field_name = st.text_input("Field Name")
    area = st.number_input("Area (hectares)", min_value=0.0, step=0.1)
    field_type = st.selectbox("Zone Type", ["Irrigated", "Rainfed", "Buffer Zone", "Organic Zone", "Others"])
    image = st.file_uploader("Upload Image (Optional)", type=["jpg", "png"])
    submitted = st.form_submit_button("Add Field")

    if submitted and field_name:
        st.session_state.field_data.append({
            "Field Name": field_name,
            "Area (ha)": area,
            "Zone Type": field_type,
            "Image": image,
            "Logs": []
        })
        st.success(f"Field '{field_name}' added!")

# Display and manage fields
st.subheader("📍 Your Mapped Fields")
for i, field in enumerate(st.session_state.field_data):
    st.markdown(f"**{field['Field Name']}** ({field['Area (ha)']} ha, {field['Zone Type']})")
    if field["Image"]:
        st.image(field["Image"], caption="Field Image", use_column_width=True)

    # Add log entry
    with st.expander("➕ Add Log Entry"):
        log_note = st.text_area(f"Log for {field['Field Name']}", key=f"log_{i}")
        log_date = st.date_input("Date", datetime.today(), key=f"date_{i}")
        if st.button(f"Save Log for {field['Field Name']}", key=f"save_log_{i}"):
            field["Logs"].append({"Date": log_date.strftime("%Y-%m-%d"), "Note": log_note})
            st.success("Log saved.")

    # View logs
    with st.expander("📖 View Logbook"):
        if field["Logs"]:
            df_logs = pd.DataFrame(field["Logs"])
            st.table(df_logs)
        else:
            st.info("No logs recorded yet.")

