import subprocess
print('\n\n')
x = str(input('Want to install the relevent libraries? (Ollama, customtkinter)  [Y, N] ->   '))
print()
if x.upper() == 'Y':
   subprocess.run(['pip', 'install', 'ollama'])
   subprocess.run(['pip', 'install', 'customtkinter'])
   print("\n\nIf no errors happened, these 2 libraries should be correctly installed, just in case of an issue, the program will stop itself, once you re-run, please type 'N' or any other letters")
   print('\n\n')
   quit()


import ollama
import customtkinter as ctk



app = ctk.CTk()
app.geometry('1400x720')
app.title('Ollama GUI')
app.resizable(False, False)
app.iconbitmap()




l_model = []

b = ollama.list()
if b['models'] == []:
  a = str(input("It seems like you have no models installed. Please enter one below, enter h for recommended models ->   "  ))
  if a.lower() == 'h':
    print(
    """\n\n
     3 recommended models:
          

      -phi3: small and lightweight. Can be run pretty easily.
      -mistral: not too big not too small, requires better specs
      -llama-3: very ressource intensive, but a very capable model

          

      You can also check other models on the ollama website: https://ollama.com/library
      \n\n\n
    """)
    a = str(input("now choose one! ->  "))
  print('\n\n')
  subprocess.run(['ollama', 'pull', a])

b = ollama.list()

for i in range(len(b['models'])):
    l_model.append(b['models'][i]['name'])


def downloader():
  button_d.configure(text="Check terminal")
  button_d.configure(state='diabled')
  a = str(input("What is the name of the model you wish to download? (From Ollama)  "))
  print('\n\n')
  subprocess.run(['ollama', 'pull', a])
  button_d.configure(text="Download more models (in terminal)")
  button_d.configure('normal')
  n_model = []
  b = (ollama.list())
  for i in range(len(b['models'])):
    n_model.append(b['models'][i]['name'])
  dropdown.configure(values=n_model)
  t.set(n_model[0])
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
    



t = ctk.StringVar(value=l_model[0])
dropdown = ctk.CTkOptionMenu(app, values=l_model, variable=t)
dropdown.pack(pady=(20, 25))

answer = ctk.CTkLabel(app, width=1250, text='', font=('Arial', 20), fg_color='gray', wraplength=1300, corner_radius=5)
answer.pack(pady=5)

button_d = ctk.CTkButton(app, text="Download more models (in terminal)", command=downloader)
button_d.pack(side="bottom", pady=(0, 10))

txt = ctk.StringVar()
entry = ctk.CTkEntry(app, width=800, textvariable=txt, corner_radius=10, font=('Arial', 22), height=35)
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