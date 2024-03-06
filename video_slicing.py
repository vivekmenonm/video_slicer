import cv2
import os

def extract_frames(video_path, num_frames, output_dir, target_width=640, target_height=640):
    cap = cv2.VideoCapture(video_path)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    
    if num_frames > frame_count:
        num_frames = frame_count
        
    indices = sorted(set([int(i * frame_count / num_frames) for i in range(num_frames)]))
    
    for idx in indices:
        cap.set(cv2.CAP_PROP_POS_FRAMES, idx)
        ret, frame = cap.read()
        if ret:
            frame = cv2.resize(frame, (target_width, target_height))
            frame_path = os.path.join(output_dir, f"frame_{idx}.jpg")
            cv2.imwrite(frame_path, frame)
    
    cap.release()

# Example usage:
video_path = "elephant.mp4"
num_frames = 200  # Number of frames needed
output_dir = "elephant"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

extract_frames(video_path, num_frames, output_dir)
print(f"Frames saved in {output_dir}.")
