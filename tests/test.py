from datetime import date
from pydantic import ValidationError
import requests

from app.main import SStudent


# def get_students_with_param_requests(course: int):
#     url = "http://127.0.0.1:8000/students"
#     response = requests.get(url, params={"course": course})
#     return response.json()


# students = get_students_with_param_requests(3)
# for student in students:
#     print(student)


# def get_all_students():
#     url = 'http://127.0.0.1:8000/students'
#     response = requests.get(url)
#     return response.json()


# students = get_all_students()
# for i in students:
#     print(i)


# def get_students_with_param_path(course: int):
#     url = f"http://127.0.0.1:8000/students/{course}"
#     response = requests.get(url)
#     return response.json()


# students = get_students_with_param_path(2)
# for student in students:
#     print(student)


# def get_students_with_param_mix(course: int, major: str, enrollment_year: int):
#     url = f'http://127.0.0.1:8000/students/{course}'
#     response = requests.get(url)
#     return response.json()


# students = get_students_with_param_mix(2, major=None, enrollment_year=2018)
# print(students)


#query parametr
# def get_id_students_with_param_path(student_id: int):
#     url = f'http://127.0.0.1:8000/student'
#     response = requests.get(url, params={'student_id': student_id})
#     return response.json()

# students = get_id_students_with_param_path(student_id=3)
# print(students)


#path parametr
# def get_id_students_with_param_path(student_id: int):
#     url = f'http://127.0.0.1:8000/student/{student_id}'
#     response = requests.get(url)
#     return response.json()

# students = get_id_students_with_param_path(3)
# print(students)


student_data = {
    "student_id": 1,
    "phone_number": ""
    "+1234567890",
    "first_name": "Иван",
    "last_name": "Иванов",
    "date_of_birth": date(2000, 1, 1),
    "email": "ivan.ivanov@example.com",
    "address": "Москва, ул. Пушкина, д. Колотушкина",
    "enrollment_year": 2022,
    "major": "Информатика",
    "course": 3,
    "special_notes": "Увлекается программированием"
}


def test_valid_student(data: dict) -> None:
    try:
        student = SStudent(**data)
        print(student)
    except ValidationError as e:
        print(f"Ошибка валидации: {e}")

student_data_test = test_valid_student(student_data)