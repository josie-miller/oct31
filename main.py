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

# Drop duplicate rows
tech_df.drop_duplicates(inplace=True)
avail_df.drop_duplicates(inplace=True)

# Rename columns to make them consistent
tech_df.rename(columns={'MEDICAL_TECH': 'MEASURE', 'Medical technology': 'MEDICAL_TECH'}, inplace=True)
avail_df.rename(columns={'Medical technology': 'MEDICAL_TECH'}, inplace=True)

# Merge tech and availability datasets on common columns
merged_df = pd.merge(tech_df, avail_df, on=['REF_AREA', 'MEASURE', 'MEDICAL_TECH', 'TIME_PERIOD', 'OBS_VALUE'], how='outer')

# Normalize the 'OBS_VALUE' column to a range of 0 to 1
merged_df['HTI'] = (merged_df['OBS_VALUE'] - merged_df['OBS_VALUE'].min()) / (merged_df['OBS_VALUE'].max() - merged_df['OBS_VALUE'].min())

# Rename columns for consistency with life expectancy dataset
merged_df.rename(columns={'REF_AREA': 'Code', 'TIME_PERIOD': 'Year', 'OBS_VALUE': 'Tech_Value'}, inplace=True)

# Merge with life expectancy dataset
combined_df = pd.merge(merged_df, life_expectancy_df, on=['Code', 'Year'], how='inner')

# Step 2: Define Technologies and Their Impact
technologies = ['CRISPR_Cas9', 'CAR_T_Therapy', 'Genetic_Screening', 'mRNA_Vaccines', '3D_Printed_Prosthetics', 'BCI_Neurorehabilitation', 'Gene_Therapy_Cystic_Fibrosis', 'Liquid_Biopsies_Cancer']
for tech in technologies:
    combined_df[tech] = 0

# Define a function to assign impact weights based on HTI
def assign_impact_weights(row):
    weights = {}
    base_weight = 0.05
    for tech in technologies:
        weights[tech] = base_weight + (row['HTI'] * 0.3)
    return weights

combined_df['Impact_Weights'] = combined_df.apply(assign_impact_weights, axis=1)

# Step 3: Create Future Projections
last_year = combined_df['Year'].max()
future_years = range(last_year + 1, last_year + 11)

# Create a DataFrame for future projections
future_rows = []
for country in combined_df['Country'].unique():
    country_data = combined_df[combined_df['Country'] == country].iloc[-1]
    for year in future_years:
        future_row = country_data.copy()
        future_row['Year'] = year
        future_rows.append(future_row)

future_df = pd.DataFrame(future_rows)

# Step 4: Streamlit Interface for Interactive Technology Adoption
st.title('Healthcare Technology Impact Analysis')

# Displaying available technologies for user selection
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
historical_df = combined_df[combined_df['Year'] <= last_year]
combined_projection_df = pd.concat([historical_df, future_df], ignore_index=True)

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
