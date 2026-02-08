import duckdb 

conn = duckdb.connect("canteen_complaints.db")

conn.execute("""
    CREATE SEQUENCE IF NOT EXISTS category_id_seq START 1;
    CREATE TABLE IF NOT EXISTS ComplaintCategories (
        id INTEGER PRIMARY KEY DEFAULT nextval('category_id_seq'),
        name VARCHAR NOT NULL UNIQUE
    );
             
    CREATE SEQUENCE IF NOT EXISTS canteen_id_seq START 1;
    CREATE TABLE IF NOT EXISTS Canteens (
        id INTEGER PRIMARY KEY DEFAULT nextval('canteen_id_seq'),
        name VARCHAR NOT NULL,
        location VARCHAR NOT NULL
    );
             
    CREATE SEQUENCE IF NOT EXISTS stall_id_seq START 1;
    CREATE TABLE IF NOT EXISTS Stalls (
        id INTEGER PRIMARY KEY DEFAULT nextval('stall_id_seq'),
        name VARCHAR NOT NULL,
        canteen_id INTEGER NOT NULL,
        FOREIGN KEY (canteen_id) REFERENCES Canteens(id)
    );
    
    CREATE SEQUENCE IF NOT EXISTS complaint_id_seq START 1;
    CREATE TABLE IF NOT EXISTS Complaints (
        id INTEGER PRIMARY KEY DEFAULT nextval('complaint_id_seq'),
        stall_id INTEGER NOT NULL,
        complaint_date DATE NOT NULL DEFAULT CURRENT_DATE,
        category_id INTEGER NOT NULL,
        description TEXT NOT NULL,
        status VARCHAR NOT NULL,
        FOREIGN KEY (stall_id) REFERENCES Stalls(id),
        FOREIGN KEY (category_id) REFERENCES ComplaintCategories(id)
    );
             
    CREATE SEQUENCE IF NOT EXISTS response_id_seq START 1;
    CREATE TABLE IF NOT EXISTS Responses (
        id INTEGER PRIMARY KEY DEFAULT nextval('response_id_seq'),
        complaint_id INTEGER NOT NULL,
        response_text TEXT NOT NULL,
        response_date DATE NOT NULL DEFAULT CURRENT_DATE,
        FOREIGN KEY (complaint_id) REFERENCES Complaints(id)
    );
             
""")

conn.execute("""
    INSERT INTO ComplaintCategories (name) VALUES
        ('ความสะอาด'),
        ('รสชาติ'),
        ('การบริการ'),
        ('ราคา'),
        ('คุณภาพอาหาร'),
        ('เวลารอ')
    ON CONFLICT DO NOTHING;;
             
    INSERT INTO Canteens (name, location) VALUES
        ('Canteen A', 'Engineering Building'),
        ('Canteen B', 'Science Building'),
        ('Canteen C', 'Arts Building');
             
    INSERT INTO Stalls (name, canteen_id) VALUES
        ('กะเพราเดือดจัง', 1),
        ('ร้านชาไข่มุก', 1),
        ('ร้านข้าวแกง', 1),
        ('ข้าวมันไก่ฉ่ำ', 2),
        ('ขนมหวาน', 2),
        ('ส้มตำสายแซ่บ', 2),
        ('ราเมง ข้าวญี่ปุ่น', 2),
        ('Mixue', 3),
        ('เบเกอรี่หน้าใส', 3),
        ('ร้านสเต็ก', 3);
    
    INSERT INTO Complaints (stall_id, complaint_date, category_id, description, status) VALUES
        (1, '2024-10-01', 1, 'โต๊ะสกปรกมาก ไม่มีการทำความสะอาด', 'รอตรวจสอบ'),
        (2, '2024-10-02', 2, 'ชาไข่มุกหวานเกินไป', 'รอตรวจสอบ'),
        (4, '2024-10-03', 3, 'พนักงานบริการไม่สุภาพ', 'รอตรวจสอบ'),
        (5, '2024-10-04', 4, 'ราคาแพงเกินไปเมื่อเทียบกับปริมาณ', 'รอตรวจสอบ'),
        (7, '2024-10-05', 5, 'คุณภาพอาหารไม่ดี เนื้อหมูแข็งมาก', 'รอตรวจสอบ'),
        (8, '2024-10-06', 6, 'รออาหารนานเกินไป', 'ดำเนินการแล้ว'),
        (3, '2024-10-07', 1, 'พื้นเปื้อนน้ำมัน เดินลำบาก', 'รอตรวจสอบ'),
        (6, '2024-10-08', 2, 'รสชาติไม่เหมือนเดิม', 'ดำเนินการแล้ว'),
        (9, '2024-10-09', 3, 'พนักงานไม่ยิ้มแย้มแจ่มใส', 'รอตรวจสอบ'),
        (1, '2024-10-10', 4, 'ราคาไม่สมเหตุสมผล', 'รอตรวจสอบ'),
        (2, '2024-10-11', 5, 'อาหารไม่สดใหม่', 'รอตรวจสอบ');
             
    INSERT INTO Responses (complaint_id, response_text) VALUES
        (6, 'sry na krub we will imporve naja'),
        (6, 'ok jaaaa'),
        (8, 'i check it for ya');
""")