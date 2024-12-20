import streamlit as st
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import numpy as np
elements = [
    {"symbol": "H", "atomic_number": 1, "group": 1, "period": 1, "category": "Nonmetal", "atomic_weight": 1.008, "electronegativity": 2.20, "ionization_energy": 13.598},
    {"symbol": "He", "atomic_number": 2, "group": 18, "period": 1, "category": "Noble Gas", "atomic_weight": 4.0026, "electronegativity": None, "ionization_energy": 24.587},
    {"symbol": "Li", "atomic_number": 3, "group": 1, "period": 2, "category": "Alkali Metal", "atomic_weight": 6.94, "electronegativity": 0.98, "ionization_energy": 5.392},
    {"symbol": "Be", "atomic_number": 4, "group": 2, "period": 2, "category": "Alkaline Earth Metal", "atomic_weight": 9.0122, "electronegativity": 1.57, "ionization_energy": 9.322},
    {"symbol": "B", "atomic_number": 5, "group": 13, "period": 2, "category": "Metalloid", "atomic_weight": 10.81, "electronegativity": 2.04, "ionization_energy": 8.298},
    {"symbol": "C", "atomic_number": 6, "group": 14, "period": 2, "category": "Nonmetal", "atomic_weight": 12.011, "electronegativity": 2.55, "ionization_energy": 11.260},
    {"symbol": "N", "atomic_number": 7, "group": 15, "period": 2, "category": "Nonmetal", "atomic_weight": 14.007, "electronegativity": 3.04, "ionization_energy": 14.534},
    {"symbol": "O", "atomic_number": 8, "group": 16, "period": 2, "category": "Nonmetal", "atomic_weight": 15.999, "electronegativity": 3.44, "ionization_energy": 13.618},
    {"symbol": "F", "atomic_number": 9, "group": 17, "period": 2, "category": "Halogen", "atomic_weight": 18.998, "electronegativity": 3.98, "ionization_energy": 17.423},
    {"symbol": "Ne", "atomic_number": 10, "group": 18, "period": 2, "category": "Noble Gas", "atomic_weight": 20.180, "electronegativity": None, "ionization_energy": 21.564},
    {"symbol": "Na", "atomic_number": 11, "group": 1, "period": 3, "category": "Alkali Metal", "atomic_weight": 22.990, "electronegativity": 0.93, "ionization_energy": 5.139},
    {"symbol": "Mg", "atomic_number": 12, "group": 2, "period": 3, "category": "Alkaline Earth Metal", "atomic_weight": 24.305, "electronegativity": 1.31, "ionization_energy": 7.646},
    {"symbol": "Al", "atomic_number": 13, "group": 13, "period": 3, "category": "Post-Transition Metal", "atomic_weight": 26.982, "electronegativity": 1.61, "ionization_energy": 5.986},
    {"symbol": "Si", "atomic_number": 14, "group": 14, "period": 3, "category": "Metalloid", "atomic_weight": 28.085, "electronegativity": 1.90, "ionization_energy": 8.151},
    {"symbol": "P", "atomic_number": 15, "group": 15, "period": 3, "category": "Nonmetal", "atomic_weight": 30.974, "electronegativity": 2.19, "ionization_energy": 10.487},
    {"symbol": "S", "atomic_number": 16, "group": 16, "period": 3, "category": "Nonmetal", "atomic_weight": 32.06, "electronegativity": 2.58, "ionization_energy": 10.360},
    {"symbol": "Cl", "atomic_number": 17, "group": 17, "period": 3, "category": "Halogen", "atomic_weight": 35.45, "electronegativity": 3.16, "ionization_energy": 12.968},
    {"symbol": "Ar", "atomic_number": 18, "group": 18, "period": 3, "category": "Noble Gas", "atomic_weight": 39.948, "electronegativity": None, "ionization_energy": 15.760},
    {"symbol": "K", "atomic_number": 19, "group": 1, "period": 4, "category": "Alkali Metal", "atomic_weight": 39.098, "electronegativity": 0.82, "ionization_energy": 4.341},
    {"symbol": "Ca", "atomic_number": 20, "group": 2, "period": 4, "category": "Alkaline Earth Metal", "atomic_weight": 40.078, "electronegativity": 1.00, "ionization_energy": 6.113},
    {"symbol": "Sc", "atomic_number": 21, "group": 3, "period": 4, "category": "Transition Metal", "atomic_weight": 44.956, "electronegativity": 1.36, "ionization_energy": 6.561},
    {"symbol": "Ti", "atomic_number": 22, "group": 4, "period": 4, "category": "Transition Metal", "atomic_weight": 47.867, "electronegativity": 1.54, "ionization_energy": 6.828},
    {"symbol": "V", "atomic_number": 23, "group": 5, "period": 4, "category": "Transition Metal", "atomic_weight": 50.942, "electronegativity": 1.63, "ionization_energy": 6.746},
    {"symbol": "Cr", "atomic_number": 24, "group": 6, "period": 4, "category": "Transition Metal", "atomic_weight": 51.996, "electronegativity": 1.66, "ionization_energy": 6.767},
    {"symbol": "Mn", "atomic_number": 25, "group": 7, "period": 4, "category": "Transition Metal", "atomic_weight": 54.938, "electronegativity": 1.55, "ionization_energy": 7.434},
    {"symbol": "Fe", "atomic_number": 26, "group": 8, "period": 4, "category": "Transition Metal", "atomic_weight": 55.845, "electronegativity": 1.83, "ionization_energy": 7.902},
    {"symbol": "Co", "atomic_number": 27, "group": 9, "period": 4, "category": "Transition Metal", "atomic_weight": 58.933, "electronegativity": 1.88, "ionization_energy": 7.881},
    {"symbol": "Ni", "atomic_number": 28, "group": 10, "period": 4, "category": "Transition Metal", "atomic_weight": 58.693, "electronegativity": 1.91, "ionization_energy": 7.640},
    {"symbol": "Cu", "atomic_number": 29, "group": 11, "period": 4, "category": "Transition Metal", "atomic_weight": 63.546, "electronegativity": 1.90, "ionization_energy": 7.726},
    {"symbol": "Zn", "atomic_number": 30, "group": 12, "period": 4, "category": "Transition Metal", "atomic_weight": 65.38, "electronegativity": 1.65, "ionization_energy": 9.394},
    {"symbol": "Ga", "atomic_number": 31, "group": 13, "period": 4, "category": "Post-Transition Metal", "atomic_weight": 69.723, "electronegativity": 1.81, "ionization_energy": 5.999},
    {"symbol": "Ge", "atomic_number": 32, "group": 14, "period": 4, "category": "Metalloid", "atomic_weight": 72.63, "electronegativity": 2.01, "ionization_energy": 7.9},
    {"symbol": "As", "atomic_number": 33, "group": 15, "period": 4, "category": "Metalloid", "atomic_weight": 74.9216, "electronegativity": 2.18, "ionization_energy": 9.788},
    {"symbol": "Se", "atomic_number": 34, "group": 16, "period": 4, "category": "Nonmetal", "atomic_weight": 78.971, "electronegativity": 2.55, "ionization_energy": 9.752},
    {"symbol": "Br", "atomic_number": 35, "group": 17, "period": 4, "category": "Halogen", "atomic_weight": 79.904, "electronegativity": 2.96, "ionization_energy": 11.813},
    {"symbol": "Kr", "atomic_number": 36, "group": 18, "period": 4, "category": "Noble Gas", "atomic_weight": 83.798, "electronegativity": 3.0, "ionization_energy": 13.999},
    {"symbol": "Rb", "atomic_number": 37, "group": 1, "period": 5, "category": "Alkali Metal", "atomic_weight": 85.4678, "electronegativity": 0.82, "ionization_energy": 4.177},
    {"symbol": "Sr", "atomic_number": 38, "group": 2, "period": 5, "category": "Alkaline Earth Metal", "atomic_weight": 87.62, "electronegativity": 0.95, "ionization_energy": 5.694},
    {"symbol": "Y", "atomic_number": 39, "group": 3, "period": 5, "category": "Transition Metal", "atomic_weight": 88.90584, "electronegativity": 1.22, "ionization_energy": 6.217},
    {"symbol": "Zr", "atomic_number": 40, "group": 4, "period": 5, "category": "Transition Metal", "atomic_weight": 91.224, "electronegativity": 1.33, "ionization_energy": 6.634},
    {"symbol": "Nb", "atomic_number": 41, "group": 5, "period": 5, "category": "Transition Metal", "atomic_weight": 92.90637, "electronegativity": 1.6, "ionization_energy": 6.759},
    {"symbol": "Mo", "atomic_number": 42, "group": 6, "period": 5, "category": "Transition Metal", "atomic_weight": 95.95, "electronegativity": 2.16, "ionization_energy": 7.092},
    {"symbol": "Tc", "atomic_number": 43, "group": 7, "period": 5, "category": "Transition Metal", "atomic_weight": 98.0, "electronegativity": 1.9, "ionization_energy": 7.28},
    {"symbol": "Ru", "atomic_number": 44, "group": 8, "period": 5, "category": "Transition Metal", "atomic_weight": 101.07, "electronegativity": 2.2, "ionization_energy": 7.36},
    {"symbol": "Rh", "atomic_number": 45, "group": 9, "period": 5, "category": "Transition Metal", "atomic_weight": 102.9055, "electronegativity": 2.28, "ionization_energy": 7.459},
    {"symbol": "Pd", "atomic_number": 46, "group": 10, "period": 5, "category": "Transition Metal", "atomic_weight": 106.42, "electronegativity": 2.2, "ionization_energy": 8.337},
    {"symbol": "Ag", "atomic_number": 47, "group": 11, "period": 5, "category": "Transition Metal", "atomic_weight": 107.8682, "electronegativity": 1.93, "ionization_energy": 7.576},
    {"symbol": "Cd", "atomic_number": 48, "group": 12, "period": 5, "category": "Transition Metal", "atomic_weight": 112.414, "electronegativity": 1.69, "ionization_energy": 8.993},
    {"symbol": "In", "atomic_number": 49, "group": 13, "period": 5, "category": "Post-Transition Metal", "atomic_weight": 114.818, "electronegativity": 1.78, "ionization_energy": 5.786},
    {"symbol": "Sn", "atomic_number": 50, "group": 14, "period": 5, "category": "Post-Transition Metal", "atomic_weight": 118.71, "electronegativity": 1.96, "ionization_energy": 7.344},
    {"symbol": "Sb", "atomic_number": 51, "group": 15, "period": 5, "category": "Metalloid", "atomic_weight": 121.76, "electronegativity": 2.05, "ionization_energy": 8.608},
    {"symbol": "Te", "atomic_number": 52, "group": 16, "period": 5, "category": "Metalloid", "atomic_weight": 127.6, "electronegativity": 2.1, "ionization_energy": 9.009},
    {"symbol": "I", "atomic_number": 53, "group": 17, "period": 5, "category": "Halogen", "atomic_weight": 126.90447, "electronegativity": 2.66, "ionization_energy": 10.451},
    {"symbol": "Xe", "atomic_number": 54, "group": 18, "period": 5, "category": "Noble Gas", "atomic_weight": 131.293, "electronegativity": 2.6, "ionization_energy": 12.129},
    {"symbol": "Cs", "atomic_number": 55, "group": 1, "period": 6, "category": "Alkali Metal", "atomic_weight": 132.90545, "electronegativity": 0.79, "ionization_energy": 3.894},
    {"symbol": "Ba", "atomic_number": 56, "group": 2, "period": 6, "category": "Alkaline Earth Metal", "atomic_weight": 137.327, "electronegativity": 0.89, "ionization_energy": 5.212},
    {"symbol": "La", "atomic_number": 57, "group": None, "period": 6, "category": "Lanthanide", "atomic_weight": 138.90547, "electronegativity": 1.1, "ionization_energy": 5.576},
    {"symbol": "Ce", "atomic_number": 58, "group": None, "period": 6, "category": "Lanthanide", "atomic_weight": 140.116, "electronegativity": 1.12, "ionization_energy": 5.538},
    {"symbol": "Pr", "atomic_number": 59, "group": None, "period": 6, "category": "Lanthanide", "atomic_weight": 140.90766, "electronegativity": 1.13, "ionization_energy": 5.464},
    {"symbol": "Nd", "atomic_number": 60, "group": None, "period": 6, "category": "Lanthanide", "atomic_weight": 144.242, "electronegativity": 1.14, "ionization_energy": 5.525},
    {"symbol": "Pm", "atomic_number": 61, "group": None, "period": 6, "category": "Lanthanide", "atomic_weight": 145.0, "electronegativity": 1.13, "ionization_energy": 5.582},
    {"symbol": "Sm", "atomic_number": 62, "group": None, "period": 6, "category": "Lanthanide", "atomic_weight": 150.36, "electronegativity": 1.17, "ionization_energy": 5.643},
    {"symbol": "Eu", "atomic_number": 63, "group": None, "period": 6, "category": "Lanthanide", "atomic_weight": 151.964, "electronegativity": 1.2, "ionization_energy": 5.670},
    {"symbol": "Gd", "atomic_number": 64, "group": None, "period": 6, "category": "Lanthanide", "atomic_weight": 157.25, "electronegativity": 1.2, "ionization_energy": 6.149},
    {"symbol": "Tb", "atomic_number": 65, "group": None, "period": 6, "category": "Lanthanide", "atomic_weight": 158.92535, "electronegativity": 1.1, "ionization_energy": 5.863},
    {"symbol": "Dy", "atomic_number": 66, "group": None, "period": 6, "category": "Lanthanide", "atomic_weight": 162.5, "electronegativity": 1.22, "ionization_energy": 5.938},
    {"symbol": "Ho", "atomic_number": 67, "group": None, "period": 6, "category": "Lanthanide", "atomic_weight": 164.93033, "electronegativity": 1.23, "ionization_energy": 6.021},
    {"symbol": "Er", "atomic_number": 68, "group": None, "period": 6, "category": "Lanthanide", "atomic_weight": 167.259, "electronegativity": 1.24, "ionization_energy": 6.108},
    {"symbol": "Tm", "atomic_number": 69, "group": None, "period": 6, "category": "Lanthanide", "atomic_weight": 168.93422, "electronegativity": 1.25, "ionization_energy": 6.184},
    {"symbol": "Yb", "atomic_number": 70, "group": None, "period": 6, "category": "Lanthanide", "atomic_weight": 173.045, "electronegativity": 1.1, "ionization_energy": 6.254},
    {"symbol": "Lu", "atomic_number": 71, "group": None, "period": 6, "category": "Lanthanide", "atomic_weight": 174.9668, "electronegativity": 1.27, "ionization_energy": 5.425},
    {"symbol": "Hf", "atomic_number": 72, "group": 4, "period": 6, "category": "Transition Metal", "atomic_weight": 178.49, "electronegativity": 1.3, "ionization_energy": 6.825},
    {"symbol": "Ta", "atomic_number": 73, "group": 5, "period": 6, "category": "Transition Metal", "atomic_weight": 180.94788, "electronegativity": 1.5, "ionization_energy": 7.549},
    {"symbol": "W", "atomic_number": 74, "group": 6, "period": 6, "category": "Transition Metal", "atomic_weight": 183.84, "electronegativity": 2.36, "ionization_energy": 7.864},
    {"symbol": "Re", "atomic_number": 75, "group": 7, "period": 6, "category": "Transition Metal", "atomic_weight": 186.207, "electronegativity": 1.9, "ionization_energy": 7.833},
    {"symbol": "Os", "atomic_number": 76, "group": 8, "period": 6, "category": "Transition Metal", "atomic_weight": 190.23, "electronegativity": 2.2, "ionization_energy": 8.7},
    {"symbol": "Ir", "atomic_number": 77, "group": 9, "period": 6, "category": "Transition Metal", "atomic_weight": 192.217, "electronegativity": 2.2, "ionization_energy": 9.1},
    {"symbol": "Pt", "atomic_number": 78, "group": 10, "period": 6, "category": "Transition Metal", "atomic_weight": 195.084, "electronegativity": 2.28, "ionization_energy": 9.0},
    {"symbol": "Au", "atomic_number": 79, "group": 11, "period": 6, "category": "Transition Metal", "atomic_weight": 196.966569, "electronegativity": 2.54, "ionization_energy": 9.225},
    {"symbol": "Hg", "atomic_number": 80, "group": 12, "period": 6, "category": "Transition Metal", "atomic_weight": 200.592, "electronegativity": 2.0, "ionization_energy": 10.437},
    {"symbol": "Tl", "atomic_number": 81, "group": 13, "period": 6, "category": "Post-Transition Metal", "atomic_weight": 204.38, "electronegativity": 1.62, "ionization_energy": 6.108},
    {"symbol": "Pb", "atomic_number": 82, "group": 14, "period": 6, "category": "Post-Transition Metal", "atomic_weight": 207.2, "electronegativity": 2.33, "ionization_energy": 7.417},
    {"symbol": "Bi", "atomic_number": 83, "group": 15, "period": 6, "category": "Post-Transition Metal", "atomic_weight": 208.9804, "electronegativity": 2.02, "ionization_energy": 7.285},
    {"symbol": "Po", "atomic_number": 84, "group": 16, "period": 6, "category": "Metalloid", "atomic_weight": 209.0, "electronegativity": 2.0, "ionization_energy": 8.414},
    {"symbol": "At", "atomic_number": 85, "group": 17, "period": 6, "category": "Halogen", "atomic_weight": 210.0, "electronegativity": 2.2, "ionization_energy": 9.3},
    {"symbol": "Rn", "atomic_number": 86, "group": 18, "period": 6, "category": "Noble Gas", "atomic_weight": 222.0, "electronegativity": 0.0, "ionization_energy": 10.748},
    {"symbol": "Fr", "atomic_number": 87, "group": 1, "period": 7, "category": "Alkali Metal", "atomic_weight": 223.0, "electronegativity": 0.7, "ionization_energy": 4.072},
    {"symbol": "Ra", "atomic_number": 88, "group": 2, "period": 7, "category": "Alkaline Earth Metal", "atomic_weight": 226.0, "electronegativity": 0.9, "ionization_energy": 5.278},
    {"symbol": "Ac", "atomic_number": 89, "group": None, "period": 7, "category": "Actinide", "atomic_weight": 227.0, "electronegativity": 1.1, "ionization_energy": 5.17},
    {"symbol": "Th", "atomic_number": 90, "group": None, "period": 7, "category": "Actinide", "atomic_weight": 232.0377, "electronegativity": 1.3, "ionization_energy": 6.306},
    {"symbol": "Pa", "atomic_number": 91, "group": None, "period": 7, "category": "Actinide", "atomic_weight": 231.03588, "electronegativity": 1.5, "ionization_energy": 5.89},
    {"symbol": "U", "atomic_number": 92, "group": None, "period": 7, "category": "Actinide", "atomic_weight": 238.02891, "electronegativity": 1.38, "ionization_energy": 6.194},
    {"symbol": "Np", "atomic_number": 93, "group": None, "period": 7, "category": "Actinide", "atomic_weight": 237.0, "electronegativity": 1.36, "ionization_energy": 6.265},
    {"symbol": "Pu", "atomic_number": 94, "group": None, "period": 7, "category": "Actinide", "atomic_weight": 244.0, "electronegativity": 1.28, "ionization_energy": 6.026},
    {"symbol": "Am", "atomic_number": 95, "group": None, "period": 7, "category": "Actinide", "atomic_weight": 243.0, "electronegativity": 1.13, "ionization_energy": 5.993},
    {"symbol": "Cm", "atomic_number": 96, "group": None, "period": 7, "category": "Actinide", "atomic_weight": 247.0, "electronegativity": 1.28, "ionization_energy": 5.991},
    {"symbol": "Bk", "atomic_number": 97, "group": None, "period": 7, "category": "Actinide", "atomic_weight": 247.0, "electronegativity": 1.3, "ionization_energy": 6.197},
    {"symbol": "Cf", "atomic_number": 98, "group": None, "period": 7, "category": "Actinide", "atomic_weight": 251.0, "electronegativity": 1.3, "ionization_energy": 6.281},
    {"symbol": "Es", "atomic_number": 99, "group": None, "period": 7, "category": "Actinide", "atomic_weight": 252.0, "electronegativity": 1.3, "ionization_energy": 6.42},
    {"symbol": "Fm", "atomic_number": 100, "group": None, "period": 7, "category": "Actinide", "atomic_weight": 257.0, "electronegativity": None, "ionization_energy": 6.5},
    {"symbol": "Md", "atomic_number": 101, "group": None, "period": 7, "category": "Actinide", "atomic_weight": 258.0, "electronegativity": None, "ionization_energy": 6.58},
    {"symbol": "No", "atomic_number": 102, "group": None, "period": 7, "category": "Actinide", "atomic_weight": 259.0, "electronegativity": None, "ionization_energy": 6.65},
    {"symbol": "Lr", "atomic_number": 103, "group": None, "period": 7, "category": "Actinide", "atomic_weight": 262.0, "electronegativity": None, "ionization_energy": 4.9},
    {"symbol": "Rf", "atomic_number": 104, "group": 4, "period": 7, "category": "Transition Metal", "atomic_weight": 267.0, "electronegativity": None, "ionization_energy": None},
    {"symbol": "Db", "atomic_number": 105, "group": 5, "period": 7, "category": "Transition Metal", "atomic_weight": 270.0, "electronegativity": None, "ionization_energy": None},
    {"symbol": "Sg", "atomic_number": 106, "group": 6, "period": 7, "category": "Transition Metal", "atomic_weight": 271.0, "electronegativity": None, "ionization_energy": None},
    {"symbol": "Bh", "atomic_number": 107, "group": 7, "period": 7, "category": "Transition Metal", "atomic_weight": 270.0, "electronegativity": None, "ionization_energy": None},
    {"symbol": "Hs", "atomic_number": 108, "group": 8, "period": 7, "category": "Transition Metal", "atomic_weight": 277.0, "electronegativity": None, "ionization_energy": None},
    {"symbol": "Mt", "atomic_number": 109, "group": 9, "period": 7, "category": "Transition Metal", "atomic_weight": 278.0, "electronegativity": None, "ionization_energy": None},
    {"symbol": "Ds", "atomic_number": 110, "group": 10, "period": 7, "category": "Transition Metal", "atomic_weight": 281.0, "electronegativity": None, "ionization_energy": None},
    {"symbol": "Rg", "atomic_number": 111, "group": 11, "period": 7, "category": "Transition Metal", "atomic_weight": 282.0, "electronegativity": None, "ionization_energy": None},
    {"symbol": "Cn", "atomic_number": 112, "group": 12, "period": 7, "category": "Transition Metal", "atomic_weight": 285.0, "electronegativity": None, "ionization_energy": None},
    {"symbol": "Nh", "atomic_number": 113, "group": 13, "period": 7, "category": "Post-Transition Metal", "atomic_weight": 286.0, "electronegativity": None, "ionization_energy": None},
    {"symbol": "Fl", "atomic_number": 114, "group": 14, "period": 7, "category": "Post-Transition Metal", "atomic_weight": 289.0, "electronegativity": None, "ionization_energy": None},
    {"symbol": "Mc", "atomic_number": 115, "group": 15, "period": 7, "category": "Post-Transition Metal", "atomic_weight": 290.0, "electronegativity": None, "ionization_energy": None},
    {"symbol": "Lv", "atomic_number": 116, "group": 16, "period": 7, "category": "Post-Transition Metal", "atomic_weight": 293.0, "electronegativity": None, "ionization_energy": None},
    {"symbol": "Ts", "atomic_number": 117, "group": 17, "period": 7, "category": "Halogen", "atomic_weight": 294.0, "electronegativity": None, "ionization_energy": None},
    {"symbol": "Og", "atomic_number": 118, "group": 18, "period": 7, "category": "Noble Gas", "atomic_weight": 294.0, "electronegativity": None, "ionization_energy": None}        
    ]
atomic_radii_data = [
    {"Atomic Number": 1, "Symbol": "H", "Calculated Radius": 53},
    {"Atomic Number": 2, "Symbol": "He", "Calculated Radius": 31},
    {"Atomic Number": 3, "Symbol": "Li", "Calculated Radius": 167},
    {"Atomic Number": 4, "Symbol": "Be", "Calculated Radius": 112},
    {"Atomic Number": 5, "Symbol": "B", "Calculated Radius": 87},
    {"Atomic Number": 6, "Symbol": "C", "Calculated Radius": 67},
    {"Atomic Number": 7, "Symbol": "N", "Calculated Radius": 56},
    {"Atomic Number": 8, "Symbol": "O", "Calculated Radius": 48},
    {"Atomic Number": 9, "Symbol": "F", "Calculated Radius": 42},
    {"Atomic Number": 10, "Symbol": "Ne", "Calculated Radius": 38},
    {"Atomic Number": 11, "Symbol": "Na", "Calculated Radius": 190},
    {"Atomic Number": 12, "Symbol": "Mg", "Calculated Radius": 145},
    {"Atomic Number": 13, "Symbol": "Al", "Calculated Radius": 118},
    {"Atomic Number": 14, "Symbol": "Si", "Calculated Radius": 111},
    {"Atomic Number": 15, "Symbol": "P", "Calculated Radius": 98},
    {"Atomic Number": 16, "Symbol": "S", "Calculated Radius": 88},
    {"Atomic Number": 17, "Symbol": "Cl", "Calculated Radius": 79},
    {"Atomic Number": 18, "Symbol": "Ar", "Calculated Radius": 71},
    {"Atomic Number": 19, "Symbol": "K", "Calculated Radius": 243},
    {"Atomic Number": 20, "Symbol": "Ca", "Calculated Radius": 194},
    {"Atomic Number": 21, "Symbol": "Sc", "Calculated Radius": 184},
    {"Atomic Number": 22, "Symbol": "Ti", "Calculated Radius": 176},
    {"Atomic Number": 23, "Symbol": "V", "Calculated Radius": 171},
    {"Atomic Number": 24, "Symbol": "Cr", "Calculated Radius": 166},
    {"Atomic Number": 25, "Symbol": "Mn", "Calculated Radius": 161},
    {"Atomic Number": 26, "Symbol": "Fe", "Calculated Radius": 156},
    {"Atomic Number": 27, "Symbol": "Co", "Calculated Radius": 152},
    {"Atomic Number": 28, "Symbol": "Ni", "Calculated Radius": 149},
    {"Atomic Number": 29, "Symbol": "Cu", "Calculated Radius": 145},
    {"Atomic Number": 30, "Symbol": "Zn", "Calculated Radius": 142},
    {"Atomic Number": 31, "Symbol": "Ga", "Calculated Radius": 136},
    {"Atomic Number": 32, "Symbol": "Ge", "Calculated Radius": 125},
    {"Atomic Number": 33, "Symbol": "As", "Calculated Radius": 114},
    {"Atomic Number": 34, "Symbol": "Se", "Calculated Radius": 103},
    {"Atomic Number": 35, "Symbol": "Br", "Calculated Radius": 94},
    {"Atomic Number": 36, "Symbol": "Kr", "Calculated Radius": 88},
    {"Atomic Number": 37, "Symbol": "Rb", "Calculated Radius": 265},
    {"Atomic Number": 38, "Symbol": "Sr", "Calculated Radius": 219},
    {"Atomic Number": 39, "Symbol": "Y", "Calculated Radius": 212},
    {"Atomic Number": 40, "Symbol": "Zr", "Calculated Radius": 206},
    {"Atomic Number": 41, "Symbol": "Nb", "Calculated Radius": 198},
    {"Atomic Number": 42, "Symbol": "Mo", "Calculated Radius": 190},
    {"Atomic Number": 43, "Symbol": "Tc", "Calculated Radius": 183},
    {"Atomic Number": 44, "Symbol": "Ru", "Calculated Radius": 178},
    {"Atomic Number": 45, "Symbol": "Rh", "Calculated Radius": 173},
    {"Atomic Number": 46, "Symbol": "Pd", "Calculated Radius": 169},
    {"Atomic Number": 47, "Symbol": "Ag", "Calculated Radius": 165},
    {"Atomic Number": 48, "Symbol": "Cd", "Calculated Radius": 161},
    {"Atomic Number": 49, "Symbol": "In", "Calculated Radius": 156},
    {"Atomic Number": 50, "Symbol": "Sn", "Calculated Radius": 145},
    {"Atomic Number": 51, "Symbol": "Sb", "Calculated Radius": 133},
    {"Atomic Number": 52, "Symbol": "Te", "Calculated Radius": 123},
    {"Atomic Number": 53, "Symbol": "I", "Calculated Radius": 115},
    {"Atomic Number": 54, "Symbol": "Xe", "Calculated Radius": 108},
    {"Atomic Number": 55, "Symbol": "Cs", "Calculated Radius": 298},
    {"Atomic Number": 56, "Symbol": "Ba", "Calculated Radius": 253},
    {"Atomic Number": 57, "Symbol": "La", "Calculated Radius": 226},
    {"Atomic Number": 58, "Symbol": "Ce", "Calculated Radius": 210},
    {"Atomic Number": 59, "Symbol": "Pr", "Calculated Radius": 247},
    {"Atomic Number": 60, "Symbol": "Nd", "Calculated Radius": 206},
    {"Atomic Number": 61, "Symbol": "Pm", "Calculated Radius": 205},
    {"Atomic Number": 62, "Symbol": "Sm", "Calculated Radius": 238},
    {"Atomic Number": 63, "Symbol": "Eu", "Calculated Radius": 231},
    {"Atomic Number": 64, "Symbol": "Gd", "Calculated Radius": 233},
    {"Atomic Number": 65, "Symbol": "Tb", "Calculated Radius": 225},
    {"Atomic Number": 66, "Symbol": "Dy", "Calculated Radius": 228},
    {"Atomic Number": 67, "Symbol": "Ho", "Calculated Radius": 226},
    {"Atomic Number": 68, "Symbol": "Er", "Calculated Radius": 226},
    {"Atomic Number": 69, "Symbol": "Tm", "Calculated Radius": 222},
    {"Atomic Number": 70, "Symbol": "Yb", "Calculated Radius": 222},
    {"Atomic Number": 71, "Symbol": "Lu", "Calculated Radius": 217},
    {"Atomic Number": 72, "Symbol": "Hf", "Calculated Radius": 208},
    {"Atomic Number": 73, "Symbol": "Ta", "Calculated Radius": 200},
    {"Atomic Number": 74, "Symbol": "W", "Calculated Radius": 193},
    {"Atomic Number": 75, "Symbol": "Re", "Calculated Radius": 188},
    {"Atomic Number": 76, "Symbol": "Os", "Calculated Radius": 185},
    {"Atomic Number": 77, "Symbol": "Ir", "Calculated Radius": 180},
    {"Atomic Number": 78, "Symbol": "Pt", "Calculated Radius": 177},
    {"Atomic Number": 79, "Symbol": "Au", "Calculated Radius": 174},
    {"Atomic Number": 80, "Symbol": "Hg", "Calculated Radius": 171},
    {"Atomic Number": 81, "Symbol": "Tl", "Calculated Radius": 156},
    {"Atomic Number": 82, "Symbol": "Pb", "Calculated Radius": 154},
    {"Atomic Number": 83, "Symbol": "Bi", "Calculated Radius": 143},
    {"Atomic Number": 84, "Symbol": "Po", "Calculated Radius": 135},
    {"Atomic Number": 85, "Symbol": "At", "Calculated Radius": 127},
    {"Atomic Number": 86, "Symbol": "Rn", "Calculated Radius": 120},
    {"Atomic Number": 87, "Symbol": "Fr", "Calculated Radius": None},
    {"Atomic Number": 88, "Symbol": "Ra", "Calculated Radius": None},
    {"Atomic Number": 89, "Symbol": "Ac", "Calculated Radius": None},
    {"Atomic Number": 90, "Symbol": "Th", "Calculated Radius": None},
    {"Atomic Number": 91, "Symbol": "Pa", "Calculated Radius": None},
    {"Atomic Number": 92, "Symbol": "U", "Calculated Radius": None},
    {"Atomic Number": 93, "Symbol": "Np", "Calculated Radius": None},
    {"Atomic Number": 94, "Symbol": "Pu", "Calculated Radius": None},
    {"Atomic Number": 95, "Symbol": "Am", "Calculated Radius": None},
    {"Atomic Number": 96, "Symbol": "Cm", "Calculated Radius": None},
    {"Atomic Number": 97, "Symbol": "Bk", "Calculated Radius": None},
    {"Atomic Number": 98, "Symbol": "Cf", "Calculated Radius": None},
    {"Atomic Number": 99, "Symbol": "Es", "Calculated Radius": None},
    {"Atomic Number": 100, "Symbol": "Fm", "Calculated Radius": None},
    {"Atomic Number": 101, "Symbol": "Md", "Calculated Radius": None},
    {"Atomic Number": 102, "Symbol": "No", "Calculated Radius": None},
    {"Atomic Number": 103, "Symbol": "Lr", "Calculated Radius": None},
    {"Atomic Number": 104, "Symbol": "Rf", "Calculated Radius": None},
    {"Atomic Number": 105, "Symbol": "Db", "Calculated Radius": None},
    {"Atomic Number": 106, "Symbol": "Sg", "Calculated Radius": None},
    {"Atomic Number": 107, "Symbol": "Bh", "Calculated Radius": None},
    {"Atomic Number": 108, "Symbol": "Hs", "Calculated Radius": None},
    {"Atomic Number": 109, "Symbol": "Mt", "Calculated Radius": None},
    {"Atomic Number": 110, "Symbol": "Ds", "Calculated Radius": None},
    {"Atomic Number": 111, "Symbol": "Rg", "Calculated Radius": None},
    {"Atomic Number": 112, "Symbol": "Cn", "Calculated Radius": None},
    {"Atomic Number": 113, "Symbol": "Nh", "Calculated Radius": None},
    {"Atomic Number": 114, "Symbol": "Fl", "Calculated Radius": None},
    {"Atomic Number": 115, "Symbol": "Mc", "Calculated Radius": None},
    {"Atomic Number": 116, "Symbol": "Lv", "Calculated Radius": None},
    {"Atomic Number": 117, "Symbol": "Ts", "Calculated Radius": None},
    {"Atomic Number": 118, "Symbol": "Og", "Calculated Radius": None},
]

atomic_radii_dict = {entry["Atomic Number"]: entry["Calculated Radius"] for entry in atomic_radii_data}

# Updating elements
for element in elements:
    atomic_number = element["atomic_number"]
    if atomic_number in atomic_radii_dict:
        element["Calculated Radius"] = atomic_radii_dict[atomic_number]

category_colors = {
    "Nonmetal": "#99ccff",
    "Noble Gas": "#ffcc99",
    "Alkali Metal": "#ff9999",
    "Alkaline Earth Metal": "#ffcc00",
    "Metalloid": "#cc99ff",
    "Halogen": "#66ff66",
    "Transition Metal": "#ff9966",
    "Lanthanide": "#9966ff",
    "Actinide": "#663399",
    "Post-Transition Metal": "#cccccc",
}
max_groups = 18
min_electronegativity = min(e["electronegativity"] for e in elements if e["electronegativity"] is not None)
max_electronegativity = max(e["electronegativity"] for e in elements if e["electronegativity"] is not None)
theta_main = []
r_main = []
hover_text_main = []
marker_colors_main = []
marker_size_main = []
font_size_main = []
opacity_main = []

theta_outer = []
r_outer = []
hover_text_outer = []
marker_colors_outer = []
marker_size_outer = []
font_size_outer = []
opacity_outer = []

for element in elements:
    size = 13 + (element["atomic_weight"] / 20)
    electronegativity = element["electronegativity"] or (min_electronegativity + 0.5)
    opacity = 0.2 + 0.8 * ((electronegativity - min_electronegativity) / (max_electronegativity - min_electronegativity))
    hover_text = (
        f"Symbol: {element['symbol']}<br>"
        f"Atomic Number: {element['atomic_number']}<br>"
        f"Atomic Weight: {element['atomic_weight']}<br>"
        f"Electronegativity: {element['electronegativity'] or 'N/A'}<br>"
        f"1st Ionization Energy: {element['ionization_energy'] or 'N/A'} eV<br>"
        f"Category: {element['category']}<br>"
        f"Group: {element['group'] or 'N/A'}<br>"
        f"Period: {element['period']}"
        f"Calculated Radius: {element['Calculated Radius'] or 'N/A'} pm<br>"
    )
    if element["category"] in ["Lanthanide", "Actinide"]:
        if element["category"] == "Lanthanide":
            r_outer.append(8) 
        else:
            r_outer.append(9) 
        theta_outer.append(2 * np.pi * (element["atomic_number"] - 57) / 15)
        hover_text_outer.append(hover_text)
        marker_colors_outer.append(category_colors[element["category"]])
        marker_size_outer.append(size)
        font_size_outer.append(size * 0.5)
        opacity_outer.append(opacity)
    else:
        theta_main.append(2 * np.pi * (element["group"] - 1) / max_groups)
        r_main.append(element["period"])
        hover_text_main.append(hover_text
        )
        marker_colors_main.append(category_colors[element["category"]])
        marker_size_main.append(size)
        font_size_main.append(size * 0.5) 
        opacity_main.append(opacity)

fig = go.Figure()
fig.add_trace(
    go.Scatterpolar(
        r=r_main,
        theta=np.degrees(theta_main),
        mode="markers+text",
        text=[e["symbol"] for e in elements if e["category"] not in ["Lanthanide", "Actinide"]],
        textposition="middle center",
        marker=dict(
            size=marker_size_main,
            color=marker_colors_main,
            opacity=opacity_main,
            line=dict(color="black", width=1),
        ),
        hoverinfo="text",
        hovertext=hover_text_main,
        textfont=dict(size=font_size_main, color="black"),
        showlegend = False,
    )
)
fig.add_trace(
    go.Scatterpolar(
        r=r_outer,
        theta=np.degrees(theta_outer),
        mode="markers+text",
        text=[e["symbol"] for e in elements if e["category"] in ["Lanthanide", "Actinide"]],
        textposition="middle center",
        marker=dict(
            size=marker_size_outer,
            color=marker_colors_outer,
            opacity=opacity_outer,
            line=dict(color="black", width=1),
        ),
        hoverinfo="text",
        hovertext=hover_text_outer,
        textfont=dict(size=font_size_outer, color="black"),
        showlegend = False,
    )
)
legend_categories = list(category_colors.keys())
legend_colors = list(category_colors.values())
for category, color in zip(legend_categories, legend_colors):
    fig.add_trace(
        go.Scatterpolar(
            r=[0],
            theta=[0],
            mode="markers",
            marker=dict(size=15, color=color, line=dict(color="black", width=1)),
            name=category, 
            hoverinfo="none",
            showlegend=True,
        )
    )
fig.update_layout(
    polar=dict(
        angularaxis=dict(
            tickmode="array",
            tickvals=np.linspace(0, 360, max_groups, endpoint=False),
            ticktext=[str(i) for i in range(1, max_groups + 1)],
            rotation=90,
            direction="clockwise",
            showline=False,
        ),
        radialaxis=dict(
            showline=False,
            showticklabels=False,
        ),
    ),
    legend=dict(
        title=dict(text="Element Categories", font=dict(size=12)),
        orientation="h",
        yanchor="top",
        y=-0.2,
        xanchor="center",
        x=0.5,
    ),
    showlegend=True,
    margin=dict(t=100, b=150, l=100, r=100),
    title="Circular Periodic Table Redesign",
)
st.plotly_chart(fig, use_container_width=True)