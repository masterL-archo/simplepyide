import subprocess
import tkinter as tk 
from tkinter import ttk 

import os 


comm = subprocess.run('where python', capture_output=True, shell=True, text=True)

interpreters = [path.strip() for path in comm.stdout.splitlines() if path.strip()]


def run_file(file_path, code_box, interpath, alogs_list,   live_interpreter, chunk_size = 1024):
    try:
        file_extension = os.path.splitext(file_path)[1]
        if file_extension == '.py':
            if file_path == '':
                pass
            else:
                save_contents = code_box.get('1.0', tk.END)
                with open(file_path, 'w', encoding='utf-8') as writer:
                    for start in range(0, len(save_contents), chunk_size):
                        writer.write(save_contents[start: start + chunk_size])
            command = f'\"{interpath}\" \"{file_path}\"'
            x = subprocess.run(f'start cmd /k "{command}" ', shell = True, cwd = os.path.dirname(file_path), text = True)
            alogs_list.insert(tk.END, f'ACTION: File ({os.path.basename(file_path)}) was ran using {live_interpreter}')
        else:
            alogs_list.insert(tk.END, 'ERROR: Unable to run a non python file.')
            alogs_list.itemconfig(tk.END, {'fg':'red'})
    except Exception as e:
        pass
    

def run_python_shell(alogs, interpath):
    print(interpath)
    try:
         subprocess.run(f'start cmd /k{interpath}', shell = True)
         alogs.insert(tk.END, 'Python shell is running.')
    except Exception as e:
        print(e)

def start_terminal(alogs):
    try:
        subprocess.run(f'start cmd', shell=True )
        alogs.insert(tk.END, 'Started the terminal.')
    except Exception as e:
        print(e)



