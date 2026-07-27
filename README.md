# 🐍 Curso Python Guanabara - Exercícios Resolvidos

Repositório com **64 desafios** do famoso **Curso de Python do Gustavo Guanabara**. Uma progressão estruturada para aprender Python desde o básico até conceitos mais avançados como loops, condicionais, funções e manipulação de dados.

---

## 📂 Estrutura do Repositório

```
curso-python-guanabara/
├── 01_Fundamentos/          # Entrada/saída, variáveis, operações básicas
├── 02_Condicionais/         # if, elif, else, comparações
├── 03_Loops/                # for, while, iterações
├── 04_Strings/              # Manipulação de textos
├── 05_Listas_e_Dados/       # Listas, tuplas, randomização
├── 06_Funções_e_Calculos/   # Cálculos, fatoriais, PA, PG, Fibonacci
├── Aulas/                   # Exemplos de conceitos das aulas
├── Praticas/                # Exercícios de treinamento livre
└── README.md
```

---

## 🎯 Índice de Desafios por Categoria

### **01 - FUNDAMENTOS** (Desafios 1-8)
Conceitoa básicos: entrada, saída, variáveis, tipos de dados e operações aritméticas.

| # | Nome | Conceito |
|---|------|----------|
| **Desafio 1** | Olá Mundo com Input | Usar `input()` e `print()` com strings |
| **Desafio 2** | Data de Nascimento | Concatenar múltiplas entradas de texto |
| **Desafio 6** | Operações com Números | Dobro, triplo, raiz quadrada (operadores: `*`, `**`) |
| **Desafio 7** | Média de Notas | Cálculo de média aritmética com `float` |
| **Desafio 8** | Conversão de Unidades | Converter metros para cm e mm |
| **Desafio 9** | Tabuada (Apagado) | *(Arquivo não disponível)* |
| **Desafio 12** | Desconto em Produto | Calcular porcentagem (desconto de 5%) |
| **Desafio 14** | Conversão de Temperatura | Converter Celsius para Fahrenheit (fórmula: C*1.8 + 32) |
| **Desafio 16** | Parte Inteira de um Número | Usar `math.trunc()` para extrair parte inteira |

---

### **02 - CONDICIONAIS** (Desafios 28-45)
Uso de `if`, `elif`, `else` para tomar decisões baseadas em condições.

| # | Nome | Conceito |
|---|------|----------|
| **Desafio 28** | Jogo de Adivinhação Simples | Comparar entrada com valor aleatório (`random.randint()`) |
| **Desafio 29** | Multa por Velocidade | Condicional simples com cálculo de multa |
| **Desafio 30** | Par ou Ímpar | Usar operador módulo (`%`) para verificar resto |
| **Desafio 31** | Preço de Passagem | Desconto baseado em distância |
| **Desafio 32** | Ano Bissexto | Validar bissexto com múltiplas condições |
| **Desafio 33** | Maior e Menor | Comparar 3 números com `max()` e `min()` |
| **Desafio 34** | Aumento de Salário | Aumentos diferentes baseados no salário |
| **Desafio 36** | Aprovação de Empréstimo | Verificar se prestação é <= 30% do salário |
| **Desafio 37** | Conversão de Base Numérica | Converter para binário, octal, hexadecimal com `bin()`, `oct()`, `hex()` |
| **Desafio 38** | Comparação de Números | Comparar dois números (maior, menor, igual) |
| **Desafio 39** | Alistamento Militar | Múltiplos `if/elif` com lógica de datas |
| **Desafio 40** | Média Escolar com Conceito | Classificar nota em reprovado, recuperação, aprovado |
| **Desafio 41** | Classificação de Idade | Categorias de natação (Mirim, Infantil, Junior, Sênior, Master) |
| **Desafio 42** | Análise de Triângulo | Verificar se forma triângulo e qual tipo (equilátero, isósceles, escaleno) |
| **Desafio 43** | Cálculo de IMC | Calcular IMC e classificar (magro, normal, sobrepeso, obeso) |
| **Desafio 44** | Formas de Pagamento | Múltiplas opções com descontos e juros |
| **Desafio 45** | Jokenpô | Jogo de pedra-papel-tesoura com lógica condicional complexa |

---

### **03 - LOOPS** (Desafios 46-64)
Iteração com `for` e `while` para executar código múltiplas vezes.

#### **Com FOR:**

| # | Nome | Conceito |
|---|------|----------|
| **Desafio 46** | Contagem Regressiva | `for` com `range(10, -1, -1)` (decrescente) |
| **Desafio 47** | Números Pares até 50 | `for` com step de 2 em `range()` |
| **Desafio 48** | Números Ímpares Múltiplos de 3 | `for` com condição interna (`if num % 3 == 0`) |
| **Desafio 49** | Tabuada | `for` de 1 a 10 multiplicando um número |
| **Desafio 50** | Soma de Pares | `for` com acumulador e filtro |
| **Desafio 51** | PA (Progressão Aritmética) | Gerar 10 termos de PA com `range()` |
| **Desafio 52** | Teste de Número Primo | `for` de 1 até n verificando divisibilidade |
| **Desafio 54** | Maioridade de 7 Pessoas | `for` com `range(1, 8)` e cálculo de idade |
| **Desafio 55** | Maior e Menor Peso | Rastrear máximo e mínimo em 5 iterações |
| **Desafio 56** | Análise de Grupo | Múltiplas condições dentro de `for`: idade média, homem mais velho, mulheres < 20 |

#### **Com WHILE:**

| # | Nome | Conceito |
|---|------|----------|
| **Desafio 57** | Validação com While | Loop até entrada válida (M ou F) |
| **Desafio 58** | Adivinhação com Dica | `while True` com `break` quando acerta |
| **Desafio 59** | Calculadora em Loop | Menu interativo com múltiplas operações |
| **Desafio 60** | Fatorial | `while` decrementando até 0 |
| **Desafio 61** | PA com While | Versão de Desafio 51 com `while` |
| **Desafio 62** | PA Extensível | PA que pergunta se quer mais termos (while aninhado) |
| **Desafio 63** | Fibonacci | Gerar sequência de Fibonacci com `while` |
| **Desafio 64** | Soma com Parada | Somar números até digitar 999 |

---

### **04 - STRINGS** (Desafios 22, 23, 27, 53)
Manipulação de texto, busca, inversão e padrões.

| # | Nome | Conceito |
|---|------|----------|
| **Desafio 22** | Análise de Nome | `.upper()`, `.lower()`, `.len()`, `.count()`, `.find()`, `.replace()` |
| **Desafio 23** | Extração de Dígitos | Usar operadores `//` e `%` para extrair unidade, dezena, centena, milhar |
| **Desafio 27** | Primeiro e Último Nome | `.split()` e indexação com `[0]` e `[-1]` |
| **Desafio 53** | Palíndromo | `.replace()` para remover espaços, slicing com `[::-1]` para inverter |

---

### **05 - LISTAS E DADOS** (Desafio 20)
Trabalhar com coleções de dados e funções como `random.shuffle()`.

| # | Nome | Conceito |
|---|------|----------|
| **Desafio 20** | Embaralhamento | Criar lista, usar `random.shuffle()` para randomizar |

---

### **06 - FUNÇÕES E CÁLCULOS AVANÇADOS**
Sequências matemáticas e programação mais complexa (PA, PG, Fibonacci, fatorial).

*Estes desafios se integram com loops e condicionais*

---

## 🚀 Como Usar

### Executar um desafio individual:
```bash
python 01_Fundamentos/desafio_01.py
```

### Rodar uma aula:
```bash
python Aulas/Aula_09.py
```

### Praticar:
```bash
python Praticas/treinando_1.py
```

---

## 📋 Progressão de Dificuldade

1. **Fácil** → Desafios 1-16 (Fundamentos)
2. **Intermediário** → Desafios 28-50 (Condicionais + Loops iniciais)
3. **Médio-Alto** → Desafios 51-64 (Loops complexos, Fibonacci, PA)
4. **Alto** → Desafios 42, 45, 56, 59, 62 (Lógica combinada)

---

## 📚 Conceitos-Chave por Desafio

### Operadores Importantes:
- Aritmética: `+`, `-`, `*`, `/`, `//`, `%`, `**`
- Comparação: `>`, `<`, `==`, `!=`, `>=`, `<=`
- Lógicos: `and`, `or`, `not`
- String: `.upper()`, `.lower()`, `.replace()`, `.split()`, `.find()`, `.count()`, slicing `[:]`

### Funções Integradas:
- `input()` - entrada do usuário
- `print()` - saída
- `int()`, `float()`, `str()` - conversão de tipos
- `len()` - comprimento
- `max()`, `min()` - maior e menor
- `range()` - sequência de números
- `random.randint()`, `random.choice()`, `random.shuffle()` - randomização
- `math.trunc()` - parte inteira
- `bin()`, `oct()`, `hex()` - conversão de bases
- `date.today()` - data atual

---

## 💡 Dicas

- Comece pelos **Fundamentos** se nunca programou em Python
- Pratique **Condicionais** antes de partir para **Loops**
- Os desafios com `_clean` são versões **refatoradas** — compare-as para aprender boas práticas
- Use `print()` estrategicamente para entender o fluxo do código
- Experimente modificar os programas e quebrar propositalmente para aprender

---

## ✅ Versões Refatoradas

Alguns desafios têm versões `_clean` ou `_v2`, `_v3`, `_v4`:
- **Desafio 45_clean** - Jokenpô melhorado
- **Desafio 52_clean** - Número Primo otimizado
- **Desafio 58_clean** - Adivinhação melhorada
- **Desafio 59_clean** - Calculadora em loop refatorada
- **Desafio 60_clean** - Fatorial com while otimizado
- **Desafio 61_clean** - PA com while melhorado
- **Desafio 62_clean** - PA Extensível mais limpo

Compare com as versões originais para ver diferentes abordagens!

---

## 📖 Referência Rápida

### Estrutura IF-ELIF-ELSE:
```python
if condicao1:
    # faz algo
elif condicao2:
    # faz outra coisa
else:
    # padrão
```

### Loop FOR:
```python
for i in range(1, 11):  # 1 a 10
    print(i)
```

### Loop WHILE:
```python
while True:
    entrada = input("Digite algo: ")
    if entrada == "sair":
        break
```

### Acumulador em Loop:
```python
soma = 0
for num in [1, 2, 3]:
    soma += num
print(soma)  # 6
```

---

## 🎓 Créditos

Todos os exercícios são baseados no **Curso de Python** do **Gustavo Guanabara** (disponível gratuitamente no YouTube).

---

## 📝 Notas Pessoais

- **Desafio 9**: Arquivo perdido — era uma tabuada
- Alguns desafios têm múltiplas soluções comentadas dentro do arquivo
- Use as cores ANSI (`\033[...]`) para customizar output (veja Desafio 29 como exemplo)

---

**Última atualização:** 27/07/2026  
**Status:** 64/64 desafios resolvidos ✅
