import tkinter as tk
from tkinter import messagebox, filedialog
import qrcode
from PIL import Image, ImageTk

class QRCodeGeneratorApp:
    def __init__(self, master):
        self.master = master
        master.title("QR Code Generator")

        self.label = tk.Label(master, text="Enter Ticket Information:")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.generate_button = tk.Button(master, text="Generate QR Code", command=self.generate_qr_code)
        self.generate_button.pack()

        self.save_button = tk.Button(master, text="Save QR Code", command=self.save_qr_code)
        self.save_button.pack()

        self.qr_label = tk.Label(master)
        self.qr_label.pack()

    def generate_qr_code(self):
        ticket_info = self.entry.get()

        # Generate QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(ticket_info)
        qr.make(fit=True)

        # Create an image from the QR Code instance
        qr_img = qr.make_image(fill_color="black", back_color="white")

        # Convert Image object to Tkinter PhotoImage
        img = ImageTk.PhotoImage(qr_img)

        # Update QR code label
        self.qr_label.config(image=img)
        self.qr_label.image = img

        self.qr_img = qr_img  # Store the QR image for saving

    def save_qr_code(self):
        if not hasattr(self, 'qr_img'):
            messagebox.showerror("Error", "No QR code generated yet.")
            return

        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if file_path:
            self.qr_img.save(file_path)

def main():
    root = tk.Tk()
    app = QRCodeGeneratorApp(root)
    root.geometry("500x500")
    root.minsize(200,200)
    root.mainloop()

if __name__ == "__main__":
    main()
