"""
Module: logistics.py
Package: core
Chức năng: Hiển thị lịch trình và tính toán hậu cần (số thùng nước khoáng dự phòng).
"""

import math


def display_flight_schedule(flight_list: list) -> None:
    """
    Duyệt danh sách chuyến bay, tính số thùng nước khoáng dự phòng
    theo quy tắc: mỗi 10 hành khách cần 1 thùng, làm tròn lên bằng math.ceil().
    """
    print("\n----- DANH SÁCH CHUYẾN BAY & HẬU CẦN -----")

    if not flight_list:
        print("  (Chưa có chuyến bay nào trong hệ thống.)")
        return

    for index, flight in enumerate(flight_list, start=1):
        flight_id     = flight["flight_id"]
        depart_time   = flight["depart_time"]
        passengers    = flight["passengers"]
        water_crates  = math.ceil(passengers / 10)

        print(
            f"{index}. Mã: {flight_id} | "
            f"Khởi hành: {depart_time} | "
            f"Số khách: {passengers:<3} | "
            f"Dự phòng: {water_crates} thùng nước."
        )
