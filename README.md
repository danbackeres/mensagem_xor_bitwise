# Alterando Mensagens com Operadores Bitwise

Olá!
Este repositório apresenta um exemplo simples e prático de como utilizar o operador **XOR bitwise** para transformar uma mensagem em outra, trabalhando diretamente com seus valores binários.

## O que você encontrará aqui?

- **Uso prático do operador XOR (`^`)**: Uma demonstração clara de como ele pode ser usado para alterar mensagens.
- **Explicação de lógica bitwise**: Transformei uma mensagem original em outra utilizando cálculos baseados em binários.
- **Um exemplo básico, mas educativo!**

---

## Como funciona o código?

O programa:
1. Compara cada caractere da mensagem original e da mensagem desejada.
2. Gera chaves exclusivas para cada caractere, utilizando o operador XOR.
3. Transforma a mensagem original na nova mensagem aplicando novamente o operador XOR.

---

## Execução

### Pré-requisitos:
- Python 3 instalado na sua máquina.

### Como rodar:
1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   ```
2. Entre na pasta do projeto:
   ```bash
   cd seu-repositorio
   ```
3. Execute o script:
   ```bash
   python alterar_mensagem.py
   ```
   
#### Exemplo de Saída:
```plaintext
Original (binário): [79, 108, 225, 32, 32]
Nova (binário): [84, 99, 104, 97, 117]
Chaves (binário): [27, 15, 129, 65, 85]
Mensagem Transformada: Tchau
```
---
## Observações
* Este exemplo usa preenchimento com espaços para garantir que mensagens de tamanhos diferentes possam ser processadas.
* O código foi feito para ser simples e fácil de entender, mas fique à vontade para expandir. 😉
**Atenção:** É apenas uma demonstração de conceitos, cuidado!
   
