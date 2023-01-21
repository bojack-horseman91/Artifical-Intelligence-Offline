import random
from typing import List
from ConstraintsAndVariables.CoursesAsNodes import Course
from ConstraintsAndVariables.StudentAsEdge import Student
from PertubationHeuristics.KempeChain import *
from PertubationHeuristics.PairSwapOperator import *
MAX_ITERATIONS=3000

def MinPenaltyReduction(courses:List[Course], students:List[Student], isKempeChainInterchange:bool):
    """
    This function is used to try and reduce the penalty by performing either Kempe-chain interchange
    or pair swap operator.
    :param courses: List of all the courses
    :param students: List of all the students
    :param isKempeChainInterchange: flag to indicate which operation to perform. If True, perform Kempe-chain interchange.
                                    If False, perform pair swap operator
    """



    # Iterating for penalty reduction
    for i in range(MAX_ITERATIONS):
        if i==MAX_ITERATIONS/10:  
            print(i)
        if i==MAX_ITERATIONS/5:
            print(i)
        if i==MAX_ITERATIONS/2:
            print(i)
        
        if isKempeChainInterchange:
            # Kempe-chain interchange
            current = random.randint(0,len(courses)-1)
            overlappingCourses = courses[current].get_overlapping_courses()
            if overlappingCourses:
                kempe_chain_interchange(courses, students, courses[current], overlappingCourses[random.randint(0,len(overlappingCourses)-1)].get_time_slot())
        else:
            # Pair swap operator
            doPairSwapOperator(students, courses[random.randint(0,len(courses)-1)], courses[random.randint(0,len(courses)-1)])
    
    
    return 
