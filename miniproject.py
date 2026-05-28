
qty_laptop = 0
qty_phone = 0
qty_tablet = 0

while True:
    print("\n========== HỆ THỐNG QUẢN LÝ KHO ==========")
    print("1. Xem báo cáo tồn kho")
    print("2. Nhập kho")
    print("3. Xuất kho")
    print("4. Cảnh báo tồn kho thấp")
    print("5. Thoát chương trình")

    choice = input("Vui lòng nhập chức năng (1-5): ")

    if choice == "1":
        print("\n===== BÁO CÁO TỒN KHO =====")

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

        input("\nNhấn Enter để tiếp tục...")

    elif choice == "2":
        print("\n===== NHẬP KHO =====")
        print("1 - Laptop")
        print("2 - Phone")
        print("3 - Tablet")

        type_goods = input("Chọn mặt hàng muốn nhập (1-3): ")

        if type_goods in ["1", "2", "3"]:

            while True:
                try:
                    import_amount = int(input("Nhập số lượng cần thêm: "))

                    if import_amount > 0:
                        break
                    else:
                        print("Số lượng phải lớn hơn 0!")

                except ValueError:
                    print("Vui lòng nhập số nguyên!")

            if type_goods == "1":
                qty_laptop += import_amount

            elif type_goods == "2":
                qty_phone += import_amount

            elif type_goods == "3":
                qty_tablet += import_amount

            print("Nhập kho thành công!")

        else:
            print("Mặt hàng không hợp lệ!")

        input("\nNhấn Enter để tiếp tục...")

    elif choice == "3":
        print("\n===== XUẤT KHO =====")
        print("1 - Laptop")
        print("2 - Phone")
        print("3 - Tablet")

        type_goods = input("Chọn mặt hàng muốn xuất (1-3): ")

        if type_goods in ["1", "2", "3"]:

            while True:
                try:
                    export_amount = int(input("Nhập số lượng cần xuất: "))

                    if export_amount > 0:
                        break
                    else:
                        print("Số lượng phải lớn hơn 0!")

                except ValueError:
                    print("Vui lòng nhập số nguyên!")

            if type_goods == "1":

                if export_amount > qty_laptop:
                    print("Không đủ hàng!")

                else:
                    qty_laptop -= export_amount
                    print("Xuất kho thành công!")

            elif type_goods == "2":

                if export_amount > qty_phone:
                    print("Không đủ hàng!")

                else:
                    qty_phone -= export_amount
                    print("Xuất kho thành công!")

            elif type_goods == "3":

                if export_amount > qty_tablet:
                    print("Không đủ hàng!")

                else:
                    qty_tablet -= export_amount
                    print("Xuất kho thành công!")

        else:
            print("Mặt hàng không hợp lệ!")

        input("\nNhấn Enter để tiếp tục...")

    elif choice == "4":
        print("\n===== CẢNH BÁO TỒN KHO THẤP =====")

        warning = False

        if qty_laptop < 10:
            print(f"Laptop sắp hết! Còn {qty_laptop}")
            warning = True

        if qty_phone < 10:
            print(f"Phone sắp hết! Còn {qty_phone}")
            warning = True

        if qty_tablet < 10:
            print(f"Tablet sắp hết! Còn {qty_tablet}")
            warning = True

        if warning == False:
            print("Tất cả mặt hàng đều an toàn!")

        input("\nNhấn Enter để tiếp tục...")

    elif choice == "5":
        print("Đã thoát chương trình!")
        break

    
    else:
        print("Lựa chọn không hợp lệ!")
