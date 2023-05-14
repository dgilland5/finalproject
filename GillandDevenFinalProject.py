import tkinter as tk
from PIL import ImageTk, Image
class MainApplication:
    def __init__(self, master):
        self.master = master
        self.master.title("Panel Viewer")
        self.master.iconbitmap("icon.ico")
        self.image1 = ImageTk.PhotoImage(Image.open("image1.png"))
        self.image2 = ImageTk.PhotoImage(Image.open("image2.png"))
        self.image3 = ImageTk.PhotoImage(Image.open("image3.png"))

        # Loads the background image and resizes it to fit the window
        background_image = Image.open("background.jpg")
        background_image = background_image.resize((300, 150), resample=Image.LANCZOS)
        self.background_image_tk = ImageTk.PhotoImage(background_image)
        self.background_label = tk.Label(self.master, image=self.background_image_tk)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.create_widgets()
    def create_widgets(self):
        # Three buttons that each open a new window with a image and text
        self.button1 = tk.Button(self.master, text="Click to view!", command=self.display_image1)
        self.button1.grid(row=0, column=0, padx=10, pady=10)
        self.label1 = tk.Label(self.master, text="Oak Panel")
        self.label1.grid(row=1, column=0)
        self.button2 = tk.Button(self.master, text="Click to view!", command=self.display_image2)
        self.button2.grid(row=0, column=1, padx=10, pady=10)
        self.label2 = tk.Label(self.master, text="Walnut Panel")
        self.label2.grid(row=1, column=1)
        self.button3 = tk.Button(self.master, text="Click to view!", command=self.display_image3)
        self.button3.grid(row=0, column=2, padx=10, pady=10)
        self.label3 = tk.Label(self.master, text="Maple Panel")
        self.label3.grid(row=1, column=2)
        # Label with instruction text and exit button to close out of the program
        self.intro_label = tk.Label(self.master, text="Please view a selection of our panels!")
        self.intro_label.grid(row=2, column=0, columnspan=3, pady=10)
        self.exit_button = tk.Button(self.master, text="Exit", command=self.master.quit)
        self.exit_button.grid(row=3, column=1, pady=10)
        # Loads Image 1 in new window
    def display_image1(self):
        new_window = tk.Toplevel(self.master)
        image_label = tk.Label(new_window, image=self.image1)
        image_label.image = self.image1
        image_label.pack()
        alt_text_label = tk.Label(new_window, text="Here is a example of our oak panels!")
        alt_text_label.pack()
        # Loads Image 2 in new window
    def display_image2(self):
        new_window = tk.Toplevel(self.master)
        image_label = tk.Label(new_window, image=self.image2)
        image_label.image = self.image2
        image_label.pack()
        alt_text_label = tk.Label(new_window, text="Here is a example of our walnut panels!")
        alt_text_label.pack()
        # Loads Image 3 in new window
    def display_image3(self):
        new_window = tk.Toplevel(self.master)
        image_label = tk.Label(new_window, image=self.image3)
        image_label.image = self.image3
        image_label.pack()
        alt_text_label = tk.Label(new_window, text="Here is a example of our maple panels!")
        alt_text_label.pack()
def main():
    root = tk.Tk()
    app = MainApplication(root)
    x_coord = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
    y_coord = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
    root.geometry(f"300x150+{int(x_coord)}+{int(y_coord)}")
    root.mainloop()
if __name__ == "__main__":
    main()