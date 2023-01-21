class Course:


    def __init__(self, course_id: str, total_enrollment: int):
        """
        Initializes a new Course object with the given course_id and total_enrollment.
        Also, initializes the time_slot to -1, the overlapping_courses list to an empty list,
        the conflict and dfs_status to 0, and sets the object as not visited.
        """
        self._course_id = course_id
        self._total_enrollment = total_enrollment
        self._time_slot = -1
        self._overlapping_courses = []
        self._conflict = 0
        self._dfs_status = 0
        self.degree =0


    def get_course_id(self):
        return int(self._course_id)

    
    def get_degree(self)->int:
        return self.degree


    def set_time_slot(self, time_slot: int):
        """Sets the time slot for this course."""
        self._time_slot = time_slot

    def get_time_slot(self) -> int:
        """Returns the time slot for this course."""
        return self._time_slot




    def add_overlapping_course(self, course: "Course"):
        """Adds a course that overlaps with this course to the overlapping_courses list."""
        self._overlapping_courses.append(course)
        self.degree += 1

    def get_overlapping_courses_number(self) -> int:
        """Returns the number of overlapping courses for this course."""
        return len(self._overlapping_courses)

    def get_overlapping_courses(self) :
        """Returns the list of overlapping courses for this course."""
        return self._overlapping_courses




    def set_conflict(self, conflict: int):
        """Sets the conflict for this course."""
        self._conflict = conflict

    def get_conflict(self) -> int:
        """Returns the conflict for this course."""
        return self._conflict





    def set_dfs_status(self, dfs_status: int):
        """Sets the dfs status for this course."""
        self._dfs_status = dfs_status

    def get_dfs_status(self) -> int:
        """Returns the dfs status for this course."""
        return self._dfs_status




    def __str__(self):
        """
        Returns a string representation of this course in the format:
        'course_id time_slot total_enrollment conflict dfs_status'.
        """
        return f"CourseID:{self._course_id} has timeSlot : {self._time_slot} with total_Enrollment :{self._total_enrollment} numberOfConflicts :{self._conflict} dfs: {self._dfs_status}"

    def __repr__(self) -> str:
        """
        Returns a string representation of this course in the format:
        'course_id time_slot total_enrollment conflict dfs_status'.
        """
        return f"CourseID:{self._course_id} has timeSlot : {self._time_slot} with total_Enrollment :{self._total_enrollment} numberOfConflicts :{self._conflict} dfs: {self._dfs_status}"