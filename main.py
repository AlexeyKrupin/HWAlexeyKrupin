class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.grade_average = 0


    def rate_lecrurer(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def calculation_of_the_average_score(self):
        count = 0
        x = 0
        for n in self.grades:
            m = 0
            for i in self.grades[n]:
                count += 1
                m += i
            x += m
        self.grade_average += x/count

    def __str__(self):
        res = (f"Имя: {self.name}"" \n"
               f"Фамилия: {self.surname}"" \n"
               f"Средняя оценка за домашнее задание: {self.grade_average}"" \n"
               f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}"" \n"
               f"Завершенные курсы: {', '.join(self.finished_courses)}")
        return res
    def __gt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student!')
            return
        return self.grade_average > other.grade_average



class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Reviewer(Mentor):
    def __init__(self, name, surname):
        pass
        super().__init__(name, surname)
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = (f"Имя: {self.name}"" \n"
               f"Фамилия: {self.surname}")
        return res


class Lecturer(Mentor):
    def __init__(self, name, surname):
        self.grade_average = 0
        super().__init__(name, surname)
        self.grades = {}

    def calculation_of_the_average_score(self):
        count = 0
        x = 0
        for n in self.grades:
            m = 0
            for i in self.grades[n]:
                count += 1
                m += i
            x += m
        self.grade_average += x/count



    def __str__(self):
        res = (f"Имя: {self.name}"" \n"
                f"Фамилия: {self.surname}"" \n"
                f"Средняя оценка за лекции: {self.grade_average}")
        return res
    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer!')
            return
        return self.grade_average > other.grade_average



lecturer_one = Lecturer('Some', 'Buddy')
lecturer_one.courses_attached += ['Python']

student_one = Student('Ruoy', 'Eman', 'your_gender')
student_one.courses_in_progress += ['Python', 'Git']
student_one.finished_courses += ['Введение в программирование']

reviewer_one = Reviewer('Some', 'Buddy')
reviewer_one.courses_attached += ['Python']

lecturer_two = Lecturer('Игорь', 'Николаев')
lecturer_two.courses_attached += ['Python']

student_two = Student('Леонид', 'Агутин', 'your_gender')
student_two.courses_in_progress += ['Python', 'Git']
student_two.finished_courses += ['Введение в программирование']

reviewer_two = Reviewer('Валерий', 'Леонтьев')
reviewer_two.courses_attached += ['Python', 'Git']

student_one.rate_lecrurer(lecturer_one, 'Python', 9.9)
student_one.rate_lecrurer(lecturer_one, 'Python', 9.9)
student_one.rate_lecrurer(lecturer_one, 'Python', 9.9)

reviewer_one.rate_hw(student_one, 'Python', 9.9)
reviewer_one.rate_hw(student_one, 'Python', 9.9)
reviewer_one.rate_hw(student_one, 'Python', 9.9)

student_two.rate_lecrurer(lecturer_two, 'Python', 9)
student_two.rate_lecrurer(lecturer_two, 'Python', 9)
student_two.rate_lecrurer(lecturer_two, 'Python', 9)

reviewer_two.rate_hw(student_two, 'Python', 10)
reviewer_two.rate_hw(student_two, 'Python', 10)
reviewer_two.rate_hw(student_two, 'Python', 10)

reviewer_two.rate_hw(student_two, 'Git', 5)
reviewer_two.rate_hw(student_two, 'Git', 5)
reviewer_two.rate_hw(student_two, 'Git', 5)

student_one.calculation_of_the_average_score()
lecturer_one.calculation_of_the_average_score()
student_two.calculation_of_the_average_score()
lecturer_two.calculation_of_the_average_score()


print(reviewer_one)
print('')
print(lecturer_one)
print('')
print(student_one)
print('')
print(reviewer_two)
print('')
print(lecturer_two)
print('')
print(student_two)
print('')
print(student_one.__gt__(student_two))
print('')
print(student_two.__gt__(student_one))
print('')
print(lecturer_one.__gt__(lecturer_two))
print('')
print(lecturer_two.__gt__(lecturer_one))