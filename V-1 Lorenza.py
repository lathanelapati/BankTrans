import sys
YR_LVL = range(9,14)
score = 0
opt_count = 0

#List of questions user will be asked
questions = {
    "What is the symbol of the first element in the periodic table?": "H",
    "What is the outermost shell of an atom called?": "Valence shell",
    "What is the neutral charge in the nucleus of an atom called?": "Neutron"
    }
#List of options user will be given to choose from
options =[
    ["K", "H", "Cl"],
    ["Out Shell", "Crust", "Valence shell"],
    ["Electron", "Proton", "Neutron"]
    ]
    
# Initial function
def welcome_user():
    play = input("Would you like to play the quiz? (Y/N) : ")
    if play.upper() == "Y":
        print("Welcome to the quiz!")
        print("These are the instructions:")
        print(" - Answer ALL questions\n - Choose from the multiple choices\n - If you get a question right, you earn a point\n")

        # Ask for user details
        def user_details():
            while True:
                name = input("Enter your name : ")
                if name.isalpha():
                    break
                else:
                    print("Invalid name. Please enter your name in letters.")
            while True:
                try:
                    yr_lvl = int(input("Enter your year level : "))
                except ValueError:
                     print("Invalid year level. Please enter your year level in integers.")
                     continue
                if yr_lvl not in YR_LVL:
                    sys.exit("You are not eligible to partake in the quiz. \nThis quiz is only for students in year 9 to year 13. Try again later.")
                else:
                    break
        
            return name
        name = user_details()
        
        # Main quiz loop
        def main_quiz():
            global score
            global opt_count
            
            for k, v in questions.items():
                print(f"\nQuestion: {k}")
                option = options[opt_count]
                print(f"Choices: {option}")
                user_ans = input("Your answer : ")
                if user_ans.upper() == v.upper():
                    print("Correct!")
                    score+=1
                    opt_count+=1
                else:
                    print(f"Incorrect, the correct answer was {v}.\n")
                    opt_count+=1       
        main_quiz()
        
        # Display user's score
        def display_score():  
            total_questions = len(questions)
            percent = 100*score / total_questions
            print(f"Quiz completed!\n{name}'s score: {percent :.2f}%")
        display_score()
    else:
        sys.exit("Thank you, you may try again later.")

welcome_user()


