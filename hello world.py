"""
FLL Python Basics (FFLL-2025)
This file teaches beginner Python concepts with simple examples.
"""

# 1) Printing text
print("Hello, FLL students!")

# 2) Variables and data types
team_name = "Robo Builders"   # string (text)
team_number = 2025            # integer (whole number)
score = 9.5                   # float (decimal number)
is_ready = True               # boolean (True or False)

print("Team:", team_name)
print("Team number:", team_number)
print("Practice score:", score)
print("Ready for challenge?", is_ready)

# 3) Basic math
missions_completed = 3
points_per_mission = 20
total_points = missions_completed * points_per_mission
print("Total points:", total_points)

# 4) if / else decisions
if total_points >= 60:
    print("Great work! You reached your points goal.")
else:
    print("Keep practicing to reach your points goal.")

# 5) Loops (repeat actions)
print("Robot checks:")
for check in range(1, 4):
    print("Check", check, "complete")

# 6) Functions (reusable code blocks)
def celebrate(team):
    print("Nice job,", team + "!")

celebrate(team_name)
