for i in range(1, 101):
    num = str(i)
    clap_count = num.count('3') + num.count('6') + num.count('9')

    if clap_count > 0:
        print("짝" * clap_count + "!")
    else:
        print(i)