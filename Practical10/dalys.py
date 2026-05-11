import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# os.chdir("C:/Users/desktop/IBI1_2025-26/Practical10")

# 1. Set working directory
# This makes Python use the folder where this script is saved
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

print("Current working directory:")
print(os.getcwd())

print("\nFiles in this folder:")
print(os.listdir())

# 2. Import dataset
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")

print("\nFirst 5 rows of the dataset:")
print(dalys_data.head(5))

print("\nInformation about the dataframe:")
print(dalys_data.info())

print("\nSummary statistics:")
print(dalys_data.describe())

# 3. Basic questions using describe()
print("\nMaximum DALYs across all rows:")
print(dalys_data["DALYs"].max())

print("\nMinimum DALYs across all rows:")
print(dalys_data["DALYs"].min())

print("\nFirst year when DALYs were recorded:")
print(dalys_data["Year"].min())

print("\nMost recent year when DALYs were recorded:")
print(dalys_data["Year"].max())


# 4. Practice with iloc
print("\nValue in first row, fourth column:")
print(dalys_data.iloc[0, 3])

print("\nRows 2 to 9, columns 0 to 4:")
print(dalys_data.iloc[2:10, 0:5])

print("\nEvery second row from first 10 rows, columns 0 to 4:")
print(dalys_data.iloc[0:10:2, 0:5])

print("\nThird and fourth columns for the first 10 rows:")
print(dalys_data.iloc[0:10, 2:4])

first_10_rows = dalys_data.iloc[0:10]
max_first_10_row = first_10_rows.loc[first_10_rows["DALYs"].idxmax()]

print("\nMaximum DALYs in the first 10 rows:")
print(max_first_10_row["DALYs"])

print("\nYear with the maximum DALYs in the first 10 rows:")
print(max_first_10_row["Year"])
# In the first 10 years recorded for Afghanistan, the maximum DALYs value was recorded in 1998.

# 5. Practice with Boolean columns
print("\nFirst 3 rows, selected columns using column numbers:")
print(dalys_data.iloc[0:3, [0, 1, 3]])

my_columns = [True, True, False, True]

print("\nFirst 3 rows, selected columns using Booleans:")
print(dalys_data.iloc[0:3, my_columns])

# 6. Practice with loc
print("\nRows 2 to 4, Year column:")
print(dalys_data.loc[2:4, "Year"])

print("\nAll years for Zimbabwe:")
zimbabwe_years = dalys_data.loc[dalys_data["Entity"] == "Zimbabwe", "Year"]
print(zimbabwe_years)

zimbabwe_first_year = zimbabwe_years.min()
zimbabwe_last_year = zimbabwe_years.max()

print("\nFirst year recorded for Zimbabwe:")
print(zimbabwe_first_year)

print("\nLast year recorded for Zimbabwe:")
print(zimbabwe_last_year)
# DALYs were recorded for Zimbabwe from 1990 to 2019.

print("\nAll rows for Zimbabwe:")
zimbabwe_data = dalys_data.loc[dalys_data["Entity"] == "Zimbabwe"]
print(zimbabwe_data)

# 7. Examining the situation across countries in 2019
recent_data = dalys_data.loc[
    dalys_data["Year"] == 2019,
    ["Entity", "DALYs"]
]

recent_data = recent_data.dropna()

print("\nRecent data from 2019:")
print(recent_data.head())

max_row = recent_data.loc[recent_data["DALYs"].idxmax()]
min_row = recent_data.loc[recent_data["DALYs"].idxmin()]
# In 2019, the country or region with the largest DALYs was Lesotho.
# In 2019, the country or region with the smallest DALYs was Singapore.

print("\nCountry or region with the largest DALYs in 2019:")
print(max_row["Entity"], max_row["DALYs"])

print("\nCountry or region with the smallest DALYs in 2019:")
print(min_row["Entity"], min_row["DALYs"])

# 8. Plot DALYs over time for one of the countries identified above
# I chose Lesotho because it had the largest DALYs value in 2019.
lesotho = dalys_data.loc[dalys_data["Entity"] == "Lesotho"]

plt.figure(figsize=(8, 5), dpi=150)
plt.plot(lesotho["Year"], lesotho["DALYs"], "b+")
plt.xticks(lesotho["Year"], rotation=90)
plt.xlabel("Year")
plt.ylabel("DALYs")
plt.title("DALYs in Lesotho over time")
plt.tight_layout()
plt.savefig("lesotho_dalys_over_time.png", format="png")
plt.show()


# 9. One other question
# Question:
# What was the distribution of DALYs across all countries or regions in 2019?
plt.figure(figsize=(8, 5), dpi=150)
plt.hist(recent_data["DALYs"], bins=20)
plt.xlabel("DALYs")
plt.ylabel("Number of countries or regions")
plt.title("Distribution of DALYs across countries or regions in 2019")
plt.tight_layout()
plt.savefig("dalys_distribution_2019.png", format="png")
plt.show()

mean_dalys_2019 = recent_data["DALYs"].mean()
median_dalys_2019 = recent_data["DALYs"].median()
max_dalys_2019 = recent_data["DALYs"].max()
min_dalys_2019 = recent_data["DALYs"].min()

question_file = open("question.txt", "w")

question_file.write("Question:\n")
question_file.write("What was the distribution of DALYs across all countries or regions in 2019?\n\n")

question_file.write("Line number where the code starts:\n")
question_file.write("The code answering this question starts at line 136 of dalys.py. The histogram starts at line 139.\n\n")

question_file.write("Results:\n")
question_file.write("Mean DALYs in 2019: " + str(mean_dalys_2019) + "\n")
question_file.write("Median DALYs in 2019: " + str(median_dalys_2019) + "\n")
question_file.write("Maximum DALYs in 2019: " + str(max_dalys_2019) + "\n")
question_file.write("Minimum DALYs in 2019: " + str(min_dalys_2019) + "\n\n")

question_file.write("Discussion:\n")
question_file.write("The histogram shows that the DALYs values are not evenly distributed across countries or regions. ")
question_file.write("Some countries or regions have much higher DALYs than others. ")
question_file.write("This suggests that the burden of disease differs substantially between places in 2019.\n")

question_file.close()

print("\nFinished analysis.")
print("Saved plots:")
print("lesotho_dalys_over_time.png")
print("dalys_distribution_2019.png")
print("Saved written answer:")
print("question.txt")