from ConstraintsAndVariables.CoursesAsNodes import *
from typing import List
class Student:
    def __init__(self):
        self.enrolled_courses = []

    def add_enrolled_course(self, course):
        self.enrolled_courses.append(course)

    def get_enrolled_courses(self)->List[Course]:
        return self.enrolled_courses

    def calculate_total_penalty(self):
        total_penalty = 0
        self.enrolled_courses.sort(key=lambda x: x.get_time_slot())

        for i in range(len(self.enrolled_courses) - 1):
            for j in range(i+1, len(self.enrolled_courses)):
                gap = self.enrolled_courses[j].get_time_slot() - self.enrolled_courses[i].get_time_slot()
                if gap < 6:
                    total_penalty += 2 ** (5 - gap)
        return total_penalty
    def __repr__(self) -> str:
        return self.enrolled_courses.__repr__()