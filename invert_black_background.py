import cv2
import numpy as np

print("Inverting")
# Path to the input video
input_path = "assets/samples.mp4"
output_path = "assets/samples_inverted.mp4"

# Open the video file
cap = cv2.VideoCapture(input_path)

# Get video properties
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))
fourcc = cv2.VideoWriter_fourcc(*'mp4v')

# Define the video writer
out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Invert black to white
    # Create a mask for black pixels
    black_mask = cv2.inRange(frame, (0, 0, 0), (15, 15, 15))  # Adjust threshold as needed
    
    # Invert only the black pixels
    inverted_frame = frame.copy()
    inverted_frame[black_mask > 0] = 255 - inverted_frame[black_mask > 0]
    print("Inverted frame")
    # Write the frame to the output video
    out.write(inverted_frame)

# Release resources
cap.release()
out.release()
cv2.destroyAllWindows()

print(f"Inverted video saved to {output_path}")