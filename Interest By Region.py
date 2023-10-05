"""
Marie Gregory 
10/5/2023
Project for ThetechProject,co portfolio
Resources: Google Trends
Python 3
Exploring AI Interest Trends (10/1/2022 - 10/1/2023) using Python
"""

import pandas as pd
import matplotlib.pyplot as plt
# Load the "Interest by Region" data
interest_by_region = pd.read_csv("C:\\Users\\reish\\OneDrive\\Projects\\InterestByRegion.csv")

# Assuming you have columns 'Country' and 'AI 2022-2023' in your dataset
region_column = 'Country'
interest_column = 'AI 2022-2023'

# Filter out rows with no value in the 'Interest' column
interest_by_region = interest_by_region.dropna(subset=[interest_column])

# Create a bar chart
plt.figure(figsize=(12, 6))
plt.bar(interest_by_region[region_column], interest_by_region[interest_column])
plt.title("AI Interest by Region")
plt.xlabel("Region")
plt.ylabel("Interest Score")
plt.xticks(rotation=90)
plt.tight_layout()

# Show the plot or save it as an image
plt.show()
