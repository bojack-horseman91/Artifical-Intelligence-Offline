from ConstraintsAndVariables.CoursesAsNodes import *
from typing import List
def do_timetabling(courses: List[Course]) -> int:
    """
    Assigns a time slot to each course based on the overlapping courses.
    The time slot assigned to each course is the smallest possible slot number
    that is not occupied by any of its overlapping courses.
    """
    total_time_slot = 0
    
    for course in courses:
        # Get the time slots occupied by the overlapping courses
        overlapping_courses = course.get_overlapping_courses()
        slot_occupied = [oc.get_time_slot() for oc in overlapping_courses]
        slot_occupied.sort()
        
        suitable_time_slot = 0
        for occupied_slot in slot_occupied:
            if occupied_slot != -1:
                if suitable_time_slot == occupied_slot:
                    suitable_time_slot += 1
                if suitable_time_slot < occupied_slot:
                    course.set_time_slot(suitable_time_slot)
                    break
        
        # If no suitable time slot was found, assign the next available slot
        if course.get_time_slot() == -1:
            if suitable_time_slot == total_time_slot:
                course.set_time_slot(total_time_slot)
                total_time_slot += 1
            else:
                course.set_time_slot(suitable_time_slot)
    
    return total_time_slot
