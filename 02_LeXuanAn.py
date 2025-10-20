# student_manager.py

student_list = [
    {"name": "Nguyen Van An", "year_of_birth": 2003, "address": "Da Nang"},
    {"name": "Tran Thi Binh", "year_of_birth": 2002, "address": "Quang Nam"},
    {"name": "Le Van Hung", "year_of_birth": 2003, "address": "Hue"}
]

def search_student(search_name):
    """
    Tìm kiếm sinh viên theo tên (không phân biệt hoa thường).
    """
    print("--- KET QUA TIM KIEM ---")
    found = False
    for s in student_list:
        if search_name.lower() in s['name'].lower():
            print(f" - Ten: {s['name']}, Nam sinh: {s['year_of_birth']}, Dia chi: {s['address']}")
            found = True
    if not found:
        print("Khong tim thay sinh vien nao.")

if __name__ == "__main__":
    search_student("an")
    search_student("Dung")
