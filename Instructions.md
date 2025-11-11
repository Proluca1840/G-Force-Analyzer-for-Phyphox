# 📘 Instructions for Phypox G-Force Analyzer

This guide explains how to install dependencies, use the script, and adapt it to your own Phypox data files.

---

## ⚙️ Requirements

Before running the script, make sure you have **Python 3.8+** installed.  
You will also need the following Python libraries:

```bash
pip install pandas matplotlib openpyxl xlrd
```
## 📂 Preparing your data

Open the **Phypox** app on your phone.

Go to the experiment where you recorded accelerations.

Export your data as an **Excel file** (.xls or .xlsx).

Copy that file **into the same folder as the script**.

## ▶️ Running the script

Launch the script with:
```bash
python phypox_analyzer.py
```
When prompted, enter the file name without extension, for example:
```pgsql
Enter the file name (without extension .xls or .xlsx): Example
```
The program will:

-Read the Excel file

-Calculate the total acceleration using the formula:
```python
G_tot = sqrt(ax**2 + ay**2 + az**2) / 9.81
```
-Print **the maximum G value** found

-Plot a graph of G vs. time

-Save the plot as graph_Example.png

## 🧠 Adapting the script

If your file uses different column names (for example, "accX" instead of "Acceleration x (m/s^2)"), edit this section in the script:
```python
df["G_tot"] = (
    (df["Acceleration x (m/s^2)"]**2 +
     df["Acceleration y (m/s^2)"]**2 +
     df["Acceleration z (m/s^2)"]**2) ** 0.5
) / 9.81
```
Just replace the column names with the ones in your dataset.

## 💾 Output

Console output example:
```bash
✅ Maximum G peak in 'Example': 2.37
```
Image saved automatically as:
```bash
graph_Example.png
```
## 🧑‍🔬 Notes

You can use this script to analyze any motion data collected with Phypox (not only G-force).

The code is **open source** and can be freely modified or improved.

**If you reuse or modify this project, please give proper credit to the original author.**

Contributions, forks, and pull requests are welcome!

## 🪪 Credits and License

This script was created by **Proluca1840** as a small open-source project to analyze accelerometer data exported from **Phypox**.
You are free to **use, modify, and share** this code for educational or research purposes, **as long as proper credit is given to the original author.**
If you publish a modified version, please **mention the original project name and author** somewhere in your documentation or code comments.

