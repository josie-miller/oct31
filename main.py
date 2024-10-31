import streamlit as st
import pandas as pd
import numpy as np
from scipy.optimize import curve_fit
import plotly.graph_objects as go

data_path_usa = 'populationUSA.csv'
population_data_usa = pd.read_csv(data_path_usa)
population_data_usa['Year'] = pd.to_numeric(population_data_usa['Year'], errors='coerce')
population_data_usa = population_data_usa[['Year', 'Population']].dropna()

period_1_end_usa = 1600
period_2_end_usa = 1900
period_3_end_usa = 2023

data_period_1_usa = population_data_usa[population_data_usa['Year'] <= period_1_end_usa]
data_period_2_usa = population_data_usa[(population_data_usa['Year'] > period_1_end_usa) & (population_data_usa['Year'] <= period_2_end_usa)]
data_period_3_usa = population_data_usa[(population_data_usa['Year'] > period_2_end_usa) & (population_data_usa['Year'] <= period_3_end_usa)]

years_1_usa, pop_1_usa = data_period_1_usa['Year'].values, data_period_1_usa['Population'].values
years_2_usa, pop_2_usa = data_period_2_usa['Year'].values, data_period_2_usa['Population'].values
years_3_usa, pop_3_usa = data_period_3_usa['Year'].values, data_period_3_usa['Population'].values

P0_period_1 = 233969    
P0_period_2 = 778503
P0_period_3 = 74829905

def exponential_model_period1(t, r, P0):
    return P0 * np.exp(r * (t - years_1_usa[0]))

def logistic_model(t, r, K, N0, t0):
    return K / (1 + ((K - N0) / N0) * np.exp(-r * (t - t0)))

params_exp1_usa, _ = curve_fit(lambda t, r: exponential_model_period1(t, r, P0_period_1), years_1_usa, pop_1_usa, p0=[0.00001])
r_exp1_usa = params_exp1_usa[0]

params_log2_usa, _ = curve_fit(lambda t, r, K: logistic_model(t, r, K, P0_period_2, years_2_usa[0]), years_2_usa, pop_2_usa, p0=[0.001, 5e8])
r_log2_usa, K_log2_usa = params_log2_usa

params_log3_usa, _ = curve_fit(lambda t, r, K: logistic_model(t, r, K, P0_period_3, years_3_usa[0]), years_3_usa, pop_3_usa, p0=[0.02, 4e9])
r_log3_usa, K_log3_usa = params_log3_usa

def combined_model_usa(years):
    pop_combined = []
    for year in years:
        if year <= period_1_end_usa:
            pop_combined.append(exponential_model_period1(year, r_exp1_usa, P0_period_1))
        elif period_1_end_usa < year <= period_2_end_usa:
            pop_combined.append(logistic_model(year, r_log2_usa, K_log2_usa, P0_period_2, years_2_usa[0]))
        else:
            pop_combined.append(logistic_model(year, r_log3_usa, K_log3_usa, P0_period_3, years_3_usa[0]))
    return np.array(pop_combined)

st.title("U.S. Population Projection Model")

future_years_usa = np.arange(-10000, 3001)
future_years_selected = st.slider("Select future years range for projection", min_value=-10000, max_value=3000, value=(1900, 3000))
future_years_filtered = future_years_usa[(future_years_usa >= future_years_selected[0]) & (future_years_usa <= future_years_selected[1])]

fig = go.Figure()

fig.add_trace(go.Scatter(x=population_data_usa['Year'], y=population_data_usa['Population'], mode='markers', name='U.S. Historical Data', marker=dict(color='blue')))

predicted_population = combined_model_usa(future_years_filtered)
fig.add_trace(go.Scatter(x=future_years_filtered, y=predicted_population, mode='lines', name='Projected Population Model', line=dict(color='teal')))

fig.add_hline(y=K_log3_usa, line_dash="dash", line_color="red", annotation_text=f'Carrying Capacity (Modern): {K_log3_usa:.2e}', annotation_position="bottom left")

fig.update_layout(
    title="Combined Population Model for the United States (Pre-Colonial to Future Projections)",
    xaxis_title="Year",
    yaxis_title="Population",
    legend_title="Legend"
)

st.plotly_chart(fig)
