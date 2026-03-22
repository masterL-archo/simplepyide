import tkinter as tk
from tkinter import ttk
import chlorophyll as cl
from pygments.lexers.python import Python3Lexer


import os 


def wrap_selected_with(wrapper: str, code_box):
    try:
        wrapper_dict = {
            '{': "}", "[": "]", "(": ")", "`": "`", "<" : ">", "^": "^", "'":"'", '"':'"'
        }
        start_index, end_index = code_box.tag_ranges('sel')
        wrapper_text = code_box.get(start_index, end_index)
        wrapped_text = wrapper + wrapper_text + wrapper_dict[wrapper]
        code_box.delete(start_index, end_index)
        code_box.insert(start_index, wrapped_text)
    except Exception as e:
        print(e)



from pyflowchart import Flowchart, output_html
import webbrowser as wb 

def generate_to_html_simplified(code_box,output_file):
    code = code_box.get('1.0', 'end')
    flowchart_class = Flowchart.from_code(code=code, simplify=True, field='')
    dsl_text = flowchart_class.flowchart()

    output_html(output_name=output_file, field_name=f'generated code flowchart (simplified)', flowchart=dsl_text)

    file_url = 'file://' + output_file
    wb.open(file_url)

    

   

def generate_to_html_nonsimplified(code_box, output_file, master, bg, fg,):
    code = code_box.get('1.0', 'end')
    flowchart_class = Flowchart.from_code(code=code, simplify=False, field='')
    dsl_text = flowchart_class.flowchart()

    output_html(output_name=output_file, field_name=f'generated code flowchart (Non simplified)', flowchart=dsl_text)

    file_url = 'file://' + output_file
    wb.open(file_url)
   
def comment_selection(code_box):
    if code_box.tag_ranges('sel'):
        selection_start = code_box.index('sel.first')
        selection_end = code_box.index('sel.last')
        selection = code_box.get(selection_start, selection_end)
        edited = '"""' + selection + '"""'
        code_box.delete(selection_start, selection_end)
        code_box.insert(selection_start, edited)
        return 'break'
    else:
        pass


def highlight_selection(code_box):
    try:
        if code_box.tag_ranges('sel'):
            selection_start = code_box.index('sel.first')
            selection_end = code_box.index('sel.last')
            code_box.tag_configure('highlight', background = '#B5F69C')
            code_box.tag_add('highlight', selection_start, selection_end)
            code_box.tag_remove('sel', '1.0', 'end')
    except Exception as e:
        print(e)

def unhighlight_selection(code_box):
    try:
        if code_box.tag_ranges('sel'):
            selection_start = code_box.index('sel.first')
            selection_end = code_box.index('sel.last')
            code_box.tag_configure('highlight', background = 'green')
            code_box.tag_remove('highlight', selection_start, selection_end)
            code_box.tag_remove('sel', '1.0', 'end')
    except Exception as e:
        print(e)

def remove_all_tags(code_box):
    try:
        code_box.tag_remove('highlight', '1.0', 'end')
    except Exception as e:
        print(e)


def summary(code_box, file_name , master, bg ,fg):
    top_level = tk.Toplevel(master)

    def widgets():
        try:
            information = {
                'File name': os.path.basename(file_name),
                'Full path': file_name, 
                'File Type': os.path.splitext(os.path.basename(file_name))[1],
                'Line amount': int(code_box.index('end').split('.')[0]) - 1
            }
        except :
            pass

        try:   
            label1 = tk.Label(top_level, text = f'File name: {information['File name']}', font = ('Consolas', 9), bg=bg, fg=fg)
            label1.grid(row=0, column=0, sticky='w', padx=5)

            label2 = ttk.Entry(top_level, width=65)
            label2.insert(0, f'File path: {information['Full path']}')
            label2.config(state=tk.DISABLED)
            label2.grid(row=1, column=0, sticky='w', padx=5)

            label3 = tk.Label(top_level, text = f'File type: {information['File Type']}', font = ('Consolas', 9),bg=bg, fg=fg)
            label3.grid(row=2, column=0, sticky='w', padx=5)

            label4 = tk.Label(top_level, text = f'Lines number: {information['Line amount']}', font = ('Consolas', 9), bg=bg, fg=fg)
            label4.grid(row=3, column=0, sticky='w', padx=5)

        except :
            pass


    widgets()

    top_level.wm_attributes('-toolwindow', True)
    width = 420
    height = 85
    screen_width = top_level.winfo_screenwidth()
    screen_height = top_level.winfo_screenheight()

    x = (screen_width // 2) - (width // 2) - 10
    y = ((screen_height // 2) - (height // 2)) - 35

    top_level.geometry(f'{width}x{height}+{x}+{y}'); top_level.resizable(0,0)
    top_level.title('File summary'); top_level.config(bg=bg)
    top_level.mainloop()

