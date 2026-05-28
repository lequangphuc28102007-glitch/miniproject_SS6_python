qty_laptop = 0 
qty_phone = 0
qty_tablet = 0

while True:
    print("\n--- HỆ THỐNG QUẢN LÝ KHO (MATCH-CASE) ---")
    print("1. Xem báo cáo tồn kho")
    print("2. Nhập kho")
    print("3. Xuất kho")
    print("4. Cảnh báo tồn kho thấp")
    print("5. Thoát chương trình")

    choice = int(input("Vui lòng nhập chức năng (1-5): "))

    # Dùng match-case cho Menu chính
    match choice:
        case 1:
            print("\n--- BÁO CÁO TỒN KHO HIỆN TẠI ---")
            print(f"Laptop ({qty_laptop}): " + "*" * qty_laptop)
            print(f"Phone ({qty_phone}): " + "*" * qty_phone)
            print(f"Tablet ({qty_tablet}): " + "*" * qty_tablet)

        case 2:
            print("\n--- NHẬP KHO ---")
            print("1 - Laptop\n2 - Điện thoại\n3 - Máy tính bảng")
            type_goods = int(input("Chọn mặt hàng muốn nhập (1-3): "))

            # Kiểm tra mặt hàng bằng match-case, nếu đúng 1, 2, 3 mới cho nhập số lượng
            match type_goods:
                case 1 | 2 | 3:  # Dùng dấu | nghĩa là "hoặc" (1 hoặc 2 hoặc 3)
                    while True:
                        import_amount = int(input("Nhập số lượng cần thêm: "))
                        if import_amount >= 0:
                            break
                        print("Số lượng không hợp lệ, vui lòng nhập lại!")

                    # Cộng dồn vào từng mặt hàng
                    match type_goods:
                        case 1: qty_laptop += import_amount
                        case 2: qty_phone += import_amount
                        case 3: qty_tablet += import_amount
                    print("Nhập kho thành công!")
                case _:
                    print("Mặt hàng chọn không hợp lệ. Hủy thao tác!")

        case 3:
            print("\n--- XUẤT KHO ---")
            print("1 - Laptop\n2 - Điện thoại\n3 - Máy tính bảng")
            type_goods = int(input("Chọn mặt hàng muốn xuất (1-3): "))

            match type_goods:
                case 1 | 2 | 3:
                    while True:
                        export_amount = int(input("Nhập số lượng cần xuất: "))
                        if export_amount >= 0:
                            break
                        print("Số lượng không hợp lệ, vui lòng nhập lại!")

                    # Kiểm tra và trừ kho cho từng mặt hàng
                    match type_goods:
                        case 1:
                            if export_amount > qty_laptop: print("Không đủ hàng!")
                            else: qty_laptop -= export_amount; print("Xuất thành công!")
                        case 2:
                            if export_amount > qty_phone: print("Không đủ hàng!")
                            else: qty_phone -= export_amount; print("Xuất thành công!")
                        case 3:
                            if export_amount > qty_tablet: print("Không đủ hàng!")
                            else: qty_tablet -= export_amount; print("Xuất thành công!")
                case _:
                    print("Mặt hàng chọn không hợp lệ. Hủy thao tác!")

        case 4:
            print("\n--- CẢNH BÁO TỒN KHO THẤP (< 10) ---")
            report = False
            if qty_laptop < 10:
                print(f"[CẢNH BÁO] Laptop sắp hết (Còn {qty_laptop}).")
                report = True
            if qty_phone < 10:
                print(f"[CẢNH BÁO] Điện thoại sắp hết (Còn {qty_phone}).")
                report = True
            if qty_tablet < 10:
                print(f"[CẢNH BÁO] Máy tính bảng sắp hết (Còn {qty_tablet}).")
                report = True
            if not report:
                print("Tất cả an toàn!")

        case 5:
            print("Đã thoát chương trình. Tạm biệt thủ kho!")
            break  

        case _: 
            print("Lựa chọn sai! Vui lòng chọn từ 1-5.")