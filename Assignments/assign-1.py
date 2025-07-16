print("Welcome to Duolingo Learning Info System\n")

# Task 1: Collect user language learning details
user_id = int(input("Enter User ID: "))
user_name = input("Enter User Name: ")
learning_language = input("Enter Language Being Learned: ")
progress_percentage = float(input("Enter Overall Progress Percentage: "))

topics_input = input("Enter Topics Covered (comma-separated): ")
topics_covered = topics_input.split(',')

daily_goal_minutes = int(input("Enter Daily Goal (in minutes): "))
days_completed = int(input("Enter Days Completed: "))
learning_streak = (daily_goal_minutes, days_completed)

score = float(input("Enter Last Quiz Score (out of 100): "))

skills_input = input("Enter Unlocked Skills (comma-separated): ")
unlocked_skills = set(skills_input.split(','))

profile_name = input("Enter Profile Name: ")
profile_email = input("Enter Email ID: ")
profile_country = input("Enter Country: ")
user_profile = {
    "name": profile_name,
    "email": profile_email,
    "country": profile_country
}

print("\n--- Duolingo Learning Details ---")

# Task 2: Display using different formatting methods

# 1. Comma Separation (sep=',')
print("User ID, Name, Language:", user_id, user_name, learning_language, sep=',')

# 2. Percentage Formatting (% operator)
print("Progress: %.2f%%" % progress_percentage)

# 3. f-strings
print(f"User: {user_name}")
print(f"Learning: {learning_language}")
print(f"Daily Goal: {learning_streak[0]} minutes, Days Completed: {learning_streak[1]} days")
print(f"Last Quiz Score: {score}/100")
print(f"Topics Covered: {', '.join(topics_covered)}")
print(f"Unlocked Skills: {', '.join(unlocked_skills)}")

# 4. .format() method
print("Profile Info: Name - {}, Email - {}, Country - {}".format(
    user_profile["name"],
    user_profile["email"],
    user_profile["country"]
))

#
'''
Enter User ID: 101
Enter User Name: Vaishnavi
Enter Language Being Learned: Spanish
Enter Overall Progress Percentage: 75.5
Enter Topics Covered (comma-separated): Basics, Greetings, Food, Travel
Enter Daily Goal (in minutes): 20
Enter Days Completed: 45
Enter Last Quiz Score (out of 100): 88.75
Enter Unlocked Skills (comma-separated): Grammar, Listening, Speaking
Enter Profile Name: Vaishnavi Thandu
Enter Email ID: vaishnavi@gmail.com
Enter Country: India

--- Duolingo Learning Details ---
User ID, Name, Language:,2001,Vaishnavi,Spanish
Progress: 80.50%
User: Vaishnavi
Learning: Spanish
Daily Goal: 20 minutes, Days Completed: 45 days
Last Quiz Score: 88.75/100
Topics Covered: Basics,  Greetings,  Food,  Travel      
Unlocked Skills:  Listening,  Speaking, Grammar
Profile Info: Name - Vaishnavi Thandu, Email - vaishnavi@gmail.com, Country - India

'''#