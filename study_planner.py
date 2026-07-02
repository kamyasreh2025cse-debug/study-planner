subjects = []
hours = []

n = int(input("Enter number of subjects: "))

for i in range(n):
    sub = input("Enter subject name: ")
    hr = int(input("Enter hours needed: "))
    subjects.append(sub)
    hours.append(hr)

# Combine and sort subjects based on hours (priority)
combined = list(zip(subjects, hours))
combined.sort(key=lambda x: x[1], reverse=True)

print("\n📚 Optimized Study Plan:")
total_hours = 0

for sub, hr in combined:
    print(sub, "->", hr, "hours")
    total_hours += hr

print("\nTotal study time:", total_hours, "hours")

if total_hours > 6:
    print("⚠️ Take breaks between study sessions!")
else:
    print("✅ Manageable schedule, stay consistent!")
