from PIL import Image, ImageSequence
import tkinter as tk
from tkinter import filedialog

def process_images():
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    # Ask user to select a background JPEG image
    background_path = filedialog.askopenfilename(title="Select Background JPEG",
                                                 filetypes=[("JPEG Files", "*.jpg"), ("All Files", "*.*")])
    if not background_path:
        print("No background image selected.")
        return

    # Ask user to select a GIF image
    gif_path = filedialog.askopenfilename(title="Select GIF File",
                                          filetypes=[("GIF Files", "*.gif"), ("All Files", "*.*")])
    if not gif_path:
        print("No GIF file selected.")
        return

    # Specify the position (x, y) where you want to place the top-left corner of the GIF on the background
    gif_position = (2216, 2459)  # You can modify this position as needed

    background = Image.open(background_path)
    gif_image = Image.open(gif_path)

    # Resize the GIF image to fit into the background image
    new_width = int(gif_image.width * 0.5)  # Adjust the scaling factor if needed
    new_height = int(gif_image.height * 0.5)  # Adjust the scaling factor if needed
    gif_image = gif_image.resize((new_width, new_height), Image.ANTIALIAS)

    # Paste the GIF onto the background at the specified position
    output = background.copy()
    output.paste(gif_image, gif_position, gif_image)

    # Get the directory and file name to save the output GIF
    save_path = filedialog.asksaveasfilename(title="Save As",
                                             filetypes=[("GIF Files", "*.gif"), ("All Files", "*.*")],
                                             defaultextension=".gif")
    if not save_path:
        print("No file selected for saving.")
        return

    output.save(save_path)
    print(f"Image saved as {save_path}")

if __name__ == "__main__":
    process_images()
