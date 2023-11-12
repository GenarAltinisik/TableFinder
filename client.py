import socket

# Sunucunun IP adresi ve port numarası
host = "10.0.209.255"  # Sunucunun IP adresini buraya girin
port = 8080

# Soket oluşturma
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Sunucuya bağlanma
client_socket.connect((host, port))
print(f"Sunucuya bağlandı.")

# Veri gönderme ve alma
while True:
    message = input("Mesajınızı girin (çıkmak için 'q' veya 'quit'): ")
    
    if message.lower() == 'q' or message.lower() == 'quit':
        break
    
    # Veriyi sunucuya gönderme
    client_socket.send(message.encode('utf-8'))

    # Sunucudan yanıt alma
    response = client_socket.recv(1024)
    print(f"Gelen yanıt sunucudan: {response.decode('utf-8')}")

# Bağlantıyı kapat
client_socket.close()
