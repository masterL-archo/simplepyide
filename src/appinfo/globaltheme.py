import os 
import subprocess


appname_operation = 'temp_saves'

global_roaming_path = os.getenv('APPDATA')
save_folder_path = os.path.join(global_roaming_path, appname_operation)

if os.path.exists(save_folder_path) == True:
    pass
else:
    os.mkdir(save_folder_path)

theme_save_path = os.path.join(save_folder_path, 'current_theme.txt')
if os.path.exists(theme_save_path) == True:
    pass
else:
    with open(theme_save_path, 'w') as writer:
        writer.write('lightcontrast\n12\nayu-light')
# themes (lightmodern, darkmodern)


class themeSaveManager:
    def save_partial_theme(self,position, value):
        # Read existing lines or create default if file not exists or empty
        try:
            with open(theme_save_path, 'r') as reader:
                lines = reader.read().splitlines()
        except FileNotFoundError:
            lines = ['', '', '']

        # Ensure list length is at least 3
        while len(lines) < 3:
            lines.append('')

        # Update specific position (0-based)
        if 0 <= position < 3:
            lines[position] = str(value)

        # Write all lines back to file
        with open(theme_save_path, 'w') as writer:
            for line in lines:
                writer.write(line + '\n')

    def extract_theme(self):
        with open(theme_save_path, 'r') as reader:
            lines = reader.read().splitlines()
        # Ensure list has at least 3 items, fill with defaults if needed
        while len(lines) < 3:
            lines.append('')
        return lines[:3]



manager1 = themeSaveManager()
theme = manager1.extract_theme()[0]
code_size = int(manager1.extract_theme()[1])
highlight = manager1.extract_theme()[2]

bg = "#F8F8F8"  # very light gray (almost white)
fg = "#1A1A1A"  # very dark gray (almost black)
dbg = "#D1D1D1"  # medium light gray for subtle depth


font = 'Consolas' # global used font type. 
code_font = 'Consolas'




learn_save_path = os.path.join(save_folder_path, 'realtime_learn.txt')
if os.path.exists(learn_save_path) == True:
    pass
else:
    with open(learn_save_path, 'w') as writer:
        writer.write('True')


def extract_realtime_learn():
    with open(learn_save_path, 'r') as reader:
        i = reader.read()
    return i 


def change_realtime_learn(val):
    with open(learn_save_path, 'w') as writer:
        writer.write(val)


current_interpreter = os.path.join(save_folder_path, 'current_interpreter.txt')

comm = subprocess.run('where python', capture_output=True, shell=True, text=True)

interpreters = [path.strip() for path in comm.stdout.splitlines() if path.strip()]

if os.path.exists(current_interpreter) == True:
    pass
else:
    with open(current_interpreter, 'w') as writer:
        writer.write(interpreters[0])

def extract_interpreter():
    with open(current_interpreter, 'r') as reader:
        i = reader.read()
    return i 


def change_interpreter(val):
    with open(current_interpreter, 'w') as writer:
        writer.write(val)



last_chosen_file_save = os.path.join(save_folder_path, 'last_chosen_file.txt')

if os.path.exists(last_chosen_file_save):
    pass
else:
    with open(last_chosen_file_save, 'w') as writer:
        writer.write('')


def change_last_chosen_file(file_path):
    with open(last_chosen_file_save, 'w') as writer:
        writer.write(file_path)

def extract_last_chosen_file():
    with open(last_chosen_file_save, 'r') as reader:
        path = reader.read()
        pass
    return path 



