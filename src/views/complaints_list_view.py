def render_complaints_list(rows):
    print("\n" + "=" * 90)
    print("หน้ารวมการร้องเรียนทั้งหมด (เรียงตามวันที่ร้องเรียน)")
    print("=" * 90)

    if not rows:
        print("ยังไม่มีการร้องเรียน")
        input("กด Enter เพื่อกลับ...")
        return ("back", None)

    print(f"{'ID':<5} {'วันที่':<12} {'ร้าน':<20} {'โรงอาหาร':<15} {'ประเภท':<12} {'สถานะ':<15}")
    print("-" * 90)

    for r in rows:
        cid = r[0] if len(r) > 0 else "-"
        cdate = str(r[1]) if len(r) > 1 else "-"
        stall = str(r[2]) if len(r) > 2 else "-"
        canteen = str(r[3]) if len(r) > 3 else "-"
        cate = str(r[4]) if len(r) > 4 else "-"
        status = str(r[5]) if len(r) > 5 else "-"
        print(f"{cid:<5} {cdate:<12} {stall:<20.20} {canteen:<15.15} {cate:<12.12} {status:<15.15}")

    print("\nพิมพ์ ID เพื่อดูรายละเอียด")
    print("พิมพ์ 0 เพื่อกลับหน้าหลัก")

    while True:
        s = input("เลือก: ").strip()
        if s == "0":
            return ("back", None)
        if s.isdigit():
            return ("detail", int(s))
        print("กรุณากรอกเป็นเลข ID หรือ 0")
