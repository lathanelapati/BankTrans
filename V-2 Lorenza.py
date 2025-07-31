import sys
import easygui

# Valid year levels
YR_LVL = range(9, 14)
    
# Questions and answers
questions = {
    "What is the symbol of the first element in the periodic table?": "H",
    "What is the outermost shell of an atom called?": "Valence shell",
    "What is the neutral charge in the nucleus of an atom called?": "Neutron"
}
    
# Multiple choice options
options = [
    ["K", "H", "Cl"],
    ["Out Shell", "Crust", "Valence shell"],
    ["Electron", "Proton", "Neutron"]
]

    
# Ask for user details
def ask_user_details():
    while True:
        name = easygui.enterbox("Enter your name: ")
        if name is None:
            easygui.msgbox("Thank you, you may try again later.")
            sys.exit()
        elif name.isalpha():
            break
        else:
            easygui.msgbox("Invalid name. Please enter your name in letters.")
    
    while True:
        year_level = easygui.enterbox("Enter your year level: ")
        if year_level is None:
            easygui.msgbox("Thank you, you may try again later.")
            sys.exit()
        elif year_level.isnumeric():
            year_level = int(year_level)
            if year_level in YR_LVL:
                break
            else:
                easygui.msgbox("You are not eligible to partake in the quiz.\nYour year level is not between 9 to 13. Try again later.")
                sys.exit()
        else:
            easygui.msgbox("Invalid year level. Please enter your year level in integers.")
    return name


# Main quiz loop
def main_quiz_loop():
    score = 0
    opt_count = 0

    for k, v in questions.items():
        user_answer = easygui.buttonbox(f"\nQuestion: {k}", choices = options[opt_count])
        if user_answer is None:
            easygui.msgbox("Thank you for playing, you may try again later.")
            sys.exit()
        elif user_answer == v:
            easygui.msgbox("Correct!")
            score += 1
        else:
            easygui.msgbox(f"Incorrect. The correct answer was {v}.")
    
        opt_count += 1

    return score


# Display user's score
def display_score(score, name):
    total_questions = len(questions)
    score_percent = 100 * score / total_questions
    easygui.msgbox(f"\nQuiz completed!\n{name}'s score: {score_percent:.2f}%")


# Ask user if they want to replay
def replay_quiz():
    replay = easygui.buttonbox("Would you like to restart the quiz?", choices = ("Yes", "No"))
    if replay == "Yes":
        easygui.msgbox("THE QUIZ WILL NOW RESTART")
        welcome_user()
    else:
        easygui.msgbox("Thank you for playing, you may try again later.")
        sys.exit()
        
# Initial function
def welcome_user():
    play = easygui.buttonbox("Would you like to play the quiz?", choices = ("Yes", "No"))
    
    if play == "Yes":
        easygui.msgbox("\nWelcome to the quiz!")
        easygui.msgbox("These are the instructions:\n- Answer ALL questions\n- Choose from the multiple choices\n- If you get a question right, you earn a point\n")

        name = ask_user_details()
        score = main_quiz_loop()
        display_score(score, name)
        replay_quiz()
        
    else:
        easygui.msgbox("Thank you, you may try again later.")
        sys.exit()


# Start the program
welcome_user()



