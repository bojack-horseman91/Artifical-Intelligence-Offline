from ConstraintsAndVariables.StudentAsEdge import*
from typing import List
def calculate_average_penalty(students:List[Student]):
    """
    This function calculates the average penalty of the current timetable.
    """
    total_penalty = 0
    for student in students:
        total_penalty += student.calculate_total_penalty()
    return total_penalty / len(students)
