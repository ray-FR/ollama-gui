import ollama
import tkinter
import customtkinter as ctk
import sys
import importlib







app = ctk.CTk()
app.geometry('600x400')
app.title('test')
app.resizable(True, False)


test = ctk.CTkLabel(app, width=300, text="AAA")
test.pack()
entry = ctk.CTkEntry(app, width=200, placeholder_text="testing")
entry.pack(padx = 20, pady = 50)





#note stuff
"""
a = (ollama.list())
print(a['models'][0]['name'])
print(a['models'][1]['name'])
print(len(a['models']))

response = ollama.chat(model='phi3', messages=[
  {
    'role': 'user',
    'content': 'what is CO2?',
  },
])
print(response['message']['content'])
"""
"""
if 'ttkbootstrap' in sys.modules:
    print('N')
future code to be used to check if a certain lib is installed on the system
def check(lib_n):
  try:
    importlib.import_module(lib_n)

  except ModuleNotFoundError:
    import subprocess
    subprocess.run(['pip', 'install', lib_n])

"""    

app.mainloop()