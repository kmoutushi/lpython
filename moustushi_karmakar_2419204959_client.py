import socket

def run_client():
    server_ip = "127.0.0.1"
    server_port = 13333

    # Fill in your details here
    name = "MoutushiKarmakar"
    reg_num = "2419204959"
    payload = f"{name}_{reg_num}"

    # Create UDP socket
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_sock.settimeout(5) # Wait 5 seconds before giving up

    try:
        print(f"Sending: {payload}")
        client_sock.sendto(payload.encode('utf-8'), (server_ip, server_port))

        # Receive the echoed response
        echoed_data, server_addr = client_sock.recvfrom(1024)
        print(f"Echo from server: {echoed_data.decode('utf-8')}")

    except socket.timeout:
        print("The server didn't respond in time.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        client_sock.close()

if __name__ == "__main__":
    run_client()