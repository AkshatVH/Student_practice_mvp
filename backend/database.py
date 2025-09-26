import lancedb
import os

DB_DIR = os.path.join(os.path.dirname(__file__), "student_practice.lancedb")
db = lancedb.connect(DB_DIR)
