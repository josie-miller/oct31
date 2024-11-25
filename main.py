# Import necessary libraries
import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px

# Step 1: Data Preparation
# Load the provided CSV files
tech_file_path = 'TECH.csv'
avail_file_path = 'AVAIL.csv'
life_expectancy_file_path = 'LIFEEXPECT.csv'

# Load the datasets
tech_df = pd.read_csv(tech_file_path)
avail_df = pd.read_csv(avail_file_path)
life_expectancy_df = pd.read_csv(life_expectancy_file_path)

# Drop duplicate rows if any exist
tech_df = tech_df.drop_duplicates()
avail_df = avail_df.drop_duplicates()

# Rename columns in both datasets to make them consistent
tech_df.rename(columns={'MEDICAL_TECH': 'MEASURE', 'Medical technology': 'MEDICAL_TECH'}, inplace=True)
avail_df.rename(columns={'Medical technology': 'MEDICAL_TECH'}, inplace=True)

# Merge the datasets on common columns
merged_df = pd.merge(tech_df, avail_df, on=['REF_AREA', 'Reference area', 'MEASURE', 'MEDICAL_TECH', 'TIME_PERIOD', 'OBS_VALUE'], how='outer')

# Normalizing the 'OBS_VALUE' column to a range of 0 to 1
min_value = merged_df['OBS_VALUE'].min()
max_value = merged_df['OBS_VALUE'].max()
merged_df['HTI'] = (merged_df['OBS_VALUE'] - min_value) / (max_value - min_value)

# Rename columns in the merged HTI dataset for consistency with life expectancy dataset
merged_df.rename(columns={'REF_AREA': 'Code', 'Reference area': 'Country', 'TIME_PERIOD': 'Year'}, inplace=True)

# Merge the HTI dataset with the life expectancy dataset on 'Country', 'Code', and 'Year'
combined_df = pd.merge(merged_df, life_expectancy_df, on=['Country', 'Code', 'Year'], how='inner')

# Step 2: Define Technologies and Their Impact
technologies = ['CRISPR_Cas9', 'CAR_T_Therapy', 'Genetic_Screening', 'mRNA_Vaccines', '3D_Printed_Prosthetics', 'BCI_Neurorehabilitation', 'Gene_Therapy_Cystic_Fibrosis', 'Liquid_Biopsies_Cancer']
for tech in technologies:
    combined_df[tech] = 0

# Define a function to assign impact weights based on HTI and healthcare infrastructure
def assign_impact_weights(row):
    weights = {}
    base_weight = 0.05  # Base impact weight for all technologies
    for tech in technologies:
        weights[tech] = base_weight + (row['HTI'] * 0.3)  # Increase weight based on HTI level
    return weights

combined_df['Impact_Weights'] = combined_df.apply(assign_impact_weights, axis=1)

# Step 3: Create Future Projections
# Define future projection years (e.g., from 2023 to 2033)
last_year = combined_df['Year'].max()
future_years = range(last_year + 1, last_year + 11)

# Create a new DataFrame for future projections
future_rows = []
for country in combined_df['Country'].unique():
    country_data = combined_df[combined_df['Country'] == country].iloc[-1]
    for year in future_years:
        future_row = country_data.copy()
        future_row['Year'] = year
        for tech in technologies:
            future_row[tech] = 0  # Initially set future technologies to 0
        future_rows.append(future_row)

future_df = pd.DataFrame(future_rows)

# Step 4: Streamlit Interface for Interactive Technology Adoption
st.title('Healthcare Technology Impact Analysis')

# Displaying the available technologies and allowing user selection
st.write("### Select Healthcare Technologies to Adopt in the Future")
selected_techs = []
for tech in technologies:
    if st.checkbox(f"Adopt {tech}"):
        selected_techs.append(tech)

# Adjust future life expectancy based on selected technologies
if selected_techs:
    for tech in selected_techs:
        future_df[tech] = 1
        future_df['Life Expectancy'] += future_df['Impact_Weights'].apply(lambda x: x.get(tech, 0))

# Combine historical and future data
combined_projection_df = pd.concat([combined_df, future_df], ignore_index=True)

# Step 5: Visualization
st.write("### Interactive Population Projection Graph")
country_selection = st.selectbox("Select a Country", combined_projection_df['Country'].unique())
filtered_df = combined_projection_df[combined_projection_df['Country'] == country_selection]

# Plot life expectancy projections using Plotly
fig = px.line(
    filtered_df, 
    x='Year', 
    y='Life Expectancy',
    labels={'Life Expectancy': 'Life Expectancy (Years)', 'Year': 'Year'},
    title=f'Life Expectancy Projections for {country_selection}'
)
fig.update_traces(mode='lines+markers')
fig.update_layout(yaxis_title='Life Expectancy (Years)')

# Display the updated graph
st.plotly_chart(fig)

# Note: The graph shows the historical life expectancy values along with future projections, which are modified based on selected technologies.
