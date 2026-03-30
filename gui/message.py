from tkinter import messagebox, Tk

class ErrorMessage(Tk):
    def __init__(self, message: str):
        self.message = message

    def __str__(self):
        return f"Error: {self.message}"
    
    def show_error(self):
        messagebox.showerror("Error", self.message)
    
    
class SuccessMessage(Tk):
    def __init__(self, message: str):
        self.message = message

    def show_success(self):
        messagebox.showinfo("Success", self.message)

    def __str__(self):
        return f"Success: {self.message}"


if __name__ == "__main__":
    error_msg = ErrorMessage("Invalid account number.")
    success_msg = SuccessMessage("Deposit successful.")
    
    print(error_msg)
    print(success_msg)
    
    
    
