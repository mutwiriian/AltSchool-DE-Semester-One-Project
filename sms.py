"""
This module creates a student management system that is
composed of Student and Instructor classes, which inherit their properties
from the Person class, a Course class. The Enrollment class tracks student
membership in courses and their grades.

The StudentManagementClass class combines properties and methods in each of these classes
to implement its functionalities like creating students, removing course,
assigning grades, ...
"""


class Person:
    def __init__(self, name: str, id_number: int):
        """Initialize class attributes with arguments passed"""
        self.name = name.title()
        self.id_number = id_number

    def __str__(self):
        """Return string representation of Person attributes"""
        return f"\nName: {self.name}, \nID: {self.id_number}"


class Student(Person):
    """Inherit Person's attributes and methods to Student class"""

    def __init__(self, name: str, id_number: int, major: str):
        """Initialize parent(Student) class attributes in child(Person) class"""
        super().__init__(name=name, id_number=id_number)
        self.major = major.title()

    def __str__(self):
        """Return string representation of Student attributes"""
        return f"\nName: {self.name},\nRole: Student \nID: {self.id_number}, \nMajor: {self.major}"


class Instructor(Person):
    """Inherit Person's attributes and methods to Instructor class"""

    def __init__(self, name: str, id_number: int, department: str):
        """Initialize parent(Person) class attributes in child(Instructor) class"""
        super().__init__(name=name, id_number=id_number)
        self.department = department

    def __str__(self):
        """Return string representation of Instructor attributes"""
        return f"\nName: {self.name},\nRole: Instructor \nID: {self.id_number}, \nDepartment: {self.department}"


class Course:
    def __init__(
        self, course_name: str, course_id: str, enrolled_students: set[int] | None = set()
    ):
        """Initialize class attributes with arguments passed"""
        self.course_name = course_name
        self.course_id = course_id
        self.enrolled_students = enrolled_students

    def add_student(self, student: Student):
        """Adds student to enrolled_students list"""
        self.enrolled_students.add(student)

    def remove_student(self, student_id: int):
        """Remove student from enrolled_students list"""
        for student in self.enrolled_students:
            if student.id_number == student_id:
                self.enrolled_students.remove(student)

    def __str__(self):
        """Return string representation of Course attributes"""
        return (
            f"\nCourse Name: {self.course_name} \nCourse ID: {self.course_id}\n{'-'*20}"
        )


class Enrollment:
    def __init__(self, student: Student, course: Course):
        """Initialize class attributes with arguments passed"""
        self.student = student
        self.course = course

    def assign_grade(self, grade: str):
        """Assigns a grade to an enrolled student"""
        self.grade = grade.capitalize()

    def __str__(self):
        """Return string representation of Enrollment attributes conditional on self.grade"""
        if self.grade:
            return f"\nStudent\n{'-'*20} \nName: {self.student.name}\nID: {self.student.id_number}\nMajor: {self.student.major}\n\nStudent's Course\n{'-'*20}\nName: {self.course.course_name}\nID: {self.course.course_id}\nGrade: {self.grade}"
        else:
            return f"\nStudent\n{'-'*20} \nName: {self.student.name}\nID: {self.student.id_number}\nMajor: {self.student.major}\n\nStudent's Course\n{'-'*20}\nName: {self.course.course_name}\nID: {self.course.course_id}"


class StudentManagementSystem:
    def __init__(
        self,
        students: list[Student] | None = [],
        instructors: list[Instructor] | None = [],
        courses: list[Course] | None = [],
        enrollments: list[Enrollment] | None = [],
    ):
        """
        Initialize class attributes with arguments passed
        Data structures can be empty on class initialization
        """
        self.students = students
        self.instructors = instructors
        self.courses = courses
        self.enrollments = enrollments

    def add_student(self, student: Student):
        """Adds student to students list"""
        self.students.append(student)

    def get_student(self, id_number: int):
        """Get a student from the students list"""
        for student in self.students:
            if student.id_number == id_number:
                return student

    def update_student(self, student_updated: Student):
        """
        Update Student attributes from new Student instance
        student.id_number uniquely identifies each student and thus not subject to change
        """
        for student in self.students:
            if student.id_number == student_updated.id_number:
                student.name = student_updated.name
                student.major = student_updated.major

    def remove_student(self, student_id: int):
        """Remove student from the students list"""
        for student in self.students:
            if student.id_number == student_id:
                self.students.remove(student)

    def add_instructor(self, instructor: Instructor):
        """Add an instructor to instructors list"""
        self.instructors.append(instructor)

    def get_instructor(self, id_number: int):
        """Get instructor from the list of instructors"""
        for instructor in self.instructors:
            if instructor.id_number == id_number:
                return instructor

    def update_instructor(self, instructor_updated: Instructor):
        """
        Update Student attributes from new Student instance
        instructor.id_number uniquely identifies each instructor and thus not subject to change
        """
        for instructor in self.instructors:
            if instructor.id_number == instructor_updated.id_number:
                instructor.name = instructor_updated.name
                instructor.department = instructor_updated.department

    def remove_instructor(self, instructor_id: int):
        """Remove instructor from instructors list"""
        for instructor in self.instructors:
            if instructor.id_number == instructor_id:
                self.instructors.remove(instructor)

    def add_course(self, course: Course):
        """Add course to courses list"""
        self.courses.append(course)

    def get_course(self, course_id: int):
        """Get a course from the list of courses"""
        for course in self.courses:
            if course.course_id == course_id:
                return course

    def update_course(self, course_updated: Course):
        """
        Update Student attributes from new Student instance
        course.course_id uniquely identifies each instructor and thus not subject to change
        """
        for course in self.courses:
            if course.course_id == course_updated.course_id:
                course.course_name = course_updated.course_name
                course.enrolled_students = course_updated.enrolled_students

    def remove_course(self, course_id: int):
        """Remove course from courses list"""
        for course in self.courses:
            if course.course_id == course_id:
                self.courses.remove(course)

    def enroll_student(self, student_id: int, course_id: int):
        """
        Enroll a student to a course
        """
        student = self.get_student(id_number=student_id)
        course = self.get_course(course_id=course_id)

        if student and course:
            enrollment = Enrollment(student=student, course=course)
            self.enrollments.append(enrollment)

            course.enrolled_students.add(student_id)

    def assign_grade(self, grade: str, student_id: int, course_id: int):
        """Assign a grade to course a given student is taking"""
        for enrollment in self.enrollments:
            if (
                student_id == enrollment.student.id_number
                and course_id == enrollment.course.course_id
            ):
                enrollment.assign_grade(grade=grade)

    def get_students_in_course(self, course_id: int):
        """Extract students enrolled in a course"""
        students = set()
        course = self.get_course(course_id=course_id)

        for student_id in course.enrolled_students:
            student = self.get_student(id_number=student_id)
            students.add(student)
        return students

    def get_courses_for_student(self, student_id: int):
        """Extract courses a student is enrolled in"""
        course_list = []

        for course in self.courses:
            if student_id in course.enrolled_students:
                course_list.append(course)

        return course_list


# --------------------------- TESTS ------------------------------------

# Instantiate the management class
system = StudentManagementSystem()

# Create students
imma = Student("imma", 5443, "mathematics")
ian = Student("ian", 6444, "english")
lucky = Student("lucky", 5493, "chemistry")


# Add students to system
system.add_student(student=imma)
system.add_student(student=ian)
system.add_student(student=lucky)

# Create courses
biology = Course("biology", 103)
english = Course("mathematics", 100)
geography = Course("geography", 107)

# Add courses to system
system.add_course(biology)
system.add_course(english)
system.add_course(geography)

# Enroll students to courses
system.enroll_student(6444, 100)
system.enroll_student(6444, 103)
system.enroll_student(6444, 107)

system.enroll_student(5493, 100)
system.enroll_student(5493, 103)
system.enroll_student(5493, 107)

system.enroll_student(5443, 100)
system.enroll_student(5443, 103)
system.enroll_student(5443, 107)

# Assign grades to students
system.assign_grade("a", 6444, 100)
system.assign_grade("b", 5493, 100)
system.assign_grade("d", 5453, 100)
system.assign_grade("b", 6444, 103)
system.assign_grade("c", 5493, 103)
system.assign_grade("a", 5453, 103)
system.assign_grade("d", 6444, 107)
system.assign_grade("b", 5493, 107)
system.assign_grade("c", 5453, 107)

# Create instructors
instructor_one = Instructor("james", 3782, "biology")
instructor_two = Instructor("alfred", 7352, "physics")
instructor_three = Instructor("jane", 8255, "business")

# Add instructors to system
system.add_instructor(instructor_one)
system.add_instructor(instructor_two)
system.add_instructor(instructor_three)

# Get instructors
print("Instructors")
print("-" * 20)
for instructor in system.instructors:
    print(instructor.__str__())

# Get students' enrolled in a course
print("\nStudents")
print("-" * 20)
students_in_biology = system.get_students_in_course(103)

for student in students_in_biology:
    print(student.__str__())

# Get courses a student is enrolled in
print("\nCourses")
print("-" * 20)
ian_courses = system.get_courses_for_student(6444)

for course in ian_courses:
    print(course.__str__())
