# phypox_analyzer.py
# Phypox G-Force Analyzer
# Author: Proluca1840
# Description: Analyze accelerometer data exported from the Phypox app.
# Supports .xls and .xlsx files. Calculates total G-force and plots a graph.

import pandas as pd
import matplotlib.pyplot as plt
import os

# Ask the user for the filename (without extension)
file_name = input("Enter the file name (without extension .xls or .xlsx): ")

# Add extension automatically (.xls first, fallback to .xlsx)
file_path_xls = f"{file_name}.xls"
file_path_xlsx = f"{file_name}.xlsx"

if os.path.exists(file_path_xls):
    file_path = file_path_xls
elif os.path.exists(file_path_xlsx):
    file_path = file_path_xlsx
else:
    print(f"❌ Error: The file '{file_name}.xls' or '{file_name}.xlsx' does not exist in the current folder.")
    exit()

# Load the Excel file
df = pd.read_excel(file_path)

# Calculate total G-force
df["G_tot"] = (
    (df["Acceleration x (m/s^2)"]**2 +
     df["Acceleration y (m/s^2)"]**2 +
     df["Acceleration z (m/s^2)"]**2) ** 0.5
) / 9.81

# Show maximum G-force value
print(f"✅ Maximum G peak in '{file_name}':", round(df["G_tot"].max(), 2))

# Plot G vs Time
plt.plot(df["Time (s)"], df["G_tot"])
plt.title(f"Total Acceleration (G) - {file_name}")
plt.xlabel("Time (s)")
plt.ylabel("G-Force")
plt.grid(True)

# Save plot as PNG with filename
png_name = f"graph_{file_name}.png"
plt.savefig(png_name)
plt.show()

print(f"📊 Graph saved as '{png_name}'")

# Notes:
# - You can adapt this script for any dataset exported from Phypox by changing column names.
# - Open-source project: feel free to modify or improve, but please credit the original author.
