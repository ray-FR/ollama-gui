import subprocess
print('\n\n')
x = str(input('Want to install the relevent libraries? (Ollama, customtkinter)  [Y, N] ->   '))
print()
if x.upper() == 'Y':
   subprocess.run(['pip', 'install', 'ollama'])
   subprocess.run(['pip', 'install', 'customtkinter'])
   print("\n\nIf no errors happened, these 2 libraries should be correctly installed, if theres an issue, just relaunch the program, enjoy! ")
   print('\n\n')



import ollama
import customtkinter as ctk



b = ollama.list()
if b['models'] == None:
  te = ctk.CTkInputDialog(title="Model download" ,text="It seems you don't have any models installed, please enter one below, if you choose to cancel then the program will stop itself")
  te.focus()
  inp = te.get_input()
  if inp:
    subprocess.run(['ollama', 'pull', inp])
  else:
    quit()
     
  

app = ctk.CTk()
app.geometry('1400x720')
app.title('Ollama GUI')
app.resizable(False, False)









b = ollama.list()
n_model = []

for i in range(len(b['models'])):
    n_model.append(b['models'][i]['name'])


def downloader():
  button_do.configure(text="Check pop-up")
  button_do.configure(state='diabled')
  mod_get = ctk.CTkInputDialog(text="What is the name of the model you want?", title="Model download")
  ans = mod_get.get_input()
  if ans:
    subprocess.run(['ollama', 'pull', ans])
    n_model = []
    b = (ollama.list())
    for i in range(len(b['models'])):
      n_model.append(b['models'][i]['name'])
    dropdown.configure(values=n_model)
    t.set(n_model[0])

  button_do.configure(text="Download more models")
  button_do.configure('normal')
  print('\n\n')

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
    



t = ctk.StringVar(value=n_model[0])
dropdown = ctk.CTkOptionMenu(app, values=n_model, variable=t, font=("Arial", 12))
dropdown.pack(pady=(10, 30))

answer = ctk.CTkLabel(app, width=1250, text='', font=('Arial', 18), fg_color='gray', wraplength=1300, corner_radius=5)
answer.pack(pady=5)

butt_frame = ctk.CTkFrame(app)
butt_frame.pack(side="bottom")

button_do = ctk.CTkButton(app, text="Download more models", command=downloader, font=("Arial", 11))
button_do.pack(in_=butt_frame  ,side="left", pady=(0, 10), padx=(0, 15))

button_de = ctk.CTkButton(app, text="Delete models", font=("Arial", 11))
button_de.pack(in_=butt_frame  ,side="left", pady=(0, 10))

txt = ctk.StringVar()
entry = ctk.CTkEntry(app, width=800, textvariable=txt, corner_radius=10, font=('Arial', 22), height=35)
entry.pack(padx = 20, pady = 25, side="bottom")
entry.focus()












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