class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
 
    def add_courses(self, course_name):
        self.finished_courses.append(course_name)  
    
    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            lecturer.grades += [grade]
        else:
            return 'Ошибка'

    def get_avg_grade(self):
        sum_hw = 0
        count = 0
        for grades in self.grades.values():
            sum_hw += sum(grades)
            count += len(grades)
        return round(sum_hw / count, 2)

    def __str__(self):
        res = f'Имя: {self.name} \n'\
              f'Фамилия: {self.surname} \n'\
              f'Средняя оценка за ДЗ: {self.get_avg_grade()} \n'
        return res
    
    def __lt__(self, other_student):
        if not isinstance(other_student, Student):
                print('Такого студента нет')
                return
        else:
            compare = self.get_avg_grade() < other_student.get_avg_grade()
            if compare:
                print(f'{self.name} {self.surname} уиться хуже, чем {other_student.name} {other_student.surname}')
            else:
                print(f'{other_student.name} {other_student.surname} уиться хуже, чем {self.name} {self.surname}')
                return compare

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress and grade <= 10:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name} \n'\
              f'Фамилия: {self.surname} \n'
        return res
            
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = []
    
    def get_avg_grade_lec(self):
        sum_hw = 0
        for grades in self.grades:
            sum_hw += sum(grades)
        return round(sum_hw / len(grades), 2)
    

    def __str__(self):
        res = f'Имя: {self.name} \n'\
              f'Фамилия: {self.surname} \n'\
              f'Средняя оценка за ДЗ: {sum(self.grades) / len(self.grades) :.2f} \n'
        return res

    def __lt__(self, other_lecturer):
        if not isinstance(other_lecturer, Lecturer):
                print('Такого лектора нет')
                return
        else:
            compare = ((sum(self.grades) / len(self.grades)) < (sum(other_lecturer.grades) / len(other_lecturer.grades))
            if compare:
                print(f'{self.name} {self.surname} читает лекции хуже, чем {other_lecturer.name} {other_lecturer.surname}')
            else:
                print(f'{other_lecturer.name} {other_lecturer.surname} читает лекции хуже, чем {self.name} {self.surname}')
                return compare


best_student = Student('Ruoy', 'Eman', 'M')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git'] 

next_student = Student('John', 'Watson', 'M')
next_student.courses_in_progress += ['Python']
next_student.courses_in_progress += ['Git']

nice_mentor = Mentor('Michel', 'Smith')
nice_mentor.courses_attached += ['Python']

next_mentor = Mentor('Some', 'Buddy')
next_mentor.courses_attached += ['Python']

good_reviwer = Reviewer('Kate', 'Solomina')
good_reviwer.courses_attached += ['Python']
good_reviwer.courses_attached += ['Git']

next_reviwer = Reviewer('Ann', 'Ivanova')
next_reviwer.courses_attached += ['Python']
next_reviwer.courses_attached += ['Git']

interesting_lecturer = Lecturer('Alice', 'Petrova')
interesting_lecturer.courses_attached += ['Python']
interesting_lecturer.courses_attached += ['Git']

next_lecturer = Lecturer('Natalia', 'Sidorova')
next_lecturer.courses_attached += ['Python']
next_lecturer.courses_attached += ['Git']
 
good_reviwer.rate_hw(best_student, 'Python', 6)
good_reviwer.rate_hw(best_student, 'Python', 9)
good_reviwer.rate_hw(next_student, 'Python', 8)
good_reviwer.rate_hw(next_student, 'Python', 4)


best_student.rate_lecturer(interesting_lecturer, 'Python', 5)
best_student.rate_lecturer(interesting_lecturer, 'Git', 8)
next_student.rate_lecturer(next_lecturer, 'Python', 7)
next_student.rate_lecturer(next_lecturer, 'Git', 9)

print(good_reviwer)

print(interesting_lecturer)

print(best_student)

print(next_lecturer.grades)
print(interesting_lecturer.grades)

print(sum(next_lecturer.grades))

print(best_student < next_student)

print(interesting_lecturer < next_lecturer)

def get_avg_hw_grade(student_list, course):
    total_sum = 0 

    for student in student_list:
         for c, grades in student.grades.items():
            if c == course:
                total_sum += sum(grades) / len(grades)
    return round(total_sum / len(student_list), 2)

print(get_avg_hw_grade([best_student, next_student], 'Python'))

def get_avg_lec_grade(list_lecture):
    total_sum = 0 

    for lecture in list_lecture:
        total_sum += sum(lecture.grades) / len(lecture.grades)
    return total_sum / len(list_lecture)

print(get_avg_lec_grade([interesting_lecturer, next_lecturer]))
