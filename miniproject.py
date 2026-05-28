qty_laptop = 0 
qty_phone = 0
qty_tablet = 0

while True:
    print("\n--- HỆ THỐNG QUẢN LÝ KHO ---")
    print("1. Xem báo cáo tồn kho")
    print("2. Nhập kho")
    print("3. Xuất kho")
    print("4. Cảnh báo tồn kho thấp")
    print("5. Thoát chương trình")

    try:
        choice = int(input("Vui lòng nhập chức năng (1-5): "))
    except ValueError:
        print("Vui lòng chỉ nhập số nguyên từ 1 đến 5!")
        continue

    if choice == 1:
        print("\n--- BÁO CÁO TỒN KHO HIỆN TẠI ---")
        
        print(f"Laptop ({qty_laptop}): ", end="")
        for i in range(qty_laptop):
            print("*", end="")
        print() 
        
        print(f"Phone ({qty_phone}): ", end="")
        for i in range(qty_phone):
            print("*", end="")
        print()
        
        print(f"Tablet ({qty_tablet}): ", end="")
        for i in range(qty_tablet):
            print("*", end="")
        print()

    elif choice == 2:
        print("\n--- NHẬP KHO ---")
        print("1 - Laptop\n2 - Điện thoại\n3 - Máy tính bảng")
        try:
            type_goods = int(input("Chọn mặt hàng muốn nhập (1-3): "))
            
        except ValueError:
            print("Mã mặt hàng không hợp lệ. Hủy thao tác!")
            continue

        if type_goods == 1 or type_goods == 2 or type_goods == 3:
            while True:
                try:
                    import_amount = int(input("Nhập số lượng cần thêm: "))
                    if import_amount >= 0:
                        break
                    print("Số lượng không hợp lệ, vui lòng nhập lại!")

                except ValueError:
                    print("Vui lòng nhập một số nguyên lớn hơn hoặc bằng 0!")

            if type_goods == 1:
                qty_laptop += import_amount

            elif type_goods == 2:
                qty_phone += import_amount

            elif type_goods == 3:
                qty_tablet += import_amount

            print("Nhập kho thành công!")

        else:
            print("Mặt hàng chọn không hợp lệ. Hủy thao tác!")

    elif choice == 3:
        print("\n--- XUẤT KHO ---")
        print("1 - Laptop\n2 - Điện thoại\n3 - Máy tính bảng")
        try:
            type_goods = int(input("Chọn mặt hàng muốn xuất (1-3): "))

        except ValueError:
            print("Mã mặt hàng không hợp lệ. Hủy thao tác!")
            continue

        if type_goods == 1 or type_goods == 2 or type_goods == 3:
            while True:
                try:
                    export_amount = int(input("Nhập số lượng cần xuất: "))
                    if export_amount >= 0:
                        break
                    print("Số lượng không hợp lệ, vui lòng nhập lại!")

                except ValueError:
                    print("Vui lòng nhập một số nguyên lớn hơn hoặc bằng 0!")

            if type_goods == 1:
                if export_amount > qty_laptop:
                    print("Không đủ hàng!")

                else:
                    qty_laptop -= export_amount
                    print("Xuất thành công!")

            elif type_goods == 2:
                if export_amount > qty_phone:
                    print("Không đủ hàng!")

                else:
                    qty_phone -= export_amount
                    print("Xuất thành công!")

            elif type_goods == 3:
                if export_amount > qty_tablet:
                    print("Không đủ hàng!")

                else:
                    qty_tablet -= export_amount
                    print("Xuất thành công!")

        else:
            print("Mặt hàng chọn không hợp lệ. Hủy thao tác!")

    elif choice == 4:
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

    elif choice == 5:
        print("Đã thoát chương trình. Tạm biệt thủ kho!")
        break  

    else: 
        print("Lựa chọn sai! Vui lòng chọn từ 1-5.")