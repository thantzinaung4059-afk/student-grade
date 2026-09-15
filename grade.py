# Student Grade Program

name = input("Enter student name: ")
mark1 = float(input("Enter first subject mark: "))
mark2 = float(input("Enter second subject mark: "))


total_mark = mark1 + mark2
avg_mark = total_mark / 2


result = "Pass" if avg_mark >= 50 else "Fail"


print(f"Student Name: {name}")
print(f"Total Mark: {total_mark:.0f}")
print(f"Average Mark: {avg_mark:.0f}")
print(f"Result: {result}")









=======
print(f"Result: {result}")
>>>>>>> cb66e4dcd63a22a69931fc3fde2d6d7039adfbb5
