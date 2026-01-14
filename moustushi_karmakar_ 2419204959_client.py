import socket

def send_test_packet():
    target_ip = "127.0.0.1"
    target_port = 13333
    my_message = "Hey there, testing the UDP port 13333."

    # Create the socket object
    client_conn = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Set a 3-second wait limit so the program doesn't hang forever
    client_conn.settimeout(3)

    try:
        print(f"Sending data to {target_ip}...")
        client_conn.sendto(my_message.encode('utf-8'), (target_ip, target_port))

        # Look for the response
        response, server_info = client_conn.recvfrom(4096)
        print(f"Server replied: {response.decode('utf-8')}")

    except socket.timeout:
        print("No response... the server might be down.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client_conn.close()
        print("Connection closed.")

if __name__ == "__main__":
    send_test_packet()