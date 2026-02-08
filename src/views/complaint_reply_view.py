def render_reply_form(complaint):
    """
    complaint: tuple จาก get_description_by_id(complaint_id)
    คืนค่า: reply_text (str) | None (ถ้ายกเลิก)
    """
    print("\n" + "=" * 90)
    print("หน้าตอบกลับการร้องเรียน (เพิ่มการตอบกลับ)")
    print("=" * 90)

    cid = complaint[0] if len(complaint) > 0 else None
    stall = complaint[1] if len(complaint) > 1 else "-"
    desc = complaint[4] if len(complaint) > 4 else "-"

    print(f"รหัสร้องเรียน: {cid}")
    print(f"ร้าน: {stall}")
    print("-" * 90)
    print("รายละเอียดร้องเรียน:")
    print(desc)
    print("-" * 90)

    print("พิมพ์ข้อความตอบกลับ (เว้นว่างแล้วกด Enter = ยกเลิก)")
    text = input("ตอบกลับ: ").strip()
    if not text:
        return None
    return text
