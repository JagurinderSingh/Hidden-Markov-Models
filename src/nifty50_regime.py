import glob
import os
import pandas as pd

# 1. Define the folder path where your yearly CSV files are located
folder_path = r"C:\Users\Riddhima Singh\Desktop\Hidden-Markov-Models\Nifty 50 Historical Data"  # Replace with your actual folder path

#Initializing an empty master dataframe
master_dataframe = pd.DataFrame()

# Loop explicitly from 1 to 37 (range stops right before 38)
for i in range(1, 38):
  # Construct the exact filename dynamically (1.csv, 2.csv, etc.)
  file_name = f"{i}.csv"
  file_path = os.path.join(folder_path, file_name)
  #Load into a baby dataframe
  baby_dataframe = pd.read_csv(file_path)
  # Appending it to master dataframe
  master_dataframe = pd.concat([master_dataframe, baby_dataframe], ignore_index=True)

# Sorting chronoligically based on the date
master_dataframe["Date"] = pd.to_datetime(master_dataframe["Date"])

# 2. Sort chronologically: oldest date at the top, newest at the bottom
master_sorted_dataframe = master_dataframe.sort_values(by="Date", ascending=True).reset_index(drop=True)

print(master_sorted_dataframe)

# # 2. Use glob to match all CSV files in that directory
# all_files = glob.glob(os.path.join(folder_path, "*.csv"))

# print(all_files)

# # Sort the file path list so they merge in proper chronological order
# all_files.sort()

# # 3. Read each CSV file into a temporary list
# df_list = []
# for file in all_files:
#   df_temp = pd.read_csv(file)
#   df_list.append(df_temp)

# # 4. Concatenate all dataframes together into one master dataset
# master_df = pd.concat(df_list, ignore_index=True)

# # 5. Clean, sort by date chronologically, and drop duplicate rows
# master_df["Date"] = pd.to_datetime(master_df["Date"])
# master_df = (
#     master_df.sort_values("Date").drop_duplicates().reset_index(drop=True)
# )

# print(f"Successfully combined {len(all_files)} files!")
# print(f"Total rows in master DataFrame: {len(master_df)}")
# print(master_df.head())