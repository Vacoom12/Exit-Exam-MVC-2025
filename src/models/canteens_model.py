import duckdb

con = duckdb.connect("canteen_complaints.db")

def get_all_canteens():
    return con.sql("""
        SELECT id, name, location
        FROM Canteens
        ORDER BY id
    """).fetchall()