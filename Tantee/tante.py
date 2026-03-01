import sys
import time

def jalan_lirik():
    lirik = [
        ("\033[34m Temanku semua pada jahat tante", 0.1),
        ("\033[31m aku lagi susah mereka gak ada", 0.1),
        ("\033[33m coba kalau lagi jayaaa", 0.1),
        ("\033[34m aku dipuja puja tante", 0.1),
        ("\033[31m sudah terbiasa terjadi tante", 0.1),
        ("\033[33m teman datang ketika lagi butuh saja", 0.1),
        ("\033[34m coba kalau lagi susahhhh", 0.1),
        ("\033[31m mereka semua menghilaaaaanggg", 0.1),
    ]

    delay = [1.1, 1.4, 1.3, 1.6, 1.25, 1.1, 1, 1.5, ]
    print("~TAANTEEEEEEEE~")
    time.sleep(3)
    for i, (baris_lagu, delay_char) in enumerate(lirik):
        for char in baris_lagu:
            print(char, end='')
            sys.stdout.flush()
            time.sleep(delay_char)
        time.sleep(delay[i])
        print('')

    print("// Code By Amad")

jalan_lirik()