from Helpers.CalculateAvrPenalty import *
from ConstraintsAndVariables.CoursesAsNodes import *
from ConstraintsAndVariables.StudentAsEdge import *
from typing import List

def doPairSwapOperator(students: List[Student], course1: Course, course2: Course):
    # get the time slots of both courses
    time_slot1 = course1.get_time_slot()
    time_slot2 = course2.get_time_slot()

    # check if swapping is possible
    if time_slot1 == time_slot2:
        return
    if any(x.get_time_slot() == time_slot2 for x in course1.get_overlapping_courses()):
        return
    if any(x.get_time_slot() == time_slot1 for x in course2.get_overlapping_courses()):
        return

    # perform swap and calculate penalty
    current_penalty = calculate_average_penalty(students)
    

    # perform the pair swap by swapping the time slots of u and v
    course1.set_time_slot(time_slot2)
    course2.set_time_slot(time_slot1)
    
    # calculate the new penalty after the pair swap
    new_penalty = calculate_average_penalty(students)

    # compare penalties and undo swap if needed
    if current_penalty <= new_penalty:
        course1.set_time_slot(time_slot1)
        course2.set_time_slot(time_slot2)
    