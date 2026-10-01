from data_cleaner import load_prepare_nifty_data

# Import required libraries
import os
import pandas as pd
from dotenv import load_dotenv

#Load the variables from the .env file into Python's environment
load_dotenv()

#Access the variable using os.getenv()
folder_path = os.getenv("folder_path_env")
output_file_path = os.getenv("output_file_path_env") # Folder path where your yearly CSV files are located

#Master dataframe initialized to be used
master_dataframe = pd.DataFrame()

# Calling the function
output_df = load_prepare_nifty_data(folder_path)

# Save master dataframe to csv
output_df.to_csv(output_file_path, index=False)

print("Success!")


