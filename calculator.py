import tkinter as tk
def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operation_var.get()
        if operation == '+':
            result.set(num1 + num2)
        elif operation == '-':
            result.set(num1 - num2)
        elif operation == '*':
            result.set(num1 * num2)
        elif operation == '/':
            if num2 == 0:
                result.set("Error (÷0)")   
            else:
                result.set(num1 / num2)
        else:
            result.set("Invalid operator")
    except ValueError:
        result.set("Enter numbers")
root = tk.Tk()
root.title("CALCULATOR")
entry1 =  tk.Entry(root) 
entry1.grid(row=0,column=1)
entry2 = tk.Entry(root)
entry2.grid(row=1,column=1)
window_width = 600
window_height = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_x = int(screen_width/ 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)
root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")
tk.Label(root,text="Number 1").grid(row=0)
tk.Label(root, text="Number 2").grid(row=1) 
operation_var = tk.StringVar(root) 
operation_var.set('+')
operations_menu = tk.OptionMenu(root, operation_var, '+', '-', '*', '/')
operations_menu.grid(row=2, column=1)
tk.Button(root, text='Calculate', command=calculate).grid(row=3, column=1)
result = tk.StringVar()
tk.Label(root, textvariable=result).grid(row=4, column=1)
root.mainloop()                                 
