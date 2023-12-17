import tkinter as tk
from tkinter import ttk, colorchooser, simpledialog

class CustomWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Apk Editor")

        window_width = 400
        window_height = 300
        self.root.geometry(f"{window_width}x{window_height}")

        header = tk.Frame(root, bg='#3498db')
        header.pack(side=tk.TOP, fill=tk.X)

        close_button = tk.Label(header, text='X', font=('Arial', 16), bg='#e74c3c', fg='#fff', padx=5, cursor='hand2')
        close_button.pack(side=tk.RIGHT)
        close_button.bind("<Button-1>", lambda e: self.close_window())

        ttk.Label(header, text="Contrast", background='#3498db', foreground='#fff').pack(side=tk.LEFT, padx=5)
        self.contrast_slider = ttk.Scale(header, from_=-1, to=20, orient=tk.HORIZONTAL, command=self.adjust_contrast)
        self.contrast_slider.set(0)
        self.contrast_slider.pack(side=tk.LEFT, pady=5, padx=5, fill=tk.X)

        color_button = tk.Button(header, text='Color', command=self.choose_color)
        color_button.pack(side=tk.LEFT)

        self.canvas = tk.Canvas(root, width=100, height=100, bg='white')
        self.canvas.pack(expand=True)
        self.canvas.bind("<Button-1>", self.change_color)

        length_frame = tk.Frame(root, bg='#3498db')
        length_frame.pack(side=tk.BOTTOM, fill=tk.X)

        length_button = tk.Button(length_frame, text='Panjang', command=self.set_length)
        length_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.length_label = tk.Label(length_frame, text='Panjang: 100', font=('Arial', 12), bg='#3498db', fg='#fff')
        self.length_label.pack(side=tk.LEFT, padx=5, pady=5)

        width_button = tk.Button(length_frame, text='Lebar', command=self.set_width)
        width_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.width_label = tk.Label(length_frame, text='Lebar: 100', font=('Arial', 12), bg='#3498db', fg='#fff')
        self.width_label.pack(side=tk.LEFT, padx=5, pady=5)

        generate_button = tk.Button(length_frame, text='Generate', command=self.generate_canvas)
        generate_button.pack(side=tk.LEFT, padx=5, pady=5)

        zoom_in_button = tk.Button(header, text='Zoom In', command=self.zoom_in)
        zoom_in_button.pack(side=tk.LEFT)

        zoom_out_button = tk.Button(header, text='Zoom Out', command=self.zoom_out)
        zoom_out_button.pack(side=tk.LEFT)

        # Simpan nilai kontras awal dan ukuran awal
        self.initial_contrast = 0
        self.initial_length = 100
        self.initial_width = 100
        # Simpan warna yang dapat diubah
        self.custom_color = 'white'

    def close_window(self):
        try:
            self.root.destroy()
        except Exception as e:
            print(f"Error closing window: {e}")

    def adjust_contrast(self, value):
        try:
            value = float(value)
            color = self.canvas.cget("bg")
            r, g, b = int(color[1:3], 16), int(color[3:5], 16), int(color[5:7], 16)
            factor = (value + 100) / 100.0

            avg = (r + g + b) // 3
            new_r = min(255, max(0, int(avg + factor * (r - avg))))
            new_g = min(255, max(0, int(avg + factor * (g - avg))))
            new_b = min(255, max(0, int(avg + factor * (b - avg))))

            new_color = f"#{new_r:02X}{new_g:02X}{new_b:02X}"
            self.canvas.configure(bg=new_color)
            # Update warna yang dapat diubah saat mengubah kontras
            self.custom_color = new_color
        except Exception as e:
            print(f"Error adjusting contrast: {e}")

    def choose_color(self):
        try:
            color = colorchooser.askcolor()[1]
            print('Chosen color:', color)
            self.canvas.configure(bg=color)
            # Update warna yang dapat diubah saat memilih warna
            self.custom_color = color
        except Exception as e:
            print(f"Error choosing color: {e}")

    def change_color(self, event):
        try:
            # Gunakan warna yang dapat diubah saat mengganti warna di kanvas
            self.canvas.configure(bg=self.custom_color)
        except Exception as e:
            print(f"Error changing color: {e}")

    def set_width(self):
        try:
            length_options = [50, 100, 150, 500]
            selected_length = simpledialog.askinteger("Pilih Panjang", "Pilih panjang:", initialvalue=self.initial_length, minvalue=50, maxvalue=500)
            if selected_length is not None:
                self.length_label.config(text=f'Panjang: {selected_length}')
                self.initial_length = selected_length
        except Exception as e:
            print(f"Error setting length: {e}")

    def set_length(self):
        try:
            width_options = [50, 100, 150, 500]
            selected_width = simpledialog.askinteger("Pilih Lebar", "Pilih lebar:", initialvalue=self.initial_width, minvalue=50, maxvalue=500)
            if selected_width is not None:
                self.width_label.config(text=f'Lebar: {selected_width}')
                self.initial_width = selected_width
        except Exception as e:
            print(f"Error setting width: {e}")

    def generate_canvas(self):
        try:
            self.update_canvas_size()
            print('Canvas dihasilkan dengan panjang:', self.initial_length, 'dan lebar:', self.initial_width)
        except Exception as e:
            print(f"Error generating canvas: {e}")

    def zoom_in(self):
        try:
            self.initial_length *= 1.2  # Faktor zoom in
            self.initial_width *= 1.2
            self.update_canvas_size()
            print('Zoom In:', self.initial_length, self.initial_width)
        except Exception as e:
            print(f"Error zooming in: {e}")

    def zoom_out(self):
        try:
            self.initial_length /= 1.2  # Faktor zoom out
            self.initial_width /= 1.2
            self.update_canvas_size()
            print('Zoom Out:', self.initial_length, self.initial_width)
        except Exception as e:
            print(f"Error zooming out: {e}")

    def update_canvas_size(self):
        length = int(self.initial_length)
        width = int(self.initial_width)
        self.canvas.config(width=length, height=width)
        self.length_label.config(text=f'Panjang: {length}')
        self.width_label.config(text=f'Lebar: {width}')

if __name__ == "__main__":
    root = tk.Tk()
    app = CustomWindow(root)
    root.mainloop()
