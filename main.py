import pandas as pd
import streamlit as st
import plotly.graph_objs as go
import numpy as np

# Step 1: Load and Prepare Data

# Load the provided CSV files
tech_data = pd.read_csv('TECH.csv')
life_expect_data = pd.read_csv('USA.csv')
avail_data = pd.read_csv('AVAIL.csv')

# Step 1a: Clean the Data
# Remove any duplicates and handle missing values
tech_data_clean = tech_data.drop_duplicates().dropna()
life_expect_clean = life_expect_data.drop_duplicates().dropna(subset=['Country', 'Year']).copy()
avail_data_clean = avail_data.drop_duplicates().dropna()

# Step 1b: Filter Data for USA Only
tech_data_usa = tech_data_clean[tech_data_clean['REF_AREA'] == 'USA']
life_expect_usa = life_expect_clean[life_expect_clean['Country'] == 'United States']
avail_data_usa = avail_data_clean[avail_data_clean['REF_AREA'] == 'USA']

# Step 1c: Add Historical Technology Adoption Columns for USA
technologies = ['CRISPR_Cas9', 'CAR_T_Therapy', 'Genetic_Screening', 'mRNA_Vaccines', 
                '3D_Printed_Prosthetics', 'BCI_Neurorehabilitation', 
                'Gene_Therapy_Cystic_Fibrosis', 'Liquid_Biopsies_Cancer']

for tech in technologies:
    if tech not in tech_data_usa.columns:
        tech_data_usa[tech] = 0  # Initialize with 0, assuming no initial adoption information is available

# Step 2: Modeling Impact on Population and Life Expectancy

# Step 2a: Define Impact Scores (Based on Research)
# Impact scores indicate the potential improvement in life expectancy due to each healthcare technology.
tech_impact_scores = {
    'CRISPR_Cas9': 0.15,  # High impact for curing genetic diseases like Sickle Cell Anemia
    'CAR_T_Therapy': 0.12,  # Significant impact for treating cancer
    'Genetic_Screening': 0.10,  # Important for early detection of hereditary diseases
    'mRNA_Vaccines': 0.14,  # High impact due to rapid deployment for infectious diseases
    '3D_Printed_Prosthetics': 0.05,  # Moderate impact on quality of life for those needing prosthetics
    'BCI_Neurorehabilitation': 0.07,  # Moderate impact for neurorehabilitation, improving quality of life
    'Gene_Therapy_Cystic_Fibrosis': 0.13,  # High impact for treating cystic fibrosis
    'Liquid_Biopsies_Cancer': 0.11  # Significant impact for early cancer detection and treatment
}

# Step 2b: Define Different Impact Types
# Different ways technologies could impact life expectancy over time.
impact_types = {
    'Incremental': lambda life_expectancy, impact_score: life_expectancy + impact_score * life_expectancy,
    'Exponential': lambda life_expectancy, impact_score: life_expectancy * (1 + impact_score),
    'Step Increase': lambda life_expectancy, impact_score, step=2: life_expectancy + (impact_score * step),
    'Random Fluctuation': lambda life_expectancy, impact_score: life_expectancy * (1 + impact_score * np.random.uniform(0.8, 1.2)),
    'Delayed Effect': lambda life_expectancy, impact_score, delay=1: life_expectancy * (1 + (impact_score if delay == 0 else 0))
}

# Step 3: Setting up Streamlit for Interactive Visualization

# Step 3a: Streamlit App Layout
st.title("Healthcare Technology Impact on Population and Life Expectancy (USA Only)")

st.write("## Goals of This Analysis")
st.write("The goal of this application is to demonstrate how different healthcare technologies can influence life expectancy in the USA. We analyze the potential impacts of eight significant advancements in healthcare technologies on population health over time. By selecting different technologies and impact types, you can see how they might change future life expectancy trends.")

# Technology selection
st.write("### Select Technologies to Analyze")
st.write("Choose from the list of healthcare advancements to see how each technology might influence the life expectancy of the population.")
selected_techs = st.multiselect('Select Technologies:', technologies)

# Select Impact Type
st.write("### Select Impact Type")
st.write("Choose the type of impact each selected technology will have on life expectancy. Each impact type represents a different scenario of how technology might affect the population over time.")
selected_impact_type = st.selectbox('Select Impact Type:', list(impact_types.keys()), index=0)

# Filter data for the selected country (USA)
country_data = life_expect_usa.copy()

# Ensure column names are consistent
life_expectancy_column = next((col for col in ['Life Expectancy', 'Life_Expectancy'] if col in country_data.columns), None)

if life_expectancy_column is None:
    st.error("Life expectancy column not found in the dataset.")
else:
    # Step 3b: Update Life Expectancy Based on Selected Technologies
    # Only apply changes for years after 2021

    def calculate_dynamic_life_expectancy(row, selected_techs, impact_func):
        dynamic_life_expectancy = row[life_expectancy_column]
        
        if pd.isna(dynamic_life_expectancy):
            return None

        if row['Year'] > 2021:
            for tech in selected_techs:
                impact_score = tech_impact_scores.get(tech, 0.0)
                # Apply the selected impact function
                dynamic_life_expectancy = impact_func(dynamic_life_expectancy, impact_score)

        return dynamic_life_expectancy

    # Get the selected impact function
    impact_func = impact_types[selected_impact_type]

    # Calculate the dynamic life expectancy
    country_data['Dynamic_Life_Expectancy'] = country_data.apply(
        lambda row: calculate_dynamic_life_expectancy(row, selected_techs, impact_func), axis=1
    )

    # Drop rows with NaN values in 'Dynamic_Life_Expectancy'
    country_data.dropna(subset=['Dynamic_Life_Expectancy'], inplace=True)

    # Step 3c: Plotting Life Expectancy Over Time
    st.write("### Life Expectancy Over Time")
    st.write("This graph shows the base life expectancy over time compared to the adjusted life expectancy after applying the effects of selected technologies.")
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=country_data['Year'],
        y=country_data[life_expectancy_column],
        mode='lines',
        name='Base Life Expectancy'
    ))

    fig.add_trace(go.Scatter(
        x=country_data['Year'],
        y=country_data['Dynamic_Life_Expectancy'],
        mode='lines+markers',
        name='Adjusted Life Expectancy'
    ))

    fig.update_layout(
        title="Life Expectancy Over Time for USA",
        xaxis_title='Year',
        yaxis_title='Life Expectancy',
        template='plotly_white'
    )

    st.plotly_chart(fig)

    st.write("### Explanation of Impact Types")
    st.write("- **Incremental**: A gradual increase in life expectancy proportional to the impact score. This simulates continuous improvements over time.")
    st.write("- **Exponential**: A multiplicative effect, where life expectancy grows exponentially, representing significant breakthroughs.")
    st.write("- **Step Increase**: Life expectancy increases in discrete steps, simulating sudden improvements due to technological adoption.")
    st.write("- **Random Fluctuation**: Introduces randomness, reflecting uncertainty or variability in the impact of technology.")
    st.write("- **Delayed Effect**: The impact of the technology is delayed, simulating scenarios where benefits take time to materialize.")

    st.write("This tool allows you to explore how healthcare advancements might shape the future health of the population. Use the different settings to visualize and understand the potential impacts.")
