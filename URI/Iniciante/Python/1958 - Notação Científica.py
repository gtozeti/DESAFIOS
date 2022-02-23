n_ = input()

if n_ == '-0':
    print("-0.0000E+00")
else:
    n = float(n_)
    if n >= 0:
        print('+%.4E' %(n))
    else:
        print('%.4E' % (n))
