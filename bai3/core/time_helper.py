"""
Module: time_helper.py
Package: utils
Chức năng: Tính thời gian hạ cánh dự kiến (ETA) dựa trên giờ cất cánh và số phút bay.
"""

from datetime import datetime, timedelta


def calculate_eta(flight_list: list) -> None:
    """
    Nhận mã chuyến bay từ bàn phím, tìm trong danh sách,
    rồi tính ETA bằng cách cộng timedelta(minutes=duration_min)
    vào thời gian cất cánh đã được parse bằng strptime().
    """
    print("\n----- TÍNH TOÁN THỜI GIAN HẠ CÁNH (ETA) -----")

    flight_id_input = input("Nhập mã chuyến bay cần tính: ").strip().upper()

    # Tìm chuyến bay trong danh sách
    target_flight = None
    for flight in flight_list:
        if flight["flight_id"].upper() == flight_id_input:
            target_flight = flight
            break

    if target_flight is None:
        print(f">> [LỖI] Không tìm thấy chuyến bay '{flight_id_input}' trong hệ thống.")
        return

    # Parse thời gian cất cánh
    depart_dt = datetime.strptime(target_flight["depart_time"], "%Y-%m-%d %H:%M:%S")

    # Tính ETA
    eta_dt = depart_dt + timedelta(minutes=target_flight["duration_min"])

    print(f"-> Chuyến bay {target_flight['flight_id']} cất cánh lúc: {depart_dt}")
    print(f"-> Thời gian hạ cánh dự kiến (ETA): {eta_dt}")
