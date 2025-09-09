# Dictionary to store student data
students = {
    "E0224018": "NALIN R",
    "E0224019": "AJAY ADHITHYAN V",
    "E0224020": "D VIJAY GANESH"
}

print("Students in dictionary:")
print(students)

# Searching for a student by ID
search_id = "E0224019"
if search_id in students:
    print(f"Student found: ID={search_id}, Name={students[search_id]}")
else:
    print(f"Student with ID {search_id} not found.")
