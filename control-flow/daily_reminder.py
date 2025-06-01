print("📝 Daily Task Reminder")

while True:
    task = input("Enter your task: ").strip()
    priority = input("Priority (high/medium/low): ").strip().lower()
    time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

    if priority in ("high", "medium", "low") and time_bound in ("yes", "no"):
        break
    else:
        print("Invalid input. Please enter correct values for priority and time-bound.")

match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
    case "medium":
        reminder = f"'{task}' is a medium priority task"
    case "low":
        reminder = f"'{task}' is a low priority task"
    case _:
        reminder = f"'{task}' has an unknown priority"

if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    reminder += ". Consider completing it when you have free time."

print("\nReminder:", reminder)

# End message
print("✅ Well done on completing this project! Let the world hear about this milestone achieved.")