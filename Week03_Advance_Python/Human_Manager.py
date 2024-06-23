class Person:
    """Lớp cha đại diện cho một người trong phường."""

    def __init__(self, name):
        self.name = name

    def describe(self):
        print(f"{self.__class__.__name__} - Name: {self.name}")


class Student(Person):
    """Lớp con đại diện cho học sinh."""

    def __init__(self, name, yob, grade):
        super().__init__(name)
        self.yob = yob
        self.grade = grade

    def describe(self):
        super().describe()
        print(f"- YoB: {self.yob} - Grade: {self.grade}")


class Teacher(Person):
    """Lớp con đại diện cho giáo viên."""

    def __init__(self, name, yob, subject):
        super().__init__(name)
        self.yob = yob
        self.subject = subject

    def describe(self):
        super().describe()
        print(f"- YoB: {self.yob} - Subject: {self.subject}")


class Doctor(Person):
    """Lớp con đại diện cho bác sĩ."""

    def __init__(self, name, yob, specialist):
        super().__init__(name)
        self.yob = yob
        self.specialist = specialist

    def describe(self):
        super().describe()
        print(f"- YoB: {self.yob} - Specialist: {self.specialist}")


class Ward:
    """Lớp đại diện cho một phường."""

    def __init__(self, name):
        self.name = name
        self.people = []

    def add_person(self, person):
        """Thêm một người mới vào phường."""
        self.people.append(person)

    def describe(self):
        """In ra tên phường và mô tả của từng người."""
        print(f"Ward Name: {self.name}")
        for person in self.people:
            person.describe()

    def count_doctor(self):
        """Đếm số lượng bác sĩ trong phường."""
        count = 0
        for person in self.people:
            if isinstance(person, Doctor):
                count += 1
        return count

    def sort_age(self):
        """Sắp xếp mọi người trong phường theo tuổi tăng dần."""
        self.people.sort(key=lambda p: p.yob)

    def compute_average(self):
        """Tính trung bình năm sinh của các giáo viên trong phường."""
        total_yob = 0
        teacher_count = 0
        for person in self.people:
            if isinstance(person, Teacher):
                total_yob += person.yob
                teacher_count += 1
        if teacher_count > 0:
            return total_yob / teacher_count
        else:
            return None  # Trả về None nếu không có giáo viên nào


# Tạo các đối tượng student, teacher, doctor
student1 = Student("studentA", 2010, "7")
teacher1 = Teacher("teacherA", 1969, "Math")
doctor1 = Doctor("doctorA", 1945, "Endocrinologists")

# Hiển thị thông tin của từng người
student1.describe()
teacher1.describe()
doctor1.describe()

# Tạo phường và thêm người
ward1 = Ward("Ward1")
ward1.add_person(student1)
ward1.add_person(teacher1)
ward1.add_person(Teacher("teacherB", 1995, "History"))
ward1.add_person(doctor1)
ward1.add_person(Doctor("doctorB", 1975, "Cardiologists"))

# Hiển thị thông tin của phường và tất cả mọi người
print("1. Danh sách người trong phường:")
ward1.describe()

# Hiển thị thông tin của phường và tất cả mọi người sau khi sắp xếp tăng dần
print("\n2. Sau khi sắp xếp theo tuổi, danh sách người trong phường:")
ward1.sort_age()
ward1.describe()

# Đếm số lượng bác sĩ
print(
    f"\n3. Số lượng bác sĩ trong phường {ward1.name}: {ward1.count_doctor()}")

# Tuổi trung bình của số lượng bác sĩ
average_yob = ward1.compute_average()
print(
    f"\nTrung bình năm sinh của giáo viên trong phường {ward1.name}: {average_yob}")