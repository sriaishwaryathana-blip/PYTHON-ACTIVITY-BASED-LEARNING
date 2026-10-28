# Attendance Recovery Computation
total_classes = int(input("Enter total classes: "))
attended = int(input("Enter classes attended: "))
attendance = (attended / total_classes) * 100
print("Attendance Percentage:", attendance)
if attendance >= 75:
    print("Attendance is sufficient")
else:
    required = (0.75 * total_classes - attended) / 0.25
    print("Attendance is below 75%")
    print("More classes to attend:", int(required) + (required % 1 > 0))