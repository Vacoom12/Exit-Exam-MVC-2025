def render_home_menu():
    print("\n" + "=" * 90)
    print("ระบบติดตามการร้องเรียนคุณภาพอาหารในโรงอาหาร")
    print("=" * 90)
    print("1) ดูการร้องเรียนทั้งหมด")
    print("2) ดูร้านอาหาร (จำนวนการร้องเรียนต่อร้าน)")
    print("0) ออก")

    while True:
        choice = input("เลือกเมนู: ").strip()
        if choice in ("0", "1", "2"):
            return choice
        print("กรุณาเลือก 0, 1 หรือ 2")
