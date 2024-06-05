# print menu
#( as) for change
from data import student_grads as student_infos
# print ("Student Graduation:",student_infos)

# Function:print Men
def show_menu()-> None:
    """
    This function is used to print the menu
     ========|Menu|=======
    1. print all student")
    2. Print student with highest score
    3. Add new all student information
    4. Modify student score
    5. Count female and male student
    0. Exit
    """
    print("========|Menu|=======")
    print("1. print all student")
    print("2. Print student with highest score")
    print("3. Add new all student information")
    print("4. Modify student score")
    print("5. Count female and male student")
    print("0. Exit")

# Function: format header table
def table_header() ->None:
    id="ID"
    name="Name"
    gender="Gender (M/F)"
    math = "Math"
    physic = "Physic"
    chemistry = "Chemistry"
    total ="Total"
    avg ="Average"
    print(f"{id:<15} {name:<25} {gender:<15} {math:<10} {physic:<10}{chemistry:<15}{total:<15}{avg:<}")
# table_header()
# Function: Format student record
# (Id, Name, isMale score[math,physic,chemistry])
def table_record(student_intfo: tuple) -> None:
    id =student_intfo[0]
    name=student_intfo[1]
    isMale= "M" if student_intfo[2] else "F" 
    student_score=student_intfo[3]
    math=student_intfo[3] [0]
    physic=student_intfo[3][1]
    chemistry=student_intfo [3][2]
    # total=math+physic+chemistry
    # avg=total/3
    total=sum(student_score)
    avg=total/len(student_score)
    print(f"{id:<15} {name:<25} {isMale:<15} {math:<10} {physic:<10}{chemistry:<15}{total:<15}{avg:<10.2f}")
# table_record()
def print_all_student() -> None:
    table_header()
    for student_intfo in student_infos:
        table_record(student_intfo)
# print_all_student()

# find_max_score()
def find_max_score() -> tuple:
    max_score = 0
    max_student_info = None
    for student_info in student_infos:
        total_score = sum(student_info[3])
        if total_score > max_score:
            max_score = total_score
            max_student_info = student_info
    if max_student_info:
        print("Student with the highest score:")
        table_header()
        table_record(max_student_info)
    else:
        print("No student information found.")

# Function to add new student information
def add_new_student_info() -> None:
    """
    This function allows the user to add new student information
    """
    id = input("Enter student ID: ")
    name = input("Enter student name: ")
    gender = input("Enter student gender (M/F): ").upper() == 'M'
    math = float(input("Enter math score: "))
    physic = float(input("Enter physic score: "))
    chemistry = float(input("Enter chemistry score: "))
    student_infos.append((id, name, gender, (math, physic, chemistry)))
    print("Student information added successfully.")

def modify_student_score() -> None:
    
    """
    This function allows the user to modify a student's scores
    """
    student_id = input("Enter student ID whose score you want to modify: ")
    for student_info in student_infos:
        if student_info[0] == student_id:
            math = float(input("Enter new math score: "))
            physic = float(input("Enter new physic score: "))
            chemistry = float(input("Enter new chemistry score: "))
            student_info = (student_info[0], student_info[1], student_info[2], (math, physic, chemistry))
            print("Student score modified successfully.")
            return
    print("Student ID not found.")

def count_female_male_students() -> None:
    """
    This function counts the number of female and male students
    """
    female_count = sum(1 for student_info in student_infos if not student_info[2])
    male_count = len(student_infos) - female_count
    print(f"Number of female students: {female_count}")
    print(f"Number of male students: {male_count}")

def menu() -> None:
    """
    This function displays the menu and handles user input
    """
    while True:
        show_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            print_all_student()
        elif choice == '2':
            find_max_score()
        elif choice == '3':
            add_new_student_info()
        elif choice == '4':
            modify_student_score()
        elif choice == '5':
            count_female_male_students()
        elif choice == '0':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
menu()