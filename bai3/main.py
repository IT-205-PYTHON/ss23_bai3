"""
File: main.py
Vai trò: Điểm khởi chạy duy nhất của chương trình.
         Chỉ chứa vòng lặp while điều hướng menu và gọi hàm từ các module.
"""

from core.logistics   import display_flight_schedule
from core.manager     import add_new_flight
from utils.time_helper import calculate_eta
from utils.file_helper import create_log_folder

# ---------------------------------------------------------------------------
# Dữ liệu ban đầu
# ---------------------------------------------------------------------------
flights = [
    {
        "flight_id":    "RA001",
        "passengers":   154,
        "depart_time":  "2026-06-15 08:00:00",
        "duration_min": 120,
    },
    {
        "flight_id":    "RA002",
        "passengers":   85,
        "depart_time":  "2026-06-15 13:30:00",
        "duration_min": 45,
    },
]

# ---------------------------------------------------------------------------
# Vòng lặp menu chính
# ---------------------------------------------------------------------------
def main() -> None:
    while True:
        print("\n===== HỆ THỐNG ĐIỀU HÀNH BAY RIKKEI AVIATION =====")
        print("1. Hiển thị lịch trình và Thống kê hậu cần")
        print("2. Tiếp nhận chuyến bay mới")
        print("3. Tính thời gian hạ cánh dự kiến (ETA)")
        print("4. Khởi tạo thư mục lưu trữ log hệ thống")
        print("5. Thoát chương trình")
        print("==================================================")

        try:
            choice = int(input("Nhập lựa chọn của bạn: "))
        except ValueError:
            print(">> [LỖI] Vui lòng nhập một số từ 1 đến 5.")
            continue

        if choice == 1:
            display_flight_schedule(flights)
        elif choice == 2:
            add_new_flight(flights)
        elif choice == 3:
            calculate_eta(flights)
        elif choice == 4:
            create_log_folder()
        elif choice == 5:
            print("\nCảm ơn kỹ sư đã sử dụng hệ thống!")
            break
        else:
            print(">> [LỖI] Lựa chọn không hợp lệ. Vui lòng nhập từ 1 đến 5.")


if __name__ == "__main__":
    main()
