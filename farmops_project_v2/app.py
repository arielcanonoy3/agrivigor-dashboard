import streamlit as st
import folium
from streamlit_folium import st_folium
from shapely.geometry import shape

st.set_page_config(page_title="FarmOps – Module 3", layout="wide")

st.title("📍 FarmOps Module 3: Farm Mapping & Field Logbook")

# Initialize session state
if "field_logs" not in st.session_state:
    st.session_state["field_logs"] = []

# Step 1: Draw on map
st.subheader("🗺️ Draw Farm Plot on Map")

m = folium.Map(location=[10.3157, 123.8854], zoom_start=6)

draw = folium.plugins.Draw(export=True)
draw.add_to(m)

map_data = st_folium(m, width=700, height=500, key="map_draw")

# Step 2: Crop and notes
st.subheader("🌿 Farm Details")

crop = st.selectbox("Select crop", [
    "Rice", "Corn", "Sugarcane", "Turmeric", "Annatto", "Butterfly Pea", "Hibiscus",
    "Purple Sweet Potato", "Bitter Gourd", "Neem", "Moringa", "Aloe Vera", "Lemongrass",
    "Soursop", "Ginger", "Ashwagandha", "Cassava", "Yellow Malanga", "Groundnuts",
    "Watermelon", "Eggplant", "Tomato", "Bell Pepper", "Banana", "Papaya", "Dragon Fruit",
    "Coffee", "Cacao"
], key="crop_selection")

notes = st.text_area("📝 Notes or Activity Description", key="log_notes")

if st.button("➕ Add Field Log", key="add_log_btn"):
    if map_data.get("last_active_drawing"):
        geom = map_data["last_active_drawing"]["geometry"]
        geom_type = geom["type"]
        coords = geom["coordinates"]

        log_entry = {
            "Crop": crop,
            "Notes": notes,
            "Shape Type": geom_type,
            "Coordinates": str(coords)
        }

        st.session_state["field_logs"].append(log_entry)
        st.success("✅ Field log added successfully!")
    else:
        st.warning("⚠️ Please draw a shape on the map before submitting.")

# Step 3: Display logbook
if st.session_state["field_logs"]:
    st.subheader("📒 Field Activity Logbook")
    st.table(st.session_state["field_logs"])

