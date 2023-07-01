import tkinter as tk
from tkinter import filedialog
from PIL import Image
import os

def change_color(image, r_factor, g_factor, b_factor):

    r, g, b = image.split()
    r = r.point(lambda i: int(i * r_factor))
    g = g.point(lambda i: int(i * g_factor))
    b = b.point(lambda i: int(i * b_factor))
    return Image.merge("RGB", (r, g, b))

def save_variations(image_path, output_prefix):

    image = Image.open(image_path)

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

    output_folder = "output"
    os.makedirs(output_folder, exist_ok=True)

    for i, factors in enumerate(color_factors):
        output_path = os.path.join(output_folder, f"{output_prefix}_{i}.jpg")
        modified_image = change_color(image, *factors)
        modified_image.save(output_path)
        print(f"Saved variation {i+1}: {output_path}")

def select_file():

    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
    if file_path:
        input_entry.delete(0, tk.END)
        input_entry.insert(0, file_path)

def apply_color_changes():

    image_path = input_entry.get()
    output_prefix = "output_image"
    save_variations(image_path, output_prefix)
    status_label.config(text="Color changes applied!")

window = tk.Tk()
window.title("Image Color Change")
window.geometry("400x200")

input_label = tk.Label(window, text="Select an image:")
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
