from MainFiles.TimeTabling import *

def timetable_by_largest_weighted_degree(courses, students)->int:
    for i in range(len(students)):
        enrolled_courses = students[i].get_enrolled_courses()
        for j in range(len(enrolled_courses)):
            enrolled_courses[j].set_conflict(enrolled_courses[j].get_conflict() + len(enrolled_courses) - 1)
    courses.sort(key=lambda x: x.get_conflict(), reverse=True)
    return do_timetabling(courses)