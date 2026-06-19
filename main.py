def calcular_nivel(vitorias, derrotas):
    # Calcula o saldo de rankeadas
    saldo_vitorias = vitorias - derrotas
    
    # Estrutura de decisão para determinar o nível baseado nas VITÓRIAS
    if vitorias < 10:
        nivel = "Ferro"
    elif 11 <= vitorias <= 20:
        nivel = "Bronze"
    elif 21 <= vitorias <= 50:
        nivel = "Prata"
    elif 51 <= vitorias <= 80:
        nivel = "Ouro"
    elif 81 <= vitorias <= 90:
        nivel = "Diamante"
    elif 91 <= vitorias <= 100:
        nivel = "Lendário"
    else:  # Maior ou igual a 101
        nivel = "Imortal"
        
    return saldo_vitorias, nivel

# --- Testando a função com um laço de repetição ---
# Lista de tuplas simulando diferentes jogadores: (vitórias, derrotas)
jogadores_teste = [
    (8, 2),    # Ferro
    (15, 5),   # Bronze
    (45, 10),  # Prata
    (65, 35),  # Ouro
    (85, 5),   # Diamante
    (95, 10),  # Lendário
    (120, 20)  # Imortal
]

for v, d in jogadores_teste:
    # Armazena o retorno da função nas variáveis
    saldo, rank = calcular_nivel(v, d)
    # Exibe a saída formatada (f-string)
    print(f"O Herói tem de saldo de {saldo} está no nível de {rank}")