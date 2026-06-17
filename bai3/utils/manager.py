"""
Module: manager.py
Package: core
Chức năng: Tiếp nhận và quản lý chuyến bay mới.
"""

from datetime import datetime


# ---------------------------------------------------------------------------
# Helper Function
# ---------------------------------------------------------------------------

def check_duplicate_id(flight_id: str, flight_list: list) -> bool:
    """
    Kiểm tra xem mã chuyến bay có bị trùng với danh sách hiện tại không.
    Áp dụng .strip().upper() để chuẩn hoá trước khi so sánh.

    Trả về True nếu trùng, False nếu chưa có.
    """
    normalized_id = flight_id.strip().upper()
    for flight in flight_list:
        if flight["flight_id"].upper() == normalized_id:
            return True
    return False


# ---------------------------------------------------------------------------
# Main Function
# ---------------------------------------------------------------------------

def add_new_flight(flight_list: list) -> None:
    """
    Thu thập thông tin chuyến bay từ bàn phím, kiểm tra hợp lệ rồi
    thêm vào danh sách chuyến bay (truyền vào bằng tham chiếu).
    """
    print("\n----- TIẾP NHẬN CHUYẾN BAY MỚI -----")

    # --- Nhập mã chuyến bay ---
    raw_id = input("Nhập mã chuyến bay: ")
    flight_id = raw_id.strip().upper()

    if check_duplicate_id(flight_id, flight_list):
        print(f">> [LỖI] Mã chuyến bay '{flight_id}' đã tồn tại! Vui lòng kiểm tra lại.")
        return

    # --- Nhập số hành khách ---
    try:
        passengers = int(input("Nhập số lượng hành khách: "))
        if passengers < 0:
            print(">> [LỖI] Số hành khách không được âm.")
            return
    except ValueError:
        print(">> [LỖI] Số lượng hành khách phải là số nguyên.")
        return

    # --- Nhập thời gian cất cánh ---
    raw_depart = input("Nhập thời gian cất cánh (YYYY-MM-DD HH:MM:SS): ")
    try:
        datetime.strptime(raw_depart.strip(), "%Y-%m-%d %H:%M:%S")
        depart_time = raw_depart.strip()
    except ValueError:
        print(">> [LỖI] Sai định dạng thời gian! Vui lòng nhập đúng chuẩn YYYY-MM-DD HH:MM:SS")
        return

    # --- Nhập số phút bay ---
    try:
        duration_min = int(input("Nhập số phút bay: "))
        if duration_min <= 0:
            print(">> [LỖI] Số phút bay phải lớn hơn 0.")
            return
    except ValueError:
        print(">> [LỖI] Số phút bay phải là số nguyên.")
        return

    # --- Thêm vào danh sách ---
    new_flight = {
        "flight_id":    flight_id,
        "passengers":   passengers,
        "depart_time":  depart_time,
        "duration_min": duration_min,
    }
    flight_list.append(new_flight)
    print(f">> Thêm chuyến bay {flight_id} thành công!")
