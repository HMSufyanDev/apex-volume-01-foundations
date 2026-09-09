# Compare Your Skills

current_skills = {
    "Python",
    "Git",
    "GitHub",
    "JavaScript"
}

target_skills = {
    "Python",
    "Machine Learning",
    "Deep Learning",
    "FastAPI",
    "Git"
}

# Find:
# All unique skills
# Skills you already have that are also required
# Skills you still need to learn

unique_skills = current_skills | target_skills
print(unique_skills)

have_skill = current_skills & target_skills
print(have_skill)

need_learn = target_skills - current_skills
print(need_learn)


# -------------------------- Student Course Manager ------------------------
courses = (
    "Python",
    "JavaScript",
    "AI",
    "Web Development",
    "Cyber Security"
)

python_students = {
    "Sufyan",
    "Ali",
    "Ahmed",
    "Sara"
}

ai_students = {
    "Sufyan",
    "Ahmed",
    "Fatima",
    "Usman"
}

# Task 1: Display Available Courses
print ("Available Courses:")
print(f"1. {courses[0]}")
print(f"2. {courses[1]}")
print(f"3. {courses[2]}")
print(f"4. {courses[3]}")
print(f"5. {courses[4]}")

# Task 2: Tuple Practice
print(f"First course: {courses[0]}")
print(f"Last course: {courses[-1]}")
print(f"Total courses: {len(courses)}")
print(f"First 3 courses: {courses[:3]}")

# Task 3: Find Students in Both Courses
print(f"Students learning both Python and AI: {python_students & ai_students}")

# Task 4: Find All Unique Students
print(f"All unique students: {python_students | ai_students}")

# Task 5: Find Python-Only Students
print(f"Students who study Python but not AI: {python_students - ai_students}")

# Task 6: Check Student Enrollment
name = input("Enter student name: ").capitalize()
is_in_python = name in python_students
is_in_ai = name in ai_students

if is_in_python and is_in_ai:
    print(f"{name} is enrolled in: Python and AI")
elif is_in_python:
    print(f"{name} is enrolled in: Python")
elif is_in_ai:
    print(f"{name} is enrolled in: AI")
else:
    print(f"{name} is not enrolled")
