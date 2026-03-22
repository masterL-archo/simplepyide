import tkinter as tk 
import os
from pygments.lexers.python import Python3Lexer



already_chosen_file = ''
project_files = []



def is_binary_file(file_path):
    try:
        with open(file_path, 'rb') as file:
            chunk = file.read(512)
            if not chunk:
                return False  
            if b'\x00' in chunk:
                return True 
            text_chars = bytearray(range(32, 127)) + b'\n\r\t\b'
            nontext = [byte for byte in chunk if byte not in text_chars]
            if len(nontext) / len(chunk) > 0.3:
                return True
            return False
    except Exception:
        return True



def open_file(file_path: str, code_box, files_listbox, alogs_list, forget_label , chunk_size=1024):
    forget_label.place_forget()
    global already_chosen_file, project_files
    if file_path:
        if file_path in project_files:
            alogs_list.insert(tk.END, f'File is already in the project list.')
            return
        else:
            if already_chosen_file == '':
                try:
                    if os.path.exists(file_path):
                        if is_binary_file(file_path=file_path):
                            alogs_list.insert(tk.END, f'Error: Unable to read binary files.')
                            alogs_list.itemconfig(tk.END, {'fg':'red'})
                        else:
                            already_chosen_file = file_path
                            project_files.append(file_path)
                            code_box.delete('1.0', tk.END)
                            with open(file_path, 'r', encoding='utf-8') as reader:
                                while True:
                                    try:
                                        contents = reader.read(chunk_size)
                                    except Exception as e:
                                        alogs_list.insert(tk.END, f'Error: {e}')
                                        alogs_list.itemconfig(tk.END, {'fg':'red'})
                                        break
                                    if not contents:
                                        break
                                    try:
                                        code_box.insert(tk.END, contents)
                                        code_box.update_idletasks()
                                    except Exception as e:
                                        alogs_list.insert(tk.END, f'Error: {e}')
                                        alogs_list.itemconfig(tk.END, {'fg':'red'})

                            files_listbox.insert(tk.END, file_path)
                            files_listbox.selection_clear(0, tk.END)
                            files_listbox.selection_set(tk.END)
                            code_box.edit_reset()
                            
                except Exception as e:
                    alogs_list.insert(tk.END, f'Error: {e}')
                    alogs_list.itemconfig(tk.END, {'fg':'red'})
                    
            else:
                try:
                    with open(already_chosen_file, 'w', encoding='utf-8') as writer:
                        contents = code_box.get('1.0', tk.END)
                        for start in range(0, len(contents), chunk_size):
                            try:
                                writer.write(contents[start:start + chunk_size])
                            except Exception as e:
                                alogs_list.insert(tk.END, f'Error: {e}')
                                alogs_list.itemconfig(tk.END, {'fg':'red'})

                    already_chosen_file = file_path
                    project_files.append(file_path)
                    code_box.delete('1.0', tk.END)
                    with open(file_path, 'r', encoding='utf-8') as reader:
                        while True:
                            try:
                                contents = reader.read(chunk_size)
                            except Exception as e:
                                alogs_list.insert(tk.END, f'Error: {e}')
                                alogs_list.itemconfig(tk.END, {'fg':'red'})
                                break
                            if not contents:
                                break
                            try:
                                code_box.insert(tk.END, contents)
                                code_box.update_idletasks()
                            except Exception as e:
                                alogs_list.insert(tk.END, f'Error: {e}')
                                alogs_list.itemconfig(tk.END, {'fg':'red'})

                    files_listbox.insert(tk.END, file_path)
                    files_listbox.selection_clear(0, tk.END)
                    files_listbox.selection_set(tk.END)
                    code_box.edit_reset()
                except Exception as e:
                    alogs_list.insert(tk.END, f'Error: {e}')
                    alogs_list.itemconfig(tk.END, {'fg':'red'})
    else:
        pass

def try_last_chosen(content, code_box, files_listbox, alogs_listbox, forget_label, master):
    if content:
        path = content 
        # withdraw
        master.withdraw()
        open_file(file_path=path, code_box=code_box, files_listbox=files_listbox, alogs_list=alogs_listbox, forget_label=forget_label) # if there was a last a last chosen file we make contents.
        # relaunch 
        master.deiconify()
    else:
        pass


def _on_switch(files_listbox, code_box, alogs_list, forget_label,chunk_size=1024):
    forget_label.place_forget()
    global already_chosen_file
    if not already_chosen_file:
        return

    try:
        contents = code_box.get('1.0', tk.END)
    except Exception as e:
        alogs_list.insert(tk.END, f'Error: {e}')
        alogs_list.itemconfig(tk.END, {'fg':'red'})
        contents = ''

    try:
        with open(already_chosen_file, 'w', encoding='utf-8') as writer:
            for start in range(0, len(contents), chunk_size):
                try:
                    writer.write(contents[start:start + chunk_size])
                except Exception as e:
                    alogs_list.insert(tk.END, f'Error: {e}')
                    alogs_list.itemconfig(tk.END, {'fg':'red'})

    except Exception as e:
        alogs_list.insert(tk.END, f'Error saving file: {e}')

    try:
        selection = files_listbox.curselection()
    except Exception as e:
        alogs_list.insert(tk.END, f'Error: {e}')
        alogs_list.itemconfig(tk.END, {'fg':'red'})
        selection = []

    if not selection:
        return

    try:
        new_path = files_listbox.get(selection[0])
    except Exception as e:
        alogs_list.insert(tk.END, f'Error: {e}')
        alogs_list.itemconfig(tk.END, {'fg':'red'})
        return

    try:
        already_chosen_file = new_path
    except Exception as e:
        alogs_list.insert(tk.END, f'Error: {e}')
        alogs_list.itemconfig(tk.END, {'fg':'red'})

    code_box.delete('1.0', tk.END)
    try:
        with open(new_path, 'r', encoding='utf-8') as reader:
            while True:
                try:
                    chunk = reader.read(chunk_size)
                except Exception as e:
                    alogs_list.insert(tk.END, f'Error: {e}')
                    alogs_list.itemconfig(tk.END, {'fg':'red'})
                    break
                if not chunk:
                    break
                code_box.insert(tk.END, chunk)
    

    except Exception as e:
        alogs_list.insert(tk.END, f'Error switching files: {e}')
    code_box.edit_reset()

def save_file(code_box, alogs_list , chunk_size=1024):
    global already_chosen_file, project_files , ext_to_lexer
    try:
        if already_chosen_file == '':
            pass
        else:
            save_contents = code_box.get('1.0', tk.END)
            with open(already_chosen_file, 'w', encoding='utf-8') as writer:
                for start in range(0, len(save_contents), chunk_size):
                    try:
                        writer.write(save_contents[start: start + chunk_size])
                    except Exception as e:
                        alogs_list.insert(tk.END, f'Error: {e}')
                        alogs_list.itemconfig(tk.END, {'fg':'red'})
    except Exception as e:
        alogs_list.insert(tk.END, f'Error: {e}')
        alogs_list.itemconfig(tk.END, {'fg':'red'})

def save_as(new_file_path: str, code_box, list_box, alogs_list, forget_label, chunk_size = 1024):
    forget_label.place_forget()
    global already_chosen_file, project_files , ext_to_lexer
    try:
        if already_chosen_file:
            try:
                with open(already_chosen_file, 'w', encoding='utf-8') as writer:
                    contents = code_box.get('1.0', tk.END)
                    for start in range(0, len(contents), chunk_size):
                        try:
                            writer.write(contents[start: start + chunk_size])
                        except Exception as e:
                            alogs_list.insert(tk.END, f'Error: {e}')
                            alogs_list.itemconfig(tk.END, {'fg':'red'})
            except Exception as e:
                alogs_list.insert(tk.END, f'Error: {e}')
                alogs_list.itemconfig(tk.END, {'fg':'red'})
        else:
            pass

        new_contents = code_box.get('1.0', tk.END)
        new_file = new_file_path

        if new_file in project_files:
            pass

        else:
            already_chosen_file = new_file
            try:
                with open(new_file, 'w', encoding='utf-8') as writer:
                    for start in range(0, len(new_contents), chunk_size):
                        try:
                            writer.write(new_contents[start: start + chunk_size])
                        except Exception as e:
                            alogs_list.insert(tk.END, f'Error: {e}')
                            alogs_list.itemconfig(tk.END, {'fg':'red'})

                code_box.delete('1.0', tk.END)
                code_box.insert('1.0', new_contents)
                project_files.append(new_file)
                list_box.insert(tk.END, new_file)
                list_box.selection_clear(0, tk.END)
                list_box.selection_set(tk.END)
            except Exception as e:
                alogs_list.insert(tk.END, f'Error: {e}')
                alogs_list.itemconfig(tk.END, {'fg':'red'})
    except Exception as e:
        alogs_list.insert(tk.END, f'Error: {e}')
        alogs_list.itemconfig(tk.END, {'fg':'red'})

def close_file(code_box, list_box, alogs_list, forget_label,  chunk_size=1024):
    forget_label.place_forget()
    try:
        global already_chosen_file, project_files
        index = list_box.curselection()[0]
        path = list_box.get(index)

        autosave_contents = code_box.get('1.0', tk.END)
        try:
            with open(path, 'w', encoding='utf-8') as writer:
                for start in range(0, len(autosave_contents), chunk_size ):
                    try:
                        writer.write(autosave_contents[start: start + chunk_size])
                    except Exception as e:
                        alogs_list.insert(tk.END, f'Error: {e}')
                        alogs_list.itemconfig(tk.END, {'fg':'red'})
        except Exception as e:
            alogs_list.insert(tk.END, f'Error: {e}')
            alogs_list.itemconfig(tk.END, {'fg':'red'})

        project_files.remove(path)
        list_box.delete(index)
        code_box.delete('1.0', tk.END)
        list_box.selection_clear(0, tk.END)

        if len(project_files) == 0:
            already_chosen_file = ''
        else:
            newset_path = project_files[-1]
            already_chosen_file = newset_path
            try:
                with open(newset_path, 'r', encoding='utf-8') as reader:
                    while True:
                        try:
                            contents = reader.read(chunk_size)
                        except Exception as e:
                            alogs_list.insert(tk.END, f'Error: {e}')
                            alogs_list.itemconfig(tk.END, {'fg':'red'})
                            break
                        if not contents:
                            break
                        code_box.insert(tk.END, contents)

                list_box.selection_set(tk.END)
            except Exception as e:
                alogs_list.insert(tk.END, f'Error: {e}')
                alogs_list.itemconfig(tk.END, {'fg':'red'})

    except Exception as e:
        alogs_list.insert(tk.END, f'Error: {e}')
        alogs_list.itemconfig(tk.END, {'fg':'red'})
    code_box.edit_reset()

def exit_handle(master, choice: bool, code_box, alogs_list , chunk_size=1024):
    global already_chosen_file, project_files
    if choice == True:
        try:
            if already_chosen_file == '':
                pass
            else:
                save_contents = code_box.get('1.0', tk.END)
                with open(already_chosen_file, 'w', encoding='utf-8') as writer:
                    for start in range(0, len(save_contents), chunk_size):
                        try:
                            writer.write(save_contents[start: start + chunk_size])
                        except Exception as e:
                            alogs_list.insert(tk.END, f'Error: {e}')
                            alogs_list.itemconfig(tk.END, {'fg':'red'})
        except Exception as e:
            alogs_list.insert(tk.END, f'Error: {e}')
            alogs_list.itemconfig(tk.END, {'fg':'red'})

        master.destroy()
    else:
        return

def close_all_files(code_box, list_box, alogs_list , forget_label, chunk_size=1024):
    forget_label.place_forget()
    try:
        global already_chosen_file, project_files
        autosave_contents = code_box.get('1.0', tk.END)
        with open(already_chosen_file, 'w', encoding='utf-8') as writer:
            for start in range(0, len(autosave_contents), chunk_size):
                try:
                    writer.write(autosave_contents[start: start + chunk_size])
                except Exception as e:
                    alogs_list.insert(tk.END, f'Error: {e}')
                    alogs_list.itemconfig(tk.END, {'fg':'red'})

        project_files = []
        already_chosen_file = ''    
        code_box.delete('1.0', tk.END)
        list_box.delete(0, tk.END)
        list_box.selection_clear(0, tk.END)
    except Exception as e:
        alogs_list.insert(tk.END, f'Error: {e}')
        alogs_list.itemconfig(tk.END, {'fg':'red'})

def new_file(new_file_path: str, code_box, list_box, alogs_list, forget_label, chunk_size = 1024):
    forget_label.place_forget()
    global already_chosen_file, project_files , ext_to_lexer
    try:
        if already_chosen_file:
            try:
                with open(already_chosen_file, 'w', encoding='utf-8') as writer:
                    contents = code_box.get('1.0', tk.END)
                    for start in range(0, len(contents), chunk_size):
                        try:
                            writer.write(contents[start: start + chunk_size])
                        except Exception as e:
                            alogs_list.insert(tk.END, f'Error: {e}')
                            alogs_list.itemconfig(tk.END, {'fg':'red'})
            except Exception as e:
                alogs_list.insert(tk.END, f'Error: {e}')
                alogs_list.itemconfig(tk.END, {'fg':'red'})
        else:
            pass

        new_contents = '' # Nothing at all.
        new_file = new_file_path

        if new_file in project_files:
            pass

        else:
            already_chosen_file = new_file
            try:
                with open(new_file, 'w', encoding='utf-8') as writer:
                    for start in range(0, len(new_contents), chunk_size):
                        try:
                            writer.write(new_contents[start: start + chunk_size])
                        except Exception as e:
                            alogs_list.insert(tk.END, f'Error: {e}')
                            alogs_list.itemconfig(tk.END, {'fg':'red'})

                code_box.delete('1.0', tk.END)
                code_box.insert('1.0', new_contents)
                project_files.append(new_file)
                list_box.insert(tk.END, new_file)
                list_box.selection_clear(0, tk.END)
                list_box.selection_set(tk.END)
            except Exception as e:
                alogs_list.insert(tk.END, f'Error: {e}')
                alogs_list.itemconfig(tk.END, {'fg':'red'})
    except Exception as e:
        alogs_list.insert(tk.END, f'Error: {e}')
        alogs_list.itemconfig(tk.END, {'fg':'red'})
        