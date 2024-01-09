import random
import time

class MurakkabIlonOyini:
    def __init__(self, daraja):
        self.daraja = daraja
        self.ilon = random.randint(1, daraja**2)
        self.kiritilgan_soni = 0

    def oyna(self):
        while True:
            taxmin = int(input(f"1 dan {self.daraja**2} gacha son kiriting: "))
            self.kiritilgan_soni += 1

            if taxmin < 1 or taxmin > self.daraja**2:
                print("Noto'g'ri son kiritdingiz. Qaytadan urinib ko'ring.")
                continue

            if taxmin < self.ilon:
                print("Katta son kiriting.")
            elif taxmin > self.ilon:
                print("Kichik son kiriting.")
            else:
                print(f"Tabriklaymiz! Siz {self.kiritilgan_soni} urinishda to'g'ri javob topdingiz.")
                break

if __name__ == "__main__":
    daraja = int(input("Ilonning darajasini kiriting (3, 4, 5, ...): "))
    oyin = MurakkabIlonOyini(daraja)
    print(f"Men 1 dan {daraja**2} gacha son o'yladim. Topa olasizmi?")
    time.sleep(1)
    oyin.oyna()


















