print("Hello, welcome to the student grade finder!")

grade_book = {"Maxien":72, "Krishna":2, "Samantha":80, "Prisha":74, "Viraaj":100}

grade = 0

for key in grade_book:
    grade = grade + grade_book[key]

average = grade/5

print(average)

print(f"{max(grade_book)}Is the one with the highest results.")
print(f"{min(grade_book)}Is the one with the lowest results.")

name = input("Whose score do you want to find out: ")

print(grade_book.get(f"{name} Is the score", "Not found, sorry"))