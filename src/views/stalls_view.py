# src/views/stalls_view.py

def render_stalls_page(rows):
    """
    rows: list of tuples จาก get_complaint_count_each_stall()
    คาดว่า: (stall_id, stall_name, complaint_count) หรือ (stall_name, complaint_count)
    คืนค่า: ("back", None)
    """
    print("\n" + "=" * 90)
    print("หน้าร้านอาหาร (จำนวนการร้องเรียนต่อร้าน)")
    print("=" * 90)

    if not rows:
        print("ไม่พบข้อมูลร้านอาหาร")
        input("กด Enter เพื่อกลับ...")
        return ("back", None)

    print(f"{'ร้านอาหาร':<30} {'จำนวนร้องเรียน':>12}")
    print("-" * 90)

    for r in rows:
        name = str(r[1])
        cnt = str(r[3])
        print(f"{name:<30} {cnt:^12}")

    input("\nกด Enter เพื่อกลับ...")
    return ("back", None)
