import cv2
import os

# Path to the video file
video_file = '/home/kia/ComputerVision/VisualOdometry/saved1 (trimmed).mp4'

# Create a subfolder to save the frames
output_folder = '/home/kia/ComputerVision/VisualOdometry/ROBOT_1'
os.makedirs(output_folder, exist_ok=True)

# Open the video file
cap = cv2.VideoCapture(video_file)

# Check if the video file was opened successfully
if not cap.isOpened():
    print("Error: Could not open video file.")
    exit()

# Initialize frame counter
frame_count = 0

# Loop through the video frames
while True:
    # Read a frame from the video
    ret, frame = cap.read()

    # Break the loop if we have reached the end of the video
    if not ret:
        break

    # Save the frame as an image
    frame_filename = os.path.join(output_folder, f'frame_{frame_count:04d}.jpg')
    cv2.imwrite(frame_filename, frame)

    # Increment the frame counter
    frame_count += 1

# Release the video capture object
cap.release()

# Print the total number of frames saved
print(f"Total frames saved: {frame_count}")


