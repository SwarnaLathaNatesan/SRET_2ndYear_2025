# Dictionary to store student data
students = {
    "E0224018": "NALIN R",
    "E0224019": "AJAY ADHITHYAN V",
    "E0224020": "D VIJAY GANESH"
}

print("Students in dictionary:")
print(students)


students["E10"] = "Swarna"
#Mr/Ms Swarna
print("after update Students in dictionary:")
print(students)






print(hash("E10"))





# Searching for a student by ID
search_id = "E0224019"
if search_id in students:
    print(f"Student found: ID={search_id}, Name={students[search_id]}")
else:
    print(f"Student with ID {search_id} not found.")



for search_id in students:
    print(f"Student found: ID={search_id}, Name=Mr/Ms {students[search_id]}")





for search_id in students:
    students[search_id] = "Mr/Ms" + students[search_id]
