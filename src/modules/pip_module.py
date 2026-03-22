import tkinter as tk;from tkinter import ttk; import threading ; import subprocess


def install_module(module_name):
    try:
        subprocess.run(f'start cmd /k pip install {module_name.strip()}', shell = True, text = True, capture_output=True)
    except Exception as e:
        print(e)

def uninstall_module(module_name):
    try:
        subprocess.run(f'start cmd /k pip uninstall {module_name.strip()}', shell = True, text = True, capture_output=True)
    except Exception as e:
        print(e)
def list_all_modules():
    try:
        subprocess.run(f'start cmd /k pip list', shell = True, text = True, capture_output=True)
    except Exception as e:
        print(e)


def module_inspector(module_name, information_listbox):
    try:
        information_listbox.delete(0, 'end')
        module_information = subprocess.run(f'pip show {module_name.strip()}', shell = True, text = True, capture_output=True).stdout 
        module_information_list = module_information.strip().split('\n')
        for item in module_information_list:
            information_listbox.insert(tk.END, item)
    except Exception as e:
        print(e)

    return 'break'




def pip_module(master, bg, fg, font, dbg):

    toplevel = tk.Toplevel(master)
    toplevel.wm_attributes('-toolwindow', True)
    toplevel.resizable(0,0)  
    pipfuncs_frame = tk.Frame(toplevel,  bg = bg)
    pipfuncs_frame.pack(expand=True, fill = 'both')


    download_module_frame = tk.LabelFrame(pipfuncs_frame , text = 'Install package&library', font = (font, 10), bg=bg, fg = fg)
    download_module_frame.grid(row = 0, column = 0, padx = 10, pady=5)
    def install_module_():
        module_name = module_name_entry.get()
        install_module(module_name=module_name)

    module_name_label = tk.Label(download_module_frame, text = ' Module name', font = (font, 9), bg =bg, fg = fg)
    module_name_label.grid(row = 0, column = 0, padx= 5, pady = 5)

    module_name_entry = ttk.Entry(download_module_frame, font = (font, 9), width = 25)
    module_name_entry.grid(row=0, column = 1, padx = (0,5), pady = 5)

    install_module_button = ttk.Button(download_module_frame, text = 'Install' , width = 15, command=lambda: threading.Thread(target = install_module_, daemon=True).start())
    install_module_button.grid(row = 0, column = 2, pady = 5, padx = (0, 10))

    
    uninstall_module_frame = tk.LabelFrame(pipfuncs_frame , text = 'Uninstall package&library', font = (font, 10), bg=bg, fg = fg)
    uninstall_module_frame.grid(row = 1, column = 0, padx = 10, pady=5)
    def uninstall_module_():
        module_name_ = module_name_entry2.get()
        uninstall_module(module_name=module_name_)

    module_name_label2 = tk.Label(uninstall_module_frame, text = ' Module name', font = (font, 9), bg =bg, fg = fg)
    module_name_label2.grid(row = 0, column = 0, padx= 5, pady = 5)

    module_name_entry2 = ttk.Entry(uninstall_module_frame, font = (font, 9), width = 25)
    module_name_entry2.grid(row=0, column = 1, padx = (0,5), pady = 5)

    uninstall_module_button = ttk.Button(uninstall_module_frame, text = 'Uninstall',  width = 15, command = lambda: threading.Thread(target = uninstall_module_, daemon=True).start())
    uninstall_module_button.grid(row = 0, column = 2, pady = 5, padx = (0, 10))


    information_module_frame = tk.LabelFrame(pipfuncs_frame , text = 'Information for package&library', font = (font, 10), bg=bg, fg = fg)
    information_module_frame.grid(row = 2, column = 0, padx = 10, pady=5)


    def insert_module_information():
        final_module_name = module_name_entry3.get()
        module_inspector(module_name=final_module_name, information_listbox=information_module_listbox)

    module_name_label3 = tk.Label(information_module_frame, text = ' Module name', font = (font, 9), bg =bg, fg = fg)
    module_name_label3.grid(row = 0, column = 0, padx= 5, pady = 5)

    module_name_entry3 = ttk.Entry(information_module_frame, font = (font, 9), width = 25)
    module_name_entry3.grid(row=0, column = 1, padx = (0,5), pady = 5)

    show_module_button = ttk.Button(information_module_frame, text = 'Show',  width = 15, command = insert_module_information)
    show_module_button.grid(row = 0, column = 2, pady = 5, padx = (0, 10))


    module_information_list_frame = tk.Frame(information_module_frame, bg = bg)
    module_information_list_frame.grid(row=1, column=0, columnspan=15, padx = 5, pady = 5)

    scrollbar_list_information = tk.Scrollbar(module_information_list_frame, orient=tk.VERTICAL)
    scrollbar_list_information.pack(side='right', fill='y')

    Hscrollbar_list_information = tk.Scrollbar(module_information_list_frame, orient=tk.HORIZONTAL)
    Hscrollbar_list_information.pack(side='bottom', fill='x')

    information_module_listbox = tk.Listbox(module_information_list_frame, bd = 0, relief='solid', font = (font, 10),
                                             width = 50, height=17, bg = dbg, fg= fg)
    information_module_listbox.pack(side='left', fill = 'both')

    information_module_listbox.config(yscrollcommand=scrollbar_list_information.set, xscrollcommand=Hscrollbar_list_information.set)
    scrollbar_list_information.config(command=information_module_listbox.yview)
    Hscrollbar_list_information.config(command = information_module_listbox.xview)

    
    def list_packages():
        list_all_modules()

    modules_packages_list_button = ttk.Button(pipfuncs_frame, text = 'List installed packages', width = 65, command=lambda: threading.Thread(target=list_packages, daemon=True).start())
    modules_packages_list_button.grid(row=3, column = 0, padx = 5, pady = (5,10))


    toplevel.title('PIP module')
    toplevel.mainloop()
    