import duckdb

conn = duckdb.connect("canteen_complaints.db")

def get_complaint_count_each_stall():
    result = conn.sql("""
        SELECT 
            s.id,
            s.name,
            c.name AS canteen_name,
            COUNT(cp.id) AS complaint_count
        FROM Stalls s
        JOIN Canteens c ON c.id = s.canteen_id
        LEFT JOIN Complaints cp ON cp.stall_id = s.id
        GROUP BY s.id, s.name, c.name
        ORDER BY complaint_count DESC, s.id
    """).fetchall()
    return result
