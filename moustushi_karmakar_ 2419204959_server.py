import socket

def start_udp_listener():
    # Setup the basics
    host_ip = "127.0.0.1"
    port_num = 13333

    # Init the socket - using DGRAM for UDP
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        sock.bind((host_ip, port_num))
        print(f"--- Server active on port {port_num} ---")

        while True:
            # Grab the packet and the sender's info
            raw_data, sender_address = sock.recvfrom(4096)
            incoming_msg = raw_data.decode('utf-8')

            print(f"Got a ping from {sender_address}: {incoming_msg}")

            # Quick bounce-back message
            acknowledgment = "Got your message, thanks!"
            sock.sendto(acknowledgment.encode('utf-8'), sender_address)

    except Exception as err:
        print(f"Something went wrong: {err}")
    finally:
        sock.close()

if __name__ == "__main__":
    start_udp_listener()