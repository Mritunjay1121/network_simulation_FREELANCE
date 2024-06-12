import socket
import argparse
import time

SERVER_IP = '127.0.0.1'
SERVER_PORT = 9999

# Create UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
parser = argparse.ArgumentParser(description='Client for video streaming consent.')
parser.add_argument('--consent', choices=['yes', 'no'], default='no', help='Consent to stream video (yes/no)')
args = parser.parse_args()

try:
    # Send consent to server
    client_socket.sendto(args.consent.encode(), (SERVER_IP, SERVER_PORT))
    print(f'Sent consent to server: {args.consent}')

    # Measure connection speed
    start_time = time.time()
    buffer_size = client_socket.getsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF)
    # time.sleep(5)


    data, _ = client_socket.recvfrom(1024)

    # time.sleep(5)




    end_time = time.time()
    elapsed_time = end_time - start_time

    # Calculate connection speed in kbps if elapsed time is not zero
    if elapsed_time > 0:
        connection_speed_kbps = (buffer_size * 8) / (elapsed_time * 1000)  # Convert buffer size to bits and time to milliseconds
        connection_speed = round(connection_speed_kbps, 2)  # Round to 2 decimal places

        # Print connection speed in kbps
        print(f'Connection speed with server: {connection_speed} kbps')
        # print(f'Received results from server {data.decode()}')

    else:
        print("Error: Elapsed time is zero.")
        # print(f'Received results from server {data.decode()}')


    # Receive results from server
    # data, _ = client_socket.recvfrom(1024)
    print(f'Received results from server: {data.decode()}')

finally:
    # Close socket
    client_socket.close()
