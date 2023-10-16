pip install Pydrive
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import pandas as pd

# Authenticate account and create and authorize a local webserver for OAuth2.0
gauth = GoogleAuth()
gauth.LocalWebserverAuth()

# Create a GoogleDrive instance with authenticated GoogleAuth instance
drive = GoogleDrive(gauth)

# Shared link to stages_TourDeFrance.csv
# https://drive.google.com/file/d/10ztDH5gUoFNciJFeFg4UZsfIUvE8tBwB/view?usp=sharing

# Hardcoding the ID from the shareable file
id_stages = '10ztDH5gUoFNciJFeFg4UZsfIUvE8tBwB'

stages_drive = drive.CreateFile({'id': id_stages})
stages_localname_csv = "stages_TourDeFrance.csv"
stages_drive.GetContentFile(stages_localname_csv)

# Read the CSV data into a DataFrame
tdfstages = pd.read_csv("stages_TourDeFrance.csv")

print(f"Importing CSV data from {stages_localname_csv}.\n")

# Setting max_rows to be None so that we see all Series data in the output.
pd.options.display.max_rows = None

# Extract the year from the 'Date' column and add it as a new 'Year' column
tdfstages['Year'] = tdfstages['Date'].apply(lambda date: date.split('/')[2])

# Display the last rows of the DataFrame
print(tdfstages.tail())

# Filter the DataFrame to show only rows where Mark Cavendish is the winner
mc_df = tdfstages[tdfstages['Winner'] == "Mark Cavendish"]
print(mc_df)

# Find and display the row with the longest stage
longest_stage_row = tdfstages[tdfstages['Distance'] == tdfstages['Distance'].max()]
print(f"The longest stage ever in the Tour de France was:\n{longest_stage_row}\n")

# Calculate the average distance of stages in the Tour de France
average_distance = tdfstages['Distance'].mean()
print(f"The average distance of stages in the Tour de France is {average_distance} km.")

unique_winners = tdfstages['Winner'].nunique()
print(f"\nThe total number of unique stage winners is {unique_winners}.\n")

# Calculate the number of stages per year
stages_per_year = tdfstages['Year'].value_counts().sort_index()
print(f"Number of stages per year:\n{stages_per_year}\n")