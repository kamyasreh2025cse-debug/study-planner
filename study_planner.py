subjects = []
hours = []
priority = []

n = int(input("Enter number of subjects: "))

for i in range(n):
    sub = input("Enter subject name: ")
    hr = int(input("Enter hours needed: "))
    pr = input("Enter priority (High/Medium/Low): ")

    subjects.append(sub)
    hours.append(hr)
    priority.append(pr)

# Combine all data
combined = list(zip(subjects, hours, priority))

# Sort by hours (priority of study time)
combined.sort(key=lambda x: x[1], reverse=True)

print("\n📚 Optimized Study Plan:")
total_hours = 0

for sub, hr, pr in combined:
    print(sub, "->", hr, "hours | Priority:", pr)
    total_hours += hr

print("\nTotal study time:", total_hours, "hours")

if total_hours > 6:
    print("⚠️ Take breaks between study sessions!")
else:
    print("✅ Manageable schedule, stay consistent!")
