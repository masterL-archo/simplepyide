import tkinter as tk 
import tkhtmlview as thk
import sys 
import platform



def about_html(master,  app_name, app_version, app_build, app_maker, app_description, app_link, release_date):
    windows_version = platform.version()

    html_code = f"""<h1 style="font-family: 'Courier New', Courier, monospace; font-weight: bold; color: black;">
  {app_name}
</h1>
<p style="font-family: 'Courier New', Courier, monospace; font-size: 12px; color: #555; margin-top: 0;">
  {app_version}  {app_build}
</p>
<p style="font-family: 'Courier New', Courier, monospace; font-size: 8px; color: #333;">
  {app_description}
</p>
<p style="font-family: 'Courier New', Courier, monospace; font-size: 10px; color: #333;">
  <a href="{app_link}" target="_blank" rel="noopener noreferrer" style="color: #007acc;">Visit us on our website</a>
</p>
<p style="font-family: 'Courier New', Courier, monospace; font-size: 10px; color: #333;">
  Windows Version: {windows_version}
</p>
<p style="font-family: 'Courier New', Courier, monospace; font-size: 10px; color: #333;">
  Made by {app_maker}
</p>
"""
    popup = tk.Toplevel(master)
    popup.wm_attributes('-toolwindow', True)
    popup.resizable(0,0)
    popup.bell()

    html_box = thk.HTMLLabel(popup, html=html_code)
    html_box.pack(expand=True, fill = 'both')
    html_box.fit_height()

    popup.title('About')

    width = 300
    height = 280

    screen_width = popup.winfo_screenwidth()
    screen_height = popup.winfo_screenheight()

    x = (screen_width // 2) - (width // 2) - 10
    y = ((screen_height // 2) - (height // 2)) - 35

    popup.geometry(f'{width}x{height}+{x}+{y}')
    popup.mainloop()

