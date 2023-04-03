import socket
import threading

#création de serveur avec une adresse IP "neutre" et un port non utilisé
HOST = "127.0.0.1"
PORT = 1234

serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serveur.bind((HOST, PORT))

serveur.listen()

clients = []
nicknames = []

def affichage(message, client):
    for c in clients:
        if c != client:
            c.send(message)

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            print(f"{nicknames[clients.index(client)]} send {message}")
            affichage(message, client) 
        except ValueError:
            print("Client déconnecté")
            break
        except:
            if client in clients:
                index = clients.index(client)
                clients.remove(client)
                client.close()
                nicknames1 = nicknames[index]
                nicknames.remove(nicknames1)
                break

def message_aff():
    while True:
        client, adress = serveur.accept()
        print("You are connected to the server")

        client.send("NOM".encode('utf-8'))
        nickname = client.recv(1024).decode('utf-8')
        nicknames.append(nickname)
        clients.append(client)

        print(f"{nickname} now connected to the server".encode('utf-8'))
        client.send("Connected".encode("utf-8"))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

print("serveur running...")
message_aff()
