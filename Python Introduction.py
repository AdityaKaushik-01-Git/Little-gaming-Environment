import tkinter as tk
from PIL import Image, ImageTk  # Requires: pip install Pillow

class ForestGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Escape the Woods")
        self.root.geometry("600x500")
        
        # Load Images (Update extensions to .png, .jpg, etc., as needed)
        try:
            self.bg_forest_raw = Image.open("forest background.png").resize((600, 300))
            self.bg_exit_raw = Image.open("Exit.jpg").resize((600, 300))
            
            self.img_forest = ImageTk.PhotoImage(self.bg_forest_raw)
            self.img_exit = ImageTk.PhotoImage(self.bg_exit_raw)
        except Exception as e:
            # Fallback if images are missing so the game still runs
            print(f"Error loading images: {e}")
            self.img_forest = None
            self.img_exit = None

        # Image Display Area
        self.image_label = tk.Label(root, image=self.img_forest)
        self.image_label.pack(pady=10)

        # Story Text Area
        self.text_label = tk.Label(root, text="You are in the woods.\nYou see a path to the left and a path to the right.", 
                                   font=("Arial", 12), justify="center")
        self.text_label.pack(pady=10)

        # Choice Buttons Frame
        self.btn_frame = tk.Frame(root)
        self.btn_frame.pack(pady=10)

        self.left_btn = tk.Button(self.btn_frame, text="Go Left", width=15, command=self.choose_left)
        self.left_btn.grid(row=0, column=0, padx=10)

        self.right_btn = tk.Button(self.btn_frame, text="Go Right", width=15, command=self.choose_right)
        self.right_btn.grid(row=0, column=1, padx=10)

    def choose_left(self):
        # Update image to exit
        if self.img_exit:
            self.image_label.config(image=self.img_exit)
        
        # Update text and disable buttons
        self.text_label.config(text="You walk down the left path and find a way out of the woods!\nYou win!")
        self.left_btn.config(state=tk.DISABLED)
        self.right_btn.config(state=tk.DISABLED)

    def choose_right(self):
        # Keep forest background and show loop message
        self.text_label.config(text="You walk down the right path and found yourself in the same spot again.\nChoose again:")

if __name__ == "__main__":
    root = tk.Tk()
    game = ForestGame(root)
    root.mainloop()
    