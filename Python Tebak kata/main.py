import random

#Tuple kata buat ditebak
Tuple = ("monyet", "ikan", "kuda", "zebra")

#Function untuk ngeprint
def mulai_game():
    print("Selamat datang di game tebak kata!")
    
def ingame():
     kata = random.choice(Tuple)
     while True:
        user = input("Masukkan nama hewan: ")
        if user == kata:  # Cek kesamaan, bukan sekadar ada di dalam
            print("Benar!")
            break
        else:
            print("Coba lagi")
   
mulai_game()

ingame()