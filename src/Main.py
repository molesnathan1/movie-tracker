from System import System
from App import Signin
import tkinter as tk

def main(): 
    system = System()

    root = tk.Tk()
    root.update_idletasks()
    root.geometry("1000x600")
    app = Signin(root, system)
    root.mainloop()

    del system

if __name__ == '__main__':
    main()