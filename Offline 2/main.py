from ConstraintsAndVariables.StudentAsEdge import *
from ConstraintsAndVariables.CoursesAsNodes import *
from ReadingFilesHelper.readingHelpers import *
from MainFiles.MinConflict import *
from MainFiles.TimeTabling import *
from ConstructiveHeuristics.ByLargestNumberOfConflicts import *
from ConstructiveHeuristics.DeSaturation import *
from ConstructiveHeuristics.ByLargestWeigthedDegree import *


FILE_NAME="car-f-92"

def solve(file_name):
    _courses=read_courses(file_name)
    _students=read_students(file_name,_courses)
    conflict_matrix=create_conflict_matrix(_courses,_students)
    create_overlapping_courses(_courses,conflict_matrix)
    # total_time_slots=do_timetabling(_courses)
    # total_time_slots=timetableByDSaturAlgorithm(_courses)
    # total_time_slots=timetableByLargestStudentsWithConflict(_courses,_students)
    total_time_slots=timetable_by_largest_weighted_degree(_courses,_students)
    print(total_time_slots)

    print(calculate_average_penalty(_students))
    MinPenaltyReduction(_courses,_students,True)
    print(calculate_average_penalty(_students))
solve(FILE_NAME)
