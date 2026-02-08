import duckdb

conn = duckdb.connect("canteen_complaints.db")

STATUS_PENDING = "รอตรวจสอบ"
STATUS_DONE = "ดำเนินการแล้ว"

def get_all_complaints():
    result = conn.sql(""" 
        SELECT 
            cp.id, 
            cp.complaint_date,
            s.name, 
            c.name, 
            cc.name, 
            cp.status,
            cp.description
        FROM Complaints cp
        JOIN Stalls s ON cp.stall_id = s.id
        JOIN Canteens c ON s.canteen_id = c.id
        JOIN ComplaintCategories cc ON cp.category_id = cc.id
        ORDER BY cp.complaint_date DESC
        """).fetchall()
    return result

def get_description_by_id(complaint_id: int):
    result = conn.sql("""
        SELECT 
            cp.id,
            s.name,
            cp.complaint_date,
            cc.name,
            cp.description,
            cp.status,
            s.id,
            c.name,
            c.location
        FROM Complaints cp
        JOIN Stalls s ON s.id = cp.stall_id
        JOIN Canteens c ON c.id = s.canteen_id
        JOIN ComplaintCategories cc ON cc.id = cp.category_id
        WHERE cp.id = $1
    """, params=[complaint_id]).fetchone()
    return result

def set_status_done(complaint_id: int):
    conn.sql("""
        UPDATE Complaints
        SET status = $1
        WHERE id = $2
    """, params=[STATUS_DONE, complaint_id])
    return True