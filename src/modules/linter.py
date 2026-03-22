
import ast
from pyflakes import checker
import tkinter as tk ; import os 

def lint_and_append(file_path, code_box, lint_log_listbox, alogs_listbox):
    def lint_file():
        global list_issues
        list_issues = []
        try:
            if file_path:
                source = code_box.get('1.0', tk.END)

                tree = ast.parse(source, filename=file_path)

                w = checker.Checker(tree, file_path)

                if w.messages:
                    
                    
                    for message in sorted(w.messages, key=lambda m: m.lineno):
                        args_str = tuple(str(arg) for arg in getattr(message, 'message_args', ()))
                        friendly_msg = message.message % args_str if args_str else message.message
                        list_issues.append(f'Line: {message.lineno}-{friendly_msg}')
                    return list_issues
                else:
                    return ['No issues found.']
                
            else:
                empty_list = ['File is not found.']
                return empty_list
        except Exception as e:
            list_issues.append(e)
            return list_issues
    list_ = lint_file()
    lint_log_listbox.delete(0, 'end')
    for index, item in enumerate(list_):
        lint_log_listbox.insert(tk.END, f'{item}')
    alogs_listbox.insert('end', 'ACTION: Scanned for available issues in file.')
    

def lint_append_and_savelog(code_box, file_path, lint_log_listbox, output_file, alogs_listbox):
    def lint_file():
        global list_issues
        list_issues = []
        try:
            if file_path:
                source = code_box.get('1.0', tk.END)

                tree = ast.parse(source, filename=file_path)

                w = checker.Checker(tree, file_path)

                if w.messages:
                    
                    
                    for message in sorted(w.messages, key=lambda m: m.lineno):
                        args_str = tuple(str(arg) for arg in getattr(message, 'message_args', ()))
                        friendly_msg = message.message % args_str if args_str else message.message
                        list_issues.append(f'Line: {message.lineno}-{friendly_msg}')
                    return list_issues
                else:
                    return ['No issues found.']
                
            else:
                empty_list = ['File is not found.']
                return empty_list
        except Exception as e:
            list_issues.append(e)
            return list_issues
    list_ = lint_file()
    lint_log_listbox.delete(0, 'end')
    for index, item in enumerate(list_):
        lint_log_listbox.insert(tk.END, f'{item}')

    for index, item in enumerate(list_):
        with open(output_file, 'a') as appender:
            appender.write(f'{item}\n')
        
    

def navigate_to_line(line_text, code_box, alogs_listbox, forget_label):
    try:
        forget_label.place_forget()
        stripped_ = line_text.strip()
        splitted_ = stripped_.split('-')
        line_text = splitted_[0]
        line_number = int(line_text.split(':')[1].strip())

        code_box.tag_remove('highlight','1.0', 'end')
        start = f'{line_number}.0'
        end = f'{line_number}.end + 1c'
        code_box.tag_add('highlight', start, end)
        code_box.tag_configure('highlight', background = 'red')

        code_box.mark_set('insert', start)
        code_box.see('insert')
        alogs_listbox.insert('end' , 'ACTION: navigated to issue line.')
    except Exception as e:
        print(e)
    

def remove_tags(code_box, alogs_listbox):
    try:
        code_box.tag_remove('highlight', '1.0', 'end')   
        alogs_listbox.insert('end', 'ACTION: removed all highlight tags.')
    except:
        pass

    
