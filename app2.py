for i in range(1, 101):
<<<<<<< HEAD
    clap = sum(ch in '369' for ch in str(i))
    if clap > 0:
        print("짝" * clap)
=======
    num = str(i)
    clap_count = num.count('3') + num.count('6') + num.count('9')

    if clap_count > 0:
        print("짝" * clap_count + "!")
>>>>>>> 398b1ec99118454922f5ec3ba34671b263dc2644
    else:
        print(i)