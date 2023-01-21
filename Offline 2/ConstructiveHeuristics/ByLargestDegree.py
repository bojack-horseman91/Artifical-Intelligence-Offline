from ConstraintsAndVariables.CoursesAsNodes import *
from ConstraintsAndVariables.StudentAsEdge import *
from MainFiles.TimeTabling import *
from typing import List
def timetable_by_largest_degree(courses:List[Course])->int:
    courses.sort(key=lambda x: x.degree, reverse=True)
    return do_timetabling(courses)