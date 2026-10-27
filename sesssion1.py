import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd

st.markdown("""
    <style>
        /* Hide the top header and toolbar */
        header[data-testid="stHeader"] {
            display: none;
        }

        /* Hide the Deploy button */
        .stDeployButton {
            display: none;
        }

        /* Hide the top-right menu */
        #MainMenu {
            visibility: hidden;
        }

        /* Hide the footer */
        footer {
            visibility: hidden;
        }
    </style>
""", unsafe_allow_html=True)

st.title("My Streamlit App")

first = int(st.query_params.get("group", "1"))
second = int(st.query_params.get("property", "1"))
# ==========================================
# 1. GROUP 1: ALKALI METALS
# ==========================================

alkali_atomic_radius = {
    "Lithium": 152,
    "Sodium": 186,
    "Potassium": 227,
    "Rubidium": 248,
    "Cesium": 265,
    "Francium": 270
}

alkali_melting_point = {
    "Lithium": 180.5,
    "Sodium": 97.8,
    "Potassium": 63.4,
    "Rubidium": 39.3,
    "Cesium": 28.4,
    "Francium": 27
}

alkali_boiling_point = {
    "Lithium": 1342,
    "Sodium": 883,
    "Potassium": 759,
    "Rubidium": 688,
    "Cesium": 671,
    "Francium": 677
}

alkali_chemical_activity = {
    "Lithium": 6,
    "Sodium": 7,
    "Potassium": 8,
    "Rubidium": 9,
    "Cesium": 10,
    "Francium": 10
}


# ==========================================
# 2. GROUP 2: ALKALINE EARTH METALS
# ==========================================

alkaline_atomic_radius = {
    "Beryllium": 112,
    "Magnesium": 160,
    "Calcium": 197,
    "Strontium": 215,
    "Barium": 222,
    "Radium": 283
}

alkaline_melting_point = {
    "Beryllium": 1287,
    "Magnesium": 650,
    "Calcium": 842,
    "Strontium": 777,
    "Barium": 727,
    "Radium": 700
}

alkaline_boiling_point = {
    "Beryllium": 2469,
    "Magnesium": 1091,
    "Calcium": 1484,
    "Strontium": 1382,
    "Barium": 1845,
    "Radium": 1737
}

alkaline_chemical_activity = {
    "Beryllium": 2,
    "Magnesium": 4,
    "Calcium": 6,
    "Strontium": 7,
    "Barium": 8,
    "Radium": 8
}


# ==========================================
# 3. GROUP 17: HALOGENS
# ==========================================

halogen_atomic_radius = {
    "Fluorine": 42,
    "Chlorine": 79,
    "Bromine": 94,
    "Iodine": 115,
    "Astatine": 127,
    "Tennessine": 138
}

halogen_melting_point = {
    "Fluorine": -219.7,
    "Chlorine": -101.5,
    "Bromine": -7.2,
    "Iodine": 113.7,
    "Astatine": 302,
    "Tennessine": 350
}

halogen_boiling_point = {
    "Fluorine": -188.1,
    "Chlorine": -34.0,
    "Bromine": 58.8,
    "Iodine": 184.3,
    "Astatine": 337,
    "Tennessine": 610
}

halogen_chemical_activity = {
    "Fluorine": 10,
    "Chlorine": 8,
    "Bromine": 6,
    "Iodine": 4,
    "Astatine": 3,
    "Tennessine": 3
}


# ==========================================
# 4. GROUPS, PROPERTIES, AND DATA
# ==========================================

groups = [
    "Alkali metals",
    "Alkaline earth metals",
    "Halogens"
]

options = [
    "Atomic radius (pm)",
    "Melting point (°C)",
    "Boiling point (°C)",
    "Chemical activity (1-10)"
]

all_data = [
    [
        alkali_atomic_radius,
        alkali_melting_point,
        alkali_boiling_point,
        alkali_chemical_activity
    ],
    [
        alkaline_atomic_radius,
        alkaline_melting_point,
        alkaline_boiling_point,
        alkaline_chemical_activity
    ],
    [
        halogen_atomic_radius,
        halogen_melting_point,
        halogen_boiling_point,
        halogen_chemical_activity
    ]
]


# ==========================================
# 5. CHART FUNCTION
# ==========================================

def showchart(group_choice, property_choice):

    # Validate the selected indexes
    if not 0 <= group_choice < len(groups):
        st.error("Invalid group choice!")
        return

    if not 0 <= property_choice < len(options):
        st.error("Invalid property choice!")
        return

    # Select the correct dictionary
    data = all_data[group_choice][property_choice]

    # Convert the dictionary into a DataFrame
    df = pd.DataFrame(
        list(data.items()),
        columns=["Element", "Value"]
    )

    # Display chart title
    st.title("Periodic Table Properties")
    st.subheader(groups[group_choice])
    st.write("Property:", options[property_choice])
    fig, ax = plt.subplots(figsize=(10, 5))

    ax.plot(df["Element"], df["Value"], marker="o")

    ax.set_xlabel("Element")
    ax.set_ylabel(options[property_choice])
    ax.set_title(options[property_choice] + " by Element")

    # Keep the original order of elements
    ax.tick_params(axis="x", labelrotation=45)

    # Prevent labels from being cut off
    fig.tight_layout()

    # Display a static chart without interactive zooming or scrolling
    st.pyplot(fig)

    plt.close(fig)

        # Display the bar chart
   

    # Display the values underneath the chart
    st.subheader("Element Data")
    st.dataframe(df, hide_index=True)


# ==========================================
# 6. SELECT YOUR CHART HERE
# ==========================================

showchart(first, second)
