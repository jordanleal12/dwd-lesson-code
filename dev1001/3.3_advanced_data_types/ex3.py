# Sets Exercise

required_skills = {"python", "git", "problem-solving"}
candidate_skills = {"python", "java", "communication"}

# Given the above sets, write code to:
# 1. Add "communication" to required_skills if it's not already there.
# 2. Find out which skills the candidate has that are also required.
# 3. Find out all unique skills possessed by either (required or candidate).
# 4. Which skills are required but the candidate doesn't have.

#1 
required_skills.add("communication")
print(required_skills)
#2 
common = required_skills & candidate_skills
print(common)
#3 
