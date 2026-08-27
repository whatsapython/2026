# Grade Calculator
# You are building this yourself. Cursor is only a coach. Of Course.

# Challenge 1 instructions are in the chat.
# Write your code below this line.

print("Hello")
print("I am a Grade Calculator")
name = input("Enter your name: ").strip()

if name == "":
    print("You did not enter a name.")
    name = input("Enter your name: ").strip()

print("Hello, " + name + "!")

weighted = int(input("Choose a number for weighted (1) and unweighted (2):".strip()))
if weighted != 1 and weighted != 2:
    print("Invalid choice. Please enter 1 or 2.")
    weighted = int(input("Choose a number for weighted (1) and unweighted (2):".strip()))

if weighted == 1:
    print("You chose weighted.")
    weighted_count = int(input("How many scores? ").strip())
    
    total_weighted_points = 0
    total_weights = 0
    
    for i in range(weighted_count):
        assignment_name = input(f"\nEnter the name of assignment {i+1} (e.g., test, quiz, HW): ").strip()
        score = float(input(f"Enter score for {assignment_name} (0-100): ").strip())
        while score < 0 or score > 100:
            print("Invalid score. Please enter a score between 0 and 100.")
            score = float(input(f"Enter score for {assignment_name} (0-100): ").strip())
        weight = float(input(f"Enter the weight for {assignment_name} (e.g., 50): ").strip())
        while weight <= 0:
            print("Weight must be greater than 0.")
            weight = float(input(f"Enter the weight for {assignment_name}: ").strip())
        total_weighted_points += score * weight
        total_weights += weight
    weighted_average = total_weighted_points / total_weights # I am going to be brutally honest, I had to ask Gemini for this code prompt, I was stuck for a while.
    
    print(f"\nyour weighted average is: {weighted_average:.2f}")
    if weighted_average >= 90:
        print("You got an A!")
    elif weighted_average >= 80:
        print("You got a B!")
    elif weighted_average >= 70:
        print("You got a C!")
    elif weighted_average >= 60:
        print("You got a D!")
    else:
        print("You got an F!")
elif weighted == 2:
    print("You chose unweighted.")
    unweighted_count = int(input("How many scores? ").strip())
    unweighted_scores = []
    for i in range(unweighted_count):
        unweighted_score = float(input("Enter a score: ").strip())
        while True:
            if unweighted_score < 0 or unweighted_score > 100:
                print("Invalid score. Please enter a score between 0 and 100.")
                unweighted_score = float(input("Enter a score: ").strip())
            else:
                break
        unweighted_scores.append(unweighted_score)
    unweighted_average = sum(unweighted_scores) / len(unweighted_scores)
    print(f"your unweighted average is: {unweighted_average:.2f}")
    if unweighted_average >= 90:
        print("You got an A!")
    elif unweighted_average >= 80:
        print("You got a B!")
    elif unweighted_average >= 70:
        print("You got a C!")
    elif unweighted_average >= 60:
        print("You got a D!")
    else:
        print("You got an F!")


else:
    print("Invalid choice. Please enter 1 or 2.")
