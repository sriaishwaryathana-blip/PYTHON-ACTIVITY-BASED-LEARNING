# Examination Result and Grace-Mark Validation
marks = int(input("Enter your marks: "))
if marks >= 35:
    print("Result: Pass")
elif marks >= 30:
    marks = marks + 5
    if marks >= 35:
        print("Result: Pass with grace marks")
    else:
        print("Result: Fail")
else:
    print("Result: Fail")

print("Final Marks:", marks)
