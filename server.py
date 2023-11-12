import socket

# Sunucunun IP adresi ve port numarası
host = "10.0.209.255"  # Tüm arayüzler
port = 8080

# Soket oluşturma
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Soketi belirtilen IP ve port numarasına bağlama
server_socket.bind((host, port))

# Bağlantı beklemeye başlama
server_socket.listen(1)
print(f"Sunucu {host}:{port} üzerinde dinleniyor...")

# İstemci bağlantısını kabul etme
client_socket, client_address = server_socket.accept()
print(f"{client_address} istemcisi bağlandı.")

# Veri alışverişi
while True:
    # İstemciden veri alınması
    data = client_socket.recv(1024)
    if not data:
        break
    print(f"Gelen veri istemciden: {data.decode('utf-8')}")

    # İstemciye yanıt gönderme
    response = input("Bir mesaj girin: ")
    client_socket.send(response.encode('utf-8'))

# Bağlantıyı kapat
client_socket.close()
