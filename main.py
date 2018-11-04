from parking import Parking as Park
import os

# URLs to datasets needed
URL_P_INFO = "https://raw.githubusercontent.com/rmlassesen/dataset/master/p_pladser.csv"
URL_SOCECO = "https://raw.githubusercontent.com/rmlassesen/dataset/master/indkomstbruttohustype.csv"

prk = Park(URL_P_INFO, URL_SOCECO)

ANSWER = ""

TITLE = '''
#############################################################################
#                                                                           #
#                      PARKING SPACES IN COPENHAGEN                         #
#                                                                           #
#############################################################################
'''

QUESTIONS = {
    1: ["How many parking spaces exist in the area 'Indre By' in CPH? Which road has the most?", prk.number_of_p_spaces],
    2: ["Does CPH have more parking spaces on the side of odd or equal house numbers?\n\t - i. Which side has the most marked spaces?", prk.p_spaces_odd_even],
    3: ["Show a bar-stack plot of the distributions(in %) of private and public parking spaces for each area in CPH.", prk.public_private_distro],
    4: ["Which family-constellation has the best parking opportunities?", prk.best_parking ],
    5: ["Show the distribution of private parking spaces and spaces for electric cars compared to each areas net income pr. capita.", prk.private_electric_income],
    6: ["Colorcode a map of the areas of CPH according to the net income, and plot markers with private(P) and electric(EL) car parking spaces", prk.income_map]
}

def giveAnswer(ans):
    global ANSWER
    os.system('clear')
    num_q = len(QUESTIONS)

    try:
        ans =int(ans)

    except ValueError:
        ANSWER = "Invalid value entered - not a number"
        return False

    if ans < 1 or ans > num_q:
        ANSWER = "Entered value out of range (1-" + str(num_q) + ")"
        return False

    ANSWER = QUESTIONS[ans][1]()

def inputQuestion(q):
    global ANSWER
    os.system('clear')

    print(TITLE)

    for k, v in QUESTIONS.items():
        print(k,"-", v[0])

    if ANSWER != "":
        print("\n", ANSWER)

    print("")
    ans = input(q)
    return ans

if __name__ == '__main__':

    # Prompt for answers, please.

    while True:
        question = inputQuestion("Select a question - Enter/'blank' quits: ")
        if len(question) > 0:
            giveAnswer(question)
        else:
            break