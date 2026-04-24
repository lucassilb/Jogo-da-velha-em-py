# Criando o tabuleiro (matriz 3x3)
tabuleiro = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]


def mostrar_tabuleiro():
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("-" * 9)


def verificar_vencedor(jogador):
   
    for linha in tabuleiro:
        if linha.count(jogador) == 3:
            return True

   
    for col in range(3):
        if tabuleiro[0][col] == jogador and tabuleiro[1][col] == jogador and tabuleiro[2][col] == jogador:
            return True

   
    if tabuleiro[0][0] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][2] == jogador:
        return True
    if tabuleiro[0][2] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][0] == jogador:
        return True

    return False


def verificar_empate():
    for linha in tabuleiro:
        if " " in linha:
            return False
    return True


def jogada_valida(linha, coluna):
    return tabuleiro[linha][coluna] == " "


jogador_atual = "X"

while True:
    mostrar_tabuleiro()

    print(f"Jogador {jogador_atual}")
    linha = int(input("Escolha a linha (0, 1 ou 2): "))
    coluna = int(input("Escolha a coluna (0, 1 ou 2): "))

    if jogada_valida(linha, coluna):
        tabuleiro[linha][coluna] = jogador_atual
    else:
        print("Jogada inválida! Tente novamente.")
        continue

    
    if verificar_vencedor(jogador_atual):
        mostrar_tabuleiro()
        print(f"Jogador {jogador_atual} venceu!")
        break


    if verificar_empate():
        mostrar_tabuleiro()
        print("Empate!")
        break

  
    if jogador_atual == "X":
        jogador_atual = "O"
    else:
        jogador_atual = "X"