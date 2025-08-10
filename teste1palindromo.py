# script para verificar se uma palavra é ou não um palíndromo:
# pode-se ler da esquerda para a direita e vice-e-versa igualmente.

def um_palindromo(palavra):
    palavra=palavra.lower()
    return palavra==palavra[::-1]

palavra=input("Digite uma palavra: ")

if um_palindromo(palavra):
    print(f"A palavra '{palavra}' é um palíndromo.")
else:
    print(f"A palavra '{palavra}' não é um palíndromo")