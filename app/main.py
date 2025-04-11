from typing import Optional
from fastapi import FastAPI, HTTPException
import os
from app.students.models import SDeleteFilter, SStudent, SStudentUpdate, SUpdateFilter
from app.data_base import add_student, dell_student, upd_student
# from utils import json_to_dict_list

script_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(script_dir)
path_to_json = os.path.join(parent_dir, 'students.json')

app = FastAPI()

# @app.get('/students')
# def get_all_students():
#     return json_to_dict_list(path_to_json)

# @app.get('/')
# def home_page():
#     return {'message': 'Саламалекум'}

# @app.get('/student/{student_id}')
# def get_all_students_id(student_id: int):
#     students = json_to_dict_list(path_to_json)
#     filtered_students_id = []

#     for student in students:
#         if student['student_id'] == student_id:
#             filtered_students_id.append(student)

#     return filtered_students_id

# @app.get('/student')
# def get_all_students(student_id: Optional[int] = None):
#     students = json_to_dict_list(path_to_json)
#     if student_id is None:
#         return students
#     else:
#         return_list = []
#         for student in students:
#             if student['student_id'] == student_id:
#                 return_list.append(student)
#         return return_list

# @app.get('/students')
# def get_all_students(course: Optional[int] = None):
#     students = json_to_dict_list(path_to_json)
#     if course is None:
#         return students
#     else:
#         return_list = []
#         for student in students:
#             if student['course'] == course:
#                 return_list.append(student)
#         return return_list




class RBStudent:
    def __init__(self, course: int, major: Optional[str] = None, enrollment_year: Optional[int] = 2018):
        self.course: int = course
        self.major: Optional[str] = major
        self.enrollment_year: Optional[int] = enrollment_year

    

# @app.get("/student")
# def get_student_from_param_id(student_id: int) -> SStudent:
#     students = json_to_dict_list(path_to_json)
#     for student in students:
#         if student["student_id"] == student_id:
#             return student
        

# @app.get("/students/{course}")
# def get_all_students_course(request_body: RBStudent = Depends()) -> List[SStudent]:
#     students = json_to_dict_list(path_to_json)
#     filtered_students = []
#     for student in students:
#         if student["course"] == request_body.course:
#             filtered_students.append(student)

#     if request_body.major:
#         filtered_students = [student for student in filtered_students if student['major'].lower() == request_body.major.lower()]

#     if request_body.enrollment_year:
#         filtered_students = [student for student in filtered_students if student['enrollment_year'] == request_body.enrollment_year]

#     return filtered_students




# @app.post("/add_student")
# def add_student_handler(student: SStudent):
#     student_dict = student.model_dump()
#     check = add_student(student_dict)
#     # print(type(student_dict), student_dict)
#     if check:
#         return {"message": "Студент успешно добавлен!"}
#     else:
#         return {"message": "Ошибка при добавлении студента"}

@app.post("/add_student")
def add_student_handler(student: SStudent):
    student_dict = student.dict()
    check = add_student(student_dict)
    if check:
        return {"message": "Студент успешно добавлен!"}
    else:
        return {"message": "Ошибка при добавлении студента"}
    

@app.put("/update_student")
def update_student_handler(filter_student: SUpdateFilter, new_data: SStudentUpdate):
    check = upd_student(filter_student.dict(), new_data.dict())
    if check:
        return {"message": "Информация о студенте успешно обновлена!"}
    else:
        raise HTTPException(status_code=400, detail="Ошибка при обновлении информации о студенте")
    

@app.delete('/delete_student')
def delete_student_handler(filter_student: SDeleteFilter):
    check = dell_student(filter_student.key, filter_student.value)
    if check:
        return {"message": "Студент успешно удален!"}
    else:
        raise HTTPException(status_code=400, detail="Ошибка при удалении студента")
    