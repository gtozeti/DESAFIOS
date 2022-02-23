x = float(input())

intervalos1= ['[0,25]','(25,50]','(50,75]','(75,100]']

if x >= 0 and x <= 25:

    print ("Intervalo %s"%(intervalos1[0]))

elif x > 25 and x <= 50:

    print ("Intervalo %s"%(intervalos1[1]))

elif x > 50 and x <= 75:

    print ("Intervalo %s"%(intervalos1[2]))

elif x > 75 and x <= 100:

    print ("Intervalo %s"%(intervalos1[3]))

else:
    print ("Fora de intervalo")
