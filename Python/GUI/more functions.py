from tkinter import *
root=Tk()

# size of GUI window
root.geometry("744x544")

# title
root.title("The Best GUI Ever ")

# icon
root.wm_iconbitmap("1.ico")

# def speaker(str):
#     from win32com.client import Dispatch
#     speak= Dispatch("SAPI.SpVoice")
#     speak.Speak(str)

# to get the height-width of the screen
width=root.winfo_screenwidth()
height=root.winfo_screenheight()
# print(f"{width}x{height}")

root.mainloop()