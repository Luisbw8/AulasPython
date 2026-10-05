n1 = float(input("informe a 1 nota: "));
n2 = float(input("Informe a 2 nota: "));

media = (n1+n2) / 2;

if(media >= 6):
    print("Aluno Aprovado!!"+ "\n media: "+ str(round(media, 2)));
else:
    print("Aluno Reprovado!!"+ "\n media: "+ str(round(media, 2)));
