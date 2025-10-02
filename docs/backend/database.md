# Database Connection (`backend.database`)

Thin wrapper around LanceDB connection for local storage.

## Constants

- `DB_DIR: str`: Filesystem path to the LanceDB database directory, resolved relative to the `backend` package.

## Objects

- `db`: A connected LanceDB client returned by `lancedb.connect(DB_DIR)`.

## Usage Example

```python
from backend.database import db

# List table names
print(db.table_names())

# Create a table if it doesn't exist
import pyarrow as pa
schema = pa.schema([("id", pa.string())])
if "my_table" not in db.table_names():
    db.create_table("my_table", schema=schema, mode="overwrite")

# Open a table
my_table = db.open_table("my_table")

# Convert to pandas for quick inspection (if supported)
df = my_table.to_pandas()
print(df.head())
```
