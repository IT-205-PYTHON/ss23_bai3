"""
Module: file_helper.py
Package: utils
Chức năng: Khởi tạo thư mục lưu trữ nhật ký bay (aviation_logs) bằng thư viện os.
"""

import os

LOG_DIR = "aviation_logs"


def create_log_folder() -> None:
    """
    Kiểm tra sự tồn tại của thư mục 'aviation_logs'.
    - Nếu chưa có: tạo mới bằng os.mkdir().
    - Nếu đã có: thông báo và bỏ qua, không để văng FileExistsError.
    """
    print("\n----- KHỞI TẠO THƯ MỤC HỆ THỐNG -----")

    if os.path.exists(LOG_DIR):
        print(f"[SYSTEM] Thư mục đã tồn tại, bỏ qua bước khởi tạo")
    else:
        print(f"[SYSTEM] Thư mục '{LOG_DIR}' chưa tồn tại. Đang tiến hành khởi tạo...")
        os.mkdir(LOG_DIR)
        print("[SYSTEM] Tạo thư mục thành công!")
