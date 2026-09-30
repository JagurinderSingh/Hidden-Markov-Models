# Import required libraries
import os
import pandas as pd
from dotenv import load_dotenv

#Load the variables from the .env file into Python's environment
load_dotenv()

#Access the variable using os.getenv()
folder_path = os.getenv("folder_path_env") # Folder path where your yearly CSV files are located

#Initializing an empty master dataframe
master_dataframe = pd.DataFrame()

def load_prepare_nifty_data(master_dataframe, folder_path):
  # Loop explicitly from 1 to 37 (range stops right before 38)
  for i in range(1, 38):
    # Construct the exact filename dynamically (1.csv, 2.csv, etc.)
    file_name = f"{i}.csv"
    file_path = os.path.join(folder_path, file_name)
    #Load into a baby dataframe
    baby_dataframe = pd.read_csv(file_path)
    # Appending it to master dataframe
    master_dataframe = pd.concat([master_dataframe, baby_dataframe], ignore_index=True)
    # Converting into python datetime object
    master_dataframe["Date"] = pd.to_datetime(master_dataframe["Date"])
    # Sort chronologically: oldest date at the top, newest at the bottom
    master_sorted_dataframe = master_dataframe.sort_values(by="Date", ascending=True).reset_index(drop=True)

  return master_sorted_dataframe

print(load_prepare_nifty_data(master_dataframe, folder_path))