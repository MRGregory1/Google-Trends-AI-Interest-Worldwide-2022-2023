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

# Load the "Interest Over Time" data
interest_over_time = pd.read_csv("C:/Users/reish/OneDrive/Projects/InterestOverTime.csv")

# Assuming you have a 'Week' column and 'AI Worldwide' column
date_column = 'Week'
interest_column = 'AI Worldwide'

# Convert the 'Date' column to datetime format
interest_over_time[date_column] = pd.to_datetime(interest_over_time[date_column])

# Set the 'Date' column as the index
interest_over_time.set_index(date_column, inplace=True)

# Create a line chart
plt.figure(figsize=(12, 6))
plt.plot(interest_over_time.index, interest_over_time[interest_column], marker='o', linestyle='-', color='b')
plt.title("Worldwide AI Interest Over Time")
plt.xlabel("Date")
plt.ylabel("Interest Score")
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()

# Show the plot or save it as an image
plt.show()


