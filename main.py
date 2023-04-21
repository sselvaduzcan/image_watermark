from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont
import customtkinter


customtkinter.set_default_color_theme("blue")
ImageDraw.fontmode = "L"
im = None

# Uploads image
def upload():
    global path
    path = filedialog.askopenfilename(filetypes=[('image files', '.jpg'), ('image files', '.jpeg')])
    add_wm()


# Shows the chosen photo
def add_wm():
    global im
    im = Image.open(path)
    display_image()


def display_image():
    display_img = customtkinter.CTkImage(im, size=(400, 300))
    panel.configure(image=display_img)
    panel.image = display_img


# Adds watermark
def write_wm():
    tx = text_to_add.get()

    with Image.open(path).convert("RGBA") as base:
        # make a blank image for the text, initialized to transparent text color
        txt = Image.new("RGBA", base.size, (255, 255, 255, 0))

        # get a font
        fnt = ImageFont.truetype("C:\Windows\Fonts\\magnetob.ttf", 80)
        # get a drawing context
        d = ImageDraw.Draw(txt)

        # draw text, half opacity
        d.text((base.size[0]/2-20, base.size[1]/2-20), tx, font=fnt, fill=(255, 255, 255, 128), anchor="mm")

        out = Image.alpha_composite(base, txt)
        out.save(f"watermarked_{path.split('/')[-1].split('.')[0]}.png")
        out.show()


window = customtkinter.CTk()

window.geometry("800x800+0+0")
window.resizable(width=True, height=True)

upload_b = customtkinter.CTkButton(master=window, text="Upload", command=upload)
upload_b.place(relx=0.5, rely=0.1, anchor=CENTER)

if im:
    display_img = customtkinter.CTkImage(Image.open(im))
    panel = customtkinter.CTkLabel(master=window, image=display_img)
    panel.place(relx=0.5, rely=0.4, anchor=CENTER)
else:
    panel = customtkinter.CTkLabel(master=window, text="")
    panel.place(relx=0.5, rely=0.4, anchor=CENTER)

write_b = customtkinter.CTkButton(master=window, text="Write", command=write_wm)
write_b.place(relx=0.5, rely=0.8, anchor=CENTER)

text_to_add = customtkinter.CTkEntry(master=window, width=300)
text_to_add.place(relx=0.5, rely=0.7, anchor=CENTER)

window.mainloop()
