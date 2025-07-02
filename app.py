import streamlit as st
from datetime import datetime

# --- Tropical Country Locations ---
locations = sorted([
    # 🌴 Caribbean (including Suriname)
    "Antigua and Barbuda", "Bahamas", "Barbados", "Belize", "Cuba", "Dominica", "Dominican Republic",
    "Grenada", "Haiti", "Jamaica", "Saint Kitts and Nevis", "Saint Lucia",
    "Saint Vincent and the Grenadines", "Trinidad and Tobago", "Suriname",

    # 🌍 Africa (Tropical Belt)
    "Benin", "Botswana", "Burkina Faso", "Burundi", "Cameroon", "Central African Republic", "Chad",

    "Congo", "Democratic Republic of the Congo", "Equatorial Guinea", "Ethiopia", "Gabon", "Gambia",
    "Ghana", "Guinea", "Ivory Coast", "Kenya", "Liberia", "Madagascar", "Malawi", "Mali", "Mauritius",
    "Mozambique", "Namibia", "Niger", "Nigeria", "Rwanda", "Senegal", "Seychelles", "Sierra Leone",
    "South Sudan", "Sudan", "Tanzania", "Togo", "Uganda", "Zambia", "Zimbabwe",

    # 🌏 ASEAN
    "Brunei", "Cambodia", "Indonesia", "Laos", "Malaysia", "Myanmar", "Philippines", "Singapore",
    "Thailand", "Vietnam"
])

# --- Priority Crops List ---
crop_options = sorted([
    "Turmeric", "Ginger", "Lemongrass", "Moringa", "Aloe Vera", "Ashwagandha", "Neem", "Hibiscus", "Butterfly Pea",
    "Soursop", "Banana", "Papaya", "Dragon Fruit", "Watermelon",
    "Purple Sweet Potato", "Cassava", "Yellow Malanga", "Groundnuts",
    "Bitter Gourd", "Tomato", "Eggplant",
    "Rice", "Corn", "Sugarcane", "Coffee", "Cacao"
])

# --- Page Config & Title ---
st.set_page_config(page_title="FarmOps – Farm Dashboard", layout="centered")
st.title("🌾 FarmOps – Smart Organic Farm Management")
st.subheader("🚜 Powered by AgriVigor Green Farms Initiative")

# --- Input Section ---
st.header("📍 Farm Overview")

selected_location = st.selectbox("🌍 Select Your Country", locations)
farm_name = f"AgriVigor Green Farm – {selected_location}"
farm_size = st.number_input("📐 Farm Size (Hectares)", min_value=0.5, max_value=500.0, step=0.5)
selected_crops = st.multiselect("🌿 Crops Grown", crop_options)
planting_date = st.date_input("📅 Select Planting Date", value=datetime.today())

# --- Save to Session State ---
st.session_state["selected_location"] = selected_location
st.session_state["farm_name"] = farm_name
st.session_state["farm_size"] = farm_size
st.session_state["selected_crops"] = selected_crops
st.session_state["planting_date"] = planting_date

# --- Display Summary ---
if selected_crops:
    st.markdown(f"""
    ### 🧾 Farm Summary
    **🏷️ Farm Name:** {farm_name}  
    **📍 Location:** {selected_location}  
    **📐 Size:** {farm_size} hectares  
    **🌿 Crops:** {', '.join(selected_crops)}  
    **📅 Planting Date:** {planting_date.strftime('%Y-%m-%d')}
    """)
else:
    st.info("Please select at least one crop to proceed to the Smart Crop Calendar.")



import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# --- Crop Task Timeline Generator ---
def generate_crop_timeline(base_tasks):
    return [(task, offset) for task, offset in base_tasks]

# --- Full CROP_TASKS for 26 crops ---
CROP_TASKS = {
    "Turmeric": generate_crop_timeline([
        ("Land Preparation", 0), ("Rhizome Planting", 7), ("Irrigation", 14),
        ("Mulching", 30), ("Weeding", 60), ("Organic Fertilizer", 90), ("Harvest", 240)
    ]),
    "Ginger": generate_crop_timeline([
        ("Soil Prep", 0), ("Rhizome Planting", 5), ("Irrigation", 10),
        ("Weeding", 30), ("Earthing up", 60), ("Fertilizing", 90), ("Harvest", 210)
    ]),
    "Lemongrass": generate_crop_timeline([
        ("Land Prep", 0), ("Transplanting", 7), ("Weeding", 21),
        ("Fertilization", 30), ("Irrigation", 45), ("Harvest", 150)
    ]),
    "Moringa": generate_crop_timeline([
        ("Land Prep", 0), ("Direct Seeding", 7), ("Irrigation", 14),
        ("Pruning", 60), ("Harvest", 90)
    ]),
    "Aloe Vera": generate_crop_timeline([
        ("Land Preparation", 0), ("Transplanting Suckers", 7),
        ("Irrigation", 14), ("Weeding", 30), ("Organic Fertilizer", 45), ("Harvest", 240)
    ]),
    "Ashwagandha": generate_crop_timeline([
        ("Soil Preparation", 0), ("Direct Sowing", 7), ("Weeding", 30),
        ("Organic Compost", 40), ("Harvest", 180)
    ]),
    "Neem": generate_crop_timeline([
        ("Site Selection", 0), ("Seedling Planting", 10), ("Weeding", 30),
        ("Irrigation (if needed)", 60), ("Harvest", 365)
    ]),
    "Hibiscus": generate_crop_timeline([
        ("Land Prep", 0), ("Transplanting", 7), ("Weeding", 21),
        ("Fertilizing", 40), ("Harvest", 120)
    ]),
    "Butterfly Pea": generate_crop_timeline([
        ("Soil Prep", 0), ("Direct Seeding", 5), ("Weeding", 20),
        ("Staking", 40), ("Harvest", 90)
    ]),
    "Soursop": generate_crop_timeline([
        ("Site Prep", 0), ("Seedling Transplanting", 10), ("Weeding", 30),
        ("Pruning", 90), ("Harvest", 365)
    ]),
    "Banana": generate_crop_timeline([
        ("Land Prep", 0), ("Sucker Planting", 7), ("Irrigation", 14),
        ("Manuring", 30), ("Desuckering", 60), ("Harvest", 300)
    ]),
    "Papaya": generate_crop_timeline([
        ("Soil Prep", 0), ("Transplanting", 10), ("Weeding", 20),
        ("Fertilization", 30), ("Harvest", 240)
    ]),
    "Dragon Fruit": generate_crop_timeline([
        ("Land Prep", 0), ("Pole Setup", 7), ("Planting", 14),
        ("Training", 60), ("Fertilization", 90), ("Harvest", 180)
    ]),
    "Watermelon": generate_crop_timeline([
        ("Land Prep", 0), ("Seeding", 5), ("Weeding", 15),
        ("Irrigation", 20), ("Harvest", 80)
    ]),
    "Purple Sweet Potato": generate_crop_timeline([
        ("Soil Prep", 0), ("Vine Planting", 7), ("Irrigation", 14),
        ("Weeding", 30), ("Harvest", 120)
    ]),
    "Cassava": generate_crop_timeline([
        ("Land Prep", 0), ("Stem Planting", 7), ("Irrigation", 21),
        ("Weeding", 60), ("Harvest", 270)
    ]),
    "Yellow Malanga": generate_crop_timeline([
        ("Soil Prep", 0), ("Corm Planting", 5), ("Irrigation", 10),
        ("Fertilizing", 30), ("Harvest", 180)
    ]),
    "Groundnuts": generate_crop_timeline([
        ("Land Prep", 0), ("Sowing", 5), ("Weeding", 20),
        ("Earthing Up", 35), ("Harvest", 110)
    ]),
    "Bitter Gourd": generate_crop_timeline([
        ("Soil Prep", 0), ("Direct Sowing", 5), ("Staking", 20),
        ("Weeding", 25), ("Harvest", 80)
    ]),
    "Tomato": generate_crop_timeline([
        ("Nursery Prep", 0), ("Transplanting", 21), ("Staking", 30),
        ("Fertilizing", 40), ("Harvest", 90)
    ]),
    "Eggplant": generate_crop_timeline([
        ("Nursery Setup", 0), ("Transplanting", 21), ("Weeding", 30),
        ("Organic Fertilizer", 45), ("Harvest", 100)
    ]),
    "Rice": generate_crop_timeline([
        ("Land Prep", 0), ("Sowing", 7), ("Weeding", 30),
        ("Irrigation", 45), ("Harvest", 120)
    ]),
    "Corn": generate_crop_timeline([
        ("Land Prep", 0), ("Direct Sowing", 5), ("Weeding", 20),
        ("Earthing", 40), ("Harvest", 100)
    ]),
    "Sugarcane": generate_crop_timeline([
        ("Soil Prep", 0), ("Setts Planting", 10), ("Irrigation", 30),
        ("Earthing Up", 60), ("Harvest", 365)
    ]),
    "Coffee": generate_crop_timeline([
        ("Land Prep", 0), ("Seedling Transplanting", 14), ("Shading", 30),
        ("Pruning", 90), ("Harvest", 540)
    ]),
    "Cacao": generate_crop_timeline([
        ("Nursery Setup", 0), ("Field Transplant", 60), ("Mulching", 90),
        ("Canopy Management", 120), ("Harvest", 540)
    ])
}

# --- Session state from Module 1 ---
selected_crops = st.session_state.get("selected_crops", [])
planting_date = st.session_state.get("planting_date", datetime.today())
farm_name = st.session_state.get("farm_name", "AgriVigor Green Farm")

# --- Header ---
st.title("📅 Smart Crop Calendar")
st.subheader("🌿 Organic Task Timeline Generator")

st.markdown(f"""
📋 **Farm Name:** {farm_name}  
📍 **Planting Date:** {planting_date.strftime('%Y-%m-%d')}  
🌱 **Crops Selected:** {", ".join(selected_crops) if selected_crops else "None"}
""")

# --- Generate and Display Calendar ---
if not selected_crops:
    st.warning("⚠️ No crops selected. Return to Module 1.")
else:
    rows = []
    for crop in selected_crops:
        for task, offset in CROP_TASKS.get(crop, []):
            rows.append({
                "Crop": crop,
                "Task": task,
                "Start": planting_date + timedelta(days=offset),
                "End": planting_date + timedelta(days=offset + 3)
            })

    if rows:
        df = pd.DataFrame(rows).sort_values("Start")

        st.success("✅ Crop schedule generated.")
        st.dataframe(df)

        fig, ax = plt.subplots(figsize=(10, 6))
        colors = plt.cm.Set3.colors
        for i, row in df.iterrows():
            ax.barh(f"{row['Crop']} – {row['Task']}",
                    (row['End'] - row['Start']).days,
                    left=row['Start'], color=colors[i % len(colors)])
        ax.set_xlabel("Date")
        ax.set_ylabel("Crop – Task")
        ax.set_title("🗓️ Organic Crop Gantt Chart")
        ax.grid(True)
        st.pyplot(fig)

        csv = df.to_csv(index=False).encode("utf-8")
        st.download_button("📥 Download Timeline (CSV)", csv, "crop_schedule.csv", "text/csv")
    else:
        st.warning("⚠️ No timeline data available.")



import streamlit as st
from datetime import datetime

# --- Session Data from Module 1 ---
selected_crops = st.session_state.get("selected_crops", [])
planting_date = st.session_state.get("planting_date", datetime.today())
location = st.session_state.get("selected_location", "Tropical Region")
farm_name = st.session_state.get("farm_name", "AgriVigor Green Farm")

st.title("🧠 AI Decision Support")
st.subheader("🌿 Smart Organic Crop Recommendations")

if not selected_crops:
    st.warning("⚠️ Please select crops in Module 1.")
    st.stop()

CROP_MANAGEMENT_GUIDELINES = {
    "Turmeric": {
        "GAP": [
            "Use disease-free rhizomes, apply crop rotation with legumes, maintain 30 cm spacing, and mulch to conserve moisture and suppress weeds.",
        ],
        "Pests & Diseases": {
            "Shoot borer": {
                "Symptoms": "Shoot borer",
                "Control": "Spray neem oil 0.5% every 10 days"
            },
            "Rhizome rot": {
                "Symptoms": "N/A",
                "Control": "Use Trichoderma harzianum powder in soil at planting"
            },
        }
    },
    "Ginger": {
        "GAP": [
            "Use raised beds, organic mulch, disease-free seed rhizomes, and follow 2–3 year rotation",
            "Apply neem cake and biocontrol agents regularly.",
        ],
        "Pests & Diseases": {
            "Shoot borer": {
                "Symptoms": "Shoot borer",
                "Control": "Apply neem seed kernel extract 5% at 15-day interval"
            },
            "Soft rot": {
                "Symptoms": "N/A",
                "Control": "Apply Trichoderma viride and avoid water stagnation"
            },
        }
    },
    "Lemongrass": {
        "GAP": [
            "Use certified organic seed/planting material, maintain proper spacing, apply composted manure, rotate crops annually, and scout weekly.",
        ],
        "Pests & Diseases": {
            "Leaf blight": {
                "Symptoms": "N/A",
                "Control": "Apply garlic oil spray weekly"
            },
            "Rust": {
                "Symptoms": "N/A",
                "Control": "Use compost tea and neem extract"
            },
        }
    },
    "Moringa": {
        "GAP": [
            "Plant on raised beds, prune regularly to encourage branching, interplant with legumes, and use compost during flowering.",
        ],
        "Pests & Diseases": {
            "Aphids": {
                "Symptoms": "N/A",
                "Control": "Spray neem oil or soapy water"
            },
            "Caterpillars": {
                "Symptoms": "N/A",
                "Control": "Use Bacillus thuringiensis (Bt)"
            },
        }
    },
    "Aloe Vera": {
        "GAP": [
            "Use certified organic seed/planting material, maintain proper spacing, apply composted manure, rotate crops annually, and scout weekly.",
        ],
        "Pests & Diseases": {
            "Aphids": {
                "Symptoms": "N/A",
                "Control": "Neem oil + soap spray"
            },
            "Fungal leaf spot": {
                "Symptoms": "N/A",
                "Control": "Spray baking soda + water weekly"
            },
        }
    },
    "Ashwagandha": {
        "GAP": [
            "Use certified organic seed/planting material, maintain proper spacing, apply composted manure, rotate crops annually, and scout weekly.",
        ],
        "Pests & Diseases": {
            "Aphids": {
                "Symptoms": "N/A",
                "Control": "Neem oil + soap spray"
            },
            "Fungal leaf spot": {
                "Symptoms": "N/A",
                "Control": "Spray baking soda + water weekly"
            },
        }
    },
    "Neem": {
        "GAP": [
            "Use certified organic seed/planting material, maintain proper spacing, apply composted manure, rotate crops annually, and scout weekly.",
        ],
        "Pests & Diseases": {
            "Aphids": {
                "Symptoms": "N/A",
                "Control": "Neem oil + soap spray"
            },
            "Fungal leaf spot": {
                "Symptoms": "N/A",
                "Control": "Spray baking soda + water weekly"
            },
        }
    },
    "Hibiscus": {
        "GAP": [
            "Use certified organic seed/planting material, maintain proper spacing, apply composted manure, rotate crops annually, and scout weekly.",
        ],
        "Pests & Diseases": {
            "Aphids": {
                "Symptoms": "N/A",
                "Control": "Neem oil + soap spray"
            },
            "Fungal leaf spot": {
                "Symptoms": "N/A",
                "Control": "Spray baking soda + water weekly"
            },
        }
    },
    "Butterfly Pea": {
        "GAP": [
            "Use certified organic seed/planting material, maintain proper spacing, apply composted manure, rotate crops annually, and scout weekly.",
        ],
        "Pests & Diseases": {
            "Aphids": {
                "Symptoms": "N/A",
                "Control": "Neem oil + soap spray"
            },
            "Fungal leaf spot": {
                "Symptoms": "N/A",
                "Control": "Spray baking soda + water weekly"
            },
        }
    },
    "Soursop": {
        "GAP": [
            "Use certified organic seed/planting material, maintain proper spacing, apply composted manure, rotate crops annually, and scout weekly.",
        ],
        "Pests & Diseases": {
            "Aphids": {
                "Symptoms": "N/A",
                "Control": "Neem oil + soap spray"
            },
            "Fungal leaf spot": {
                "Symptoms": "N/A",
                "Control": "Spray baking soda + water weekly"
            },
        }
    },
    "Banana": {
        "GAP": [
            "Select healthy suckers, use banana circles with compost pits, manage irrigation, interplant with legumes, and remove old infected leaves.",
        ],
        "Pests & Diseases": {
            "Aphids": {
                "Symptoms": "N/A",
                "Control": "Neem oil + soap spray"
            },
            "Fungal leaf spot": {
                "Symptoms": "N/A",
                "Control": "Spray baking soda + water weekly"
            },
        }
    },
    "Papaya": {
        "GAP": [
            "Use certified organic seed/planting material, maintain proper spacing, apply composted manure, rotate crops annually, and scout weekly.",
        ],
        "Pests & Diseases": {
            "Damping off": {
                "Symptoms": "Damping off",
                "Control": "Seed treatment with Trichoderma + compost"
            },
            "Papaya mealybug": {
                "Symptoms": "N/A",
                "Control": "Apply neem oil and release parasitoid wasps"
            },
        }
    },
    "Dragon Fruit": {
        "GAP": [
            "Use certified organic seed/planting material, maintain proper spacing, apply composted manure, rotate crops annually, and scout weekly.",
        ],
        "Pests & Diseases": {
            "Aphids": {
                "Symptoms": "N/A",
                "Control": "Neem oil + soap spray"
            },
            "Fungal leaf spot": {
                "Symptoms": "N/A",
                "Control": "Spray baking soda + water weekly"
            },
        }
    },
    "Watermelon": {
        "GAP": [
            "Use certified organic seed/planting material, maintain proper spacing, apply composted manure, rotate crops annually, and scout weekly.",
        ],
        "Pests & Diseases": {
            "Aphids": {
                "Symptoms": "N/A",
                "Control": "Neem oil + soap spray"
            },
            "Fungal leaf spot": {
                "Symptoms": "N/A",
                "Control": "Spray baking soda + water weekly"
            },
        }
    },
    "Purple Sweet Potato": {
        "GAP": [
            "Use certified organic seed/planting material, maintain proper spacing, apply composted manure, rotate crops annually, and scout weekly.",
        ],
        "Pests & Diseases": {
            "Aphids": {
                "Symptoms": "N/A",
                "Control": "Neem oil + soap spray"
            },
            "Fungal leaf spot": {
                "Symptoms": "N/A",
                "Control": "Spray baking soda + water weekly"
            },
        }
    },
    "Cassava": {
        "GAP": [
            "Use certified organic seed/planting material, maintain proper spacing, apply composted manure, rotate crops annually, and scout weekly.",
        ],
        "Pests & Diseases": {
            "Aphids": {
                "Symptoms": "N/A",
                "Control": "Neem oil + soap spray"
            },
            "Fungal leaf spot": {
                "Symptoms": "N/A",
                "Control": "Spray baking soda + water weekly"
            },
        }
    },
    "Yellow Malanga": {
        "GAP": [
            "Use certified organic seed/planting material, maintain proper spacing, apply composted manure, rotate crops annually, and scout weekly.",
        ],
        "Pests & Diseases": {
            "Aphids": {
                "Symptoms": "N/A",
                "Control": "Neem oil + soap spray"
            },
            "Fungal leaf spot": {
                "Symptoms": "N/A",
                "Control": "Spray baking soda + water weekly"
            },
        }
    },
    "Groundnuts": {
        "GAP": [
            "Use certified organic seed/planting material, maintain proper spacing, apply composted manure, rotate crops annually, and scout weekly.",
        ],
        "Pests & Diseases": {
            "Aphids": {
                "Symptoms": "N/A",
                "Control": "Neem oil + soap spray"
            },
            "Fungal leaf spot": {
                "Symptoms": "N/A",
                "Control": "Spray baking soda + water weekly"
            },
        }
    },
    "Bitter Gourd": {
        "GAP": [
            "Use certified organic seed/planting material, maintain proper spacing, apply composted manure, rotate crops annually, and scout weekly.",
        ],
        "Pests & Diseases": {
            "Aphids": {
                "Symptoms": "N/A",
                "Control": "Neem oil + soap spray"
            },
            "Fungal leaf spot": {
                "Symptoms": "N/A",
                "Control": "Spray baking soda + water weekly"
            },
        }
    },
    "Tomato": {
        "GAP": [
            "Use resistant varieties, rotate with non-solanaceous crops, install drip irrigation, apply compost + neem cake, and prune lower leaves.",
        ],
        "Pests & Diseases": {
            "Leaf miner": {
                "Symptoms": "N/A",
                "Control": "Neem oil and sticky traps"
            },
            "Blight": {
                "Symptoms": "N/A",
                "Control": "Garlic+ginger+onion extract foliar spray"
            },
        }
    },
    "Eggplant": {
        "GAP": [
            "Use certified organic seed/planting material, maintain proper spacing, apply composted manure, rotate crops annually, and scout weekly.",
        ],
        "Pests & Diseases": {
            "Damping off": {
                "Symptoms": "N/A",
                "Control": "Soil drench with neem and Trichoderma"
            },
            "Fruit and shoot borer": {
                "Symptoms": "N/A",
                "Control": "Use pheromone traps + neem oil"
            },
        }
    },
    "Rice": {
        "GAP": [
            "Adopt SRI (System of Rice Intensification), maintain shallow water, transplant young seedlings, and use compost + azolla green manure.",
        ],
        "Pests & Diseases": {
            "Stem borer": {
                "Symptoms": "N/A",
                "Control": "Use pheromone traps and neem leaf extract"
            },
            "Brown spot": {
                "Symptoms": "N/A",
                "Control": "Apply cow dung ash or potash foliar spray"
            },
        }
    },
    "Corn": {
        "GAP": [
            "Use certified organic seed/planting material, maintain proper spacing, apply composted manure, rotate crops annually, and scout weekly.",
        ],
        "Pests & Diseases": {
            "Armyworm": {
                "Symptoms": "N/A",
                "Control": "Spray neem seed extract 3%"
            },
            "Corn borer": {
                "Symptoms": "N/A",
                "Control": "Release Trichogramma egg parasitoids"
            },
        }
    },
    "Sugarcane": {
        "GAP": [
            "Use certified organic seed/planting material, maintain proper spacing, apply composted manure, rotate crops annually, and scout weekly.",
        ],
        "Pests & Diseases": {
            "Aphids": {
                "Symptoms": "N/A",
                "Control": "Neem oil + soap spray"
            },
            "Fungal leaf spot": {
                "Symptoms": "N/A",
                "Control": "Spray baking soda + water weekly"
            },
        }
    },
    "Coffee": {
        "GAP": [
            "Use certified organic seed/planting material, maintain proper spacing, apply composted manure, rotate crops annually, and scout weekly.",
        ],
        "Pests & Diseases": {
            "Aphids": {
                "Symptoms": "N/A",
                "Control": "Neem oil + soap spray"
            },
            "Fungal leaf spot": {
                "Symptoms": "N/A",
                "Control": "Spray baking soda + water weekly"
            },
        }
    },
    "Cacao": {
        "GAP": [
            "Use certified organic seed/planting material, maintain proper spacing, apply composted manure, rotate crops annually, and scout weekly.",
        ],
        "Pests & Diseases": {
            "Aphids": {
                "Symptoms": "N/A",
                "Control": "Neem oil + soap spray"
            },
            "Fungal leaf spot": {
                "Symptoms": "N/A",
                "Control": "Spray baking soda + water weekly"
            },
        }
    },
}

# --- Display logic per crop ---
for crop in selected_crops:
    st.header(f"🌾 {crop}")
    data = CROP_MANAGEMENT_GUIDELINES.get(crop)

    if not data:
        st.warning("🚫 No data available yet for this crop.")
        continue

    st.subheader("✅ Good Agricultural Practices (GAP)")
    for practice in data["GAP"]:
        st.markdown(f"- {practice}")

    st.subheader("🛡️ Pests & Organic Controls")
    for pest, pest_info in data["Pests & Diseases"].items():
        st.markdown(f"**{pest}**")
        st.markdown(f"• *Symptoms:* {pest_info['Symptoms']}")
        st.markdown(f"• *Organic Control:* {pest_info['Control']}")
        st.markdown("---")

# --- Optional navigation ---
if st.button("🔁 Back to Module 1"):
    st.switch_page("1_Farm_Dashboard.py")


import streamlit as st
import pandas as pd
from datetime import datetime

st.title("🗂️ Farm Mapping & Activity Logbook")

# --- Pull session state ---
farm_name = st.session_state.get("farm_name", "AgriVigor Green Farm")
selected_crops = st.session_state.get("selected_crops", [])
location = st.session_state.get("selected_location", "N/A")

if not selected_crops:
    st.warning("⚠️ Please select crops in Module 1 first.")
    st.stop()

# --- Initialize logbook ---
if "farm_logbook" not in st.session_state:
    st.session_state["farm_logbook"] = []

# --- Activity Log Form ---
with st.form("activity_log_form"):
    st.subheader("➕ New Farm Activity Entry")

    log_date = st.date_input("📅 Activity Date", datetime.today())
    crop = st.selectbox("🌿 Crop", selected_crops)
    activity_type = st.selectbox("🛠️ Activity Type", [
        "Land Preparation", "Sowing/Planting", "Weeding", "Irrigation",
        "Organic Input Application", "Pest/Disease Monitoring", "Harvesting",
        "Training/Pruning", "Labor Entry", "Other"
    ])
    description = st.text_area("📝 Description/Notes", "")
    uploaded_image = st.file_uploader("📸 Optional: Upload Photo", type=["jpg", "jpeg", "png"])

    submitted = st.form_submit_button("✅ Add Entry")

    if submitted:
        st.session_state["farm_logbook"].append({
            "Date": log_date.strftime("%Y-%m-%d"),
            "Crop": crop,
            "Activity": activity_type,
            "Notes": description,
            "ImageName": uploaded_image.name if uploaded_image else "",
            "Location": location
        })
        st.success("✅ Activity logged successfully!")

# --- Display Logbook ---
st.subheader("📖 View Farm Logbook")

df_logs = pd.DataFrame(st.session_state["farm_logbook"])
if df_logs.empty:
    st.info("No activities logged yet.")
else:
    filter_crop = st.selectbox("🔍 Filter by Crop", ["All"] + selected_crops)
    filter_date = st.date_input("📅 Filter by Date", datetime.today())

    df_filtered = df_logs.copy()
    if filter_crop != "All":
        df_filtered = df_filtered[df_filtered["Crop"] == filter_crop]
    df_filtered = df_filtered[df_filtered["Date"] == filter_date.strftime("%Y-%m-%d")]

    st.dataframe(df_filtered.reset_index(drop=True), use_container_width=True)

    if not df_filtered.empty:
        st.markdown(f"🧾 Showing {len(df_filtered)} entries for {filter_crop} on {filter_date.strftime('%Y-%m-%d')}")

# --- Optional Navigation ---
if st.button("🔙 Return to Dashboard"):
    st.switch_page("1_Farm_Dashboard.py")


import streamlit as st
from datetime import datetime
import random

st.title("🧪 Crop Health Diagnosis")
st.subheader("📷 Upload Image for Simulated AI Detection")

# --- Load previous session crop info ---
selected_crops = st.session_state.get("selected_crops", [])

if not selected_crops:
    st.warning("⚠️ No crop selected from Module 1.")
    st.stop()

selected_crop = st.selectbox("🌿 Select Crop", selected_crops)

uploaded_file = st.file_uploader("📸 Upload image of affected plant", type=["jpg", "jpeg", "png"])

if uploaded_file:
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

    # --- Simulated AI prediction logic ---
    diagnosis_options = {
        "Aloe Vera": [
            ("Rust Fungus", "Yellow-orange pustules on leaves.", "Apply neem oil + baking soda weekly."),
            ("Mealybugs", "White cottony masses near base.", "Spray garlic-chili-neem solution every 5 days.")
        ],
        "Banana": [
            ("Black Sigatoka", "Dark streaks on leaves.", "Use potassium bicarbonate + Trichoderma."),
            ("Weevil Damage", "Tunnels in corm or base.", "Apply neem cake to soil, trap adults.")
        ],
        "Papaya": [
            ("Anthracnose", "Sunken spots on fruits.", "Use copper soap + neem oil."),
            ("Mealybugs", "White waxy pests on stem.", "Neem + chili + soap foliar spray.")
        ],
        "Tomato": [
            ("Early Blight", "Brown concentric spots on leaves.", "Spray with compost tea + seaweed extract."),
            ("Aphid Infestation", "Sticky leaves, curled tips.", "Apply neem + garlic spray.")
        ]
        # Add more crops with issues here...
    }

    crop_diagnoses = diagnosis_options.get(selected_crop, [
        ("Unknown issue", "Symptoms not recognized in current crop.", "Manually inspect or send sample.")
    ])

    diagnosis = random.choice(crop_diagnoses)

    st.markdown("### 🧬 Simulated Diagnosis Result")
    st.success(f"**Issue Detected:** {diagnosis[0]}")
    st.write(f"🔍 **Symptoms:** {diagnosis[1]}")
    st.write(f"🌿 **Organic Recommendation:** {diagnosis[2]}")
    st.write(f"🕒 Diagnosis Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

# Optional: save or record diagnosis (future)


import streamlit as st

st.title("💧 Soil & Irrigation Monitor")
st.subheader("🌱 Tropical Crop Soil & Water Requirements (Research-Based)")

# Load session data
selected_crops = st.session_state.get("selected_crops", [])
if not selected_crops:
    st.warning("⚠️ No crops selected. Please complete Module 1.")
    st.stop()

selected_crop = st.selectbox("🌿 Choose a crop", selected_crops, key="soil_monitor_crop")

# Input current soil conditions
soil_ph = st.slider("pH Level", 3.0, 9.0, 6.5, key="soil_ph")
moisture = st.slider("Soil Moisture (%)", 0, 100, 50, key="soil_moisture")
organic_matter = st.slider("Organic Matter (%)", 0.0, 10.0, 3.0, key="soil_om")
soil_texture = st.selectbox("Soil Texture", ["Sandy", "Loamy", "Clay", "Silty"], key="soil_texture")

# Research-based crop data
CROP_DATA = {
    "Banana":     {"pH":(6.0,7.5),"OM":(4,6),"Mthr":65,"W": {"Sandy":"2‑3d","Loamy":"3‑5d","Clay":"5‑7d","Silty":"4‑6d"}},
    "Tomato":     {"pH":(5.5,7.0),"OM":(2.5,4),"Mthr":70,"W": {"Sandy":"2‑3d","Loamy":"3‑4d","Clay":"4‑5d","Silty":"3‑4d"}},
    "Papaya":     {"pH":(6.0,7.0),"OM":(3,5),"Mthr":60,"W": {"Sandy":"4‑6d","Loamy":"7‑7d","Clay":"7‑7d","Silty":"5‑7d"}},
    "Moringa":    {"pH":(6.0,7.5),"OM":(1.5,3),"Mthr":50,"W": {"Sandy":"7‑10d","Loamy":"10‑14d","Clay":"14‑18d","Silty":"10‑12d"}},
    "Pineapple":  {"pH":(4.0,6.0),"OM":(2,4),"Mthr":55,"W": {"Sandy":"5‑7d","Loamy":"7‑10d","Clay":"10‑14d","Silty":"7‑10d"}},
    "Cassava":    {"pH":(5.0,6.5),"OM":(1.5,2.5),"Mthr":60,"W": {"Sandy":"7‑7d","Loamy":"10‑14d","Clay":"14‑18d","Silty":"12‑14d"}},
    "Lemongrass": {"pH":(6.0,7.0),"OM":(2,4),"Mthr":50,"W": {"Sandy":"3‑5d","Loamy":"5‑7d","Clay":"7‑10d","Silty":"5‑7d"}},
    "Ginger":     {"pH":(5.5,6.5),"OM":(3,5),"Mthr":70,"W": {"Sandy":"3‑4d","Loamy":"4‑5d","Clay":"5‑7d","Silty":"4‑6d"}},
    "Turmeric":   {"pH":(6.0,7.0),"OM":(3,5),"Mthr":65,"W": {"Sandy":"4‑5d","Loamy":"5‑6d","Clay":"6‑8d","Silty":"5‑7d"}},
    "Sweet Potato":{"pH":(5.5,6.5),"OM":(2,4),"Mthr":60,"W": {"Sandy":"7‑10d","Loamy":"10‑14d","Clay":"14‑18d","Silty":"10‑14d"}},
    "Eggplant":   {"pH":(5.5,6.8),"OM":(2.5,4),"Mthr":65,"W": {"Sandy":"2‑3d","Loamy":"3‑5d","Clay":"5‑7d","Silty":"3‑5d"}},
    "Chili Pepper":{"pH":(5.5,7.0),"OM":(2,4),"Mthr":60,"W": {"Sandy":"3‑4d","Loamy":"4‑6d","Clay":"6‑8d","Silty":"4‑6d"}},
    "Watermelon": {"pH":(6.0,7.0),"OM":(2,4),"Mthr":60,"W": {"Sandy":"3‑5d","Loamy":"5‑7d","Clay":"7‑10d","Silty":"5‑7d"}},
    "Cacao":      {"pH":(5.0,7.5),"OM":(3,6),"Mthr":70,"W": {"Sandy":"7‑7d","Loamy":"7‑10d","Clay":"10‑14d","Silty":"7‑10d"}},
    "Coffee":     {"pH":(5.0,6.5),"OM":(3,5),"Mthr":65,"W": {"Sandy":"5‑7d","Loamy":"7‑10d","Clay":"10‑14d","Silty":"7‑10d"}},
    "Rice":       {"pH":(5.5,6.5),"OM":(2,4),"Mthr":80,"W": {"Sandy":"Flooded","Loamy":"Flooded","Clay":"Flooded","Silty":"Flooded"}},
    "Sugarcane":  {"pH":(6.0,7.0),"OM":(3,6),"Mthr":70,"W": {"Sandy":"4‑6d","Loamy":"6‑8d","Clay":"8‑10d","Silty":"6‑8d"}},
    "Neem Tree":  {"pH":(6.0,8.0),"OM":(1,3),"Mthr":40,"W": {"Sandy":"14‑21d","Loamy":"21‑30d","Clay":"30‑40d","Silty":"21‑28d"}},
    "Soursop":    {"pH":(6.0,7.0),"OM":(3,5),"Mthr":70,"W": {"Sandy":"4‑6d","Loamy":"7‑10d","Clay":"10‑14d","Silty":"7‑10d"}},
    "Groundnuts": {"pH":(5.0,6.5),"OM":(2,4),"Mthr":65,"W": {"Sandy":"4‑6d","Loamy":"6‑8d","Clay":"8‑10d","Silty":"6‑8d"}},
    "Papaya":     {"pH":(6.0,7.0),"OM":(3,5),"Mthr":60,"W": {"Sandy":"4‑6d","Loamy":"7‑7d","Clay":"7‑7d","Silty":"5‑7d"}},
    "Cassava":    {"pH":(5.0,6.5),"OM":(1.5,2.5),"Mthr":60,"W": {"Sandy":"7‑7d","Loamy":"10‑14d","Clay":"14‑18d","Silty":"12‑14d"}},
    "Taro":       {"pH":(5.5,6.5),"OM":(3,5),"Mthr":75,"W": {"Sandy":"Flooded","Loamy":"Flooded","Clay":"Flooded","Silty":"Flooded"}},
    "Yam":        {"pH":(5.5,6.5),"OM":(2.5,4),"Mthr":70,"W": {"Sandy":"10‑14d","Loamy":"14‑18d","Clay":"18‑21d","Silty":"14‑18d"}}
}

params = CROP_DATA.get(selected_crop)
if not params:
    st.info(f"📘 Data for **{selected_crop}** coming soon.")
    st.stop()

# Evaluate
ph_ok = params["pH"][0] <= soil_ph <= params["pH"][1]
om_ok = params["OM"][0] <= organic_matter <= params["OM"][1]
moist_ok = moisture >= params["Mthr"]

# Output
st.markdown("### 🔍 Soil Suitability Analysis")
st.markdown(f"- **pH {soil_ph}**: {'✅ Optimal' if ph_ok else '⚠️ Adjust'}")
st.markdown(f"- **Organic Matter {organic_matter}%**: {'✅ Optimal' if om_ok else '⚠️ Increase'}")
st.markdown(f"- **Moisture {moisture}%**: {'✅ Optimal' if moist_ok else '⚠️ Too Low'}")
st.markdown(f"- **Texture**: {soil_texture}")

irrig = params["W"][soil_texture]
st.markdown("### 💧 Irrigation Guidance")
st.success(f"Water **{selected_crop}** in **{soil_texture} soil** every **{irrig}**")

st.markdown("### 🌿 Organic Soil Care Suggestions")
if not ph_ok:
    st.info("➡️ Use lime/ash to raise pH or sulfur-rich compost to lower it.")
if not om_ok:
    st.info("➡️ Add compost/vermicompost/manure to boost organic matter.")
if not moist_ok:
    st.info("➡️ Mulch (straw/leaves) to retain moisture and improve structure.")

st.success(f"✅ Analysis complete for **{selected_crop}**!")

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="📈 Financial Projection", layout="wide")

# Session state check
if "selected_crops" not in st.session_state or not st.session_state["selected_crops"]:
    st.warning("No crops selected. Please return to Module 1.")
    st.stop()

# Crop and location
crop = st.session_state["selected_crops"][0]
location = st.session_state.get("location", "Tropical Country")

# Sample cost, yield, price per crop (can be extended)
CROP_ECONOMICS = {
    "Banana": {"yield": 30.0, "cost": 4500.0, "price": 300.0},
    "Aloe Vera": {"yield": 25.0, "cost": 3000.0, "price": 350.0},
    "Papaya": {"yield": 35.0, "cost": 3200.0, "price": 280.0},
    "Neem Tree": {"yield": 10.0, "cost": 1800.0, "price": 200.0},
    "Ashwagandha": {"yield": 15.0, "cost": 2200.0, "price": 500.0},
    "Guava": {"yield": 28.0, "cost": 4000.0, "price": 320.0},
    "Jackfruit": {"yield": 20.0, "cost": 3700.0, "price": 450.0},
    "Moringa": {"yield": 18.0, "cost": 2000.0, "price": 250.0},
    "Soursop": {"yield": 22.0, "cost": 3400.0, "price": 400.0},
    "Turmeric": {"yield": 16.0, "cost": 2900.0, "price": 600.0},
    "Cassava": {"yield": 28.0, "cost": 3100.0, "price": 200.0},
    "Pineapple": {"yield": 32.0, "cost": 3600.0, "price": 300.0},
    "Ginger": {"yield": 20.0, "cost": 3300.0, "price": 550.0},
    "Sugarcane": {"yield": 80.0, "cost": 5200.0, "price": 100.0},
    "Taro": {"yield": 24.0, "cost": 2700.0, "price": 220.0},
    "Breadfruit": {"yield": 18.0, "cost": 3900.0, "price": 340.0},
    "Coconut": {"yield": 12.0, "cost": 4800.0, "price": 500.0},
    "Peanut": {"yield": 22.0, "cost": 3100.0, "price": 350.0},
    "Yam": {"yield": 26.0, "cost": 3300.0, "price": 280.0},
    "Bitter Gourd": {"yield": 20.0, "cost": 2600.0, "price": 300.0},
    "Sweet Potato": {"yield": 30.0, "cost": 2800.0, "price": 250.0},
    "Lemongrass": {"yield": 15.0, "cost": 2100.0, "price": 300.0},
    "Arrowroot": {"yield": 18.0, "cost": 2900.0, "price": 400.0},
    "Roselle": {"yield": 14.0, "cost": 2300.0, "price": 450.0},
    "Chili Pepper": {"yield": 20.0, "cost": 2700.0, "price": 350.0},
    "Tomato": {"yield": 25.0, "cost": 3000.0, "price": 320.0}
}

# Use values or default
data = CROP_ECONOMICS.get(crop, {"yield": 20.0, "cost": 3000.0, "price": 300.0})

st.title("📈 Financial Projection Tool")
st.subheader("Crop Economics Input")

# Input controls
p_yield = st.number_input("Projected Yield (t/ha)", value=float(data["yield"]), step=0.1)
p_cost = st.number_input("Production Cost (USD/ha)", value=float(data["cost"]), step=100.0)
p_price = st.number_input("Price (USD/t)", value=float(data["price"]), step=10.0)

# Calculation
revenue = p_yield * p_price
profit = revenue - p_cost

st.markdown("### 💰 Year 1 Summary")
st.write(f"**Estimated Revenue:** USD {revenue:,.2f}")
st.write(f"**Estimated Profit:** USD {profit:,.2f}")

# Projections
growth_rate = st.slider("Annual price increase (%)", 0, 20, 5)
projected_data = []
price = p_price

for year in range(1, 4):
    price *= (1 + growth_rate / 100)
    revenue = p_yield * price
    profit = revenue - p_cost
    projected_data.append({
        "Year": f"Year {year}",
        "Price (USD/t)": round(price, 2),
        "Revenue (USD)": round(revenue, 2),
        "Profit (USD)": round(profit, 2)
    })

df_proj = pd.DataFrame(projected_data)
st.markdown("### 📊 3-Year Financial Projection")
st.dataframe(df_proj)

# Chart
fig, ax = plt.subplots()
ax.plot(df_proj["Year"], df_proj["Revenue (USD)"], label="Revenue")
ax.plot(df_proj["Year"], df_proj["Profit (USD)"], label="Profit")
ax.set_title(f"📈 Revenue and Profit Trend for {crop}")
ax.set_ylabel("USD")
ax.legend()
st.pyplot(fig)



import streamlit as st
import pandas as pd

st.set_page_config(page_title="Module 8 – Climate Risk & Resilience", layout="wide")

st.title("🌾 Module 8: Climate Risk & Resilience")

# ------------------------------
# STEP 1: User selects country and crop
# ------------------------------
countries = ["Philippines", "Suriname"]
crops = [
    "Rice", "Corn", "Cassava", "Sweet Potato", "Taro", "Tomato", "Eggplant", "Bell Pepper",
    "Okra", "String Beans", "Cabbage", "Carrot", "Lettuce", "Onion", "Garlic",
    "Mung Bean", "Soybean", "Peanut", "Banana", "Pineapple", "Papaya", "Mango",
    "Coconut", "Coffee"
]

selected_country = st.selectbox("🌍 Select Country", countries)
selected_crop = st.selectbox("🌱 Select Crop", crops)

# ------------------------------
# STEP 2: Climate risk + resilience table
# ------------------------------
climate_risks = [
    "High Temperature", "Heavy Rain", "Drought", "Strong Winds", "Flooding", "Humidity Stress"
]

resilience_actions = {
    "High Temperature": "Use heat-tolerant varieties and increase shading.",
    "Heavy Rain": "Improve drainage and use raised beds.",
    "Drought": "Implement drip irrigation and mulching.",
    "Strong Winds": "Use windbreaks and plant support systems.",
    "Flooding": "Elevated planting beds and rapid drainage systems.",
    "Humidity Stress": "Increase plant spacing and improve air circulation."
}

# Create dynamic DataFrame based on selection
rows = []
for risk in climate_risks:
    rows.append({
        "Country": selected_country,
        "Crop": selected_crop,
        "Climate Risk": risk,
        "Risk Threshold": "High",
        "Resilience Action": resilience_actions[risk]
    })

df = pd.DataFrame(rows)

# ------------------------------
# STEP 3: Display table
# ------------------------------
st.subheader("🌧️ Climate Risks and Organic Resilience Strategies")
st.dataframe(df, use_container_width=True)

# ------------------------------
# Optional Next: Connect to Module 9 or alert logic
# ------------------------------
st.markdown("---")
st.markdown("✅ *This data will inform early alerts and suggestions in upcoming modules (Decision Support, Calendar, etc).*")



import streamlit as st

# 🌱 AgriVigor Admin Panel Login System

# Sample credentials
CREDENTIALS = {
    "admin@agrivigor.org": "Greenfarms2025"
}

# Setup Streamlit page
st.set_page_config(page_title="AgriVigor Admin Panel", layout="centered")

st.markdown("✅ *This data will inform early alerts and suggestions in upcoming modules (Decision Support, Calendar, etc).*")
st.title("🌱 AgriVigor Admin Panel")
st.header("🔐 Login")

# Initialize session state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.user = None

# Login form
if not st.session_state.logged_in:
    with st.form("login_form"):
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        submitted = st.form_submit_button("Login")

        if submitted:
            if CREDENTIALS.get(email) == password:
                st.session_state.logged_in = True
                st.session_state.user = email
                st.success(f"✅ Welcome {email}!")
                st.rerun()
            else:
                st.error("❌ Invalid credentials. Please try again.")

# Post-login dashboard
else:
    st.success(f"✅ Welcome {st.session_state.user}!")
    if st.button("🔓 Logout"):
        st.session_state.logged_in = False
        st.session_state.user = None
        st.rerun()

