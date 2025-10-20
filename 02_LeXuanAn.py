# student_manager.py

student_list = []

def add_student(name, year_of_birth, address):
    """
    Thêm sinh viên mới vào danh sách.
    """
    student = {
        "name": name,
        "year_of_birth": year_of_birth,
        "address": address
    }
    student_list.append(student)
    print(f"Da them sinh vien {name} thanh cong.")

if __name__ == "__main__":
    print("--- THEM SINH VIEN ---")
    add_student("Nguyen Van An", 2003, "Da Nang")
    add_student("Tran Thi Binh", 2002, "Quang Nam")
    print(student_list)
