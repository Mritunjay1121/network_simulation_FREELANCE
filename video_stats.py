import cv2
from moviepy.editor import VideoFileClip
import time


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



def save_video_info(video_path):
    """
    Saves FPS, backend, video width, and video height of an mp4 video at 1-second intervals while processing.

    Args:
        video_path: Path to the mp4 video file.

    Returns:
        Lists containing FPS, backend, video width, and video height at 1-second intervals.
    """
    cap = cv2.VideoCapture(video_path)

    # Check if video opened successfully
    if not cap.isOpened():
        print("Error opening video stream or file")
        return [], [], [], []

    fps_list = []
    backend_list = []
    width_list = []
    height_list = []

    start_time = time.time()


    video_length = get_video_length(video_path)
    interval = 1 if video_length < 2 else 2  # Interval in seconds to save information




    interval = 2  # Interval in seconds to save information

    while True:
        ret, _ = cap.read()

        if not ret:
            print("No more frames to process")
            break

        current_time = time.time()
        elapsed_time = current_time - start_time

        # Save information at 1-second intervals
        if elapsed_time >= interval:
            fps = cap.get(cv2.CAP_PROP_FPS)
            backend = cap.getBackendName()
            width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

            fps_list.append(fps)
            backend_list.append(backend)
            width_list.append(width)
            height_list.append(height)

            start_time = current_time  # Reset timer

        # Exit on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release resources
    cap.release()

    return fps_list, backend_list, width_list, height_list

if __name__ == "__main__":
    video_path = "video.mp4"  # Replace with your video path
    fps_list, backend_list, width_list, height_list = save_video_info(video_path)

    # Print or use the saved information as needed
    print("FPS List:", fps_list)
    print("Backend List:", backend_list)
    print("Width List:", width_list)
    print("Height List:", height_list)
