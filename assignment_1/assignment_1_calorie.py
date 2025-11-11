# NAME : ROHIT RANJAN KUMAR 
# ROLL_NO:2501730113  
# DATE: 28/10/2025 
# PROJECT_TITLE: DAILY CALORIES TRACKER

import datetime
print("Welcome to calories tracker.")
print("This tool help you to track your daily calories , help you to log your meals,calculate total and average calories, and compare it to daily calorie limit ")

meals =[]
calories = []

num_meals = int(input("How many meals would you like to log today? "))

for i in range(num_meals):
    print(f"\nMeal{i+1}")
    meal_name = input("enter meal name: ")
    cal_amount = float(input("enter calorie amount: "))
    meals.append(meal_name)
    calories.append(cal_amount)

total_calories = sum(calories)
average_calories = total_calories/len(calories)

daily_limit = float(input("enter your daily calorie limit: "))

if total_calories > daily_limit :
    print("you have exceeded your daily limit!")
else:
    print("great! you are within your daily calorie limit.")

print("   calories report   ")
print(f"{'Meal Name':<15}{'Calories':>10}")

for i in range(len(meals)):
    print(f"{meals[i]:<15}{calories[i]:>10.2f}")

print(f"{'Total:':<15}{total_calories:>10.2f}")
print(f"{'Average:':<15}{average_calories:>10.2f}")   

save_choice = input("Would you like to save this report to a file? (yes/no): ").strip().lower()

if save_choice == "yes":
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"calorie_log_{timestamp}.txt"
    with open(filename, "w") as file:
        file.write("DAILY CALORIES REPORT\n")
        file.write(f"Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        file.write(f"{'Meal Name':<15}{'Calories':>10}\n")
      
        for i in range(len(meals)):
            file.write(f"{meals[i]:<15}{calories[i]:>10.2f}\n")
        file.write(f"   \n")
      
        file.write(f"{'Total:':<15}{total_calories:>10.2f}\n")
        file.write(f"{'Average:':<15}{average_calories:>10.2f}\n")
        file.write(f"\nDaily Calorie Limit: {daily_limit:.2f}\n")
        if total_calories > daily_limit:
            file.write("Exceeded daily limit \n")
        else:
            file.write(" Within daily limit \n")


    print(f"\n Report successfully saved as '{filename}'")
else:
    print("\nReport not saved. Have a great day!")

print("\nThank you for using the Daily Calorie Tracker!")
    

