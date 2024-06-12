


import socket
import time 
from video_stats import save_video_info


# Define server address and port
SERVER_IP = '127.0.0.1'
SERVER_PORT = 9999

# Create UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((SERVER_IP, SERVER_PORT))

print('Server started...')


def get_video_length(video_path):
    """
    Get the length of the video in seconds.

    Args:
        video_path: Path to the mp4 video file.

    Returns:
        Length of the video in seconds.
    """
    clip = VideoFileClip(video_path)
    return int(clip.duration)

def process_consent(consent):
    # Simulate processing the consent and generating results
    if consent == 'yes':




        fps,backend,clipw,cliph=save_video_info("video.mp4")
        
        strr=f'since consent was granted. So at each interval Fps is {fps} , Video Backend is {backend}, Video Width is {clipw}, Video Height is {cliph} '
        return strr
    else:
        return 'Consent not granted. Cannot stream video.'

try:
    while True:
        # Receive consent from client
        consent, client_address = server_socket.recvfrom(1024)
        consent = consent.decode()
        print(f'Received consent from client ({client_address}): {consent}')
        print()

        # Process consent and generate results
        results = process_consent(consent)
        
        # Send results back to client
        server_socket.sendto(results.encode(), client_address)
        # print(f'Sent results to client ({client_address}): {results}')
        print(f'Sent results to client ')

        
        if consent == 'yes':
            # Simulate video streaming process
            for i in range(5):
                # Send video frames (simulated)
                server_socket.sendto(f'For video frame {i}'.encode(), client_address)
                time.sleep(1)
        
except :
    # Close the server socket
    server_socket.close()
    print('Server socket closed.')
