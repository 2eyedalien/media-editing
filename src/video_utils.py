import cv2, os

def create_video_from_frames(image_folder, video_name, fps=30, duration=10):
    images = sorted([img for img in os.listdir(image_folder) if img.endswith('.png') or img.endswith('.jpg')])
    if not images:
        print('No images found in folder')
        return
    frame = cv2.imread(os.path.join(image_folder, images[0]))
    height, width, layers = frame.shape
    video = cv2.VideoWriter(video_name, cv2.VideoWriter_fourcc(*'XVID'), fps, (width,height))
    for image in images:
        video.write(cv2.imread(os.path.join(image_folder, image)))
    video.release()
    print(f'Video saved to {video_name}')
