while True:

    try:

        volume = float(input())
        diam = float(input())

        altura = (volume / (3.14 * ((diam/2)**2)))
        print("ALTURA = %.2f"%altura)
        area = (3.14 * ((diam/2)**2))
        print("AREA = %.2f"%area)

    except EOFError:
        break
