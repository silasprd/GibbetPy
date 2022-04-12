import requests

word = requests.get('https://api.dicionario-aberto.net/random').json()['word']

word_complete = []

chances = 10

print ("=======> Gibbet Game <=======")
print (" ")


while True:

    letter = str(input('Digite uma letra: '))

    if len(letter) > 1:
        print("Permitido somente uma letra por vez.")
        continue

    word_complete.append(letter)
 
    word_check = ''

    for letter_check in word:
        if letter_check in word_complete:
            word_check += letter_check
        else:
            word_check += '*'

    
    if word_check == word:
        print ("Parabéns, você escapou da forca!!!")
        print (f"A palavra era: {word}")
        break
    else:
        print (f'Palavra secreta: {word_check}')

    if letter not in word:
        chances -= 1

    if chances <= 0:
        print ("Você foi enforcado!!!!")
        break

    print(f'Chances restantes: {chances}')
    




