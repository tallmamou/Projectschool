import csv

class Student:
    all = []

    def __init__(self, student_id, name, age, grade):
        self.__student_id = student_id
        self.__name = str(name)
        self.__age = int(age)
        self.__grade = str(grade)
        Student.all.append(self)

    @property
    def student_id(self):
        return self.__student_id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = int(value)

    @property
    def grade(self):
        return self.__grade

    @grade.setter
    def grade(self, value):
        self.__grade = value

    def __str__(self):
        return f"ID: {self.__student_id}, Name: {self.__name}, Age: {self.__age}, Grade: {self.__grade}"

def find_student_by_id(student_id):
    for student in Student.all:
        if student.student_id == student_id:
            return student
    return None

def new_student():
    while True:
        student_id = input("Enter your student ID: ").strip()
        if student_id:
            existing = find_student_by_id(student_id)
            if existing:
                print("Student with this ID already exists:")
                print(existing)
                return  # Exit without adding duplicate
            break
        print("Student ID cannot be empty.")

    while True:
        name = input("Enter your name: ").strip()
        if name.replace(" ", "").isalpha():
            break
        print("Name must contain only letters and spaces.")

    while True:
        age_input = input("Enter your age: ").strip()
        if age_input.isdigit():
            age = int(age_input)
            break
        print("Age must be an integer.")

    while True:
        grade = input("Enter your grade: ").strip()
        if grade.isalpha():
            break
        print("Grade must contain only letters.")

    Student(student_id, name, age, grade)
    print("New student added.")

# Load students from CSV
with open("students.csv", 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        Student(row['student_id'], row['name'], row['age'], row['grade'])

# Optionally, check if a student exists by ID before adding new
search_id = input("Enter a student ID to check if student exists: ").strip()
found_student = find_student_by_id(search_id)
if found_student:
    print("Student found:")
    print(found_student)
else:
    print("No student found with that ID.")

# Add a new student interactively
new_student()

# Print all students
for student in Student.all:
    print(student)

         

