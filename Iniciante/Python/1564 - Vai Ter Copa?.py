while True:
    try:
        n = int(input())
        if n > 0:
            print("vai ter duas!")
        else:
            print("vai ter copa!")
    except EOFError:
        break
