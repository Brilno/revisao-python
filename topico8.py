nota = float(input("Digite a nota do aluno (0 a 10): "))

if nota < 0 or nota > 10:
    print("Nota inválida. Digite um valor entre 0 e 10.")
elif nota >= 9:
    print("Conceito: A")
elif nota >= 7:
    print("Conceito: B")
else:
    print("Conceito: C")
