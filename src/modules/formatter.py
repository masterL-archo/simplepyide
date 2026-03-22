
import black 
import tkinter as tk 
from tkinter import ttk 



def BlackFormatter(app_title, master, code_box):
    def format_code() -> None:
        try:
            code = code_box.get('1.0', tk.END)
            mode_ = black.Mode(
                line_length= int(line_length_var.get()), 
                string_normalization= not skip_string_norm_var.get(), 
                magic_trailing_comma= not skip_trailing_comma_var.get()
            )
            formatted_code = black.format_str(code, mode=mode_)
            code_box.delete('1.0', tk.END)
            code_box.insert('1.0', formatted_code)
        except Exception as e:
            print(e)

    toplevel = tk.Toplevel(master)
    # All Black formatter widgets are just here. 

    skip_string_norm_var = tk.BooleanVar()
    skip_trailing_comma_var = tk.BooleanVar()
    line_length_var = tk.StringVar(value="88")

    # Checkboxes
    ttk.Checkbutton(toplevel, text="Skip string normalization", variable=skip_string_norm_var).pack(anchor=tk.W, padx=10, pady=5)
    ttk.Checkbutton(toplevel, text="Skip magic trailing comma", variable=skip_trailing_comma_var).pack(anchor=tk.W, padx=10, pady=5)

    # Line length entry
    line_frame = ttk.Frame(toplevel)
    line_frame.pack(anchor=tk.W, padx=10, pady=5)
    ttk.Label(line_frame, text="Line length:").pack(side=tk.LEFT)
    ttk.Entry(line_frame, width=5, textvariable=line_length_var).pack(side=tk.LEFT)

    # Button to print configuration (example usage)
    ttk.Button(toplevel, text="Format", command = format_code).pack(pady=10)



    toplevel.title(f'{app_title} - Black formatter')

    # Popup in the middle of the screen. 
    width = 220
    height = 137
    screen_width = toplevel.winfo_screenwidth()
    screen_height = toplevel.winfo_screenheight()

    x = (screen_width // 2) - (width // 2) - 10
    y = ((screen_height // 2) - (height // 2)) - 35
    toplevel.geometry(f'{width}x{height}+{x}+{y}') # Setting the geametry 
    toplevel.resizable(False, False) # No resizablitiy 
    toplevel.wm_attributes('-toolwindow', True)
    toplevel.mainloop()



