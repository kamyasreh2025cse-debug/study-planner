subjects = []
hours = []

n = int(input("Enter number of subjects: "))

for i in range(n):
    sub = input("Enter subject name: ")
    hr = int(input("Enter hours needed: "))
    subjects.append(sub)
    hours.append(hr)

print("\nYour Study Plan:")
for i in range(n):
    print(subjects[i], "->", hours[i], "hours")

print("\nFocus more on subjects with higher hours!")
