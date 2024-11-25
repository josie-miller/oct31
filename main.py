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

# Technology selection
selected_techs = st.multiselect('Select Technologies:', technologies)

# Select Impact Type
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

    # Debug Output to Verify Calculations
    st.write("Selected Technologies:", selected_techs)
    st.write("Selected Impact Type:", selected_impact_type)
    st.write("Sample of Adjusted Life Expectancy Calculations:")
    st.write(country_data[['Year', life_expectancy_column, 'Dynamic_Life_Expectancy']].tail(10))

    # Step 3c: Plotting Life Expectancy Over Time
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

    st.write("This graph shows the impact of healthcare technologies on life expectancy over time for the USA. Use the checkboxes to see how different technologies could potentially affect the population health in the future, starting from 2022. You can also select different impact types to visualize different ways technologies might influence life expectancy.")
