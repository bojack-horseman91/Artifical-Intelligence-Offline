import random
from ConstraintsAndVariables.CoursesAsNodes import *
from ConstraintsAndVariables.StudentAsEdge import *
from MainFiles.TimeTabling import *
from typing import List
def timetable_by_random_ordering(courses:List[Course])->int:
    random.shuffle(courses)
    return do_timetabling(courses)
