#!/bash/bin
task = input("Enter your task: ")
priority = input("Priority(high/medium/low): ")
time_bound = input("Is it time-bound? (Yes/no): ")

match priority:
    case "high":
        if time_bound == "yes":
            reminder = (f"{task} is a high priority task that requires immediate attention today!")
        else:
            reminder =  (f"{task} is a high priority task")

    case "medium":
        reminder = (f"{task} is a medium priority task")
    case "low":
        if time_bound == "yes":
            reminder = (f"{task} is a low priority task but requires attention.")
        else:
            reminder = (f"{task} is a low priority task.Consider completing it when you have free time")
print("Reminder:", reminder)