for i in range(1, 101):
    clap = sum(ch in '369' for ch in str(i))
    if clap > 0:
        print("짝" * clap)
    else:
        print(i)