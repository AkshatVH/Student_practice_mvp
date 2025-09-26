import pyarrow as pa
from database import db

# Define schemas
user_schema = pa.schema([("id", pa.string()), ("name", pa.string())])

file_schema = pa.schema(
    [
        ("id", pa.string()),
        ("user_id", pa.int64()),
        ("type", pa.string()),
        ("filename", pa.string()),
        ("path", pa.string()),
        ("processed_path", pa.string()),  # text file output
    ]
)

# Initialize tables if not exist
if "users" not in db.table_names():
    db.create_table("users", schema=user_schema, mode="overwrite")

if "files" not in db.table_names():
    db.create_table("files", schema=file_schema, mode="overwrite")

users = db.open_table("users")
files = db.open_table("files")
