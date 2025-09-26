from database import db
import pandas

# Open the tables
files_table = db.open_table("files")
users_table = db.open_table("users")

# Convert to pandas DataFrames
files_df = files_table.to_pandas()
users_df = users_table.to_pandas()

print("Files table:")
print(files_df)

print("\nUsers table:")
print(users_df)

# this is just the trial for lazy Git
