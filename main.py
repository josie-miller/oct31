# Import necessary libraries
import pandas as pd
import numpy as np
import streamlit as st

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
    base_weight = 0.1  # Base impact weight for all technologies
    for tech in technologies:
        if row[tech] == 1:  # If the technology is adopted
            weights[tech] = base_weight + (row['HTI'] * 0.5)  # Increase weight based on HTI level
        else:
            weights[tech] = 0
    return weights

# Apply the function to calculate the impact weights for each country in the dataset
combined_df['Impact_Weights'] = combined_df.apply(assign_impact_weights, axis=1)

# Display the dataset with impact weights using Streamlit
st.title('Healthcare Technology Impact Analysis')
st.write("### Merged Dataset with Healthcare Technology Impact Weights")
st.dataframe(combined_df.head())

# Displaying the available technologies and initial adoption values
st.write("### Available Healthcare Technologies")
for tech in technologies:
    combined_df[tech] = st.checkbox(f"Adopt {tech}", value=False)

# Calculate updated HTI based on selected technologies
st.write("### Updated Healthcare Technology Index (HTI)")
selected_techs = [tech for tech in technologies if combined_df[tech].any()]
combined_df['Updated_HTI'] = combined_df['HTI'] + sum([combined_df[tech] * combined_df['Impact_Weights'].apply(lambda x: x.get(tech, 0)) for tech in selected_techs])
st.dataframe(combined_df[['Country', 'Year', 'HTI', 'Updated_HTI']].head())
