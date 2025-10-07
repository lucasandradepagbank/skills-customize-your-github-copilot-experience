

# 🎮 Games in Python

## 🎯 Objetivo

Você irá criar jogos simples em Python para praticar manipulação de strings, loops, condicionais e entrada do usuário.

## 📝 Tarefas

### 🛠️ Jogo da Forca (Hangman)

#### Description
Implemente o clássico jogo da forca, onde o jogador tenta adivinhar uma palavra secreta letra por letra antes de acabar as tentativas.

#### Requirements
Completed program should:

- Selecionar palavras aleatoriamente de uma lista pré-definida
- Aceitar palpites de letras e mostrar o progresso atual (formato _ _ _)
- Controlar o número de tentativas incorretas restantes
- Encerrar quando a palavra for adivinhada ou as tentativas acabarem
- Exibir mensagens de vitória ou derrota

##### Exemplo de entrada/saída
```python
Palavra secreta: python
Palpite: p
Progresso: p _ _ _ _ _
Palpite: o
Progresso: p _ _ _ o _
...etc
```

### 🛠️ Jogo de Adivinhação de Número

#### Description
Crie um jogo onde o computador escolhe um número aleatório e o jogador deve adivinhar, recebendo dicas se o palpite está acima ou abaixo do número correto.

#### Requirements
Completed program should:

- Gerar um número aleatório dentro de um intervalo definido
- Receber palpites do usuário e informar se está acima ou abaixo
- Contabilizar o número de tentativas
- Exibir mensagem de sucesso ao acertar

##### Exemplo de entrada/saída
```python
O número está entre 1 e 100.
Palpite: 50
Resposta: Muito alto!
Palpite: 25
Resposta: Muito baixo!
Palpite: 37
Resposta: Parabéns, você acertou!
```
