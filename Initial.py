#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import List, Optional

class Student:
    def __init__(self, name: str, student_id: int):
        self.name = name
        self.id = student_id
        self.grades: List[float] = []

    def add_grade(self, grade: float) -> None:
        if 0.0 <= grade <= 100.0:
            self.grades.append(grade)
        else:
            print("Ошибка: оценка должна быть от 0 до 100!")

    def get_average(self) -> float:
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)

    def print_info(self) -> None:
        avg = self.get_average()
        print(f"ID: {self.id} | Имя: {self.name} | Средний балл: {avg:.2f} | Оценок: {len(self.grades)}")


class GradeBook:
    def __init__(self):
        self.students: List[Student] = []
        self.next_id = 1001

    def add_student(self, name: str) -> None:
        student = Student(name, self.next_id)
        self.students.append(student)
        print(f'Студент "{name}" добавлен с ID {self.next_id}')
        self.next_id += 1

    def find_student(self, student_id: int) -> Optional[Student]:
        for s in self.students:
            if s.id == student_id:
                return s
        return None

    def add_grade_to_student(self, student_id: int, grade: float) -> None:
        s = self.find_student(student_id)
        if s:
            s.add_grade(grade)
            print(f"Оценка {grade} добавлена студенту {s.name}")
        else:
            print(f"Студент с ID {student_id} не найден!")

    def show_all_students(self) -> None:
        if not self.students:
            print("Список студентов пуст.")
            return
        print("\n=== Список студентов ===")
        for s in self.students:
            s.print_info()
        print("========================")

    def show_student_details(self, student_id: int) -> None:
        s = self.find_student(student_id)
        if not s:
            print("Студент не найден!")
            return
        print("\n--- Детали студента ---")
        s.print_info()
        if s.grades:
            grades_str = ", ".join(str(g) for g in s.grades)
            print(f"Все оценки: {grades_str}")
        else:
            print("Оценок пока нет.")
        print("-----------------------")

    def remove_student(self, student_id: int) -> None:
        for i, s in enumerate(self.students):
            if s.id == student_id:
                print(f"Студент с ID {student_id} удалён.")
                del self.students[i]
                return
        print(f"Студент с ID {student_id} не найден.")

    def show_statistics(self) -> None:
        if not self.students:
            print("Нет данных для статистики.")
            return

        total_avg = 0.0
        count_with_grades = 0
        max_avg = -1.0
        min_avg = 101.0
        top_student = ""
        bottom_student = ""

        for s in self.students:
            if not s.grades:
                continue
            avg = s.get_average()
            total_avg += avg
            count_with_grades += 1
            if avg > max_avg:
                max_avg = avg
                top_student = s.name
            if avg < min_avg:
                min_avg = avg
                bottom_student = s.name

        print("\n=== Статистика ===")
        print(f"Всего студентов: {len(self.students)}")
        if count_with_grades > 0:
            print(f"Средний балл по группе: {total_avg / count_with_grades:.2f}")
            print(f"Лучший студент: {top_student} ({max_avg:.2f})")
            print(f"Студент с самым низким баллом: {bottom_student} ({min_avg:.2f})")
        else:
            print("У студентов пока нет оценок.")
        print("==================")


def print_menu() -> None:
    print("\n========== Электронный журнал ==========")
    print("1. Добавить студента")
    print("2. Добавить оценку студенту")
    print("3. Показать всех студентов")
    print("4. Показать детали студента")
    print("5. Удалить студента")
    print("6. Показать статистику")
    print("0. Выход")
    print("========================================")
    print("Выберите действие: ", end="")


def main() -> None:
    book = GradeBook()

    print("Добро пожаловать в простой электронный журнал студентов!")

    # Добавим несколько студентов для примера
    book.add_student("Иван Петров")
    book.add_student("Анна Сидорова")
    book.add_student("Алексей Козлов")
    book.add_grade_to_student(1001, 85.5)
    book.add_grade_to_student(1001, 90.0)
    book.add_grade_to_student(1002, 78.0)
    book.add_grade_to_student(1002, 82.5)
    book.add_grade_to_student(1002, 91.0)
    book.add_grade_to_student(1003, 95.0)

    while True:
        print_menu()
        try:
            choice = int(input())
        except ValueError:
            print("Неверный ввод! Введите число.")
            continue

        if choice == 1:
            name = input("Введите имя студента: ").strip()
            if name:
                book.add_student(name)
            else:
                print("Имя не может быть пустым.")
        elif choice == 2:
            try:
                student_id = int(input("Введите ID студента: "))
                grade = float(input("Введите оценку (0-100): "))
                book.add_grade_to_student(student_id, grade)
            except ValueError:
                print("Неверный ввод!")
        elif choice == 3:
            book.show_all_students()
        elif choice == 4:
            try:
                student_id = int(input("Введите ID студента: "))
                book.show_student_details(student_id)
            except ValueError:
                print("Неверный ввод!")
        elif choice == 5:
            try:
                student_id = int(input("Введите ID студента для удаления: "))
                book.remove_student(student_id)
            except ValueError:
                print("Неверный ввод!")
        elif choice == 6:
            book.show_statistics()
        elif choice == 0:
            print("До свидания!")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()
