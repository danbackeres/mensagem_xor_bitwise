# Mensagens
original = "Olá"
nova_mensagem = "Tchau"

# Ajustar para o maior tamanho, preenchendo com espaços, garantindo que as duas mensagens sejam trabalhadas no Zip com o mesmo tamanho.
tamanho_maximo = max(len(original), len(nova_mensagem))
original = original.ljust(tamanho_maximo)
nova_mensagem = nova_mensagem.ljust(tamanho_maximo)

# Converter caracteres para binário (ASCII)
# Lista de códigos ASCII
original_bin = [ord(c) for c in original]  
nova_bin = [ord(c) for c in nova_mensagem]

# Gerar as chaves para transformação (com XOR)
chaves = [o ^ n for o, n in zip(original_bin, nova_bin)]

# Alterar "Olá" em "Tchau" usando as chaves geradas
mensagem_transformada = "".join(chr(o ^ k) for o, k in zip(original_bin, chaves))

print("Original (binário):", original_bin)
print("Nova (binário):", nova_bin)
print("Chaves (binário):", chaves)
print("Mensagem Transformada:", mensagem_transformada)
