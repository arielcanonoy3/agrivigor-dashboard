import streamlit as st
import datetime

# Dummy data
farm_name = "AgriVigor Green Farm"
farm_location = "Suriname - Plot 001"
current_season = "Rainy Season"
start_date = datetime.date(2025, 7, 1)
end_date = datetime.date(2025, 12, 31)
total_area = 500  # in hectares

# Dummy metrics
yield_goal = "50 tons"
labor_used = "120 labor-days"
budget_used = "$45,000 / $100,000"
esg_score = "B+"
weather_status = "Mostly Sunny"
soil_status = "Moist, pH 6.5"

# Streamlit app layout
st.set_page_config(page_title="FarmOps - Farm Dashboard", layout="wide")
st.title("🌿 FarmOps | Farm Dashboard")

# Section: Farm Identity and Season
with st.container():
    st.subheader("📍 Farm Information")
    st.markdown(f"**Farm Name:** {farm_name}")
    st.markdown(f"**Location:** {farm_location}")
    st.markdown(f"**Season:** {current_season} ({start_date} to {end_date})")
    st.markdown(f"**Total Area:** {total_area} hectares")

# Section: Metrics Overview
with st.container():
    st.subheader("📊 Key Performance Metrics")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("🎯 Yield Goal", yield_goal)
    col2.metric("👨‍🌾 Labor Used", labor_used)
    col3.metric("💰 Budget", budget_used)
    col4.metric("✅ ESG Score", esg_score)

# Section: Current Conditions
with st.container():
    st.subheader("🌤️ Real-time Farm Conditions")
    col1, col2 = st.columns(2)
    col1.info(f"**Weather:** {weather_status}")
    col2.success(f"**Soil Status:** {soil_status}")

# -----------------------------------
# MODULE 2: SMART CROP CALENDAR
# -----------------------------------

import pandas as pd

# Dummy crop maturity data in days
crop_data = {
    "Turmeric": 270,
    "Ginger": 240,
    "Lemongrass": 180,
    "Moringa": 90,
    "Aloe Vera": 365,
    "Ashwagandha": 180,
    "Neem": 365,
    "Hibiscus": 150,
    "Butterfly Pea": 120,
    "Soursop": 365,
    "Banana": 300,
    "Papaya": 270,
    "Dragon Fruit": 180,
    "Watermelon": 90,
    "Purple Sweet Potato": 120,
    "Cassava": 300,
    "Yellow Malanga": 240,
    "Groundnuts": 110,
    "Bitter Gourd": 90,
    "Tomato": 90,
    "Eggplant": 120,
    "Rice": 120,
    "Corn": 100,
    "Sugarcane": 360,
    "Coffee": 365,
    "Cacao": 365
}

st.markdown("---")
st.header("📅 Smart Crop Calendar")

# Input fields
selected_crop = st.selectbox("Choose a crop", list(crop_data.keys()))
planting_date = st.date_input("Select planting date")

if selected_crop and planting_date:
    maturity_days = crop_data[selected_crop]
    harvest_date = planting_date + datetime.timedelta(days=maturity_days)

    st.success(f"Estimated Harvest Date: **{harvest_date.strftime('%B %d, %Y')}**")

    # Task schedule logic (basic AI-style)
    tasks = [
        {"Task": "Land Preparation", "Days After Planting": 0},
        {"Task": "Sowing/Transplanting", "Days After Planting": 7},
        {"Task": "Weeding", "Days After Planting": 21},
        {"Task": "Organic Fertilization", "Days After Planting": 30},
        {"Task": "Pest & Disease Monitoring", "Days After Planting": 45},
        {"Task": "Second Fertilization", "Days After Planting": 60},
        {"Task": "Pre-Harvest Inspection", "Days After Planting": maturity_days - 10},
        {"Task": "Harvesting", "Days After Planting": maturity_days}
    ]

    # Create schedule
    task_schedule = []
    for task in tasks:
        task_date = planting_date + datetime.timedelta(days=task["Days After Planting"])
        task_schedule.append({
            "Task": task["Task"],
            "Scheduled Date": task_date.strftime('%Y-%m-%d')
        })

    df = pd.DataFrame(task_schedule)
    st.write("📋 Recommended Task Schedule")
    st.table(df)

# -----------------------------------
# MODULE 3: AI DECISION SUPPORT (SURINAME VERSION)
# -----------------------------------

st.markdown("---")
st.header("🤖 AI Decision Support (Tropical Zones)")

# Suriname's seasons (simplified)
# Long Dry: Aug–Nov, Short Dry: Feb–Mar, Long Rainy: Apr–Aug, Short Rainy: Nov–Feb

# Updated planting guide based on Suriname’s climate
suriname_crop_windows = {
    "Rice": "April to August (Rainy Season – irrigated varieties)",
    "Corn": "February to March (Short Dry Season) or August to October (Long Dry Season)",
    "Sugarcane": "August to November (Long Dry Season)",
    "Turmeric": "May to July (Early Rainy Season)",
    "Ginger": "May to June (Early Rainy)",
    "Lemongrass": "Anytime – prefers warm, moist weather",
    "Moringa": "February to April (Dry Season)",
    "Aloe Vera": "March to May (Dry Season preferred)",
    "Ashwagandha": "June to August (Late Rainy Season)",
    "Neem": "June to August – during rainy months",
    "Hibiscus": "July to September (Rainy Season)",
    "Butterfly Pea": "August to November (Dry with light moisture)",
    "Soursop": "April to July (Rainy Season)",
    "Banana": "Year-round with irrigation support",
    "Papaya": "March to June (Transition to Rainy)",
    "Dragon Fruit": "March to May (Dry Season)",
    "Watermelon": "December to March (Short Rainy → Dry)",
    "Purple Sweet Potato": "May to July (Mid Rainy)",
    "Cassava": "August to October (Dry preferred)",
    "Yellow Malanga": "April to June (Rainy Season)",
    "Groundnuts": "February to April (Short Dry Season)",
    "Bitter Gourd": "November to January (Short Rainy)",
    "Tomato": "October to December (Transition to Rainy)",
    "Eggplant": "November to February (Short Rainy)",
    "Coffee": "June to August (needs high elevation)",
    "Cacao": "September to November (humid Dry Season)"
}

# Companion crops and soil compatibility (same as before)
# ... (reuse from earlier code, or ask me if you need them refreshed)

# Input form
soil_compatibility = {
    "Rice": ["Clay", "Loam"],
    "Corn": ["Loam", "Sandy Loam"],
    "Sugarcane": ["Loamy", "Silty"],
    "Turmeric": ["Loamy", "Well-drained"],
    "Ginger": ["Sandy Loam"],
    "Moringa": ["Sandy", "Loamy"],
    "Cassava": ["Sandy", "Loam"],
    "Cacao": ["Loam", "Clay Loam"],
    "Coffee": ["Volcanic", "Loamy"],
    "Tomato": ["Loam", "Sandy Loam"],
    "Banana": ["Loamy", "Well-drained"],
    "Groundnuts": ["Sandy", "Sandy Loam"],
    "Dragon Fruit": ["Sandy", "Well-drained"],
    "Hibiscus": ["Loam", "Sandy Loam"],
    "Eggplant": ["Loam", "Clay Loam"],
    "Papaya": ["Well-drained", "Sandy Loam"],
    "Yellow Malanga": ["Loam", "Clay Loam"],
    "Butterfly Pea": ["Loam", "Sandy"],
    "Soursop": ["Loam", "Sandy Loam"]
}
with st.form("ai_support"):
    selected_crop = st.selectbox("🌾 Select your crop", list(suriname_crop_windows.keys()))
    soil_type = st.selectbox("🧪 Select your soil type", ["Clay", "Loam", "Sandy", "Sandy Loam", "Volcanic", "Well-drained", "Silty"])
    elevation = st.number_input("⛰️ Enter your elevation (meters above sea level)", min_value=0, max_value=3000, value=100)
    submitted = st.form_submit_button("Get AI Recommendations")

if submitted:
    # Planting Window
    st.success(f"🌿 Best Planting Time for **{selected_crop}** in Suriname: {suriname_crop_windows[selected_crop]}")

    # Climate Suitability Confirmation
    st.info("🌴 This crop is suitable for **tropical environments** like **Suriname and the Caribbean.**")

    # Companion crops output (add dictionary as needed)
    if 'companion_crops' in globals() and selected_crop in companion_crops:
        st.info(f"👫 Companion Crops: {', '.join(companion_crops[selected_crop])}")

    # Soil compatibility
    if selected_crop in soil_compatibility:
        if soil_type in soil_compatibility[selected_crop]:
            st.success("✅ Soil type is compatible with this crop.")
        else:
            st.warning("⚠️ Soil type is not ideal for this crop. Consider improving soil conditions or crop switching.")

    # Elevation warnings
    if selected_crop == "Coffee" and elevation < 800:
        st.warning("⚠️ Coffee prefers highland areas above 800m. Yield and quality may suffer.")
    elif selected_crop == "Rice" and elevation > 500:
        st.warning("⚠️ Rice grows best in lowland areas. Consider upland varieties if above 500m.")
    else:
        st.success("✅ Elevation is within acceptable range.")

    # Organic input suggestion
    st.markdown("♻️ **AI Organic Input Suggestion:**")
    st.code("Use compost, fermented plant juice (FPJ), vermitea, and neem-based biopesticide for organic management.")


import folium
from streamlit_folium import st_folium
from shapely.geometry import shape
from datetime import datetime

st.markdown("---")
st.header("🗺️ Farm Mapping & Field Activity Logbook")

m = folium.Map(location=[4.0, -56.0], zoom_start=6)

from folium.plugins import Draw
Draw(export=True, filename='field.geojson').add_to(m)

map_data = st_folium(m, width=700, height=450, returned_objects=["all_drawings"])

if "field_logs" not in st.session_state:
    st.session_state["field_logs"] = []

st.subheader("📋 Tag Activity to Drawn Shape")

with st.form("log_form"):
    plot_name = st.text_input("Plot Name / Field ID")
    activity = st.text_input("Activity (e.g. Planted turmeric)")
    notes = st.text_area("Notes or remarks")
    activity_date = st.date_input("Date of activity", value=datetime.today())
    submitted = st.form_submit_button("Add to Log")

    if submitted:
        if map_data and map_data["all_drawings"]:
            geometry = map_data["all_drawings"][-1]["geometry"]
            geo_type = geometry["type"]
            geo_coords = geometry["coordinates"]

            st.session_state["field_logs"].append({
                "Plot": plot_name,
                "Activity": activity,
                "Date": str(activity_date),
                "Notes": notes,
                "Shape Type": geo_type,
                "Coordinates": str(geo_coords)
            })
            st.success("✅ Log entry added with shape.")
        else:
            st.warning("⚠️ Please draw a shape on the map before submitting.")

if st.session_state["field_logs"]:
    st.subheader("📒 Field Activity Logbook")
    st.table(st.session_state["field_logs"])

import folium
from streamlit_folium import st_folium
from shapely.geometry import shape
from datetime import datetime

st.markdown("---")
st.header("🗺️ Farm Mapping & Field Activity Logbook")

m = folium.Map(location=[4.0, -56.0], zoom_start=6)

from folium.plugins import Draw
Draw(export=True, filename='field.geojson').add_to(m)

map_data = st_folium(m, width=700, height=450, returned_objects=["all_drawings"])

if "field_logs" not in st.session_state:
    st.session_state["field_logs"] = []

st.subheader("📋 Tag Activity to Drawn Shape")

with st.form("log_form"):
    plot_name = st.text_input("Plot Name / Field ID")
    activity = st.text_input("Activity (e.g. Planted turmeric)")
    notes = st.text_area("Notes or remarks")
    activity_date = st.date_input("Date of activity", value=datetime.today())
    submitted = st.form_submit_button("Add to Log")

    if submitted:
        if map_data and map_data["all_drawings"]:
            geometry = map_data["all_drawings"][-1]["geometry"]
            geo_type = geometry["type"]
            geo_coords = geometry["coordinates"]

            st.session_state["field_logs"].append({
                "Plot": plot_name,
                "Activity": activity,
                "Date": str(activity_date),
                "Notes": notes,
                "Shape Type": geo_type,
                "Coordinates": str(geo_coords)
            })
            st.success("✅ Log entry added with shape.")
        else:
            st.warning("⚠️ Please draw a shape on the map before submitting.")

if st.session_state["field_logs"]:
    st.subheader("📒 Field Activity Logbook")
    st.table(st.session_state["field_logs"])

