import tkinter as tk # importing tkitner for the GUI stuff. 
from tkinter import ttk # Importing special tkinter . 


python_exceptions = {
    "BaseException": "The base class for all exceptions in Python. It is not meant to be directly inherited by user-defined exceptions. Handles all exceptions including system-exiting exceptions.",
    "Exception": "The base class for most built-in exceptions. User-defined exceptions should typically inherit from this.",
    "ArithmeticError": "Base class for errors occurring in numeric calculations, such as overflow, division by zero, or numeric limits exceeded.",
    "AssertionError": "Raised when an assert statement fails indicating a condition that should have been true is false.",
    "AttributeError": "Occurs when an attribute reference or assignment fails, for example if an object does not have the requested attribute.",
    "BufferError": "Raised when an operation related to an object’s buffer fails, like a memoryview or bytearray operation.",
    "EOFError": "Raised when the input() function hits end-of-file condition without reading any data.",
    "FloatingPointError": "Raised when a floating point operation fails, such as invalid floating point calculations.",
    "GeneratorExit": "Raised when a generator or coroutine is closed; usually caught internally.",
    "ImportError": "Raised when an import statement fails to find or load a module (can be a typo or missing file).",
    "ModuleNotFoundError": "A subclass of ImportError specifically raised when a module cannot be found.",
    "IndexError": "Raised when a sequence subscript (index) is out of range, for example accessing list[-10] in a list of length 5.",
    "KeyError": "Occurs when trying to access a dictionary with a key that doesn't exist.",
    "KeyboardInterrupt": "Raised when the user hits the interrupt key (typically Ctrl+C) to stop execution.",
    "MemoryError": "Raised when an operation runs out of memory, often on large data allocations.",
    "NameError": "Raised when a local or global name is not found, typically when a variable is referenced before assignment.",
    "NotImplementedError": "Typically used in abstract classes to indicate that a subclass must override a method.",
    "OSError": "Base class for system-related errors like file operations, I/O failures, or operating system errors.",
    "FileNotFoundError": "A subclass of OSError, raised when a file or directory is requested but does not exist. For example, opening a file that isn’t present.",
    "InterruptedError": "Raised when a system call is interrupted by an incoming signal.",
    "IsADirectoryError": "Raised when a file operation (like opening) is requested on a directory misuse.",
    "NotADirectoryError": "Raised when trying to perform a directory operation on a non-directory object.",
    "PermissionError": "Raised when trying to run an operation without sufficient permissions.",
    "ProcessLookupError": "Raised when a process-related operation is requested on a non-existent process.",
    "TimeoutError": "Raised when a system or socket operation times out.",
    "OverflowError": "Raised when the result of an arithmetic operation is too large to be represented.",
    "RecursionError": "Raised when the maximum recursion depth is exceeded.",
    "ReferenceError": "Raised when a weak reference proxy tries to access an object that has been garbage collected.",
    "RuntimeError": "General-purpose error raised when an error doesn’t fall into any other category.",
    "StopIteration": "Raised to signal the end of an iterator, used internally by for loops and next() calls.",
    "StopAsyncIteration": "Raised to signal the end of an asynchronous iterator.",
    "SyntaxError": "Raised by Python’s parser when it encounters invalid syntax.",
    "IndentationError": "A subclass of SyntaxError, raised when incorrect indentation is detected.",
    "TabError": "A subclass of IndentationError, raised when indentation consists of inconsistent mix of tabs and spaces.",
    "SystemError": "Indicates an internal error in the Python interpreter.",
    "SystemExit": "Raised by the sys.exit() function to exit the interpreter.",
    "TypeError": "Raised when an operation or function is applied to an object of inappropriate type.",
    "UnboundLocalError": "A subclass of NameError, raised when a local variable is referenced before assignment in a function.",
    "UnicodeError": "Base class for Unicode-related encoding/decoding errors.",
    "UnicodeEncodeError": "Raised when a Unicode encoding operation fails.",
    "UnicodeDecodeError": "Raised when a Unicode decoding operation fails.",
    "UnicodeTranslateError": "Raised when a Unicode translation operation fails.",
    "ValueError": "Raised when a function receives an argument of the right type but an inappropriate value.",
    "ZeroDivisionError": "Raised when dividing a number by zero, an illegal math operation."
}

class ErrorAssistant:
    def __init__(self, master, bg):
        self.master = master 
        self.local_frame = tk.Frame(self.master, bg=bg)

        MainTreeViewer = ttk.Treeview(self.local_frame)
        MainTreeViewer.pack(expand=True, fill = 'both', side='right')

        scroller_viewerV = tk.Scrollbar(self.local_frame, command=MainTreeViewer.yview, orient='vertical')
        scroller_viewerV.pack(fill = 'y', side='left')

        MainTreeViewer.config(yscrollcommand=scroller_viewerV.set)



        for key, value in python_exceptions.items():
            parent_ = MainTreeViewer.insert('', 'end', text = key)
            MainTreeViewer.insert(parent_, 'end', text=value)
        


    def add(self):
        self.local_frame.pack(expand = True, fill = 'both')
    pass

