students = ["Айзере", "Әдемі", "Сабина"]

def show_students():
    print("Студенттер:")
    for student in students:
        print(student)

print("6 тапсырма өзгерістер")



def search_student(name):
    if name in students:
        print("Студент табылды:", name)
    else:
        print("Студент табылмады")


def add_student(name):
    students.append(name)
    print("Жаңа студент қосылды:", name)

add_student("Дамир")
show_students()

# show_students()
# search_student("Айзере")