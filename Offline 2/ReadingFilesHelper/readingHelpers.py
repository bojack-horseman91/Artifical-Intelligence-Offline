from typing import List, Tuple

from ConstraintsAndVariables.StudentAsEdge import Student
from ConstraintsAndVariables.CoursesAsNodes import Course


def read_courses(file_name: str):
    courses = []
    with open(f"Datasets/{file_name}.crs") as file:
        for line in file:
            course_id, enrollment = line.strip().split()
            courses.append(Course(course_id, int(enrollment)))
    return courses

def read_students(file_name, courses):
    students=[]
    with open(f"Datasets/{file_name}.stu") as f:
        student_count = 0
        for line in f:
            temp_list = line.strip().split(" ")
            temp_list = [int(i) for i in temp_list]
            students.append(Student())
            for course_id in temp_list:
                students[student_count].add_enrolled_course(courses[course_id-1])
            student_count+=1
    return students
def create_conflict_matrix(courses, students):
    conflict_matrix = [[0 for _ in range(len(courses))] for _ in range(len(courses))]
    for student in students:
        enrolled_courses = student.get_enrolled_courses()
        for i in range(len(enrolled_courses) - 1):
            for j in range(i + 1, len(enrolled_courses)):
                course_1 = enrolled_courses[i]
                course_2 = enrolled_courses[j]
                conflict_matrix[course_1.get_course_id()-1][course_2.get_course_id()-1] = 1
                conflict_matrix[course_2.get_course_id()-1][course_1.get_course_id()-1] = 1
    return conflict_matrix

def create_overlapping_courses(courses: List[Course], conflict_matrix: List[List[int]]):
    for i in range(len(courses)):
        for j in range(len(courses)):
            if conflict_matrix[i][j] == 1:
                courses[i].add_overlapping_course(courses[j])


