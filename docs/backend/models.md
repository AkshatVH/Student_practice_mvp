# Data Models (`backend.models`)

Schemas and table initialization for LanceDB tables used by SmartStudy.

## Schemas

### `user_schema`
PyArrow schema for users.

Fields:
- `id`: `pa.string()` — unique identifier for the user
- `name`: `pa.string()` — display name

### `file_schema`
PyArrow schema for uploaded files.

Fields:
- `id`: `pa.string()` — unique identifier for file
- `user_id`: `pa.int64()` — user owning the file
- `type`: `pa.string()` — file type (e.g., `textbook`, `question_paper`)
- `filename`: `pa.string()` — original filename
- `path`: `pa.string()` — original storage path
- `processed_path`: `pa.string()` — path to processed text file output

## Tables

The module ensures the following tables exist on import:
- `users`
- `files`

If a table is missing, it is created with `mode="overwrite"` using the above schemas.

## Handles

- `users`: `db.open_table("users")`
- `files`: `db.open_table("files")`

## Usage Example

```python
from backend.models import users, files, user_schema, file_schema

# append or query as supported by LanceDB
print("Tables:", users.name, files.name)

# Example: ensure a new column via schema migration (pseudo)
# Note: consult LanceDB docs for altering schemas safely.
```
