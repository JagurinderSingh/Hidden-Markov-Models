# Import required libraries
import os
import pandas as pd
from dotenv import load_dotenv

#Load the variables from the .env file into Python's environment
load_dotenv()

#Access the variable using os.getenv()
folder_path = os.getenv("folder_path_env") # Folder path where your yearly CSV files are located

def load_prepare_nifty_data(folder_path):

  #Initializing an empty master dataframe
  master_list = []

  # Loop explicitly from 1 to 37 (range stops right before 38)
  for i in range(1, 38):
    # Construct the exact filename dynamically (1.csv, 2.csv, etc.)
    file_name = f"{i}.csv"
    file_path = os.path.join(folder_path, file_name)
    #Load into a baby dataframe
    baby_dataframe = pd.read_csv(file_path)
    # Converting into python datetime object
    baby_dataframe["Date"] = pd.to_datetime(baby_dataframe["Date"])
    # Sort chronologically: oldest date at the top, newest at the bottom
    baby_sorted_dataframe = baby_dataframe.sort_values(by="Date", ascending=True).reset_index(drop=True)
    # Appending it to master list
    master_list.append(baby_sorted_dataframe)
    master_dataframe = pd.concat(master_list, ignore_index=True)
    
  return master_dataframe

print(load_prepare_nifty_data(folder_path)) #- Use this line to see the output of this file