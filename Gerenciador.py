
import os

# Inicializa a matriz de assentos
def inicializar_assentos():
    return [['-' for _ in range(6)] for _ in range(20)]  # 20 fileiras e 6 colunas (A-F)

# Salva o estado dos assentos em um arquivo
def salvar_assentos(assentos, arquivo="assentos.txt"):
    with open(arquivo, "w") as f:
        for linha in assentos:
            f.write(' '.join(linha) + "\n")

# Carrega o estado dos assentos de um arquivo
def carregar_assentos(arquivo="assentos.txt"):
    if not os.path.exists(arquivo):
        return inicializar_assentos()
   
    with open(arquivo, "r") as f:
        assentos = [linha.strip().split() for linha in f.readlines()]
    return assentos

# Converte a escolha de fileira (A-F) para índice
def converter_fileira_para_indice(fileira):
    return ord(fileira.upper()) - ord('A')

# Exibe o estado atual da matriz de assentos
def mostrar_assentos(assentos):
    print("  A B C D E F")
    for i, linha in enumerate(assentos):
        print(f"{i+1:2}", ' '.join(linha))

# Verifica se um assento está disponível e o reserva
def reservar_assento(assentos, nome, fileira, numero):
    indice_fileira = converter_fileira_para_indice(fileira)
    if assentos[numero - 1][indice_fileira] == '-':
        assentos[numero - 1][indice_fileira] = 'X'  # Marca o assento como ocupado
        print(f"Assento {fileira}{numero} reservado para {nome}!")
    else:
        print(f"O assento {fileira}{numero} já está ocupado.")
    salvar_assentos(assentos)

# Cancela a reserva de um assento, se estiver ocupado
def cancelar_reserva(assentos, fileira, numero):
    indice_fileira = converter_fileira_para_indice(fileira)
    if assentos[numero - 1][indice_fileira] == 'X':  # Verifica se o assento está ocupado
        assentos[numero - 1][indice_fileira] = '-'  # Libera o assento
        print(f"Reserva do assento {fileira}{numero} foi cancelada.")
    else:
        print(f"O assento {fileira}{numero} já está vazio.")
    salvar_assentos(assentos)

# Função principal
def main():
    assentos = carregar_assentos()  # Carrega assentos do arquivo
    while True:
        mostrar_assentos(assentos)
        print("\nOpções: ")
        print("1. Reservar um assento")
        print("2. Cancelar uma reserva")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':  # Reservar assento
            nome = input("Digite seu nome: ")
            fileira = input("Escolha a fileira (A-F): ").upper()
            numero = int(input("Escolha o número da fileira (1-20): "))
           
            if fileira in 'ABCDEF' and 1 <= numero <= 20:
                reservar_assento(assentos, nome, fileira, numero)
            else:
                print("Escolha inválida. Tente novamente.")

        elif opcao == '2':  # Cancelar reserva
            fileira = input("Escolha a fileira (A-F): ").upper()
            numero = int(input("Escolha o número da fileira (1-20): "))
           
            if fileira in 'ABCDEF' and 1 <= numero <= 20:
                cancelar_reserva(assentos, fileira, numero)
            else:
                print("Escolha inválida. Tente novamente.")
       
        elif opcao == '3':  # Sair
            print("Encerrando o programa.")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()