import duckdb

from src.models import complaints_model

conn = duckdb.connect("canteen_complaints.db")

def add_response(complaint_id: int, response_text: str):
    exists = conn.sql("SELECT 1 FROM Complaints WHERE id = $1", params=[complaint_id]).fetchone()
    if not exists:
        return False
    
    conn.sql("""
        INSERT INTO Responses (complaint_id, response_text)
        VALUES ($1, $2)
    """, params=[complaint_id, response_text])

    complaints_model.set_status_done(complaint_id)

    return True

def get_responses_by_complaint_id(complaint_id: int):
    result = conn.sql("""
        SELECT id, response_text, response_date
        FROM Responses
        WHERE complaint_id = $1
        ORDER BY response_date DESC, id DESC
    """, params=[complaint_id]).fetchall()
    return result