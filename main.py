import pandas as pd
import streamlit as st
import plotly.graph_objs as go

# Step 1: Load and Prepare Data

# Load the provided CSV files
tech_data = pd.read_csv('TECH.csv')
life_expect_data = pd.read_csv('LIFEEXPECT.csv')
avail_data = pd.read_csv('AVAIL.csv')

# Step 1a: Clean the Data
# Remove any duplicates and handle missing values
tech_data_clean = tech_data.drop_duplicates().dropna()
life_expect_clean = life_expect_data.drop_duplicates().dropna(subset=['Country', 'Year']).copy()
avail_data_clean = avail_data.drop_duplicates().dropna()

# Step 1b: Rename columns for merging purposes
tech_data_clean.rename(columns={'REF_AREA': 'Country', 'TIME_PERIOD': 'Year'}, inplace=True)
avail_data_clean.rename(columns={'REF_AREA': 'Country', 'TIME_PERIOD': 'Year'}, inplace=True)

# Step 1c: Map country codes to full names
country_mapping = {
    'AUS': 'Australia', 'AUT': 'Austria', 'BEL': 'Belgium', 'CAN': 'Canada', 'CHL': 'Chile',
    'COL': 'Colombia', 'CZE': 'Czechia', 'DNK': 'Denmark', 'EST': 'Estonia', 'FIN': 'Finland',
    'FRA': 'France', 'DEU': 'Germany', 'GRC': 'Greece', 'HUN': 'Hungary', 'ISL': 'Iceland',
    'IRL': 'Ireland', 'ISR': 'Israel', 'ITA': 'Italy', 'JPN': 'Japan', 'KOR': 'South Korea',
    'LVA': 'Latvia', 'LTU': 'Lithuania', 'LUX': 'Luxembourg', 'MEX': 'Mexico', 'NLD': 'Netherlands',
    'NZL': 'New Zealand', 'NOR': 'Norway', 'POL': 'Poland', 'PRT': 'Portugal', 'SVK': 'Slovakia',
    'SVN': 'Slovenia', 'ESP': 'Spain', 'SWE': 'Sweden', 'CHE': 'Switzerland', 'TUR': 'Turkey',
    'GBR': 'United Kingdom', 'USA': 'United States', 'BRA': 'Brazil', 'BGR': 'Bulgaria',
    'HRV': 'Croatia', 'ROU': 'Romania'
}
tech_data_clean['Country'] = tech_data_clean['Country'].map(country_mapping)
avail_data_clean['Country'] = avail_data_clean['Country'].map(country_mapping)

# Step 1d: Merge the datasets on 'Country' and 'Year'
merged_data = pd.merge(tech_data_clean, life_expect_clean, on=['Country', 'Year'], how='inner')
merged_data = pd.merge(merged_data, avail_data_clean, on=['Country', 'Year'], how='inner')

# Step 1e: Add Historical Technology Adoption Columns
technologies = ['CRISPR_Cas9', 'CAR_T_Therapy', 'Genetic_Screening', 'mRNA_Vaccines', 
                '3D_Printed_Prosthetics', 'BCI_Neurorehabilitation', 
                'Gene_Therapy_Cystic_Fibrosis', 'Liquid_Biopsies_Cancer']

for tech in technologies:
    if tech not in merged_data.columns:
        merged_data[tech] = 0  # Initialize with 0, assuming no initial adoption information is available

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
st.title("Healthcare Technology Impact on Population and Life Expectancy")

# Country selection
country = st.selectbox('Select a Country:', merged_data['Country'].unique())

# Technology selection
selected_techs = st.multiselect('Select Technologies:', technologies)

# Filter data for the selected country
country_data = merged_data[merged_data['Country'] == country].copy()

# Step 3b: Update Life Expectancy Based on Selected Technologies
def calculate_dynamic_life_expectancy(row, selected_techs):
    dynamic_life_expectancy = row['Life Expectancy']
    
    for tech in selected_techs:
        adoption_level = row[tech] if tech in row else 0
        impact_score = tech_impact_scores.get(tech, 1.0)
        dynamic_life_expectancy *= (1 + adoption_level * (impact_score - 1))

    return dynamic_life_expectancy

# Add historical adoption columns for technologies if not already in the dataset
for tech in technologies:
    if tech not in country_data.columns:
        country_data[tech] = 0

# Calculate the dynamic life expectancy
country_data['Dynamic_Life_Expectancy'] = country_data.apply(
    lambda row: calculate_dynamic_life_expectancy(row, selected_techs), axis=1
)

# Step 3c: Plotting Life Expectancy Over Time
fig = go.Figure()

fig.add_trace(go.Scatter(
    x=country_data['Year'],
    y=country_data['Life Expectancy'],
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
    title=f"Life Expectancy Over Time for {country}",
    xaxis_title='Year',
    yaxis_title='Life Expectancy',
    template='plotly_white'
)

st.plotly_chart(fig)

st.write("This graph shows the impact of healthcare technologies on life expectancy over time. Use the checkboxes to see how different technologies could potentially affect the population health in the future.")
