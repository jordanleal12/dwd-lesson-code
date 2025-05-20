# --- USE: Grade Assigner ---

def score_function(score):
    honors = False
    if score >= 93:
        grade = "A"
        honors = True
    elif score >= 87:
        grade = "B+"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    elif score < 60:
        grade = "F"
    else: 
        grade = "Error in grading"
    passing = False if grade == "F" else True
    return honors, grade, passing

has_honors, letter_grade, is_passing = score_function(88)

print(f"Letter Grade: {letter_grade}")
if has_honors:
    print("Congratulations on achieving honors!")
if not is_passing and letter_grade == "F": # Example of 'or' could be: if score < 0 or score > 100: print("Invalid score")
    print("Student needs to retake the course.")

if letter_grade == "A" or letter_grade == "B+":
    print("Eligible for scholarship consideration")