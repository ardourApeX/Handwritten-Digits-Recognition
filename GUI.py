from tkinter import *
import os
from keras.models import load_model

model = None
def Load_Model():
	global model
	model = load_model("./model/model.h5")
	print("Model Loaded Successfully!")

window = Tk()
window.geometry("400x400")
window.title("Hand-Written Digit Recognition")
window.configure(bg = "light blue")

load_model_button = Button(window, text = "Load Model", fg = "white", bg = "blue", width = 14, height = 2, relief = RAISED, command = Load_Model)
load_model_button.place(x = 110, y = 110)
window.mainloop()