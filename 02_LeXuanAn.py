# student_manager.py

student_list = [
    {"name": "Nguyen Van An", "year_of_birth": 2003, "address": "Da Nang"},
    {"name": "Tran Thi Binh", "year_of_birth": 2002, "address": "Quang Nam"},
    {"name": "Le Van Hung", "year_of_birth": 2003, "address": "Hue"}
]

def print_student_list():
    """
    In danh sách sinh viên.
    """
    print("--- DANH SACH SINH VIEN ---")
    if not student_list:
        print("Danh sach trong.")
    else:
        for s in student_list:
            print(f" - Ten: {s['name']}, Nam sinh: {s['year_of_birth']}, Dia chi: {s['address']}")

if __name__ == "__main__":
    print_student_list()
