import cv2
import numpy as np
import os

# Load the video
video = cv2.VideoCapture("/Users/karthiknadar/Desktop/video processing project/Dataset.mp4")
currentframe=0;
# Read the first frame to get the video's width and height
success, frame = video.read()
if not success:
    print("Failed to read the video")
    exit()

# Create the output folder
folder_name = "output_frames"
if not os.path.exists('data'):
    os.makedirs('data')


# Loop through all the frames in the video
while True:
    # Read the next frame
    success, frame = video.read()

    # If the frame was not read correctly, break out of the loop
    if not success:
        break
    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply a Gaussian blur to the frame
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    # Write the frame to the output frame
    cv2.imshow("Output",blur)
    cv2.imwrite('./data/blur' + str(currentframe) + '.jpg' , blur)
    currentframe +=1
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
# Create an empty list to store the frames
frames = []

# Loop through all the frames in the video
for i in range(currentframe):
    # Capture the frame
    _, frame = video.read()
    # Add the frame to the list
    frames.append(frame)

# Convert the list of frames to a NumPy array
frames = np.array(frames)

# Save the NumPy array to a file
np.save('frames.npy', frames)

# Release the video and video writer
video.release()
cv2.destroyAllWindows()