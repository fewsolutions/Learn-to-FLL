"""
FLL Python Basics (FFLL-2025)
This file teaches beginner Python concepts with simple examples.
"""

# 1) Printing text
# print(...) means: show words/numbers on the screen.
print("Hello, FLL students!")

# 2) Variables and data types
# variable_name = value means: store a value so we can use it later.
team_name = "Robo Builders"   # string = text in quotes
team_number = 2025            # integer = whole number
score = 9.5                   # float = decimal number
is_ready = True               # boolean = True or False

print("Team:", team_name)
print("Team number:", team_number)
print("Practice score:", score)
print("Ready for challenge?", is_ready)

# 3) Basic math
# * means multiply.
missions_completed = 3
points_per_mission = 20
total_points = missions_completed * points_per_mission
print("Total points:", total_points)

# 4) if / else decisions
# if means "do this when the condition is True".
# else means "do this when the condition is False".
if total_points >= 60:
    print("Great work! You reached your points goal.")
else:
    print("Keep practicing to reach your points goal.")

# 5) Loops (repeat actions)
# for ... in range(1, 4): means repeat with values 1, 2, and 3.
print("Robot checks:")
for check in range(1, 4):
    print("Check", check, "complete")

# 6) Functions (reusable code blocks)
# def celebrate(team): means "define a function named celebrate with one input called team".
# The indented line below is the code that runs when the function is called.
def celebrate(team):
    print("Nice job,", team + "!")

# celebrate(team_name) means "call/run the function using team_name as the input".
celebrate(team_name)
