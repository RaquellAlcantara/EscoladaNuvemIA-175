'''
2- Crie uma função que verifique se uma palavra ou frase é um palíndromo (lê-se igual de trás para frente, ignorando espaços e pontuação). Se o resultado é True, responda “Sim”, se o resultado for False, responda “Não”.
'''
import string

def verificar_palindromo(texto):
    texto_limpo = ''.join(
        char.lower() for char in texto if char.isalnum()
    )
    return texto_limpo == texto_limpo[::-1]

try:
    frase = input("Digite uma palavra ou frase para verificar se é palíndromo: ")
    if not frase.strip():
        raise ValueError("Entrada vazia!")
    
    resultado = verificar_palindromo(frase)
    if resultado:
        print("Sim")
    else:
        print("Não")
except Exception as e:
    print(f"Erro na entrada: {e}")
