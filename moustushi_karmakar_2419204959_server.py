import socket

def run_server():
    # Local setup
    host = "127.0.0.1"
    port = 13333

    # Create UDP socket
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        server_sock.bind((host, port))
        print(f"Server is listening on port {port}...")

        while True:
            # Buffer size of 1024 is plenty for a name and ID
            data, addr = server_sock.recvfrom(1024)
            message = data.decode('utf-8')

            print(f"Received from {addr}: {message}")

            # Echo the message back exactly as it was received
            server_sock.sendto(data, addr)

    except Exception as e:
        print(f"Server error: {e}")
    finally:
        server_sock.close()

if __name__ == "__main__":
    run_server()