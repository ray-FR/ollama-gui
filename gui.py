import ollama
import tkinter
import customtkinter as ctk
import sys
import importlib




def testy(app):
    
    response = ollama.chat(model='phi3', messages=[
    {
    'role': 'user',
    'content': txt.get(),
    },
    ])
    test.configure(text=response['message']['content'])



app = ctk.CTk()
app.geometry('600x400')
app.title('test')
app.resizable(True, False)
txt = ctk.StringVar()

test = ctk.CTkLabel(app, width=450, text='a', font=('Arial', 15), fg_color='gray')
test.pack(pady=20)
entry = ctk.CTkEntry(app, width=500, placeholder_text="write something", textvariable=txt)
entry.pack(padx = 20, pady = 50)

entry.bind('<Return>', testy)








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