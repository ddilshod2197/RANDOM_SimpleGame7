import random
import time

def bomb_game_timer():
    bomba = random.randint(1, 9)

    print("🎮 Bombani top o‘yini (Timer bilan)")
    print("1-9 oralig‘ida bomba bor.")
    print("Sizda 7 soniya vaqt bor!")

    start_time = time.time()

    try:
        tanlov = int(input("Son kiriting (1-9): "))
    except:
        print("Noto‘g‘ri kiritish!")
        return

    end_time = time.time()
    ketgan_vaqt = end_time - start_time

    print(f"⏳ Ketgan vaqt: {round(ketgan_vaqt, 2)} soniya")

    if ketgan_vaqt > 7:
        print("⌛ Vaqt tugadi! Yutqazdingiz!")
        print("Bomba:", bomba)
    elif tanlov == bomba:
        print("💥 Boom! Bombani topdingiz. Yutqazdingiz!")
    else:
        print("🎉 Tabriklaymiz! Siz yutdingiz!")
        print("Bomba:", bomba)

bomb_game_timer()
