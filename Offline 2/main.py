from ConstraintsAndVariables.StudentAsEdge import *
from ConstraintsAndVariables.CoursesAsNodes import *
from ReadingFilesHelper.readingHelpers import *
from MainFiles.MinConflict import *
from MainFiles.TimeTabling import *
from ConstructiveHeuristics.ByLargestNumberOfConflicts import *
from ConstructiveHeuristics.DeSaturation import *
from ConstructiveHeuristics.ByLargestDegree import *
from ConstructiveHeuristics.ByRandom import *


problems=["car-f-92","car-s-91","yor-f-83","tre-s-92","kuf-s-93"]
solvers=[timetable_by_largest_degree,timetableByDSaturAlgorithm,timetable_by_random_ordering,timetableByLargestStudentsWithConflict]
class Solver:
    def __init__(self,fileName) -> None:
        self.FILE_NAME=fileName
    def writeToReport(self,fileName,output):
        with open(f"{fileName}.sol",'a') as writer:
            for t in output:
                writer.write(f"{t} ")
            writer.write('\n')
    def solve(self,file_name):
        i=0
        for solver in solvers:
            i+=1
            _courses=read_courses(file_name)
            _students=read_students(file_name,_courses)
            conflict_matrix=create_conflict_matrix(_courses,_students)
            create_overlapping_courses(_courses,conflict_matrix)
            # total_time_slots=do_timetabling(_courses)
            
             
            if i==4:
                total_time_slots=solver(_courses,_students)
            else:
                total_time_slots=solver(_courses)
            print(total_time_slots)
            before=calculate_average_penalty(_students)
            print(before)
            MinPenaltyReduction(_courses,_students,True)
            after1=calculate_average_penalty(_students)
            print(after1)
            MinPenaltyReduction(_courses,_students,False)
            after2=calculate_average_penalty(_students)
            print(after2)
            self.writeToReport(file_name,[before,after1,after2])

def main():
    for problem in problems:
        Solver(problem).solve(problem)


if __name__ == '__main__':
    main()
