import pandas as pd
import streamlit as st
import plotly.graph_objs as go

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

# Step 2a: Define Impact Scores
tech_impact_scores = {
    'CRISPR_Cas9': 1.05,
    'CAR_T_Therapy': 1.03,
    'Genetic_Screening': 1.02,
    'mRNA_Vaccines': 1.04,
    '3D_Printed_Prosthetics': 1.01,
    'BCI_Neurorehabilitation': 1.02,
    'Gene_Therapy_Cystic_Fibrosis': 1.03,
    'Liquid_Biopsies_Cancer': 1.02
}

# Step 3: Setting up Streamlit for Interactive Visualization

# Step 3a: Streamlit App Layout
st.title("Healthcare Technology Impact on Population and Life Expectancy (USA Only)")

# Technology selection
selected_techs = st.multiselect('Select Technologies:', technologies)

# Filter data for the selected country (USA)
country_data = life_expect_usa.copy()

# Step 3b: Update Life Expectancy Based on Selected Technologies
# Only apply changes for years after 2021

def calculate_dynamic_life_expectancy(row, selected_techs):
    dynamic_life_expectancy = row.get('Life Expectancy') or row.get('Life_Expectancy')
    
    if pd.isna(dynamic_life_expectancy):
        return None

    if row['Year'] > 2021:
        for tech in selected_techs:
            if tech in tech_data_usa.columns:
                adoption_level = tech_data_usa[tech].iloc[0]  # Use the first available value for simplicity
                impact_score = tech_impact_scores.get(tech, 1.0)
                dynamic_life_expectancy *= (1 + adoption_level * (impact_score - 1))

    return dynamic_life_expectancy

# Calculate the dynamic life expectancy
country_data['Dynamic_Life_Expectancy'] = country_data.apply(
    lambda row: calculate_dynamic_life_expectancy(row, selected_techs), axis=1
)

# Drop rows with NaN values in 'Dynamic_Life_Expectancy'
country_data.dropna(subset=['Dynamic_Life_Expectancy'], inplace=True)

# Step 3c: Plotting Life Expectancy Over Time
fig = go.Figure()

fig.add_trace(go.Scatter(
    x=country_data['Year'],
    y=country_data['Life Expectancy'] if 'Life Expectancy' in country_data.columns else country_data['Life_Expectancy'],
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

st.write("This graph shows the impact of healthcare technologies on life expectancy over time for the USA. Use the checkboxes to see how different technologies could potentially affect the population health in the future, starting from 2022.")