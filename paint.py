import tkinter as tk
from tkinter import colorchooser

# Class for paint
class SimplePainter:
    def __init__(self, master):
        self.master = master
        self.master.title("Painter") 
        self.master.geometry("600x400")  
        self.master.configure(bg="darkblue")  

        self.brush_color = "white" 

        # Create a canvas
        self.drawing_area = tk.Canvas(self.master, bg="white", width=600, height=350)
        self.drawing_area.pack(pady=10)

        
        self.drawing_area.bind("<B1-Motion>", self.draw)

        # Button to change color
        self.color_button = tk.Button(self.master, text="Change Color", command=self.pick_color)
        self.color_button.pack()

    # draw on the canvas
    def draw(self, event):
        brush_size = 5  # Fixed size for brush
        x1, y1 = (event.x - brush_size), (event.y - brush_size)
        x2, y2 = (event.x + brush_size), (event.y + brush_size)
        self.drawing_area.create_oval(x1, y1, x2, y2, fill=self.brush_color, outline=self.brush_color)

    def pick_color(self):
        new_color = colorchooser.askcolor()[1]  # Open color picker
        if new_color:
            self.brush_color = new_color  # Set new brush color


if __name__ == "__main__":
    root = tk.Tk()
    app = SimplePainter(root)
    root.mainloop()