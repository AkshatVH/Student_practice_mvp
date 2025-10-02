# Trial Script (`backend.trial`)

Utility script demonstrating how to open LanceDB tables and inspect them as pandas DataFrames.

## Behavior
- Opens `files` and `users` tables from the default `db` connection.
- Converts both to pandas DataFrames and prints them to stdout.

## Example Usage

```bash
python -m backend.trial
```

Ensure your environment has `pandas` installed and the LanceDB tables exist.
