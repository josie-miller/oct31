import streamlit as st
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import numpy as np

elements = [
    {"symbol": "H", "atomic_number": 1, "group": 1, "period": 1, "category": "Nonmetal"},
    {"symbol": "He", "atomic_number": 2, "group": 18, "period": 1, "category": "Noble Gas"},
    {"symbol": "Li", "atomic_number": 3, "group": 1, "period": 2, "category": "Alkali Metal"},
    {"symbol": "Be", "atomic_number": 4, "group": 2, "period": 2, "category": "Alkaline Earth Metal"},
    {"symbol": "B", "atomic_number": 5, "group": 13, "period": 2, "category": "Metalloid"},
    {"symbol": "C", "atomic_number": 6, "group": 14, "period": 2, "category": "Nonmetal"},
    {"symbol": "N", "atomic_number": 7, "group": 15, "period": 2, "category": "Nonmetal"},
    {"symbol": "O", "atomic_number": 8, "group": 16, "period": 2, "category": "Nonmetal"},
    {"symbol": "F", "atomic_number": 9, "group": 17, "period": 2, "category": "Halogen"},
    {"symbol": "Ne", "atomic_number": 10, "group": 18, "period": 2, "category": "Noble Gas"},
    {"symbol": "Na", "atomic_number": 11, "group": 1, "period": 3, "category": "Alkali Metal"},
    {"symbol": "Mg", "atomic_number": 12, "group": 2, "period": 3, "category": "Alkaline Earth Metal"},
    {"symbol": "Al", "atomic_number": 13, "group": 13, "period": 3, "category": "Post-Transition Metal"},
    {"symbol": "Si", "atomic_number": 14, "group": 14, "period": 3, "category": "Metalloid"},
    {"symbol": "P", "atomic_number": 15, "group": 15, "period": 3, "category": "Nonmetal"},
    {"symbol": "S", "atomic_number": 16, "group": 16, "period": 3, "category": "Nonmetal"},
    {"symbol": "Cl", "atomic_number": 17, "group": 17, "period": 3, "category": "Halogen"},
    {"symbol": "Ar", "atomic_number": 18, "group": 18, "period": 3, "category": "Noble Gas"},
    {"symbol": "K", "atomic_number": 19, "group": 1, "period": 4, "category": "Alkali Metal"},
    {"symbol": "Ca", "atomic_number": 20, "group": 2, "period": 4, "category": "Alkaline Earth Metal"},
    {"symbol": "Sc", "atomic_number": 21, "group": 3, "period": 4, "category": "Transition Metal"},
    {"symbol": "Ti", "atomic_number": 22, "group": 4, "period": 4, "category": "Transition Metal"},
    {"symbol": "V", "atomic_number": 23, "group": 5, "period": 4, "category": "Transition Metal"},
    {"symbol": "Cr", "atomic_number": 24, "group": 6, "period": 4, "category": "Transition Metal"},
    {"symbol": "Mn", "atomic_number": 25, "group": 7, "period": 4, "category": "Transition Metal"},
    {"symbol": "Fe", "atomic_number": 26, "group": 8, "period": 4, "category": "Transition Metal"},
    {"symbol": "Co", "atomic_number": 27, "group": 9, "period": 4, "category": "Transition Metal"},
    {"symbol": "Ni", "atomic_number": 28, "group": 10, "period": 4, "category": "Transition Metal"},
    {"symbol": "Cu", "atomic_number": 29, "group": 11, "period": 4, "category": "Transition Metal"},
    {"symbol": "Zn", "atomic_number": 30, "group": 12, "period": 4, "category": "Transition Metal"},
    {"symbol": "Ga", "atomic_number": 31, "group": 13, "period": 4, "category": "Post-Transition Metal"},
    {"symbol": "Ge", "atomic_number": 32, "group": 14, "period": 4, "category": "Metalloid"},
    {"symbol": "As", "atomic_number": 33, "group": 15, "period": 4, "category": "Metalloid"},
    {"symbol": "Se", "atomic_number": 34, "group": 16, "period": 4, "category": "Nonmetal"},
    {"symbol": "Br", "atomic_number": 35, "group": 17, "period": 4, "category": "Halogen"},
    {"symbol": "Kr", "atomic_number": 36, "group": 18, "period": 4, "category": "Noble Gas"},
    {"symbol": "Rb", "atomic_number": 37, "group": 1, "period": 5, "category": "Alkali Metal"},
    {"symbol": "Sr", "atomic_number": 38, "group": 2, "period": 5, "category": "Alkaline Earth Metal"},
    {"symbol": "Y", "atomic_number": 39, "group": 3, "period": 5, "category": "Transition Metal"},
    {"symbol": "Zr", "atomic_number": 40, "group": 4, "period": 5, "category": "Transition Metal"},
    {"symbol": "Nb", "atomic_number": 41, "group": 5, "period": 5, "category": "Transition Metal"},
    {"symbol": "Mo", "atomic_number": 42, "group": 6, "period": 5, "category": "Transition Metal"},
    {"symbol": "Tc", "atomic_number": 43, "group": 7, "period": 5, "category": "Transition Metal"},
    {"symbol": "Ru", "atomic_number": 44, "group": 8, "period": 5, "category": "Transition Metal"},
    {"symbol": "Rh", "atomic_number": 45, "group": 9, "period": 5, "category": "Transition Metal"},
    {"symbol": "Pd", "atomic_number": 46, "group": 10, "period": 5, "category": "Transition Metal"},
    {"symbol": "Ag", "atomic_number": 47, "group": 11, "period": 5, "category": "Transition Metal"},
    {"symbol": "Cd", "atomic_number": 48, "group": 12, "period": 5, "category": "Transition Metal"},
    {"symbol": "In", "atomic_number": 49, "group": 13, "period": 5, "category": "Post-Transition Metal"},
    {"symbol": "Sn", "atomic_number": 50, "group": 14, "period": 5, "category": "Post-Transition Metal"},
    {"symbol": "Sb", "atomic_number": 51, "group": 15, "period": 5, "category": "Metalloid"},
    {"symbol": "Te", "atomic_number": 52, "group": 16, "period": 5, "category": "Metalloid"},
    {"symbol": "I", "atomic_number": 53, "group": 17, "period": 5, "category": "Halogen"},
    {"symbol": "Xe", "atomic_number": 54, "group": 18, "period": 5, "category": "Noble Gas"},
    {"symbol": "Cs", "atomic_number": 55, "group": 1, "period": 6, "category": "Alkali Metal"},
    {"symbol": "Ba", "atomic_number": 56, "group": 2, "period": 6, "category": "Alkaline Earth Metal"},
    {"symbol": "La", "atomic_number": 57, "group": 3, "period": 6, "category": "Lanthanide"},
    {"symbol": "Ce", "atomic_number": 58, "group": 3, "period": 6, "category": "Lanthanide"},
    {"symbol": "Pr", "atomic_number": 59, "group": 3, "period": 6, "category": "Lanthanide"},
    {"symbol": "Nd", "atomic_number": 60, "group": 3, "period": 6, "category": "Lanthanide"},
    {"symbol": "Pm", "atomic_number": 61, "group": 3, "period": 6, "category": "Lanthanide"},
    {"symbol": "Sm", "atomic_number": 62, "group": 3, "period": 6, "category": "Lanthanide"},
    {"symbol": "Eu", "atomic_number": 63, "group": 3, "period": 6, "category": "Lanthanide"},
    {"symbol": "Gd", "atomic_number": 64, "group": 3, "period": 6, "category": "Lanthanide"},
    {"symbol": "Tb", "atomic_number": 65, "group": 3, "period": 6, "category": "Lanthanide"},
    {"symbol": "Dy", "atomic_number": 66, "group": 3, "period": 6, "category": "Lanthanide"},
    {"symbol": "Ho", "atomic_number": 67, "group": 3, "period": 6, "category": "Lanthanide"},
    {"symbol": "Er", "atomic_number": 68, "group": 3, "period": 6, "category": "Lanthanide"},
    {"symbol": "Tm", "atomic_number": 69, "group": 3, "period": 6, "category": "Lanthanide"},
    {"symbol": "Yb", "atomic_number": 70, "group": 3, "period": 6, "category": "Lanthanide"},
    {"symbol": "Lu", "atomic_number": 71, "group": 3, "period": 6, "category": "Lanthanide"},
    {"symbol": "Hf", "atomic_number": 72, "group": 4, "period": 6, "category": "Transition Metal"},
    {"symbol": "Ta", "atomic_number": 73, "group": 5, "period": 6, "category": "Transition Metal"},
    {"symbol": "W", "atomic_number": 74, "group": 6, "period": 6, "category": "Transition Metal"},
    {"symbol": "Re", "atomic_number": 75, "group": 7, "period": 6, "category": "Transition Metal"},
    {"symbol": "Os", "atomic_number": 76, "group": 8, "period": 6, "category": "Transition Metal"},
    {"symbol": "Ir", "atomic_number": 77, "group": 9, "period": 6, "category": "Transition Metal"},
    {"symbol": "Pt", "atomic_number": 78, "group": 10, "period": 6, "category": "Transition Metal"},
    {"symbol": "Au", "atomic_number": 79, "group": 11, "period": 6, "category": "Transition Metal"},
    {"symbol": "Hg", "atomic_number": 80, "group": 12, "period": 6, "category": "Transition Metal"},
    {"symbol": "Tl", "atomic_number": 81, "group": 13, "period": 6, "category": "Post-Transition Metal"},
    {"symbol": "Pb", "atomic_number": 82, "group": 14, "period": 6, "category": "Post-Transition Metal"},
    {"symbol": "Bi", "atomic_number": 83, "group": 15, "period": 6, "category": "Post-Transition Metal"},
    {"symbol": "Po", "atomic_number": 84, "group": 16, "period": 6, "category": "Metalloid"},
    {"symbol": "At", "atomic_number": 85, "group": 17, "period": 6, "category": "Halogen"},
    {"symbol": "Rn", "atomic_number": 86, "group": 18, "period": 6, "category": "Noble Gas"},
    {"symbol": "Fr", "atomic_number": 87, "group": 1, "period": 7, "category": "Alkali Metal"},
    {"symbol": "Ra", "atomic_number": 88, "group": 2, "period": 7, "category": "Alkaline Earth Metal"},
    {"symbol": "Ac", "atomic_number": 89, "group": 3, "period": 7, "category": "Actinide"},
    {"symbol": "Th", "atomic_number": 90, "group": 3, "period": 7, "category": "Actinide"},
    {"symbol": "Pa", "atomic_number": 91, "group": 3, "period": 7, "category": "Actinide"},
    {"symbol": "U", "atomic_number": 92, "group": 3, "period": 7, "category": "Actinide"},
    {"symbol": "Np", "atomic_number": 93, "group": 3, "period": 7, "category": "Actinide"},
    {"symbol": "Pu", "atomic_number": 94, "group": 3, "period": 7, "category": "Actinide"},
    {"symbol": "Am", "atomic_number": 95, "group": 3, "period": 7, "category": "Actinide"},
    {"symbol": "Cm", "atomic_number": 96, "group": 3, "period": 7, "category": "Actinide"},
    {"symbol": "Bk", "atomic_number": 97, "group": 3, "period": 7, "category": "Actinide"},
    {"symbol": "Cf", "atomic_number": 98, "group": 3, "period": 7, "category": "Actinide"},
    {"symbol": "Es", "atomic_number": 99, "group": 3, "period": 7, "category": "Actinide"},
    {"symbol": "Fm", "atomic_number": 100, "group": 3, "period": 7, "category": "Actinide"},
    {"symbol": "Md", "atomic_number": 101, "group": 3, "period": 7, "category": "Actinide"},
    {"symbol": "No", "atomic_number": 102, "group": 3, "period": 7, "category": "Actinide"},
    {"symbol": "Lr", "atomic_number": 103, "group": 3, "period": 7, "category": "Actinide"},
    {"symbol": "Rf", "atomic_number": 104, "group": 4, "period": 7, "category": "Transition Metal"},
    {"symbol": "Db", "atomic_number": 105, "group": 5, "period": 7, "category": "Transition Metal"},
    {"symbol": "Sg", "atomic_number": 106, "group": 6, "period": 7, "category": "Transition Metal"},
    {"symbol": "Bh", "atomic_number": 107, "group": 7, "period": 7, "category": "Transition Metal"},
    {"symbol": "Hs", "atomic_number": 108, "group": 8, "period": 7, "category": "Transition Metal"},
    {"symbol": "Mt", "atomic_number": 109, "group": 9, "period": 7, "category": "Transition Metal"},
    {"symbol": "Ds", "atomic_number": 110, "group": 10, "period": 7, "category": "Transition Metal"},
    {"symbol": "Rg", "atomic_number": 111, "group": 11, "period": 7, "category": "Transition Metal"},
    {"symbol": "Cn", "atomic_number": 112, "group": 12, "period": 7, "category": "Transition Metal"},
    {"symbol": "Nh", "atomic_number": 113, "group": 13, "period": 7, "category": "Post-Transition Metal"},
    {"symbol": "Fl", "atomic_number": 114, "group": 14, "period": 7, "category": "Post-Transition Metal"},
    {"symbol": "Mc", "atomic_number": 115, "group": 15, "period": 7, "category": "Post-Transition Metal"},
    {"symbol": "Lv", "atomic_number": 116, "group": 16, "period": 7, "category": "Post-Transition Metal"},
    {"symbol": "Ts", "atomic_number": 117, "group": 17, "period": 7, "category": "Halogen"},
    {"symbol": "Og", "atomic_number": 118, "group": 18, "period": 7, "category": "Noble Gas"}
]

# Define colors for categories
category_colors = {
    "Nonmetal": "#99ccff",
    "Noble Gas": "#ffcc99",
    "Alkali Metal": "#ff9999",
    "Alkaline Earth Metal": "#ffcc00",
    "Metalloid": "#cc99ff",
    "Halogen": "#66ff66",
    "Transition Metal": "#ff9966",
    "Lanthanide": "#9966ff",
    "Actinide": "#663399",
    "Post-Transition Metal": "#cccccc",
}

# Adjust sizes for better visibility
marker_size = 15  # Reduced marker size
font_size = 8  # Smaller font to fit inside the circles
max_groups = 18
max_periods = 7

# Create polar coordinates for each element
theta = []
r = []
hover_text = []
marker_colors = []
text_colors = []

for element in elements:
    group = element["group"]
    period = element["period"]
    category = element["category"]
    symbol = element["symbol"]
    atomic_number = element["atomic_number"]

    # Adjusting the position for lanthanides and actinides
    if period >= 6:
        r_offset = 0.5  # Add offset to place lanthanides/actinides outside the main grid
    else:
        r_offset = 0

    # Calculate angular and radial positions
    theta.append(2 * np.pi * (group - 1) / max_groups)
    r.append(period + r_offset)

    # Tooltip with detailed information
    hover_text.append(
        f"Symbol: {symbol}<br>Atomic No: {atomic_number}<br>Group: {group}<br>Period: {period}<br>Category: {category}"
    )

    # Marker color based on category
    marker_colors.append(category_colors[category])

    # Text color for symbols (dark for contrast)
    text_colors.append("black")

# Create the Plotly figure
fig = go.Figure()

# Add scatterpolar for the elements
fig.add_trace(
    go.Scatterpolar(
        r=r,
        theta=np.degrees(theta),  # Convert radians to degrees for Plotly
        mode="markers+text",
        text=[e["symbol"] for e in elements],  # Display element symbols
        textposition="middle center",
        marker=dict(size=marker_size, color=marker_colors, line=dict(color="black", width=1)),
        hoverinfo="text",
        hovertext=hover_text,
        textfont=dict(size=font_size, color=text_colors[0]),  # Smaller, darker font
    )
)

# Customize the layout for cleanliness
fig.update_layout(
    polar=dict(
        angularaxis=dict(
            tickmode="array",
            tickvals=np.linspace(0, 360, max_groups, endpoint=False),
            ticktext=[str(i) for i in range(1, max_groups + 1)],
            rotation=90,  # Rotate so group 1 starts at the top
            direction="clockwise",
            showline=False,  # Hide angular grid lines
            showticklabels=True,  # Keep group labels
        ),
        radialaxis=dict(
            showline=False,  # Hide radial grid lines
            showticklabels=False,  # Remove period labels
        ),
    ),
    showlegend=False,
    title="Elegant Circular Periodic Table",
    margin=dict(t=60, b=60, l=60, r=60),
)

# Streamlit app
st.title("Elegant Circular Periodic Table")
st.plotly_chart(fig, use_container_width=True)