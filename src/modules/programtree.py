from tkinter import ttk 
import tkinter as tk ; import ast 


class ProgramTree:
    def __init__(self, main_frame, bg, dbg, code_box, refresh_icon):

        self.code_box = code_box
        self.widgets_frame = tk.Frame(main_frame, bg=bg)
        button_set_frame = tk.Frame(self.widgets_frame, bg=bg)
        button_set_frame.pack(fill = 'x')

        scan_button = tk.Button(button_set_frame, image = refresh_icon,  width = 25, 
                                 command = self.scan_tree, bd=0, bg=bg, font = ('Consolas', 12, ), cursor = 'hand2')
        scan_button.pack(side='left', pady = 3)

        programtree_frame = tk.Frame(self.widgets_frame, bg=bg)
        programtree_frame.pack(expand = True, fill = 'both')

        
        program_treeview = ttk.Treeview(programtree_frame)
        program_treeview.heading('#0', text='Program Structure', anchor='w')
        program_treeview.pack(side='left', expand = True, fill = 'both')
        scroller_bar = tk.Scrollbar(programtree_frame, command=program_treeview.yview)
        scroller_bar.pack(fill = 'y', side = 'right')
        program_treeview.config(yscrollcommand=scroller_bar.set)

        self.program_treeview = program_treeview
        
        

    def scan_tree(self):
        try:
            self.program_treeview.delete(*self.program_treeview.get_children())
            source_code = self.code_box.get('1.0', tk.END)
            node = ast.parse(source=source_code)

            stack = [(node, '')]
            while stack:
                node, parent_id = stack.pop()
                if isinstance(node, ast.Module):
                    label = 'Module'
                elif isinstance(node, ast.ClassDef):
                    label = f'Class: {node.name}'
                elif isinstance(node, ast.FunctionDef):
                    label = f'Function: {node.name}'
                else:
                    continue
                item_id = self.program_treeview.insert(parent_id, 'end', text=label)
                children = list(ast.iter_child_nodes(node))
                for child in reversed(children):
                    stack.append((child, item_id))
        except Exception as e:
            print(e)


    def add(self):
        self.widgets_frame.pack(expand =True, fill = 'both')

