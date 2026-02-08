def render_complaint_detail(complaint, responses):
    print("\n" + "=" * 90)
    print("หน้ารายละเอียดการร้องเรียน")
    print("=" * 90)

    cid = complaint[0] if len(complaint) > 0 else None
    stall = complaint[1] if len(complaint) > 1 else "-"
    cdate = str(complaint[2]) if len(complaint) > 2 else "-"
    cate = complaint[3] if len(complaint) > 3 else "-"
    desc = complaint[4] if len(complaint) > 4 else "-"
    status = complaint[5] if len(complaint) > 5 else "-"

    print(f"รหัสร้องเรียน: {cid}")
    print(f"ร้าน: {stall}")
    print(f"วันที่ร้องเรียน: {cdate}")
    print(f"ประเภทปัญหา: {cate}")
    print(f"สถานะปัจจุบัน: {status}")
    print("-" * 90)
    print("รายละเอียด:")
    print(desc)
    print("-" * 90)

    print("การตอบกลับ:")
    if not responses:
        print("- ยังไม่มีการตอบกลับ")
    else:
        # คาดว่า response tuple อาจเป็น: (id, complaint_id, response_text, response_date) หรือ (id, response_date, response_text)
        for i, r in enumerate(responses, start=1):
            # เดาแบบยืดหยุ่น
            if len(r) >= 4:
                r_date = str(r[3])
                r_text = str(r[2])
            elif len(r) == 3:
                r_date = str(r[2])
                r_text = str(r[1])
            elif len(r) == 2:
                r_date = "-"
                r_text = str(r[1])
            else:
                r_date = "-"
                r_text = str(r[0]) if r else "-"
            print(f"{i}. [{r_date}] {r_text}")

    print("\nเมนู:")
    print("1) เพิ่มการตอบกลับ (ผู้ดูแลระบบ)")
    print("0) กลับ")

    while True:
        s = input("เลือก: ").strip()
        if s == "0":
            return ("back", None)
        if s == "1":
            return ("reply", cid)
        print("กรุณาเลือก 1 หรือ 0")
