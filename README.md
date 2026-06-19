# Calculadora de Partidas Rankeadas

Este projeto prático foi desenvolvido como parte do segundo desafio de código proposto pela **DIO (Digital Innovation One)**. O objetivo principal foi consolidar a lógica de programação através da criação de funções e manipulação de múltiplos retornos utilizando Python.

---

## 💻 Sobre o Desafio

O script calcula o saldo de partidas rankeadas de um jogador com base no número de **vitórias** e **derrotas**. Através de uma função dedicada, o sistema subtrai as derrotas das vitórias e determina o elo correspondente do jogador, cobrindo da categoria *Ferro* até *Imortal*.

### Requisitos Técnicos Aplicados:
* **Variáveis:** Armazenamento do saldo e classificação do jogador.
* **Operadores:** Operações aritméticas para cálculo de saldo e operadores de comparação.
* **Estruturas de Decisão:** Filtros condicionais (`if`, `elif`, `else`) para categorização dos níveis.
* **Funções:** Criação de escopo isolado que recebe parâmetros e retorna múltiplos valores de forma nativa.
* **Laços de Repetição:** Controle de fluxo para iteração e teste em lote de múltiplos cenários.

---

## ⚡ Diferencial Implementado

Para demonstrar uma arquitetura de código limpa e eficiência em testes, o projeto foi estruturado utilizando o conceito de **Desempacotamento de Tuplas** (*Tuple Unzipping*) combinado a um laço de repetição `for`. 

Em vez de testar um cenário por vez ou forçar inputs manuais repetitivos, o script varre uma lista contendo múltiplos perfis de teste pré-definidos (valores de vitórias e derrotas). Isso permite validar todas as regras de negócio da tabela de níveis em uma única execução automática, simulando testes unitários simples.

---

## 📊 Regras de Negócio (Tabela de Níveis)

| Vitórias Mínimas | Vitórias Máximas | Nível Correspondente |
| :--- | :--- | :--- |
| Menor que 10 | — | **Ferro** |
| 11 | 20 | **Bronze** |
| 21 | 50 | **Prata** |
| 51 | 80 | **Ouro** |
| 81 | 90 | **Diamante** |
| 91 | 100 | **Lendário** |
| Maior ou igual a 101 | — | **Imortal** |

*Nota: O saldo de partidas é calculado através da fórmula: `Vitórias - Derrotas`.*

---

## 🚀 Como Executar o Projeto

1. Certifique-se de possuir o **Python 3** instalado em seu ambiente.
2. Clone este repositório ou baixe o arquivo correspondente.
3. Abra o terminal no diretório do projeto e execute o comando:
```bash
python calculadora.py