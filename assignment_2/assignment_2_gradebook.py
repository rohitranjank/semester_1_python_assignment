# NAME : ROHIT RANJAN KUMAR 
# ROLL_NO:2501730113  
# DATE: 5/11/2025 
# PROJECT_TITLE:GRADEBOOK ANALYZER

import csv
import statistics

def print_menu():
    print("1. Enter student marks manually")
    print("2. Load student marks from CSV file")
    print("3. Exit\n")


def welcome_message():
    print("     Welcome to the Gradebook Analyzer!")
    print("This program helps you manage and analyze student grades.\n")


def manual_entry():
    marks = {}
    while True:
        name = input("Enter student name (or 'done' to finish): ").strip()
        if name.lower() == 'done':
            break
        try:
            score = float(input(f"Enter marks for {name}: "))
            marks[name] = score
        except ValueError:
            print("Invalid input! Please enter a number for marks.")
    return marks


def csv_import():
    marks = {}
    filename = input("Enter CSV filename (e.g., data.csv): ").strip()
    try:
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                if len(row) >= 2:
                    name, score = row[0], float(row[1])
                    marks[name] = score
        print("CSV data loaded successfully!")
    except FileNotFoundError:
        print("File not found! Please check the filename and try again.")
    except Exception as e:
        print(f"Error loading CSV: {e}")
    return marks


def calculate_average(marks_dict):
    return sum(marks_dict.values()) / len(marks_dict) if marks_dict else 0

def calculate_median(marks_dict):
    return statistics.median(marks_dict.values()) if marks_dict else 0

def find_max_score(marks_dict):
    return max(marks_dict.items(), key=lambda x: x[1]) if marks_dict else ("N/A", 0)

def find_min_score(marks_dict):
    return min(marks_dict.items(), key=lambda x: x[1]) if marks_dict else ("N/A", 0)


def assign_grades(marks_dict):
    grades = {}
    for name, score in marks_dict.items():
        if score >= 90:
            grade = "A"
        elif score >= 80:
            grade = "B"
        elif score >= 70:
            grade = "C"
        elif score >= 60:
            grade = "D"
        else:
            grade = "F"
        grades[name] = grade
    return grades


def grade_distribution(grades):
    distribution = {g: 0 for g in ['A', 'B', 'C', 'D', 'F']}
    for grade in grades.values():
        if grade in distribution:
            distribution[grade] += 1
    return distribution


def pass_fail_lists(marks_dict):
    passed = [name for name, score in marks_dict.items() if score >= 40]
    failed = [name for name, score in marks_dict.items() if score < 40]
    return passed, failed


def display_table(marks, grades):
    print("\nName\t\tMarks\tGrade")
    print("-" * 40)
    for name in marks:
        print(f"{name:<15}\t{marks[name]:<7.2f}\t{grades[name]}")
    print("-" * 40)


def main():
    welcome_message()

    while True:
        print_menu()
        choice = input("Choose an option (1/2/3): ").strip()

        if choice == '1':
            marks = manual_entry()
        elif choice == '2':
            marks = csv_import()
        elif choice == '3':
            print("Goodbye! ")
            break
        else:
            print("Invalid choice! Try again.")
            continue

        if not marks:
            print("No data available to analyze.")
            continue

      
        avg = calculate_average(marks)
        med = calculate_median(marks)
        top_student, top_score = find_max_score(marks)
        low_student, low_score = find_min_score(marks)

        print("\n===== Analysis Summary =====")
        print(f"Average Score: {avg:.2f}")
        print(f"Median Score:  {med:.2f}")
        print(f"Highest: {top_student} ({top_score})")
        print(f"Lowest:  {low_student} ({low_score})")

        
        grades = assign_grades(marks)
        distribution = grade_distribution(grades)

        print("\nGrade Distribution:")
        for g, count in distribution.items():
            print(f"{g}: {count} student(s)")

        
        passed, failed = pass_fail_lists(marks)
        print(f"\nPassed ({len(passed)}): {', '.join(passed) if passed else 'None'}")
        print(f"Failed ({len(failed)}): {', '.join(failed) if failed else 'None'}")

        
        display_table(marks, grades)

        again = input("\nWould you like to analyze another dataset? (y/n): ").strip().lower()
        if again != 'y':
            print("Exiting program. Have a great day!")
            break


if __name__ == "__main__":
    main()
