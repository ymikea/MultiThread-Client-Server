import socket

IP = "localhost"
PORT = 8000
ADDR = (IP, PORT)


def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    print(f"[CONNECTED] Client connected to server at {IP}:{PORT}")
    print("Client Running ...")
    while True:
        pass

if __name__ == "__main__":
    main()