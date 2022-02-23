A_1,B_1,C_1,D_1 = input().split(" ")

N1 = float(A_1)
N2 = float(B_1)
N3 = float(C_1)
N4 = float(D_1)

media = ((N1*2)+(N2*3)+(N3*4)+(N4*1))/10
media2=0

print ("Media: %.1f"%(media))

if media >= 7.0:
    print ("Aluno aprovado.")
elif media < 5.0:
    print ("Aluno reprovado.")
else:
        print ("Aluno em exame.")
        Ne = float(input())
        print ("Nota do exame: %.1f"%(Ne))
        media2 = (Ne + media)/2
        if media2 >= 5.0:
                print ("Aluno aprovado.")
                print ("Media final: %.1f"%(media2))
        else:
                print ("Aluno reprovado.")
                print ("Media final: %.1f"%(media2))
