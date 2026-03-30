from tkinter import Tk, Frame, Label, Button
# Format idget_name = tk.WidgetType(parent_container, option1=value, option2=value)
class LogonWindow(Tk):
    def __init__(self):
        super().__init__()
        self.title("SecureBank Logon")
        self.geometry("1000x700")

        self.label = Label(self, text="Hello, World!")
        self.label.pack(pady=20)

        self.button = Button(self, text="Click Me", command=self.on_button_click)
        self.button.pack(pady=10)
        
        self.frame = Frame(self, bg="black", width=300, height=100)
        self.frame.pack(pady=10)

    def on_button_click(self):
        self.label.config(text="Button Clicked!")
        
if __name__ == "__main__":
    app = LogonWindow()
    app.mainloop()
    
    