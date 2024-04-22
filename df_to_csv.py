# from ipynb.fs.full.Web_Scraper import output 
# import pandas as pd

# output.to_csv("web_scraped_data.csv")

import pandas as pd 
import sqlite3

df = pd.read_csv("cleaned_data.csv")

# Convert to .xlsx file

df.to_excel('cleaned_data.xlsx', index=False) 

# Convert to .json file

df.to_json('cleaned_data.json', orient='records')

# Convert to SQLite database

# Create a connection to a SQLite database
conn = sqlite3.connect('cleaned_data.db')

# Assuming df is your DataFrame, replace 'table_name' with the name you want for your table
df.to_sql('flights', conn, if_exists='replace', index=False)

# Close the connection
conn.close()
