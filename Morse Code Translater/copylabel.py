from tkinter import *
from tkinter.messagebox import showinfo


class CopyLabel(Tk):
    def __init__(self, text: str):
        super(CopyLabel, self).__init__()
        self.title('Your Translation')
        self.label_text = text
        self.label = Label(self, text=text)
        self.label.pack(pady=10, padx=40)
        self.copy_button = Button(self, text='COPY TO CLIPBOARD', command=self.copy)
        self.copy_button.pack(pady=5, padx=40)

    def copy(self):
        self.clipboard_clear()
        self.clipboard_append(self.label_text)
        self.update()
        showinfo(parent=self, message='Copied to clipboad!')

