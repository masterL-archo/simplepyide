import tkinter as tk 
from tkinter import ttk 

class Todo:
    def __init__(self, main_frame, bg, dbg, code_box_):
        self.main_frame = main_frame
        self.code_box_ = code_box_
        self.widgets_frame = tk.Frame(self.main_frame, bg=bg)

        buttonset_frame = tk.Frame(self.widgets_frame, bg=bg)
        buttonset_frame.pack(fill = 'x')

        scan_button = ttk.Button(buttonset_frame, text = 'Scan for TODOs', width = 15, command=self.scan_todos, cursor = 'hand2')
        scan_button.pack(side='left', pady=(2,2), padx = 2)

        notice = tk.Label(buttonset_frame, text = 'Type #todo at the end of the desired line', font = ('Consolas', 8), bg=bg)
        notice.pack(side='left', padx= 5)

        todo_list_frame = tk.Frame(self.widgets_frame,bg=bg)
        todo_list_frame.pack(expand=True, fill = 'both')

       
        
        columns = ('Line', 'Info')
        todo_list = ttk.Treeview(todo_list_frame, show='headings', columns=columns)
        todo_list.heading('Line', text = 'Line number', anchor='w')
        todo_list.heading('Info', text = 'Line info', anchor='w')
        todo_list.column('Line', width = 70, anchor='w')
        todo_list.column('Info', width = 370, anchor='w')
        
        todo_list.pack(expand = True, fill='both', side ='left')
                   
        scroller_bar = tk.Scrollbar(todo_list_frame, command = todo_list.yview)
        scroller_bar.pack( fill = 'y', side = 'left')

        todo_list.config(yscrollcommand=scroller_bar.set)
        todo_list.bind('<<TreeviewSelect>>', self.navigate_todo)

        self.todo_list = todo_list

    def scan_todos(self):
        self.todo_list.delete(*self.todo_list.get_children())
        textbox = self.code_box_
        try:
            end_line = int(textbox.index('end').split('.')[0])
            found = False
            for i in range(1, end_line):
                line_contents = textbox.get(f'{i}.0', f'{i}.end')
                if line_contents.strip().lower().endswith('#todo'):
                    self.todo_list.insert('', 'end', values=(str(i), line_contents.strip()))
                    found = True
            if not found:
                self.todo_list.insert('', 'end', values=('-----', 'No line marked with #todo was found.'))
        except Exception as e:
            print(e)

    def navigate_todo(self, event=None):
        textbox = self.code_box_
        selected_indecis = self.todo_list.selection()
        if selected_indecis:
            try:
                item_id = selected_indecis[0]
                values = self.todo_list.item(item_id, 'values')
                line_number_string = values[0].strip()
                line_number = int(line_number_string)
                textbox.mark_set('insert', f'{line_number}.0')
                textbox.see(f'{line_number}.0')
                textbox.focus_set()
                textbox.tag_remove('highlight', '1.0', 'end'); textbox.tag_configure('highlight', background='grey', foreground='white')
                textbox.tag_add('highlight', f'{line_number}.0', f'{line_number}.end')
            except Exception as e:
                print(e)


    def add_frame(self):    
        self.widgets_frame.pack(expand = True, fill = 'both')

