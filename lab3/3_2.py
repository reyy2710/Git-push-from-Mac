def student_details():
    num_students = int(input("Enter number of students: "))
    students = []

    for _ in range(num_students):
        name = input("Enter Name: ")
        roll_no = input("Enter Roll No: ")
        department = input("Enter Department: ")
        address = input("Enter Address: ")
        gender = input("Enter Gender: ")
        marks = list(map(int, input("Enter marks in 3 subjects (space-separated): ").split()))
        
        total = sum(marks)
        percentage = total / 3

        students.append({
            "Name": name,
            "Roll No": roll_no,
            "Department": department,
            "Address": address,
            "Gender": gender,
            "Marks": marks,
            "Total": total,
            "Percentage": percentage
        })

    max_student = max(students, key=lambda x: x["Total"])
    min_student = min(students, key=lambda x: x["Total"])
    failed_students = [s["Name"] for s in students if any(m < 10 for m in s["Marks"])]

    for s in students:
        print(f"\nStudent: {s['Name']}, Roll No: {s['Roll No']}, Total Marks: {s['Total']}, Percentage: {s['Percentage']:.2f}%")

    print(f"\nTop Scorer: {max_student['Name']} with {max_student['Total']} marks")
    print(f"Lowest Scorer: {min_student['Name']} with {min_student['Total']} marks")
    print(f"Failed Students: {', '.join(failed_students) if failed_students else 'None'}")

student_details()
