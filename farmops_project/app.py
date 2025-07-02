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


# -------------------- MODULE 3: AI Decision Support --------------------

import streamlit as st

st.markdown("---")
st.header("🤖 AI Decision Support: Organic Input and Elevation Advice")

# Load selected crop and elevation from session state or fallback
selected_crop = st.session_state.get("selected_crop", st.selectbox("Select a crop", [
    "Rice", "Corn", "Sugarcane", "Turmeric", "Ginger", "Lemongrass", "Moringa", "Aloe Vera", "Ashwagandha",
    "Neem", "Hibiscus", "Butterfly Pea", "Soursop", "Banana", "Papaya", "Dragon Fruit", "Watermelon",
    "Purple Sweet Potato", "Cassava", "Yellow Malanga", "Groundnuts", "Bitter Gourd", "Tomato", "Eggplant",
    "Coffee", "Cacao"
]))
elevation = st.session_state.get("elevation", st.number_input("Enter your elevation (meters above sea level)", min_value=0, max_value=3000, value=100))

# Save inputs to session state
st.session_state["selected_crop"] = selected_crop
st.session_state["elevation"] = elevation

# Elevation Suitability Check
st.subheader("📏 Elevation Suitability")

if selected_crop == "Coffee" and elevation < 800:
    st.warning("⚠️ Coffee prefers highland areas above 800m. Yield and quality may be low.")
elif selected_crop == "Rice" and elevation > 500:
    st.warning("⚠️ Rice grows best in lowland areas. Consider upland rice varieties.")
else:
    st.success("✅ Elevation is within acceptable range for the selected crop.")

# Organic Input Suggestions for All Priority Crops
st.subheader("♻️ Organic Input Suggestions")

organic_inputs = {
    "Turmeric": "Apply compost + Trichoderma + fermented ginger extract; avoid water-logging.",
    "Ginger": "Use compost, FPJ (fermented plant juice), and ash tea for pest deterrence.",
    "Lemongrass": "Apply compost + neem cake; spacing improves aroma oil production.",
    "Moringa": "Use vermicast + IMO (Indigenous Microorganisms) and foliar seaweed extract.",
    "Aloe Vera": "Apply compost + ash + EM-1; best with minimal moisture.",
    "Ashwagandha": "Use compost + turmeric leaf mulch + neem leaf extract for pests.",
    "Neem": "No external inputs needed; thrives in marginal land. Add compost if desired.",
    "Hibiscus": "Use compost + vermitea; supports flowering and deep red calyces.",
    "Butterfly Pea": "Add compost + ash solution spray; drought-tolerant legume.",

    "Soursop": "Apply compost + Trichoderma + fruit peel FPJ; control mealybugs organically.",
    "Banana": "Use compost + chopped pseudo-stem mulch + potassium foliar (banana ash tea).",
    "Papaya": "Apply FAA (fish amino acid) + EM-1 + compost; control root rot with Trichoderma.",
    "Dragon Fruit": "Use vermicast + banana peel FPJ + Trichoderma soil drench.",
    "Watermelon": "Apply compost + seaweed foliar + rice hull ash before flowering.",

    "Purple Sweet Potato": "Use compost + biochar + IMO; mulch with rice straw.",
    "Cassava": "Add compost + wood ash; avoid over-irrigation during tuber bulking.",
    "Yellow Malanga": "Use compost + leaf litter mulch; EM-1 helps reduce root rot.",

    "Groundnuts": "Use compost + Rhizobium inoculant + molasses; rotate with maize.",

    "Bitter Gourd": "Apply compost + neem oil spray + Trichoderma soil application.",
    "Tomato": "Use compost + vermicast + basil interplanting; neem foliar to prevent fruit borer.",
    "Eggplant": "Apply compost + ash foliar + marigold border to deter pests.",

    "Rice": "Use Azolla + compost + Trichoderma + fermented coconut water.",
    "Corn": "Apply compost + FFJ (fermented fruit juice) + charcoal-dust banding.",
    "Sugarcane": "Use press mud + Trichoderma + sugarcane sett treatment with cow urine.",

    "Coffee": "Use compost + banana mulch + calcium from crushed eggshells + IMO.",
    "Cacao": "Apply compost + Gliricidia mulch + Trichoderma drench + neem foliar."
}

# Get suggestion or fallback
suggestion = organic_inputs.get(selected_crop, "Use compost, FPJ, vermicast, and neem-based biocontrol agents.")

st.markdown(f"🌿 **Recommended Inputs for `{selected_crop}`:**")
st.code(suggestion, language="markdown")

# -------------------- MODULE 3: AI Decision Support --------------------

import streamlit as st

st.markdown("---")
st.header("🤖 AI Decision Support: Organic Input and Elevation Advice")

# Load selected crop and elevation from session state or fallback
selected_crop = st.session_state.get("selected_crop", st.selectbox("Select a crop", [
    "Rice", "Corn", "Sugarcane", "Turmeric", "Ginger", "Lemongrass", "Moringa", "Aloe Vera", "Ashwagandha",
    "Neem", "Hibiscus", "Butterfly Pea", "Soursop", "Banana", "Papaya", "Dragon Fruit", "Watermelon",
    "Purple Sweet Potato", "Cassava", "Yellow Malanga", "Groundnuts", "Bitter Gourd", "Tomato", "Eggplant",
    "Coffee", "Cacao"
]))
elevation = st.session_state.get("elevation", st.number_input("Enter your elevation (meters above sea level)", min_value=0, max_value=3000, value=100))

# Save inputs to session state
st.session_state["selected_crop"] = selected_crop
st.session_state["elevation"] = elevation

# Elevation Suitability Check
st.subheader("📏 Elevation Suitability")

if selected_crop == "Coffee" and elevation < 800:
    st.warning("⚠️ Coffee prefers highland areas above 800m. Yield and quality may be low.")
elif selected_crop == "Rice" and elevation > 500:
    st.warning("⚠️ Rice grows best in lowland areas. Consider upland rice varieties.")
else:
    st.success("✅ Elevation is within acceptable range for the selected crop.")

# Organic Input Suggestions for All Priority Crops
st.subheader("♻️ Organic Input Suggestions")

organic_inputs = {
    "Turmeric": "Apply compost + Trichoderma + fermented ginger extract; avoid water-logging.",
    "Ginger": "Use compost, FPJ (fermented plant juice), and ash tea for pest deterrence.",
    "Lemongrass": "Apply compost + neem cake; spacing improves aroma oil production.",
    "Moringa": "Use vermicast + IMO (Indigenous Microorganisms) and foliar seaweed extract.",
    "Aloe Vera": "Apply compost + ash + EM-1; best with minimal moisture.",
    "Ashwagandha": "Use compost + turmeric leaf mulch + neem leaf extract for pests.",
    "Neem": "No external inputs needed; thrives in marginal land. Add compost if desired.",
    "Hibiscus": "Use compost + vermitea; supports flowering and deep red calyces.",
    "Butterfly Pea": "Add compost + ash solution spray; drought-tolerant legume.",

    "Soursop": "Apply compost + Trichoderma + fruit peel FPJ; control mealybugs organically.",
    "Banana": "Use compost + chopped pseudo-stem mulch + potassium foliar (banana ash tea).",
    "Papaya": "Apply FAA (fish amino acid) + EM-1 + compost; control root rot with Trichoderma.",
    "Dragon Fruit": "Use vermicast + banana peel FPJ + Trichoderma soil drench.",
    "Watermelon": "Apply compost + seaweed foliar + rice hull ash before flowering.",

    "Purple Sweet Potato": "Use compost + biochar + IMO; mulch with rice straw.",
    "Cassava": "Add compost + wood ash; avoid over-irrigation during tuber bulking.",
    "Yellow Malanga": "Use compost + leaf litter mulch; EM-1 helps reduce root rot.",

    "Groundnuts": "Use compost + Rhizobium inoculant + molasses; rotate with maize.",

    "Bitter Gourd": "Apply compost + neem oil spray + Trichoderma soil application.",
    "Tomato": "Use compost + vermicast + basil interplanting; neem foliar to prevent fruit borer.",
    "Eggplant": "Apply compost + ash foliar + marigold border to deter pests.",

    "Rice": "Use Azolla + compost + Trichoderma + fermented coconut water.",
    "Corn": "Apply compost + FFJ (fermented fruit juice) + charcoal-dust banding.",
    "Sugarcane": "Use press mud + Trichoderma + sugarcane sett treatment with cow urine.",

    "Coffee": "Use compost + banana mulch + calcium from crushed eggshells + IMO.",
    "Cacao": "Apply compost + Gliricidia mulch + Trichoderma drench + neem foliar."
}

# Get suggestion or fallback
suggestion = organic_inputs.get(selected_crop, "Use compost, FPJ, vermicast, and neem-based biocontrol agents.")

st.markdown(f"🌿 **Recommended Inputs for `{selected_crop}`:**")
st.code(suggestion, language="markdown")

