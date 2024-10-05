# Média de notas dos alunos

grade1 = float(input()) # Recebe a primeira nota
grade2 = float(input()) # Recebe a segunda nota
grade3 = float(input()) # Recebe a terceira nota

average = ((grade1 * 2) + (grade2 * 3) + (grade3 * 5)) / (2 + 3 + 5) # Calcula a média

print(f"MEDIA = {average:.1f}") # Imprime o resultado da média
