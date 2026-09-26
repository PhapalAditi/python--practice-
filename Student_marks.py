student = {
    "name": "Aditi",
    "marks": 75,
    "branch": "AIML"
}

for key, value in student.items():
    if key == "marks":
        if value >= 40:
            print("Pass")
        else:
            print("Fail")
