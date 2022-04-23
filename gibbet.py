import requests

word = requests.get('https://api.dicionario-aberto.net/random').json()['word']

word_complete = []

chances = 10

print ("=======> Jogo de Forca <=======")
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

    if chances == 9:
        print("  ===> FORCA <=== ")
        print("  _______         ")
        print(" |       |       |")
        print(" |               |")
        print(" |               |")
        print(" |               |")
        print(" |               |")
    if chances == 8:
        print("  ===> FORCA <=== ")
        print("  _______         ")
        print(" |       |       |")
        print(" |      (_)      |")
        print(" |               |")
        print(" |               |")
        print(" |               |")
    if chances == 7:
        print("  ===> FORCA <=== ")
        print("  _______         ")
        print(" |       |       |")
        print(" |      (_)      |")
        print(" |       |       |")
        print(" |               |")
        print(" |               |")
    if chances == 6:
        print("  ===> FORCA <=== ")
        print("  _______         ")
        print(" |       |       |")
        print(" |      (_)      |")
        print(" |      \|       |")
        print(" |               |")
        print(" |               |")
    if chances == 5:
        print("  ===> FORCA <=== ")
        print("  _______         ")
        print(" |       |       |")
        print(" |      (_)      |")
        print(" |      \|/      |")
        print(" |               |")
        print(" |               |")
    if chances == 4:
        print("  ===> FORCA <=== ")
        print("  _______         ")
        print(" |       |       |")
        print(" |      (_)      |")
        print(" |      \|/      |")
        print(" |       |       |")
        print(" |               |")
    if chances == 3:
        print("  ===> FORCA <=== ")
        print("  _______         ")
        print(" |       |       |")
        print(" |      (_)      |")
        print(" |      \|/      |")
        print(" |       |       |")
        print(" |      /        |")
    if chances == 2:
        print("  ===> FORCA <=== ")
        print("  _______         ")
        print(" |       |       |")
        print(" |      (_)      |")
        print(" |      \|/      |")
        print(" |       |       |")
        print(" |      / \      |")
    if chances == 1:
        print("  ===> FORCA <=== ")
        print("  _______         ")
        print(" |       |       |")
        print(" |   ___(_)___   |")
        print(" |      \|/      |")
        print(" |       |       |")
        print(" |      / \      |")

    if chances == 0:
        print("VOCÊ FOI ENFORCADO !!!!!!!!!!")
        print("    _______________         ")
        print("   /               \       ")
        print("  /                 \      ")
        print("//                   \/\  ")
        print("\|   XXXX     XXXX   | /   ")
        print(" |   XXXX     XXXX   |/     ")
        print(" |   XXX       XXX   |      ")
        print(" |                   |      ")
        print(" \__      XXX      __/     ")
        print("   |\     XXX     /|       ")
        print("   | |           | |        ")
        print("   | I I I I I I I |        ")
        print("   |  I I I I I I  |        ")
        print("   \_             _/       ")
        print("     \_         _/         ")
        print("       \_______/           ")
        print("                           ")
        print (f"A palavra secreta era: {word}")
        break

    
