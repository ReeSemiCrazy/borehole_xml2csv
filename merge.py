import pandas as pd  
# You can install it via pip by running: 'pip install pandas' in your terminal. 
# This is necessary for data manipulation tasks
import glob        
# To list all csv files 
def merge_csv():   
# Define a function to handle the file merging. This could be named differently 
# as per your project conventions and requirements, e.g., merge_files
  csv_extension = '*.csv'  
  # Define the extension of CSV files we are interested in (in our case, all *.csv)
  csv_files = glob.glob(csv_extension)  
  # Get a list of CSV files in the current directory by matching our pattern 
  #(i.e., all *.cs*)
  df_from_each_file = [pd.read_csv(f) for f in csv_files]  
  # Read all CSV files and store the dataframes
  concat_dataframe = pd.concat(df_from_each_file, ignore_index=True)  
  # Concatenate all the dataframes into one
  concat_dataframe.to_csv('merged-file.csv', index=False)  
  # Save this merged DataFrame to a single CSV file 
  # (you can replace 'merged_files' with any filename you prefer, but it must end in .csv)
merge_csv()  
# Call the function to start merging CSV files. 
# This will create a merged file called 'merged-file' in your current directory