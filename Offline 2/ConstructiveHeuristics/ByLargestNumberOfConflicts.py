from ConstraintsAndVariables.CoursesAsNodes import *
from ConstraintsAndVariables.StudentAsEdge import *
from MainFiles.TimeTabling import *
from typing import List

def timetableByLargestStudentsWithConflict(courses: List[Course], students: List[Student]) -> int:
    for student in students:
        enrolled_courses = student.get_enrolled_courses()
        for course in enrolled_courses:
            course.set_conflict(course.get_conflict() + (len(enrolled_courses)==1))
    courses.sort(key=lambda x: x.get_conflict(), reverse=True)
    return do_timetabling(courses)
