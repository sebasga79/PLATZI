import csv

# Abrimos el archivo CSV de verbos irregulares en una lista de diccionarios

verbs = []
try:
    with open('./verbs/irregular_verbs.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        for row in reader:
            verbs.append(row)
except FileNotFoundError:
    print("Error: CSV file not found")
except Exception as e:
    print("Error:", e)

if not verbs:
    print("Error: No verbs found in CSV file")
    exit()

# Definimos la función

def irregular_verbs_game():
    import random
    score = 0
    for i in range(10):
        verb = random.choice(verbs)
        base_form = verb['BASE FORM']
        past_simple = verb['PAST SIMPLE']
        past_participle = verb['PAST PARTICIPLE']
        print(f"What is the past simple and past participle of {base_form}?")
        user_past_simple = input("Past simple: ")
        user_past_participle = input("Past participle: ")
        if user_past_simple.lower() == past_simple and user_past_participle.lower() == past_participle:
            print("Correct!")
            score += 1
        else:
            print(f"Sorry, the correct answer is {past_simple} / {past_participle}")
    print(f"Your final score is {score}/10")

# Llamamos la función del juego

irregular_verbs_game()

