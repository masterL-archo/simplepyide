import tkinter as tk
from tkinter import ttk 
import appinfo.info as information 
import appinfo.globaltheme as theming 
import chlorophyll as cl
from pygments.lexers.python import Python3Lexer
from tkinter import filedialog, messagebox
import modules.filehandle as file
import modules.edithandle as edit
import modules.pythonrunner as pr
import modules.applyhandle as apply
import modules.formatter as frmt
import os
import modules.linter as lnt
import modules.pip_module as pm
import modules.ErrorAssistant as ea
from tkinter import font 
import imgs.BINs.about_icon as t1
import imgs.BINs.cmd_icon as t2
import imgs.BINs.code_icon as t3
import imgs.BINs.exit_icon as t4
import imgs.BINs.feedback_icon as t5
import imgs.BINs.find_icon as t6
import imgs.BINs.fullscreen_icon as t7
import imgs.BINs.hashtag_icon as t8
import imgs.BINs.icon as t9
import imgs.BINs.minus_icon as t10
import imgs.BINs.newfile_icon as t11
import imgs.BINs.openfile_icon as t12
import imgs.BINs.package_icon as t13
import imgs.BINs.plus_icon as t14
import imgs.BINs.python_icon as t15
import imgs.BINs.redo_icon as t16
import imgs.BINs.refresh_icon as t17
import imgs.BINs.run_icon as t18
import imgs.BINs.save_icon as t19
import imgs.BINs.saveas_icon as t20#todo
import imgs.BINs.undo_icon as t22
import imgs.BINs.summary_icon as t23
import imgs.BINs.flow_icon as t24
import imgs.BINs.veraIDE_icon as t25
import imgs.BINs.format_icon as t26
import appinfo.colour_schemes as css 
import modules.TODO as todo
import modules.programtree as ptt
import modules.feedback_module as feed
import modules.about_html as aboutHtml

import webbrowser
root = tk.Tk()


icon_main = tk.PhotoImage(data=t25.bin)

about_icon_img = tk.PhotoImage(data=t1.bin)
cmd_icon_img = tk.PhotoImage(data=t2.bin)
code_icon_img = tk.PhotoImage(data=t3.bin)
exit_icon_img = tk.PhotoImage(data=t4.bin)
feedback_icon_img = tk.PhotoImage(data=t5.bin)
find_icon_img = tk.PhotoImage(data=t6.bin)
fullscreen_icon_img = tk.PhotoImage(data=t7.bin)
hashtag_icon_img = tk.PhotoImage(data=t8.bin)
icon_img = tk.PhotoImage(data=t9.bin)
minus_icon_img = tk.PhotoImage(data=t10.bin)
newfile_icon_img = tk.PhotoImage(data=t11.bin)
openfile_icon_img = tk.PhotoImage(data=t12.bin)
package_icon_img = tk.PhotoImage(data=t13.bin)
plus_icon_img = tk.PhotoImage(data=t14.bin)
python_icon_img = tk.PhotoImage(data=t15.bin)
redo_icon_img = tk.PhotoImage(data=t16.bin)
refresh_icon_img = tk.PhotoImage(data=t17.bin)
run_icon_img = tk.PhotoImage(data=t18.bin)
save_icon_img = tk.PhotoImage(data=t19.bin)
saveas_icon_img = tk.PhotoImage(data=t20.bin)
undo_icon_img = tk.PhotoImage(data=t22.bin)
summary_icon_img = tk.PhotoImage(data=t23.bin)
flow_icon_img = tk.PhotoImage(data=t24.bin)
format_icon_img = tk.PhotoImage(data=t26.bin)
is_full_screen = False


def context_menu(xroot, yroot, master, current_file, code_box, alogs_):
    border_colour = "#EEEEEE"
    popup_menu = tk.Menu(master, tearoff=0, background=border_colour)
    popup_menu.add_command(label ='Copy', command = lambda: edit.copy(code_box=code_box, master=master))
    popup_menu.add_command(label ='Paste', command = lambda:edit.paste(code_box=code_box, master=master))
    popup_menu.add_command(label ='Cut', command =lambda: edit.cut(code_box=code_box, master=master))
    popup_menu.add_command(label ='Select all', command = lambda:edit.select_all(code_box=code_box))
    popup_menu.add_command(label = 'Clear', command=lambda: edit.clear_all(code_box=code_box))
    popup_menu.add_separator()
    popup_menu.add_command(label ='Run current file', command = lambda:pr.run_file(file_path=current_file, code_box=code_box), image = run_icon_img, compound = 'left')
    popup_menu.add_command(label ='Launch Python', command=lambda:pr.run_python_shell(alogs=alogs_, interpath=theming.extract_interpreter()), image = python_icon_img, compound='left')
    popup_menu.add_command(label ='Launch terminal', command = lambda: pr.start_terminal(alogs=alogs_), image = cmd_icon_img, compound='left')
    popup_menu.add_command(label ='Format code', command = lambda: frmt.BlackFormatter(app_title=information.APP_NAME, master=root, code_box=code_box), image = format_icon_img, compound='left')


    popup_menu.tk_popup(x=xroot, y=yroot)

def open_feedback_popup():
    popup = tk.Toplevel()
    popup.title("Feedback")
    width = 400
    height = 300 

    popup.bell()
    screen_width = popup.winfo_screenwidth()
    screen_height = popup.winfo_screenheight()

    x = (screen_width // 2) - (width // 2) - 10
    y = ((screen_height // 2) - (height // 2)) - 35

    popup.geometry(f'{width}x{height}+{x}+{y}')

    popup.resizable(False, False)
    popup.wm_attributes('-toolwindow', True)

    # Name Label and Entry
    ttk.Label(popup, text="Name:").pack(anchor="w", padx=10, pady=(10, 2))
    name_var = tk.StringVar()
    name_entry = ttk.Entry(popup, textvariable=name_var)
    name_entry.pack(fill="x", padx=10, pady=(0, 10))

    # Feedback Label and Text box
    ttk.Label(popup, text="Feedback:").pack(anchor="w", padx=10, pady=(0, 2))

    feedback_text = tk.Text(popup, height=8, wrap="word", bd=1, relief='solid')
    feedback_text.pack(fill="both", expand=True, padx=10, pady=(0, 10))
    

    # Send button callback
    def send_feedback():
        name = name_var.get().strip()
        content = feedback_text.get("1.0", "end").strip()
        if not name or not content:
            messagebox.showwarning("Input Error", "Please enter both your name and feedback.")
            return
        # Here you would handle the feedback, e.g. print or send via email
      
        feed.send_feedback(senderemail=information.SENDER_EMAIL, receiver_email=information.RECEIVER_EMAIL, 
                           app_password=information.APP_PASSWORD, content = feedback_text.get('1.0', tk.END), name=name_entry.get(), 
                           app_name=information.APP_NAME)
        
        messagebox.showinfo("Feedback Sent", "Thank you for your feedback!")
        popup.destroy()

    send_btn = ttk.Button(popup, text="Send", command=send_feedback)
    send_btn.pack(pady=(0,7))

def Widgets(): 

    
    def new_file(event=None):
        file_path = filedialog.asksaveasfile()
        if file_path:
            file.new_file(new_file_path=file_path.name, code_box=code_box, list_box=file_listbox, alogs_list = alogs_listbox, forget_label=suggestions_label)
            alogs_listbox.insert(tk.END, f'ACTION: New file opened created at {os.path.basename(file_path.name)}')
        else:
            alogs_listbox.insert(tk.END, f'ERROR: No file was chosen.')
            alogs_listbox.itemconfig(tk.END, {'fg':'red'})

    def open_file(event=None):
        path = filedialog.askopenfilename()
        if path:
            file.open_file(file_path = path, code_box= code_box, files_listbox=file_listbox, alogs_list=alogs_listbox, forget_label=suggestions_label)
            
        else:
            alogs_listbox.insert(tk.END, f'ERROR: No file was chosen.')
            new_var = alogs_listbox.itemconfig(tk.END, {'fg':'red'})
    def _on_selection(event=None):
        file._on_switch(files_listbox=file_listbox, code_box=code_box, alogs_list=alogs_listbox, forget_label=suggestions_label)
        alogs_listbox.insert(tk.END, f'ACTION: Switched files.')
    
    def save_file(event=None):
        file.save_file(code_box = code_box, alogs_list = alogs_listbox)  
        alogs_listbox.insert(tk.END, f'ACTION: The already chosen file was saved.')

    def save_file_as(event=None):
        file_path = filedialog.asksaveasfile()
        if file_path:
            file.save_as(new_file_path=file_path.name, code_box=code_box, list_box=file_listbox, alogs_list = alogs_listbox, forget_label=suggestions_label)
            alogs_listbox.insert(tk.END, f'ACTION: Already chosen file was saved as {os.path.basename(file_path.name)}')
        else:
            pass
    
    def close_file(event=None):
        file.close_file(code_box=code_box, list_box = file_listbox, alogs_list= alogs_listbox, forget_label=suggestions_label)
        alogs_listbox.insert(tk.END, f'ACTION: Selected file was deleted.')

    def exit(event=None):
        result = messagebox.askyesno('Exit', 'Do you want to exit?')
        if result == True: # EXIT
            theming.change_last_chosen_file(file_path = file.already_chosen_file)

        file.exit_handle(master = root, choice=result, code_box=code_box, alogs_list= alogs_listbox)


    def close_all_files(event=None):
        file.close_all_files(code_box=code_box, list_box=file_listbox, alogs_list = alogs_listbox, forget_label=suggestions_label)  
        alogs_listbox.insert(tk.END, f'ACTION: All files were closed.')  
    def increase_font_size(event=None):
        limit = 15
        already_size = int(themesavermanager.extract_theme()[1])
        if already_size <= limit:
            themesavermanager.save_partial_theme(position=1, value=int(themesavermanager.extract_theme()[1]) + 1)
            code_box.config(font=(theming.code_font, int(themesavermanager.extract_theme()[1]) + 1))
        else:
            pass

    def decrease_font_size(event=None):
        limit = 9
        already_size = int(themesavermanager.extract_theme()[1])
        if already_size >= limit:
            themesavermanager.save_partial_theme(position=1, value=int(themesavermanager.extract_theme()[1]) - 1)
            code_box.config(font=(theming.code_font, int(themesavermanager.extract_theme()[1]) - 1))   
        else:
            pass

    def run_(event=None):
        pr.run_file(file_path=file.already_chosen_file, code_box=code_box, interpath=theming.extract_interpreter(),
                     alogs_list=alogs_listbox, live_interpreter=theming.extract_interpreter())
        

    # Main UI elements
    fast_access_bar = tk.Frame(root, bg = theming.bg, width = 10)
    fast_access_bar.pack(fill = 'x', pady = (0,1) )
    
    fab1 = tk.Button(fast_access_bar, image = undo_icon_img, command = lambda: edit.undo(code_box=code_box), bd=0, width=25,font=('Consolas', 10, 'bold'), bg=theming.bg, fg='grey', cursor="hand2")
    fab1.pack(side = 'left',padx=0, pady=1, ipady=2)
    fab2 = tk.Button(fast_access_bar, image = redo_icon_img, command = lambda: edit.redo(code_box=code_box), width = 25, bd=0, font=('Consolas', 10, 'bold'), bg=theming.bg, fg='grey', cursor="hand2")
    fab2.pack(side = 'left',padx=0, pady=1, ipady=2)

    fab7= tk.Button(fast_access_bar, image = run_icon_img, width = 25, font=('Consolas', 10), bd=0, fg = 'green' , bg=theming.bg, 
                    command=run_, cursor="hand2")
    fab7.pack(side = 'left',padx=0, pady=1, ipady=2)

    fabx= tk.Button(fast_access_bar, image = python_icon_img, command = lambda: pr.run_python_shell(alogs=alogs_listbox, interpath=theming.extract_interpreter())
                    , width = 25, font=('Consolas', 10), bg=theming.bg, bd=0, fg='green', cursor="hand2")
    fabx.pack(side = 'left',padx=0, pady=1, ipady=2)


    fab10= tk.Button(fast_access_bar, image = plus_icon_img ,command = increase_font_size,width = 25, font=('Consolas', 10), bg=theming.bg, bd=0, fg='grey', cursor="hand2")
    fab10.pack(side = 'left',padx=0, pady=1, ipady=2)
    fab11= tk.Button(fast_access_bar, image = minus_icon_img, command = decrease_font_size, width = 25, font=('Consolas', 10), bg=theming.bg, bd=0, fg='grey', cursor="hand2")
    fab11.pack(side = 'left',padx=0, pady=1, ipady=2)



    open_button= tk.Button(fast_access_bar, image = openfile_icon_img,command = open_file, width = 25, font=('Consolas', 10), bg=theming.bg, bd=0, cursor="hand2")
    open_button.pack(side = 'left',padx=0, pady=1, ipady=2)

    save_button= tk.Button(fast_access_bar,image = save_icon_img,command = save_file, width = 25, font=('Consolas', 10), bg=theming.bg, bd=0, cursor="hand2")
    save_button.pack(side = 'left',padx=0, pady=1, ipady=2)



    def generate_then_export(type: str):
        try:
            file_path = filedialog.asksaveasfilename(title='Select an HTML file', filetypes=[('HTML files', '*html *htm')])
            if file_path:
                if type == 'Simple':
                    try:    
                        apply.generate_to_html_simplified(code_box=code_box, output_file=file_path)
                        alogs_listbox.insert(0, 'ACTION: Generated a simple flowchart at ' + file_path)
                        pass
                    except Exception as e:
                        print(e)
                elif type == 'Normal':
                    try:
                        apply.generate_to_html_nonsimplified(code_box=code_box, output_file=file_path, master=root, bg = theming.bg, fg = theming.fg)
                        alogs_listbox.insert(0, 'ACTION: Generated an ormal flowchart at ' + file_path)
                        pass
                    except Exception as e:
                        print(e)
                else:
                    pass
            else:
                pass

        except Exception as e:
            print(e)

    fab18= tk.Button(fast_access_bar, image = flow_icon_img,command = lambda: generate_then_export(type='Normal'), width = 25, font=('Consolas', 10), bg=theming.bg, bd=0, fg='blue', cursor="hand2")
    fab18.pack(side = 'left')

    fab15= tk.Button(fast_access_bar, image = find_icon_img, width = 25, font=('Consolas', 10), bg=theming.bg, bd=0, fg='grey'
            , command=lambda: edit.go_to_line(code_box=code_box, master=root ,bg = theming.bg, fg = theming.fg, forget_label=suggestions_label), cursor="hand2")
    fab15.pack(side = 'left',padx=0, pady=1, ipady=2)

    
    terminal_button = tk.Button(fast_access_bar, image = cmd_icon_img, width = 25, font=('Consolas', 10), bg=theming.bg, bd=0, fg='grey'
            , command=lambda: pr.start_terminal(alogs=alogs_listbox), cursor="hand2")
    terminal_button.pack(side = 'left',padx=0, pady=1, ipady=2)

    
    pip_button= tk.Button(fast_access_bar, image = package_icon_img, width = 25, font=('Consolas', 10), bg=theming.bg, bd=0, fg='grey'
            ,command=lambda: pm.pip_module(master=root, bg=theming.bg, fg=theming.fg, font=theming.font, dbg=theming.dbg), cursor="hand2")
    pip_button.pack(side = 'left',padx=0, pady=1, ipady=2)




    partial_window = ttk.PanedWindow(root, orient = tk.HORIZONTAL) # seperated + sliders
    partial_window.pack(expand=True, fill = "both")



    left_part_master = tk.Frame(partial_window, bg = theming.bg)
    partial_window.add(left_part_master, weight = 1)

    left_part_notepad = ttk.Notebook(left_part_master)
    left_part_notepad.pack(expand=True, fill=tk.BOTH)

    left_part = tk.Frame(left_part_notepad, bg = theming.bg)
    left_part_notepad.add(left_part, text='Source files',)

    files_list_frame = tk.Frame(left_part)
    files_list_frame.pack(expand = True, fill = 'both')

    file_listbox = tk.Listbox(files_list_frame, bg = theming.bg, fg = theming.fg, bd = 0, font = (theming.font, 8), width=40, selectmode=tk.SINGLE, exportselection=False)
    file_listbox.pack(expand=True, fill='both', side = 'right')
    file_listbox.bind('<<ListboxSelect>>', _on_selection)

    file_list_scrollbar = ttk.Scrollbar(files_list_frame
    , orient='vertical', command=file_listbox.yview)
    file_list_scrollbar.pack(side='left', fill='y')

    file_listbox.config(yscrollcommand=file_list_scrollbar.set)
    

    close_file_button = ttk.Button(left_part, text = 'Close selected', command=close_file, cursor = 'hand2')
    close_file_button.pack(side = 'left', expand=True, fill = 'x')

    close_all_button =  ttk.Button(left_part, text = 'Close all files', command=close_all_files, cursor = 'hand2')
    close_all_button.pack(side='right', expand=True, fill = 'x')

    assistant_frame = tk.Frame(left_part_notepad, bg = theming.bg)
    left_part_notepad.add(assistant_frame, text='Error Assistant')

    ErrorAssistantWidget = ea.ErrorAssistant(master=assistant_frame, bg= theming.bg)
    ErrorAssistantWidget.add()

    med_part = tk.Frame(partial_window, bg = theming.bg)
    partial_window.add(med_part, weight = 1)
    
    name_dict = {
            "mariana": css.mariana, 
            'dracula': css.modern_dark, 
            'ayu-light': css.light, 
            'ayu-dark': css.darcula, 
            'monokai' : css.monokai
    }


    suggestions_label = tk.Text(root, bg = 'yellow', font = ('Consolas', 8), width = 67, height = 2, bd = 1, relief='solid')
    def forget_rtl_on_change(event):
        suggestions_label.place_forget()
        code_box.tag_remove('highlight', '1.0', 'end')

    partial_window.bind('<B1-Motion>', forget_rtl_on_change)

    code_box_frame = tk.Frame(med_part, bg=theming.dbg)
    code_box_frame.pack(expand=True, fill = 'both')

    code_box = cl.CodeView(code_box_frame, lexer = Python3Lexer, color_scheme=name_dict[theming.highlight], font = (theming.code_font, theming.code_size, 'normal'), undo=True, width=50)
    code_box.pack(expand = True, fill = 'both', padx = 1, pady = 1)



    def run_context_menu(event):
        context_menu(xroot=event.x_root, yroot=event.y_root, master=root, current_file=file.already_chosen_file, 
                        code_box=code_box, alogs_ = alogs_listbox)
    code_box.bind('<Button-3>', run_context_menu)    

    code_box.bind('<Button-1>', forget_rtl_on_change)


    # Auto indent feature.
    def smart_indent_manager(event):
        return edit.smart_indentation_manager( code_box=code_box, forget_label=suggestions_label)
    
    code_box.bind('<Return>', smart_indent_manager) # auto indentation keeper.
    

    def auto_tab(event):
        edit.tab(code_box=code_box)
        return "break"
    def shift_tab(event):
        edit.shift_tab(code_box=code_box)

    code_box.bind('<Tab>', auto_tab)
    code_box.bind('<Shift-Tab>', shift_tab)
    #--------------------
    # Auto paraclosing feature.
    def key_continue(event):
        try:
            character = event.char
            edit.press_continue(code_box=code_box, letter=character, forget_label = suggestions_label, realtime_learn=theming.extract_realtime_learn())
        except Exception as e:
            print(e)
    code_box.bind('<Key>', key_continue)

    #--------------------

    right_part = tk.Frame(partial_window, bg = theming.bg)
    partial_window.add(right_part, weight = 1)


    right_notepad = ttk.Notebook(right_part)
    right_notepad.pack(expand=True,fill='both')


    alogs_list_frame = tk.Frame(right_notepad, bg = theming.bg)
    alogs_list_frame.pack(expand=True, fill='both')

    alogs_listbox_megaframe = tk.Frame(alogs_list_frame, bg = theming.bg)
    alogs_listbox_megaframe.pack(expand = True, fill = 'both')

    alogs_listbox = tk.Listbox(alogs_listbox_megaframe, bg = theming.bg,bd=0 , font = ('Consolas', 9), fg=theming.fg,width=40)
    alogs_listbox.pack(side='left', expand=True, fill = 'both')

    alogs_listbox.insert(tk.END, f'ACTION: {information.APP_NAME} - {information.APP_VERSION} - {information.APP_BUILD} has been launched.')
    alogs_listbox.insert(tk.END, f'INFO: {information.APP_NAME} - {information.APP_VERSION} - {information.APP_BUILD} is running.')


    alogs_listbox_scroller = tk.Scrollbar(alogs_listbox_megaframe, orient='vertical', command=alogs_listbox.yview)
    alogs_listbox_scroller.pack(side='right', fill='y')

    alogs_listbox.config(yscrollcommand=alogs_listbox_scroller.set)

    def clear_logs():
        alogs_listbox.delete(0, tk.END)
    def save_logs():
        filepath = filedialog.asksaveasfile(title = 'Save active logs to')
        if filepath:
            path = filepath.name 
            alogs_listbox.insert(tk.END, f'Active logs were saved to {os.path.basename(filepath.name)}')
            with open(path, 'w') as writer:
                writer.write('\n'.join(alogs_listbox.get(0, tk.END)))
                pass
            messagebox.showinfo('Active logs', 'Active logs were saved to ' + os.path.basename(path))
        else:
            pass
    
    alogs_buttonset = tk.Frame(alogs_list_frame, bg = theming.bg)
    alogs_buttonset.pack(fill = 'x')

    clear_active_logs_button =  ttk.Button(alogs_buttonset, text = 'Clear active logs', 
                                          command = clear_logs, cursor = 'hand2')
    clear_active_logs_button.pack(side='left', expand=True, fill='x')

    save_active_logs_button = ttk.Button(alogs_buttonset, text = 'Save active logs',
                                          command = save_logs, cursor = 'hand2')
    save_active_logs_button.pack(side='left', expand=True, fill=tk.BOTH)
    # ----------------------------------------------
    lint_output_frame = tk.Frame(right_notepad, bg = theming.bg)
    lint_output_frame.pack(expand = True, fill = 'both')

    lint_buttonset = tk.Frame(lint_output_frame, bg = theming.bg)
    lint_buttonset.pack(fill = 'x')

    scan_button = ttk.Button(lint_buttonset, text = 'Scan for issues', width = 15, command = lambda: lnt.lint_and_append(file_path=file.already_chosen_file, 
                                                                                                                         code_box=code_box, lint_log_listbox=lint_log_listbox, alogs_listbox=alogs_listbox), cursor = 'hand2')
    scan_button.pack(side = 'left')


    def save_lint_logs():
        filepath = filedialog.asksaveasfilename(filetypes=[("Text files", "*.txt")], title="Select an output file")
        if filepath:
            lnt.lint_append_and_savelog(code_box=code_box, lint_log_listbox=lint_log_listbox, file_path=file.already_chosen_file, output_file=filepath, alogs_listbox=alogs_listbox)
            messagebox.showinfo(title = 'Linter', message = 'Lint output was saved to ' + os.path.basename(filepath))
            alogs_listbox.insert('end', 'ACTION: Issues log was saved to ' + filepath)
        else:
            alogs_listbox.insert(tk.END, f'ERROR: No file was selected.')
            alogs_listbox.itemconfig(tk.END, {'fg':'red'})


    save_button = ttk.Button(lint_buttonset, text = 'Scan and save', width = 15, command = save_lint_logs, cursor = 'hand2')
    save_button.pack(side = 'left')    


    
    clear_button = ttk.Button(lint_buttonset, text = 'Clear issues log', width = 15, command = lambda: lint_log_listbox.delete(0, 'end'), cursor = 'hand2')
    clear_button.pack(side = 'left')    

    remove_highlights = ttk.Button(lint_buttonset, text = 'Remove tags', width = 15, command = lambda: lnt.remove_tags(code_box=code_box, alogs_listbox=alogs_listbox), cursor = 'hand2')
    remove_highlights.pack(side='left')

    lint_log_listbox_frame = tk.Frame(lint_output_frame, bg = theming.bg)
    lint_log_listbox_frame.pack(expand = True, fill = 'both')

    def navigate_to_selection(event):
        selected_indecis = lint_log_listbox.curselection()
        if selected_indecis:
            selection_index = selected_indecis[0]
            line_text = lint_log_listbox.get(selection_index)
            lnt.navigate_to_line(line_text = line_text, code_box=code_box, alogs_listbox=alogs_listbox, forget_label=suggestions_label)


    lint_log_listbox = tk.Listbox(lint_log_listbox_frame, bg = theming.dbg, bd = 0, font = ('Consolas', 9))
    lint_log_listbox.pack(expand = True, fill = 'both', side = 'left')
    lint_log_listbox.bind('<<ListboxSelect>>', navigate_to_selection)

    lint_log_scroller = tk.Scrollbar(lint_log_listbox_frame, orient='vertical', command=lint_log_listbox.yview)
    lint_log_scroller.pack(fill = 'y', side = 'right')

    lint_log_listbox.config(yscrollcommand=lint_log_scroller.set)


    todo_frame = tk.Frame(right_notepad, bg=theming.bg)
    TODO_class = todo.Todo(main_frame=todo_frame, bg= theming.bg, dbg=theming.dbg, code_box_=code_box)
    TODO_class.add_frame()
    

    programtree = tk.Frame(right_notepad, bg=theming.bg)
    programtree_class = ptt.ProgramTree(main_frame=programtree, bg= theming.bg, dbg= theming.dbg, code_box=code_box, refresh_icon=refresh_icon_img)
    programtree_class.add()

    
    right_notepad.add(alogs_list_frame, text = 'Action Logger', padding=0)
    right_notepad.add(lint_output_frame, text = 'Linter', padding = 0)
    right_notepad.add(todo_frame, text = 'TODO', padding=0)
    right_notepad.add(programtree, text = 'Program tree', padding = 0)

    # ----------------
    # Secondery application toolbar. (BOTTOM)...
    bottom_toolbar = tk.Frame(root, bg = theming.dbg)
    bottom_toolbar.pack(side = 'bottom', fill = 'both')

    credit_sentence = f"{information.APP_NAME} - {information.APP_VERSION} - {information.APP_BUILD}"
    credit_label = tk.Label(bottom_toolbar, text = credit_sentence, font = (theming.font, 8, 'italic'), bg = theming.dbg, fg = theming.fg)
    credit_label.pack(side='left')


    def redirect_to_icons8(event):
        webbrowser.open_new(url = 'https://icons8.com/')

    underline_font = font.Font(family=theming.font, size=8, underline=True)

    icons8_recognition = tk.Label(bottom_toolbar, text = '- Icons by', font = ('Consolas', 8,'bold italic'), bg=theming.dbg, fg=theming.fg)
    icons8_recognition.pack(side='left')

    icons8_link = tk.Label(bottom_toolbar, text = 'Icons8', font=underline_font, bg=theming.dbg, fg=theming.fg, cursor='hand2')
    icons8_link.pack(side='left', padx=1)

    icons8_link.bind('<Button-1>', redirect_to_icons8)




    exit_button = tk.Button(bottom_toolbar, image = exit_icon_img, font = (theming.font, 7), bg = theming.dbg, bd = 0, fg='red', command=exit)
    exit_button.pack(side = 'right', padx = (0,2))

    run_button = tk.Button(bottom_toolbar, image= run_icon_img, font = (theming.font, 10), bg = theming.dbg, bd = 0, fg='green', 
                            command= run_)
    run_button.pack(side = 'right')

    interpreter_path = tk.StringVar()
    interpreter_path.set(theming.extract_interpreter())
    interlist = pr.interpreters

    def on_change(selected_path):
        theming.change_interpreter(selected_path)
    border_colour = "#EEEEEE"
    interpreters_optionmenu = tk.OptionMenu(bottom_toolbar, interpreter_path, *interlist, command = on_change)
    interpreters_optionmenu.config(bg=theming.dbg, fg= theming.fg, borderwidth=0, highlightthickness=0, font = ('Times_New_Roman', 7), relief='solid')
    interpreters_optionmenu['menu'].config(bg=border_colour, fg=theming.fg, bd=0, font = ('Times_New_Roman', 7))
    interpreters_optionmenu.pack(side='right')

    interpreter_label = tk.Label(bottom_toolbar, text = 'Interpreter:', font = ('Times_New_Roman', 7, 'bold'), bg=theming.dbg, fg=theming.fg)
    interpreter_label.pack(side='right')

    # Main application toolbar. (TOP)..
    top_toolbar = tk.Menu(root, borderwidth=0, relief = 'flat')
    root.config(menu=top_toolbar)
    border_colour = "#EEEEEE"
    file_menu = tk.Menu(top_toolbar, tearoff=False, background=border_colour, foreground=theming.fg, borderwidth=0, relief='flat', )
    
    def active_full_screen(event=None):
        global is_full_screen
        if is_full_screen ==  False:
            root.attributes('-fullscreen', True)
            is_full_screen = True
        else:
            root.attributes('-fullscreen', False)
            is_full_screen = False 
    
        
    file_menu.add_command(label = 'Fullscreen' + ' '*25, command=active_full_screen, accelerator='Ctrl+F', image = fullscreen_icon_img, compound='left')
    root.bind('<Control-F>', active_full_screen)
    root.bind('<Control-f>', active_full_screen)
    file_menu.add_command(label='Open file', command=open_file, accelerator='Ctrl+O', image=openfile_icon_img, compound='left')
    file_menu.add_separator()
    file_menu.add_command(label='New file', command=new_file, accelerator='Ctrl+N', image=newfile_icon_img, compound='left')
    root.bind('<Control-N>', new_file)
    root.bind('<Control-n>', new_file)

    file_menu.add_command(label='Save file', command=save_file, accelerator='Ctrl+S', image=save_icon_img, compound='left')
    file_menu.add_command(label='Save file as', command=save_file_as, accelerator='Ctrl+Shift+S', image=saveas_icon_img, compound='left')
    file_menu.add_separator()
    file_menu.add_command(label='Close selected file', command=close_file, accelerator='Ctrl+Delete')
    file_menu.add_command(label='Close all files', command=close_all_files, accelerator='Ctrl+Shift+W')

    

    file_menu.add_separator()
    settings_submenu = tk.Menu(file_menu, tearoff=False, background=border_colour, foreground=theming.fg, bd=0)
    settings_submenu.add_command(label='Increase font size'+ ' '*25, command=increase_font_size, accelerator='Ctrl++', image=plus_icon_img, compound='left')
    settings_submenu.add_command(label='Decrease font size', command=decrease_font_size, accelerator='Ctrl+-', image=minus_icon_img, compound='left')


    boolvar_realtime_learning = tk.BooleanVar(value=(theming.extract_realtime_learn() == 'True'))

    def toggle_learning():
        if theming.extract_realtime_learn() == 'True':
            theming.change_realtime_learn(val = 'False')
            boolvar_realtime_learning.set(False)

        else:
            theming.change_realtime_learn(val = 'True')
            boolvar_realtime_learning.set(True)

    settings_submenu.add_checkbutton(label='Toggle realtime learning', command=toggle_learning, accelerator='', variable=boolvar_realtime_learning)    
    settings_submenu.add_separator()


    themesavermanager = theming.themeSaveManager()


    syntax_subsubmenu = tk.Menu(settings_submenu, tearoff=False, background=border_colour, foreground=theming.fg)
    def change_theme(name):
        themesavermanager.save_partial_theme(position=2, value=name)
        code_box.config(color_scheme=name_dict[name])

    syntax_subsubmenu.add_command(label='Mariana', command=lambda: change_theme('mariana'))
    syntax_subsubmenu.add_command(label='Monokai', command=lambda: change_theme('monokai'))
    syntax_subsubmenu.add_command(label='Dark modern', command=lambda: change_theme('dracula'))
    syntax_subsubmenu.add_command(label='Dark contrast', command=lambda: change_theme('ayu-dark'))
    syntax_subsubmenu.add_command(label='Light modern', command=lambda: change_theme('ayu-light'))
    settings_submenu.add_cascade(label='Syntax highlight', menu=syntax_subsubmenu)

    file_menu.add_cascade(label='Settings', menu=settings_submenu)
    file_menu.add_separator()
    file_menu.add_command(label='Exit', command=exit, accelerator='Ctrl+Q', image = exit_icon_img, compound='left')
    # file menu key binding. 
    root.bind('<Control-O>', open_file)
    root.bind('<Control-o>', open_file)
    root.bind('<Control-S>', save_file)
    root.bind('<Control-s>', save_file)
    root.bind('<Control-Shift-S>', save_file_as)
    root.bind('<Control-Shift-s>', save_file_as)
    root.bind('<Control-Delete>', close_file)
    root.bind('<Control-Shift-W>', close_all_files)
    root.bind('<Control-Shift-w>', close_all_files)
    root.bind('<Control-equal>', increase_font_size)
    root.bind('<Control-minus>', decrease_font_size)
    root.bind('<Control-Q>', exit)
    root.bind('<Control-q>', exit)


    # file menu key binding END.
    top_toolbar.add_cascade(label='File', menu=file_menu)

    edit_menu = tk.Menu(top_toolbar, tearoff=False, background=border_colour, foreground=theming.fg)
    def copy(event=None):
        edit.copy(code_box=code_box, master=root)
        return "break"

    edit_menu.add_command(label='Copy'+ ' '*40, command=lambda: edit.copy(code_box=code_box, master=root), accelerator='Ctrl+C')
    def cut(event=None):
        edit.cut(code_box=code_box, master=root)
        return "break"

    edit_menu.add_command(label='Cut', command=lambda: edit.cut(code_box=code_box, master=root), accelerator='Ctrl+X')
    def paste(event=None):
        edit.paste(code_box=code_box, master=root)
        return "break"

    edit_menu.add_command(label='Paste', command=lambda: edit.paste(code_box=code_box, master=root), accelerator='Ctrl+V')
    edit_menu.add_separator()
    def undo(event=None):
        edit.undo(code_box=code_box)
        return "break"

    edit_menu.add_command(label='Undo', command=lambda: edit.undo(code_box=code_box), accelerator='Ctrl+Z')
    def redo(event=None):
        edit.redo(code_box=code_box)
        return "break"

    edit_menu.add_command(label='Redo', command=lambda: edit.redo(code_box=code_box), accelerator='Ctrl+Shift+Z')
    edit_menu.add_separator()
    def select_all(event=None):
        edit.select_all(code_box=code_box)
        return "break"

    edit_menu.add_command(label='Select all', command=lambda: edit.select_all(code_box=code_box), accelerator='Ctrl+A')
    def clear(event=None):
        edit.clear_all(code_box=code_box)
        return "break"

    edit_menu.add_command(label='Clear', command=lambda: edit.clear_all(code_box=code_box), accelerator='Shift+Delete')
    edit_menu.add_separator()
    def delete_current(event=None):
        edit.delete_current(code_box=code_box)
        return "break"

    edit_menu.add_command(label='Delete current line', command=lambda: edit.delete_current(code_box=code_box), accelerator='Ctrl+D')
    def select_current(event=None):
        edit.select_current(code_box=code_box)
        return "break"

    edit_menu.add_command(label='Select current line', command=lambda: edit.select_current(code_box=code_box), accelerator='Ctrl+L')

    def delete_after_cursor(event=None):
        edit.dac(code_box=code_box)
        return "break"
    def delete_before_cursor(event=None):
        edit.dbc(code_box=code_box)
        return "break"
    
    edit_menu.add_command(label='Delete after cursor', command=lambda: edit.dac(code_box=code_box), accelerator='Ctrl+K')
    edit_menu.add_command(label='Delete before cursor', command =lambda: edit.dbc(code_box=code_box), accelerator='Ctrl+U')
    edit_menu.add_separator()
    # --

    def remove_all_empties(event=None):
        edit.remove_empty_lines(code_box=code_box)
        return 'break'
    def comment_current(event=None):
        edit.comment_current_line(code_box=code_box)
        return "break"
    
    def capsel(event=None):
        edit.capitalize_sel(code_box=code_box)
        return "break"
    
    def decapsel(event=None):
        edit.decap_sel(code_box=code_box)
        return "break"
    
    edit_menu.add_command(label='Remove empty lines', command =lambda: edit.remove_empty_lines(code_box=code_box), accelerator='Ctrl+Shift+E')
    edit_menu.add_command(label='Comment current line', command =lambda: edit.comment_current_line(code_box=code_box), accelerator='Ctrl+Shift+C')
    edit_menu.add_separator()
    edit_menu.add_command(label='Capitalize selection', command =lambda: edit.capitalize_sel(code_box=code_box), accelerator='Ctrl+Shift+U')
    edit_menu.add_command(label='Decapitalize selection', command =lambda: edit.decap_sel(code_box=code_box), accelerator='Ctrl+Shift+L')
    edit_menu.add_separator()
    edit_menu.add_command(label = 'Indent selected lines', command = lambda: edit.tab(code_box=code_box), accelerator='Tab')
    edit_menu.add_command(label = 'Dedent selected lines', command = lambda: edit.shift_tab(code_box=code_box), accelerator='Shift+Tab')



    def select_current_word(event):
        edit.highlight_cursor_word(code_box=code_box)
        return 'break'
    
    edit_menu.add_command(label = 'Select current word', command = lambda: edit.highlight_cursor_word(code_box=code_box), accelerator='Ctrl+W')


    

    # edit menu keybindings.
    code_box.bind('<Control-W>', select_current_word)
    code_box.bind('<Control-w>', select_current_word)
    code_box.bind('<Control-C>', copy)
    code_box.bind('<Control-c>', copy)
    code_box.bind('<Control-V>', paste)
    code_box.bind('<Control-v>', paste)
    code_box.bind('<Control-X>', cut)
    code_box.bind('<Control-x>', cut)
    code_box.bind('<Control-Z>', undo)
    code_box.bind('<Control-z>', undo)
    code_box.bind('<Control-Shift-Z>', redo)
    code_box.bind('<Control-Shift-z>', redo)
    code_box.bind('<Control-A>', select_all)
    code_box.bind('<Control-a>', select_all)
    code_box.bind('<Shift-Delete>', clear)
    code_box.bind('<Control-D>', delete_current)
    code_box.bind('<Control-d>', delete_current)
    code_box.bind('<Control-L>', select_current)
    code_box.bind('<Control-l>', select_current)
    code_box.bind('<Control-K>', delete_after_cursor)
    code_box.bind('<Control-k>', delete_after_cursor)
    code_box.bind('<Control-U>', delete_before_cursor)
    code_box.bind('<Control-u>', delete_before_cursor)
    code_box.bind('<Control-Shift-E>', remove_all_empties)
    code_box.bind('<Control-Shift-e>', remove_all_empties)
    code_box.bind('<Control-Shift-C>', comment_current)
    code_box.bind('<Control-Shift-c>', comment_current)
    code_box.bind('<Control-Shift-U>', capsel)
    code_box.bind('<Control-Shift-u>', capsel)
    code_box.bind('<Control-Shift-L>', decapsel)
    code_box.bind('<Control-Shift-l>', decapsel)


    # edit menu keybindings (END).
    top_toolbar.add_cascade(label='Edit', menu=edit_menu)

    navigate_menu = tk.Menu(top_toolbar, tearoff=False, background=border_colour, foreground=theming.fg)
    def repos_end(event=None):
        edit.repos_end(code_box=code_box)
        return "break"
    def repos_start(event=None):
        edit.repos_start(code_box=code_box)
        return "break"
    def repos_endline(event=None):
        edit.repos_endline(code_box = code_box)
        return "break"
    def repos_startline(event=None):
        edit.repos_startline(code_box=code_box)
        return 'break'
    def nextword(event=None):
        edit.wordskip_advanced(code_box=code_box)
        return 'break'
    
    def preword(event=None):
        edit.wordskip_reversed(code_box=code_box)
        return "break"
    


    navigate_menu.add_command(label='Navigate to end of code'+ ' '*20, command= lambda: edit.repos_end(code_box=code_box), accelerator='Ctrl+End')
    navigate_menu.add_command(label='Navigate to start of code', command= lambda: edit.repos_start(code_box=code_box), accelerator='Ctrl+Home')
    navigate_menu.add_separator()
    navigate_menu.add_command(label='Navigate to end of line', command=lambda: edit.repos_endline(code_box=code_box), accelerator='End')
    navigate_menu.add_command(label='Navigate to start of line', command=lambda: edit.repos_startline(code_box=code_box) , accelerator='Home')
    navigate_menu.add_separator()
    navigate_menu.add_command(label='Next word', command=lambda: edit.wordskip_advanced(code_box=code_box), accelerator='Ctrl+Right')
    navigate_menu.add_command(label='Previous word', command=lambda: edit.wordskip_reversed(code_box=code_box) , accelerator='Ctrl+Left')


    def next_line(event):
        edit.next_line(code_box=code_box)
        return 'break'
    def pre_line(event):
        edit.pre_line(code_box=code_box)
        return 'break'

    navigate_menu.add_command(label='Next line', command= lambda: edit.next_line(code_box=code_box), accelerator='Alt+Down')
    code_box.bind('<Alt-Down>', next_line)

    navigate_menu.add_command(label='Previous line', command=lambda: edit.pre_line(code_box=code_box), accelerator='Alt+Up')
    code_box.bind('<Alt-Up>', pre_line)


    def go_to_line_interface(event):
        edit.go_to_line(master=root,code_box=code_box, bg=theming.bg, fg = theming.fg)
        return 'break'
    
    navigate_menu.add_command(label='Go to line', command=lambda: edit.go_to_line(code_box=code_box, master=root, bg=theming.bg, fg=theming.fg, forget_label=suggestions_label), accelerator='Ctrl+G', 
                              image = find_icon_img, compound='left')
    root.bind('<Control-G>', go_to_line_interface)
    root.bind('<Control-g>', go_to_line_interface)


    
    
    code_box.bind('<Control-End>', repos_end)
    code_box.bind('<Control-Home>', repos_start)
    code_box.bind('<End>', repos_endline)
    code_box.bind('<Home>', repos_startline)
    code_box.bind('<Control-Right>', nextword)
    code_box.bind('<Control-Left>', preword)


    top_toolbar.add_cascade(label='Navigate', menu=navigate_menu)

    apply_menu = tk.Menu(top_toolbar, tearoff=False, background=border_colour, foreground=theming.fg)
    
    
    wrappers_submenu = tk.Menu(apply_menu, tearoff=False, background=border_colour, foreground=theming.fg )
    wrappers_submenu.add_command(label = 'Wrap with ()', command =lambda: apply.wrap_selected_with(wrapper='(', code_box=code_box))
    wrappers_submenu.add_command(label =  'Wrap with []', command = lambda: apply.wrap_selected_with(wrapper='[', code_box=code_box))
    wrappers_submenu.add_command(label = 'Wrap with {}', command = lambda: apply.wrap_selected_with(wrapper='{', code_box=code_box))
    wrappers_submenu.add_command(label = 'Wrap with ""', command = lambda: apply.wrap_selected_with(wrapper='"', code_box=code_box))
    wrappers_submenu.add_command(label = "Wrap with ''", command = lambda: apply.wrap_selected_with(wrapper='\'', code_box=code_box))
    wrappers_submenu.add_command(label = 'Wrap with ``', command=lambda: apply.wrap_selected_with(wrapper='`', code_box=code_box))
    wrappers_submenu.add_command(label = 'Wrap with ^^', command = lambda: apply.wrap_selected_with(wrapper='^', code_box=code_box))
    wrappers_submenu.add_command(label = 'Wrap with <>', command = lambda: apply.wrap_selected_with(wrapper='<', code_box=code_box))

    apply_menu.add_cascade(label = 'Wrap selection with', menu = wrappers_submenu)




    diagram_submenu = tk.Menu(apply_menu, tearoff=0, background=border_colour, foreground=theming.fg)


    diagram_submenu.add_command(label='Simplified and export to (.html)', command=lambda: generate_then_export(type='Simple'), image=flow_icon_img, compound='left')
    diagram_submenu.add_command(label='Normal and export to (.html)', command=lambda: generate_then_export(type='Normal'), image=flow_icon_img, compound='left')

    apply_menu.add_cascade(label='Generate flowchart', menu=diagram_submenu)
    

    apply_menu.add_separator()
    apply_menu.add_command(label = 'Comment multiline selection', command = lambda: apply.comment_selection(code_box=code_box), accelerator='', image = hashtag_icon_img, 
                           compound='left')
    apply_menu.add_command(label = 'Generate summary for file', command = lambda: apply.summary(master=root, code_box=code_box, file_name=file.already_chosen_file, 
                                                                                                fg= theming.fg, bg=theming.bg), accelerator='',
                                                                                                image = summary_icon_img, compound='left')
    top_toolbar.add_cascade(label='Apply', menu=apply_menu)

    python_menu = tk.Menu(top_toolbar, tearoff=False, background=border_colour, foreground=theming.fg)
    python_menu.add_command(label='Run current file'+ ' '*20, command= run_, accelerator='F5', image = run_icon_img, compound='left')
    python_menu.add_command(label='Python shell', command=lambda: pr.run_python_shell(alogs=alogs_listbox, interpath=theming.extract_interpreter()), accelerator='Ctrl+P'
                            , image = python_icon_img, compound='left')
    python_menu.add_separator()
    python_menu.add_command(label='Terminal', command=lambda: pr.start_terminal(alogs=alogs_listbox), accelerator='Ctrl+T'
                            , image = cmd_icon_img, compound='left')
    python_menu.add_command(label='PIP module', command = lambda: pm.pip_module(master=root, bg=theming.bg, fg=theming.fg, dbg=theming.dbg, font=theming.font), accelerator=''
                            
                            , image = package_icon_img, compound='left')
    

    python_menu.add_command(label='Black format', command = lambda: frmt.BlackFormatter(app_title=information.APP_NAME, master = root, code_box=code_box), 
                            image = format_icon_img, compound='left')

    # Python menu keybinds. 
    root.bind('<F5>', run_)
    def python_shell(event=None):
        pr.run_python_shell(alogs=alogs_listbox, interpath=theming.extract_interpreter())
        return 'break'
    def terminal(event=None):
        pr.start_terminal(alogs=alogs_listbox)
        return 'break'
    root.bind('<Control-P>', python_shell); root.bind('<Control-p>', python_shell)
    root.bind('<Control-T>', terminal) ;     root.bind('<Control-t>', terminal)

    top_toolbar.add_cascade(label='Python', menu=python_menu)

    help_menu = tk.Menu(top_toolbar, tearoff=0, bg=border_colour, fg=theming.fg)
    help_menu.add_command(label = 'Feedback', command=open_feedback_popup,accelerator='', image = feedback_icon_img, compound='left')


    help_menu.add_command(label = 'About', command=lambda: aboutHtml.about_html(master=root, app_name=information.APP_NAME, 
                                        app_version = information.APP_VERSION, 
                                        app_build = information.APP_BUILD, 
                                        app_maker = information.APP_MAKER, 
                                        app_description=information.APP_DESC, 
                                        app_link=information.APP_WEBSITE, 
                                        release_date=information.RELEASE_DATE),accelerator='', image = about_icon_img, compound='left')

    content_of_last = theming.extract_last_chosen_file()
    file.try_last_chosen(content=content_of_last, code_box=code_box, files_listbox=file_listbox, alogs_listbox=alogs_listbox, 
                         forget_label=suggestions_label, master = root)
    top_toolbar.add_cascade(label = 'Help', menu=help_menu)

    root.protocol('WM_DELETE_WINDOW', exit)


Widgets() # call the main Function. 

#spawn in the center of the screen 

# root configurations. 
root.resizable(True, True)
root.config(bg = theming.bg) # global background
root.title(information.APP_NAME + " " + information.APP_VERSION.lower())
root.iconphoto(True, icon_main)
root.state('zoomed')
root.mainloop()
# end of the main code. 
# this is a change please preserve me
