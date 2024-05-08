import ollama
import customtkinter as ctk


app = ctk.CTk()
app.geometry('1400x720')
app.title('test')
app.resizable(False, False)




l_model = []
a = (ollama.list())
for i in range(len(a['models'])):
    l_model.append(a['models'][i]['name'])



def Response(app):
    
    
    entry.configure(state='disabled')
    
    response = ollama.chat(model=t.get(), messages=[
    {
    'role': 'user',
    'content': txt.get(),
    },
    ])
    answer.configure(text=response['message']['content'])
    txt.set("")
    entry.configure(state="normal")
    



t = ctk.StringVar(value=l_model[0])
dropdown = ctk.CTkOptionMenu(app, values=l_model, variable=t)
dropdown.pack(pady=30)

answer = ctk.CTkLabel(app, width=1250, text='', font=('Arial', 20), fg_color='gray', wraplength=1300, corner_radius=5)
answer.pack(pady=30)

txt = ctk.StringVar()
entry = ctk.CTkEntry(app, width=800, textvariable=txt, corner_radius=5, font=('Arial', 22), height=35)
entry.pack(padx = 20, pady = 25, side="bottom")









entry.bind('<Return>', Response)
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