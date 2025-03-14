import streamlit as st
import numpy as np
import plotly.graph_objects as go

# Function to generate FCC lattice points for CaF2 (Fluorite Structure)
def generate_fcc_lattice(a, n):
    points = []
    types = []
    for x in range(n):
        for y in range(n):
            for z in range(n):
                points.append([x * a, y * a, z * a])
                types.append('Ca')
                points.append([(x + 0.5) * a, (y + 0.5) * a, z * a])
                types.append('Ca')
                points.append([(x + 0.5) * a, y * a, (z + 0.5) * a])
                types.append('Ca')
                points.append([x * a, (y + 0.5) * a, (z + 0.5) * a])
                types.append('Ca')
                points.append([(x + 0.25) * a, (y + 0.25) * a, (z + 0.25) * a])
                types.append('F')
                points.append([(x + 0.75) * a, (y + 0.75) * a, (z + 0.75) * a])
                types.append('F')
    return np.array(points), types

# Function to generate BCC lattice points for Tungsten (W)
def generate_bcc_lattice(a, n):
    points = []
    for x in range(n):
        for y in range(n):
            for z in range(n):
                points.append([x * a, y * a, z * a])
                points.append([(x + 0.5) * a, (y + 0.5) * a, (z + 0.5) * a])
    return np.array(points)

# Molecular coordinates for CH2O (formaldehyde)
ch2o_molecule = np.array([
    [0.0, 0.0, 0.0],
    [1.2, 0.0, 0.0],
    [-0.6, 0.9, 0.0],
    [-0.6, -0.9, 0.0]
])
ch2o_types = ['C', 'O', 'H', 'H']

# Lattice parameters
a_CaF2 = 5.46
a_W = 3.16
n_cells = 5

# Generate lattice points
CaF2_lattice, CaF2_types = generate_fcc_lattice(a_CaF2, n_cells)
W_lattice = generate_bcc_lattice(a_W, n_cells)

# Atom color mappings
atom_colors = {'C': 'black', 'O': 'red', 'H': 'gray', 'Ca': 'blue', 'F': 'green', 'W': 'gold'}

# Streamlit App
def plot_structure(points, types, title):
    fig = go.Figure()
    for atom, color in atom_colors.items():
        atom_points = np.array([p for p, t in zip(points, types) if t == atom])
        if len(atom_points) > 0:
            fig.add_trace(go.Scatter3d(
                x=atom_points[:, 0], y=atom_points[:, 1], z=atom_points[:, 2],
                mode='markers',
                marker=dict(size=5, color=color),
                name=atom
            ))
    fig.update_layout(title=title, margin=dict(l=0, r=0, b=0, t=40))
    st.plotly_chart(fig)

# Plot CaF2
plot_structure(CaF2_lattice, CaF2_types, "CaF₂ (Fluorite Structure)")

# Plot CH2O
plot_structure(ch2o_molecule, ch2o_types, "CH₂O (Formaldehyde)")

# Plot Tungsten
plot_structure(W_lattice, ['W'] * len(W_lattice), "W (BCC Structure)")
