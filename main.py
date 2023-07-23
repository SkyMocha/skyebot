import tkinter
from tkinter import SW
from PIL import ImageTk
from PIL import Image
import time
from random import randint
from elevenlabs import generate, stream, set_api_key
import json

set_api_key(json.load(open('config.json'))['ELEVENLABS_KEY'])

audio = generate(
    text="kjlsdfan",
    voice="skye_voice_trained",
    stream=True
)

class SkyeBot(object):
    def __init__(self, master, filename_top, filename_bottom, **kwargs):
        self.master = master
        self.filename_top = filename_top
        self.filename_bottom = filename_bottom
        
        self.canvas = tkinter.Canvas(master,bg="#00ff00", width=500, height=500)
        self.canvas.pack()

        self.speaking = True

        self.process_next_frame = self.draw().__next__  # Using "next(self.draw())" doesn't work
        master.after(1, self.process_next_frame)

    def draw(self):
        image_top = Image.open(self.filename_top)
        image_bottom = Image.open(self.filename_bottom)
        print(self.process_next_frame)
        while True:
            if self.speaking:
                angle = randint(8, 16)*-1
                offset_x = randint(18,24)
                offset_y = 0
            else:
                angle = 0
                offset_x = 0
                offset_y = 0

            tkimage_top = ImageTk.PhotoImage(image_top.rotate(angle))
            tkimage_bottom = ImageTk.PhotoImage(image_bottom)
            canvas_top = self.canvas.create_image(128+offset_x, 258+offset_y, anchor=SW, image=tkimage_top)
            canvas_bottom = self.canvas.create_image(0, 500, anchor=SW, image=tkimage_bottom)
            self.master.after_idle(self.process_next_frame)
            yield
            self.canvas.delete(canvas_top)
            time.sleep(randint(1, 10) * 0.01)

root = tkinter.Tk()
stream (audio)
app = SkyeBot(root, './assets/Top.png', './assets/Bottom.png')
root.mainloop()
