#!/usr/bin/env python3
"""
Exemplo simples de script Python que demonstra algumas funcionalidades básicas.
"""

def saudacao(nome):
    """
    Função que retorna uma saudação personalizada.
    
    Args:
        nome (str): Nome da pessoa a ser saudada
        
    Returns:
        str: Mensagem de saudação
    """
    return f"Olá, {nome}! Bem-vindo ao repositório de teste."

def calcular_media(numeros):
    """
    Calcula a média de uma lista de números.
    
    Args:
        numeros (list): Lista de números
        
    Returns:
        float: Média dos números
    """
    if not numeros:
        return 0
    return sum(numeros) / len(numeros)

def main():
    # Exemplo de uso das funções
    print(saudacao("Gustavo"))
    
    # Teste da função de cálculo de média
    lista_numeros = [10, 20, 30, 40, 50]
    media = calcular_media(lista_numeros)
    print(f"A média dos números {lista_numeros} é {media}")

if __name__ == "__main__":
    main()
