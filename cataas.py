from tkinter import *
from PIL import Image, ImageTk
import requests
from io import BytesIO

def load_image():
    pass

root = Tk()
root.title('Cats!')
root.geometry('600x480')

label = Label()
label.pack()

url = 'https://cataas.com/cat'
img = load_image(url)

if img:
    label.config(image=img)
    label.image = img

root.mainloop()