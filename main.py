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
# First, calculate the min and max values of OBS_VALUE
min_value = merged_df['OBS_VALUE'].min()
max_value = merged_df['OBS_VALUE'].max()

# Create the Healthcare Technology Index (HTI) by normalizing OBS_VALUE
merged_df['HTI'] = (merged_df['OBS_VALUE'] - min_value) / (max_value - min_value)

# Rename columns in the merged HTI dataset for consistency with life expectancy dataset
merged_df.rename(columns={'REF_AREA': 'Code', 'Reference area': 'Country', 'TIME_PERIOD': 'Year'}, inplace=True)

# Merge the HTI dataset with the life expectancy dataset on 'Country', 'Code', and 'Year'
combined_df = pd.merge(merged_df, life_expectancy_df, on=['Country', 'Code', 'Year'], how='inner')

# Step 2: Quantify Individual Impact
# Define individual impact scores for each of the eight healthcare technologies based on life expectancy and quality of healthcare
# Add columns for the selected technologies with initial adoption values set to 0 (not adopted)
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

# Apply the function to calculate the impact weights for each country in the dataset
combined_df['Impact_Weights'] = combined_df.apply(assign_impact_weights, axis=1)

# Display the dataset with impact weights using Streamlit
st.title('Healthcare Technology Impact Analysis')
st.write("### Merged Dataset with Healthcare Technology Impact Weights")
st.dataframe(combined_df.head())

# Displaying the available technologies and initial adoption values
st.write("### Available Healthcare Technologies")
selected_techs = []
for tech in technologies:
    if st.checkbox(f"Adopt {tech}", value=False):
        selected_techs.append(tech)
        combined_df[tech] = 1
    else:
        combined_df[tech] = 0

# Calculate future life expectancy based on selected technologies
# Define future projection years (e.g., from 2023 to 2033)
last_year = combined_df['Year'].max()
future_years = range(last_year + 1, last_year + 11)

# Create a new DataFrame for future projections
future_df = pd.DataFrame()
for country in combined_df['Country'].unique():
    country_data = combined_df[combined_df['Country'] == country].iloc[-1]
    for year in future_years:
        future_row = country_data.copy()
        future_row['Year'] = year
        future_df = future_df.append(future_row, ignore_index=True)

# Adjust future life expectancy based on selected technologies
if selected_techs:
    for tech in selected_techs:
        future_df['Life Expectancy'] += future_df[tech] * future_df['Impact_Weights'].apply(lambda x: x.get(tech, 0))

# Combine historical and future data
combined_projection_df = pd.concat([combined_df, future_df], ignore_index=True)

# Create an interactive graph to visualize the future projections
st.write("### Interactive Population Projection Graph")
country_selection = st.selectbox("Select a Country", combined_projection_df['Country'].unique())
filtered_df = combined_projection_df[combined_projection_df['Country'] == country_selection]

# Plot life expectancy projections using Plotly
fig = px.line(
    filtered_df, 
    x='Year', 
    y='Life Expectancy',
    labels={'Life Expectancy': 'Life Expectancy', 'Year': 'Year'},
    title=f'Life Expectancy Projections for {country_selection}'
)
fig.update_traces(mode='lines+markers')
fig.update_layout(legend_title_text='Projection Type', yaxis_title='Life Expectancy (Years)')

# Display the updated graph
st.plotly_chart(fig)

# Note: The graph will now show the historical life expectancy values along with future projections, which are modified based on selected technologies.
