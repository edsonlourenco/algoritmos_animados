"""
Script de Demonstração de MapReduce em Python
Autor: Edson Lourenço
Canal do YouTube: Desvendando Codigo | https://www.youtube.com/@Desvendando_Codigo/
"""


from collections import defaultdict


def map_reduce(input_text):
    # Fase de Mapping
    words = [word.strip(",") for word in input_text.lower().split()]
    word_counts = defaultdict(int)

    for word in words:
        word_counts[word] += 1

    # Fase de Shuffling (não necessário neste exemplo)

    # Fase de Reducing
    result = {}
    for word, count in word_counts.items():
        result[word] = count

    return result

def main():
    # Fase de Imputação
    input_text = input("Digite um texto para a contagem de palavras: ")

    # Fase de Splitting (não necessário neste exemplo)

    # Executar MapReduce
    result = map_reduce(input_text)

    # Exibir resultado final
    print("\nResultado: \n")
    for word, count in result.items():
        print(f"{word}: {count}")

if __name__ == "__main__":
    main()
