# Tuples Exercise

# Student Info: (ID, Name, Major)
student_record = (101, "Alice Wonderland", "Computer Science")

# 1. Access and print the student's name.
# 2. Create a new tuple that includes the student's current term.
#       Remember, tuples are immutable, so you'll create a NEW one.
#       Hint: You can concatenate tuples using '+'
#       (Challenge) Use unpack operator instead of concatenation.
# 3. Unpack the original student_record into three separate variables.
# 4. Use the slice operator to extract the student name only.

print(student_record[1])

new_student_record = student_record + ("term three", )
print(new_student_record)

number, name, student_class = student_record

print(student_record[1]) 