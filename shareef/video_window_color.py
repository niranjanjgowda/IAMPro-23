import tkinter as tk
from tkinter import filedialog
import cv2
import os

def change_color(frame, r_factor, g_factor, b_factor):

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame[:, :, 0] = cv2.add(frame[:, :, 0], int(b_factor * 255))
    frame[:, :, 1] = cv2.add(frame[:, :, 1], int(g_factor * 255))
    frame[:, :, 2] = cv2.add(frame[:, :, 2], int(r_factor * 255))
    return frame

def save_variations(video_path, output_prefix):

    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))


    color_factors = [
        (1.2, 1.0, 1.0),   # Increase red
        (0.8, 1.0, 1.0),   # Decrease red
        (1.0, 1.2, 1.0),   # Increase green
        (1.0, 0.8, 1.0),   # Decrease green
        (1.0, 1.0, 1.2),   # Increase blue
        (1.0, 1.0, 0.8),   # Decrease blue
        (1.1, 1.1, 0.9),   # Yellowish tint
        (0.9, 1.1, 1.1),   # Bluish tint
        (1.1, 0.9, 1.1),   # Magenta tint
        (0.9, 1.1, 0.9)    # Cyanish tint
    ]

    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")

    output_folder = "output"
    os.makedirs(output_folder, exist_ok=True)

    for i, factors in enumerate(color_factors):
        output_path = os.path.join(output_folder, f"{output_prefix}_{i}.mp4")
        out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            modified_frame = change_color(frame, *factors)
            out.write(modified_frame)

        out.release()
        status_label.config(text=f"Saved variation {i+1}: {output_path}")
        status_label.update()

    cap.release()
    status_label.config(text="Color changes applied!")

def select_file():

    file_path = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4")])
    if file_path:
        input_entry.delete(0, tk.END)
        input_entry.insert(0, file_path)

def apply_color_changes():

    video_path = input_entry.get()
    output_prefix = "output_video"
    save_variations(video_path, output_prefix)


window = tk.Tk()
window.title("Video Color Change")
window.geometry("400x200")


input_label = tk.Label(window, text="Select a video:")
input_label.pack()

input_entry = tk.Entry(window, width=40)
input_entry.pack()

select_button = tk.Button(window, text="Browse", command=select_file)
select_button.pack()

apply_button = tk.Button(window, text="Apply Color Changes", command=apply_color_changes)
apply_button.pack()

status_label = tk.Label(window, text="")
status_label.pack()

window.mainloop()
