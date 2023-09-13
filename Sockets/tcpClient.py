import socket

# Configuração do cliente
host = '127.0.0.1'  # Endereço IP do servidor
port = 12345  # Porta do servidor

# Cria um objeto socket do cliente
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conecta-se ao servidor
client_socket.connect((host, port))

while True:
  # Solicita que o cliente insira uma mensagem
  message = input(
      "Digite uma mensagem para o servidor (ou digite 'exit' para sair): ")

  if message.lower() == 'exit':
    break  # Sai do loop se o cliente digitar 'exit'

  # Envia a mensagem para o servidor
  client_socket.send(message.encode())
  # Recebe a resposta do servidor
  response = client_socket.recv(1024)
  print(f"Servidor diz: {response.decode()}")

# Fecha a conexão com o servidor
client_socket.close()
