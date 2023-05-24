class Student:

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        return f"""
Имя: {self.name}
Фамилия : {self.surname}
Средняя оценка за домашнее заданее: {sum((map(sum,self.grades.values())))/len(self.grades)}
Курсы в процессе изучения: {(",".join(self.courses_in_progress))}
Завершенные курсы: {(",".join(self.finished_courses))}"""

    def __lt__(self, lecturer):
        if isinstance(lecturer, Lecturer):
            if sum((map(sum,self.grades.values())))/len(self.grades) < sum((map(sum,lecturer.rates.values())))/len(sum(lecturer.rates.values(),[])):
                return "Средняя оценка лектора выше"
            else:
                return "Некорректное сравнение"
            
    def __gt__(self, lecturer):
        if isinstance(lecturer, Lecturer):
            if sum((map(sum,self.grades.values())))/len(self.grades) > sum((map(sum,lecturer.rates.values())))/len(sum(lecturer.rates.values(),[])):
                return "Средняя оценка студента выше"
            else:
                return "Некорректное сравнение"

    def __eq__(self, lecturer):
        if isinstance(lecturer, Lecturer):
            if sum((map(sum,self.grades.values())))/len(self.grades) == sum((map(sum,lecturer.rates.values())))/len(sum(lecturer.rates.values(),[])):
                return "Средние оценки студента и лектора равны"                
   
    def rate_lecturer(self, lecturer, course, rate):
        if isinstance(lecturer, Lecturer) and course in self.finished_courses and course in lecturer.courses_attached:
            if course in lecturer.rates:
                lecturer.rates[course] += [rate]
            else:
                lecturer.rates[course] = [rate]
        else:
            return 'Ошибка'

    def add_courses(self,course_name):
        self.finished_courses.extend(course_name)

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
 
class Lecturer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.rates = {}

    def __str__(self):
        return f"""
Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за лекции: {sum((map(sum,self.rates.values())))/len(sum(self.rates.values(),[]))}"""

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.finished_courses:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
        
    def __str__(self):
        return f"""
Имя: {self.name}
Фамилия: {self.surname}"""

def middle_grade_student(student_list, course):
    res = sum([sum(student.grades[course]) for student in student_list]) / sum([len(student.grades[course]) for student in student_list])
    print(f"Средняя оценка студентов за курс {course} составляет {res}")

def middle_rate_lecturer(lecturer_list, course):
    res = sum([sum(lecturer.rates[course]) for lecturer in lecturer_list]) / sum([len(lecturer.rates[course]) for lecturer in lecturer_list])
    print(f"Средняя оценка лекторов за курс {course} составляет {res}")

student1 = Student('Иван','Иванов', 'Мужской')
student1.add_courses(['Python','Java'])
student1.courses_in_progress = ["Pascal", "Java Script"]

student2 = Student('Петр', 'Петров', 'Мужской')
student2.add_courses(['Python', 'Java'])
student2.courses_in_progress = ["Pascal", "Java Script"]

mentor1 = Reviewer('Федор', 'Добронравов')
mentor1.courses_attached = ['Java Script','Java']

mentor2 = Reviewer('Сергей', 'Лавров')
mentor2.courses_attached = ['Pascal','Python']

mentor3 = Lecturer('Дмитрий', 'Нагиев')
mentor3.courses_attached = ['Python']

mentor4 = Lecturer('Владимир', 'Путин')
mentor4.courses_attached = ['Python','Java']

student1.rate_lecturer(mentor3, 'Python', 9)
student1.rate_lecturer(mentor4, 'Python', 10)
student1.rate_lecturer(mentor4, 'Java', 10)
student2.rate_lecturer(mentor3, 'Python', 10)
student2.rate_lecturer(mentor4, 'Python', 10)
student2.rate_lecturer(mentor4, 'Java', 10)

mentor1.rate_hw(student1, 'Java', 8)
mentor2.rate_hw(student1, 'Python', 10)
mentor1.rate_hw(student2, 'Java', 6)
mentor2.rate_hw(student2, 'Python', 8)

print(student1)
print(student2)
print(mentor3)
print(mentor4)
print(mentor1)
print(mentor2)

print()

print(mentor4>student1)

print()

middle_grade_student([student1, student2], 'Python')
print()
middle_rate_lecturer([mentor3,mentor4], 'Python')
