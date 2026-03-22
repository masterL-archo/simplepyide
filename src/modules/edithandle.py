import tkinter as tk
from tkinter import ttk 


func_dict = {
    "abs": "Return absolute value of a number.",
    "all": "Return True if all elements in iterable are true.",
    "any": "Return True if any element in iterable is true.",
    "ascii": "Return printable representation escaping non-ASCII chars.",
    "bin": "Convert integer to binary string starting with '0b'.",
    "bool": "Convert a value to a Boolean, True or False.",
    "breakpoint": "Invoke the debugger at the call point.",
    "bytearray": "Return a mutable array of bytes.",
    "bytes": "Return an immutable bytes object.",
    "callable": "Return True if the object appears callable.",
    "chr": "Return character for the given Unicode code point.",
    "classmethod": "Convert a method into a class method.",
    "compile": "Compile source into a code or AST object.",
    "complex": "Create a complex number from real and imaginary parts.",
    "delattr": "Delete a named attribute from an object.",
    "dict": "Create a new dictionary object.",
    "dir": "Return list of attributes of an object.",
    "divmod": "Return quotient and remainder of division.",
    "enumerate": "Return iterator of (index, element) pairs.",
    "eval": "Evaluate a source expression in context.",
    "exec": "Execute dynamically created program code.",
    "filter": "Filter elements in iterable by a predicate.",
    "float": "Convert a number or string to floating point.",
    "format": "Return formatted representation of a value.",
    "frozenset": "Return an immutable set object.",
    "getattr": "Return value of named attribute of object.",
    "globals": "Return current global symbol table as dict.",
    "hasattr": "Return True if object has named attribute.",
    "hash": "Return hash value of an object.",
    "help": "Invoke built-in help system.",
    "hex": "Convert an integer to a hexadecimal string.",
    "id": "Return identity of an object.",
    "input": "Read a line of input from user.",
    "int": "Convert a number or string to integer.",
    "isinstance": "Check if object is instance of a class.",
    "issubclass": "Check if a class is subclass of another.",
    "iter": "Return iterator object.",
    "len": "Return length (number of items) of an object.",
    "list": "Create a list object.",
    "locals": "Return current local symbol table as dict.",
    "map": "Return iterator applying function over iterable.",
    "max": "Return largest item in iterable or arguments.",
    "memoryview": "Return memory view object.",
    "min": "Return smallest item in iterable or arguments.",
    "next": "Retrieve next item from iterator.",
    "object": "Create a new featureless object.",
    "oct": "Convert integer to octal string.",
    "open": "Open a file and return file object.",
    "ord": "Return Unicode code point of a character.",
    "pow": "Return base to the power exp, mod optional.",
    "print": "Print objects to standard output.",
    "property": "Return property attribute.",
    "range": "Return immutable sequence of numbers.",
    "repr": "Return a string representation of an object.",
    "reversed": "Return a reversed iterator.",
    "round": "Round a number to given precision.",
    "set": "Create a new set object.",
    "setattr": "Set value of named attribute on object.",
    "slice": "Return a slice object.",
    "sorted": "Return a sorted list from iterable.",
    "staticmethod": "Convert method to static method.",
    "str": "Create a string object.",
    "sum": "Return sum of a sequence of numbers.",
    "super": "Return a proxy object for parent class.",
    "tuple": "Create a tuple object.",
    "type": "Return type of an object or create new type.",
    "vars": "Return __dict__ attribute of object.",
    "zip": "Aggregate elements from multiple iterables.",
    "ascii": "Return a printable representation of an object.",
    "breakpoint": "Call sys.breakpointhook(), defaulting to pdb.set_trace().",
    "bytearray": "Return a mutable byte array.",
    "callable": "Return True if the object appears callable.",
    "classmethod": "Convert a method into a class method.",
    "complex": "Create a complex number from real and imaginary parts.",
    "delattr": "Delete a named attribute from an object.",
    "divmod": "Return the quotient and remainder of division.",
    "enumerate": "Return an enumerate object of (index, value) pairs.",
    "float": "Convert a value to a floating point number.",
    "format": "Return a formatted representation of a value.",
    "frozenset": "Return an immutable frozenset object.",
    "hash": "Return the hash value of an object.",
    "hex": "Convert an integer to a hexadecimal string.",
    "id": "Return the identity of an object.",
    "oct": "Convert an integer to an octal string.",
    "ord": "Return the Unicode code point for a one-character string.",
    "pow": "Return the value of x to the power of y; mod optional.",
    "property": "Return a property attribute.",
    "repr": "Return a string representation of an object.",
    "reversed": "Return a reversed iterator over a sequence.",
    "round": "Round a number to a given precision in decimal digits.",
    "set": "Return a new set object.",
    "slice": "Return a slice object representing set of indices.",
    "sorted": "Return a new sorted list from an iterable.",
    "staticmethod": "Convert a method into a static method.",
    "str": "Return a string version of an object.",
    "super": "Return a proxy object to delegate method calls to parent class.",
    "vars": "Return __dict__ attribute of an object or local symbol table.",
    "zip": "Return an iterator of tuples, aggregating elements from iterables.",

    # List functions
    "append": "Add a single item to the end of the list.",
    "extend": "Extend the list by appending elements from an iterable.",
    "insert": "Insert an item at a given position.",
    "remove": "Remove the first occurrence of a value.",
    "pop": "Remove and return item at index (default last).",
    "clear": "Remove all items from the list.",
    "index": "Return the index of the first matching value.",
    "count": "Return the number of occurrences of a value.",
    "sort": "Sort the list in place.",
    "reverse": "Reverse the elements of the list in place.",
    "copy": "Return a shallow copy of the list.",

    # Dict functions
    "clear": "Remove all items from the dictionary.",
    "copy": "Return a shallow copy of the dictionary.",
    "fromkeys": "Make a dict with keys from an iterable and values set to a value.",
    "get": "Return the value for a key, or default if key not found.",
    "items": "Return a view object of (key, value) pairs.",
    "keys": "Return a view object of dictionary keys.",
    "pop": "Remove specified key and return the corresponding value.",
    "popitem": "Remove and return an arbitrary (key, value) pair.",
    "setdefault": "Return value of key; if key not in dict, insert key with a value.",
    "update": "Update dictionary with key/value pairs from another dict or iterable.",
    "values": "Return a view object of dictionary values.",

    # Tuple functions (mostly operators)
    "count": "Return the number of occurrences of a value.",
    "index": "Return the index of the first matching value.",

    # Set functions
    "add": "Add an element to the set.",
    "clear": "Remove all elements from the set.",
    "copy": "Return a shallow copy of the set.",
    "difference": "Return the difference of two or more sets as a new set.",
    "difference_update": "Remove all elements of another set from this set.",
    "discard": "Remove an element if present (no error if absent).",
    "intersection": "Return the intersection of two sets as a new set.",
    "intersection_update": "Update set with the intersection of itself and another.",
    "isdisjoint": "Return True if two sets have no elements in common.",
    "issubset": "Report whether this set is a subset of another.",
    "issuperset": "Report whether this set is a superset of another.",
    "pop": "Remove and return an arbitrary set element.",
    "remove": "Remove an element; raises KeyError if not found.",
    "symmetric_difference": "Return the symmetric difference of two sets as a new set.",
    "union": "Return the union of sets as a new set.",
    "update": "Update set with the union of itself and others."
}




def smart_indentation_manager(code_box, forget_label):
    forget_label.place_forget()
    line_start = code_box.index('insert linestart')
    line_end = code_box.index('insert lineend')
    line_text = code_box.get(line_start, line_end)
    
    # Count existing indentation (spaces + tabs converted to spaces)
    indent_count = 0
    for char in line_text:
        if char == ' ':
            indent_count += 1
        elif char == '\t':
            indent_count += 4  # Treat tab as 4 spaces
        else:
            break
    indent = ' ' * indent_count  # Convert to spaces only
    
    if line_text.rstrip().endswith(':'):
        indent += '    '  # Add 4 spaces
    elif (line_text.strip().startswith(('pass', 'return', 'break', 'continue', 'raise'))):
        indent = ' ' * max(0, indent_count - 4)  # Remove 4 spaces
    
    code_box.insert('insert', '\n' + indent)
    code_box.see('insert')
    return "break"

def tab(code_box):
    if code_box.tag_ranges('sel'):
        selection_start = code_box.index('sel.first')
        selection_end = code_box.index('sel.last')
        start_line = int(selection_start.split('.')[0])
        end_line = int(selection_end.split('.')[0])
        for i in range(start_line, end_line + 1):
            line_start = f"{i}.0"
            code_box.insert(line_start, '    ')  # 4 spaces instead of '\t'
    else:
        code_box.insert(tk.INSERT, '    ')  # 4 spaces instead of '\t'
    return 'break'

def shift_tab(code_box):
    def dedent_line(line_start):
        """Remove 4 spaces or 1 tab from the start of a line."""
        line_text = code_box.get(line_start, f'{line_start} + 4c')
        if line_text.startswith('\t'):
            code_box.delete(line_start, f'{line_start} + 1c')
        elif line_text.startswith('    '):  # Exactly 4 spaces
            code_box.delete(line_start, f'{line_start} + 4c')
        elif line_text.startswith(' '):  # Any leading spaces (remove up to 4)
            to_delete = 0
            for ch in line_text:
                if ch == ' ' and to_delete < 4:
                    to_delete += 1
                else:
                    break
            if to_delete > 0:
                code_box.delete(line_start, f'{line_start} + {to_delete}c')

    if code_box.tag_ranges('sel'):
        selection_start = code_box.index('sel.first')
        selection_end = code_box.index('sel.last')
        start_line = int(selection_start.split('.')[0])
        end_line = int(selection_end.split('.')[0])
        for i in range(start_line, end_line + 1):
            line_start = f'{i}.0'
            dedent_line(line_start)
        return 'break'
    else:
        line_start = code_box.index('insert linestart')
        dedent_line(line_start)
        return 'break'




def press_continue(code_box, letter, forget_label, realtime_learn): # auto matching for doubles.
    if letter == '(' or letter == '[' or letter == '{' or letter == '\'' or letter == '\"' :
        if letter == '(':
            try:
                para_list = {
                    '(':")",
                    '\'':'\'',
                    "\"":"\"",
                    '[':"]",
                    '{':"}"
                }
                code_box.insert('insert', para_list[letter])
                code_box.mark_set('insert', f'insert -1c')
                # lanuch a BBOX
                if realtime_learn == 'True':
                    bbox = code_box.bbox('insert')
                    if bbox:
                        x, y, width, height = bbox
                        x_root = code_box.winfo_rootx() + x
                        y_root = code_box.winfo_rooty() + y + height - 40
                        forget_label.place(x=x_root, y=y_root)
                        forget_label.lift()

                        text_before_cursor = code_box.get("insert linestart", "insert")

                        ignore_chars = set('()., \t\n')
                        i = len(text_before_cursor) - 1
                        prev_word_chars = []

                        # Skip trailing punctuation/whitespace
                        while i >= 0 and text_before_cursor[i] in ignore_chars:
                            i -= 1

                        # Collect alphanumeric characters backwards into prev_word_chars
                        while i >= 0 and (text_before_cursor[i].isalnum() or text_before_cursor[i] == '_'):
                            prev_word_chars.append(text_before_cursor[i])
                            i -= 1

                        # Combine characters in correct order
                        prev_word = ''.join(reversed(prev_word_chars))


                        information = f"""\'{prev_word}\' function:
 {func_dict.get(prev_word, 'Not found.')}
"""
                        forget_label.config(state = tk.NORMAL)
                        forget_label.delete('1.0', 'end')
                        forget_label.insert('1.0', information)
                        forget_label.config(state = tk.DISABLED)
                        
                    else:
                        pass
                else:
                    pass


            except Exception as e:
                print(e)

        else:
            try:
                forget_label.place_forget()
                para_list = {
                    '(':")",
                    '\'':'\'',
                    "\"":"\"",
                    '[':"]",
                    '{':"}"
                }
                code_box.insert('insert', para_list[letter])
                code_box.mark_set('insert', f'insert -1c')
            except Exception as e:
                print(e)

    else:
        forget_label.place_forget()

def copy(code_box, master):
    try:
        selected_text = code_box.selection_get()
        master.clipboard_clear()
        master.clipboard_append(selected_text)
    except tk.TclError:
        pass
    return 'break'
    


def paste(code_box, master):
    try:
        clipboard_text = master.selection_get(selection = 'CLIPBOARD')
        code_box.insert('insert', clipboard_text)
    except:
        pass
    return 'break'
    

def cut(code_box, master):
    try:
        selected_text = code_box.selection_get()
        master.clipboard_clear()
        master.clipboard_append(selected_text)
        code_box.delete('sel.first', 'sel.last')
    except:
        pass
    return 'break'
    

def undo(code_box):
    try:
        code_box.edit_undo()
    except:
        pass
    return 'break'
    

def redo(code_box):
    try:
        code_box.edit_redo()
    except:
        pass
    return 'break'




def select_all(code_box):
    try:
        code_box.tag_add('sel', '1.0', 'end-1c')
        code_box.mark_set('insert', '1.0')
        code_box.see('insert')
    except:
        pass
    return 'break'
    

def clear_all(code_box):
    try:
        code_box.delete('1.0', 'end')
    except:
        pass
    return 'break'
    

def delete_current(code_box):
    try:
        code_box.delete('insert linestart', 'insert lineend+1c')
    except:
        pass
    return 'break'
    

def select_current(code_box):
    try:
        code_box.tag_remove('1.0', tk.END)
        code_box.tag_add('sel', 'insert linestart', 'insert lineend')
        code_box.mark_set('insert', 'insert lineend')
        code_box.focus()
    except:
        pass
    
    return 'break'

def dac(code_box):
    code_box.delete('insert', 'insert lineend')
    return 'break'
    


def dbc(code_box):
    code_box.delete('insert linestart', 'insert')


def remove_empty_lines(code_box):
    total_lines = int(code_box.index('end-1c').split('.')[0])
    for line_num in range(total_lines, 0, -1):
        current_line = code_box.get(f"{line_num}.0", f"{line_num}.end")
        if current_line.strip() == "":
            code_box.delete(f'{line_num}.0', f'{line_num + 1}.0')
    return "break"

def comment_current_line(code_box):
    line_num = int(code_box.index('insert').split('.')[0])
    first_char = code_box.get(f"{line_num}.0")[:1]
    if first_char == '#':
        pass
    else:
        code_box.insert('insert linestart', '#')
    return "break"

def capitalize_sel(code_box):
    if code_box.tag_ranges('sel'):
        try:
            sel_start = code_box.index('sel.first')
            sel_end = code_box.index('sel.last')
            selected_text = code_box.get(sel_start, sel_end)
            code_box.delete(sel_start, sel_end)
            caps = selected_text.upper()
            code_box.insert(sel_start, caps)
        except:
            pass
    else:
        pass
    
    return "break"

def decap_sel(code_box):
    if code_box.tag_ranges("sel"):
        try:
            sel_start = code_box.index('sel.first')
            sel_end = code_box.index('sel.last')
            selected_text = code_box.get(sel_start, sel_end)
            code_box.delete(sel_start, sel_end)
            caps = selected_text.lower()
            code_box.insert(sel_start, caps)
        except:
            pass
    else:
        pass
    return "break"

# Navigation .
def repos_endline(code_box):
    try:
        line_number = int(code_box.index('insert').split('.')[0])
        # repositioning. 
        endline_position = f"{line_number}.end"
        code_box.mark_set("insert", endline_position)
        code_box.see('insert')
        return "break"
    except:
        pass

def repos_startline(code_box):
    try:
        line_number = int(code_box.index('insert').split('.')[0])
        startline_pos = f"{line_number}.0"
        code_box.mark_set('insert', startline_pos)
        code_box.see('insert')
        return "break"
    except:
        pass

def repos_end(code_box):
    try:
        code_box.mark_set('insert', 'end')
        code_box.see("insert")
    except Exception as e:
        print(e)

def repos_start(code_box):
    try:
        code_box.mark_set('insert', '1.0') 
        code_box.see('insert')
    except Exception as e:
        print(e)

def wordskip_advanced(code_box):
    try:
        code_box.mark_set('insert', 'insert wordend +1c')
        code_box.see('insert')
        return "break"
    except:
        pass

def wordskip_reversed(code_box):
    try:
        code_box.mark_set('insert', 'insert wordstart -1c')
        code_box.see('insert')
        return "break"
    except:
        pass

def next_line(code_box):
    try:
        startline_index = code_box.index('insert linestart').split('.')[0]
        new_line_start = f"{int(startline_index) + 1}.0"
        code_box.mark_set('insert', new_line_start)
        code_box.see('insert')

    except Exception as e:
        print(e)
    return 'break'

def pre_line(code_box):
    try:
        startline_index = code_box.index('insert linestart').split('.')[0]
        new_line_start = f"{int(startline_index) - 1}.0"
        code_box.mark_set('insert', new_line_start)
        code_box.see('insert')

    except Exception as e:
        print(e)
    return 'break'

def cursor_up(code_box):
    try:
        code_box.mark_set('insert', 'insert +1line')
        code_box.see('insert')
    except Exception as e:
        print(e)
    

def cursor_down(code_box):
    try:
        code_box.mark_set('insert', 'insert -1line')
        code_box.see('insert')
    except Exception as e:
        print(e)


def go_to_line(code_box, master, bg, fg, forget_label):
    toplevel = tk.Toplevel(master)
    def widgets():
        def navigate_to_line():
            try:
                forget_label.place_forget()
                line_number_start = float(number_entry.get())
                line_number_end = f'{int(line_number_start)}.end'
                code_box.tag_remove('sel', '1.0', 'end')
                code_box.tag_add('sel', line_number_start, line_number_end)
                code_box.mark_set('insert', line_number_start)
                code_box.see('insert')
            except:
                pass




        label = tk.Label(toplevel, text = 'Type the line number', font=('Consolas', 10), bg=bg, fg=fg)
        label.pack()

        number_entry = ttk.Entry(toplevel, width=20)
        number_entry.pack(pady=10)

        find_number = ttk.Button(toplevel, text = 'Go to line', width=20, command=navigate_to_line)
        find_number.pack()



    widgets()


    toplevel.config(bg=bg)
    toplevel.title('Go to line')
    width = 220
    height = 100
    screen_width = toplevel.winfo_screenwidth()
    screen_height = toplevel.winfo_screenheight()

    x = (screen_width // 2) - (width // 2) - 10
    y = ((screen_height // 2) - (height // 2)) - 35

    toplevel.geometry(f'{width}x{height}+{x}+{y}')
    toplevel.resizable(0,0)
    toplevel.wm_attributes('-toolwindow', True)
    toplevel.mainloop()

def highlight_cursor_word(code_box):
    try:
        start_index = code_box.index('insert wordstart')
        end_index = code_box.index('insert wordend')
        # Highlighting... 
        code_box.tag_add('sel', start_index, end_index)
        code_box.see('insert')
    except Exception as e:
        print(e)
        pass
    pass



