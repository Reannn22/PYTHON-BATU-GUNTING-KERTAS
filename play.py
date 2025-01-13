import random

def playgame():
    choices = ["Batu", "Gunting", "Kertas"]
    botChoices = random.choice(choices)
    playerChoices = input("Masukkan Pilihan anda: ")
    print("Kamu memilih ", playerChoices)
    print("Bot memilih ", botChoices)

    if botChoices == playerChoices:
        print("Hasilnya seri!")
    elif (botChoices == "Batu" and playerChoices == "Gunting") or (botChoices == "Kertas" and playerChoices == "Batu"):
        print("Kamu kalah!")
    else:
        print("Kamu menang")

playgame()

player_life = 3
bot_life = 3

while player_life > 0 and bot_life > 0:
    choices = ["Batu", "Gunting", "Kertas"]
    botChoices = random.choice(choices)
    playerChoices = input("Masukkan Pilihan anda: ")
    print("Kamu memilih ", playerChoices)
    print("Bot memilih ", botChoices)

    if botChoices == playerChoices:
        print("Hasilnya seri!")
    elif (botChoices == "Batu" and playerChoices == "Gunting") or (botChoices == "Kertas" and playerChoices == "Batu"):
        print("Kamu kalah!")
        player_life -= 1
    else:
        print("Kamu menang")
        bot_life -= 1

    print(f"Nyawa player: {player_life}")
    print(f"Nyawa bot: {bot_life}")

if player_life == 0:
    print("Bot menang!")
else:
    print("Player menang!")