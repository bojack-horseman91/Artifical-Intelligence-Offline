from ConstraintsAndVariables.CoursesAsNodes import *
from ConstraintsAndVariables.StudentAsEdge import *
from MainFiles.TimeTabling import *
from typing import List
def timetableByDSaturAlgorithm(courses:List[Course])->int:
    # step 1: sort the courses by degree (number of overlapping courses)
    courses = sorted(courses, key=lambda x: x.degree, reverse=True)
    # step 2: assign the first course to the first timeslot
    courses[0].set_time_slot(0)
    
    # step 3: initialize total_time_slot to 1
    total_time_slot = 1
    
    # step 4: iterate through remaining courses
    for i in range(1, len(courses)):
        # step 5: find the course with the maximum saturation degree
        max_saturation_degree = -1
        max_index = -1
        selected = None
        for j in range(len(courses)):
            if courses[j].get_time_slot() == -1:
                temp = set()
                # find the timeslots that are occupied by overlapping courses
                for overlapping_course in courses[j].get_overlapping_courses():
                    if overlapping_course.get_time_slot() != -1:
                        temp.add(overlapping_course.get_time_slot())
                # compare the saturation degree with the current maximum
                if len(temp) > max_saturation_degree or (len(temp) == max_saturation_degree and courses[j].degree > courses[max_index].degree):
                    max_saturation_degree = len(temp)
                    max_index = j
                    selected = temp
        # step 6: assign the course to the next available timeslot
        suitable_time_slot = 0
        while courses[max_index].get_time_slot() == -1:
            if suitable_time_slot not in selected:
                courses[max_index].set_time_slot(suitable_time_slot)
                if suitable_time_slot == total_time_slot:
                    total_time_slot += 1
            suitable_time_slot += 1
    return total_time_slot
