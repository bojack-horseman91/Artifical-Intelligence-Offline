from Helpers.Dfs import *
from Helpers.CalculateAvrPenalty import *
def kempe_chain_interchange(courses, students, current_course, neighbor_time_slot):
    """
    This function performs kempe chain interchange on the given courses and students data
    to improve the overall penalty of the timetable.
    
    Parameters:
        - courses (List[Course]): list of all courses
        - students (List[Student]): list of all students
        - current_course (Course): current course for which the interchange is being done
        - neighbor_time_slot (int): time slot of the neighboring course
    """
    # Forming the kempe-chain
    doDepthFirstSearch(current_course, neighbor_time_slot)
    
    # Interchanging time slots among kempe-chain nodes
    current_penalty = calculate_average_penalty(students)
    current_time_slot = current_course.get_time_slot()
    
    # Interchange the time slots
    for course in courses:
        if course.get_dfs_status() == 2:
            if course.get_time_slot() == current_time_slot:
                course.set_time_slot(neighbor_time_slot)
            else:
                course.set_time_slot(current_time_slot)
    
    # Comparing obtained penalty with current penalty
    if current_penalty <= calculate_average_penalty(students):
        # undoing kempe-chain interchange
        for course in courses:
            if course.get_dfs_status() == 2:
                if course.get_time_slot() == current_time_slot:
                    course.set_time_slot(neighbor_time_slot)
                else:
                    course.set_time_slot(current_time_slot)
    
    # Resetting the dfs status of all the courses
    for course in courses:
        if course.get_dfs_status() == 2:
            course.set_dfs_status(0)
    return
