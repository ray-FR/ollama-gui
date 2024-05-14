import subprocess
import random
import requests
from PIL import ImageTk, Image



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
  te_b = ctk.CTkButton(te, text="test")
  
  inp = te.get_input()
  if inp:
    subprocess.run(['ollama', 'pull', inp])
  else:
    print("The program cannot be run if there are no models installed.\nConsider one of the following models: phi3, qwen:4b, llama3\n\n")
    quit()
     
  




app = ctk.CTk()
app.geometry('1400x720')
app.title('Ollama GUI')
app.resizable(False, False)


p1, p2 = 0,0






b = ollama.list()
n_model = []

for i in range(len(b['models'])):
    n_model.append(b['models'][i]['name'])


def downloader():

  def cat_api():
    c_api = requests.get("https://api.thecatapi.com/v1/images/search").json()
    c_url = c_api[0]["url"]
    img = Image.open(requests.get(c_url, stream=True).raw)
    img.thumbnail((400, 400))
    c_img = ImageTk.PhotoImage(img)
    ent_l2_l.configure(image=c_img)




  def RPS(c):
    global p1, p2

    

    ent_l1_res.configure(fg_color='transparent')
    res = random.randint(1, 3)

    if res == 1 and c == "R":
        ent_l1_res.configure(text=f"Tie!\nYour score: {p1}, the computer score: {p2}")
    elif res == 2 and c == "P":
        ent_l1_res.configure(text=f"Tie!\nYour score: {p1}, the computer score: {p2}")
    elif res == 3 and c == "S":
        ent_l1_res.configure(text=f"Tie!\nYour score: {p1}, the computer score: {p2}")

    elif res == 1 and c == "P":
        p1+=1
        ent_l1_res.configure(text=f"You win! +1 point\nYour score: {p1}, the computer score: {p2}")
        
    elif res == 2 and c == "S":
        p1+=1
        ent_l1_res.configure(text=f"You win! +1 point\nYour score: {p1}, the computer score: {p2}")
        
    elif res == 3 and c == "R":
        p1+=1
        ent_l1_res.configure(text=f"You win! +1 point\nYour score: {p1}, the computer score: {p2}")
        

    elif res == 1 and c == "S":
        p2+=1
        ent_l1_res.configure(text=f"You lose! +1 point for the computer!\nYour score: {p1}, the computer score: {p2}")
        
    elif res == 2 and c == "R":
        p2+=1
        ent_l1_res.configure(text=f"You lose! +1 point for the computer!\nYour score: {p1}, the computer score: {p2}")
        
    elif res == 3 and c == "P":
        p2+=1
        ent_l1_res.configure(text=f"You lose! +1 point for the computer!\nYour score: {p1}, the computer score: {p2}")
        

    if p1 == 5:
      ent_l1_res.configure(text=f"Congrats! You won!\nYour score: {p1}, the computer score: {p2}", fg_color="green")
      p1, p2 = 0, 0
    if p2 == 5:
      ent_l1_res.configure(text=f"You lose!\nYour score: {p1}, the computer score: {p2}", fg_color="red")
      p1, p2 = 0, 0







  button_do.configure(text="Check pop-up")
  button_do.configure(state='disabled')
  mod_get = ctk.CTkInputDialog(text="What is the name of the model you want?", title="Model download")
  ans = mod_get.get_input()
  if ans:
    ent = ctk.CTkToplevel(app)
    ent.geometry('580x740')
    ent.resizable(False, False)
    ent.title("Entertainment")
    ent_t = ctk.CTkLabel(ent, text="While you wait for the install of your model, you can use objects inside this window to pass time", wraplength=540)
    ent_t.pack(pady=20)
    ent_tabs = ctk.CTkTabview(ent, width=540)
    ent_tabs.pack(pady=20)
    ent1 = ent_tabs.add("Rock, Paper, Scissor")
    ent2 = ent_tabs.add("Cat photo generator")
    ent_tabs.set("Rock, Paper, Scissor")


    ent_l1 = ctk.CTkLabel(ent1, text="A simple game of rock, paper, scissor!")
    ent_l1.pack()
    ent_l1_res = ctk.CTkLabel(ent1, text="Result of the game will replace this text")
    ent_l1_res.pack()

    ent_l1_f = ctk.CTkFrame(ent1)
    ent_l1_f.pack(side="bottom")

    ent_l1_b1 = ctk.CTkButton(ent1, text="Rock", command= lambda: RPS("R"))
    ent_l1_b1.pack(in_=ent_l1_f, side="left", padx=(0, 15))
    ent_l1_b2 = ctk.CTkButton(ent1, text="Paper", command= lambda: RPS("P"))
    ent_l1_b2.pack(in_=ent_l1_f, side="left", padx=(0, 15))
    ent_l1_b3 = ctk.CTkButton(ent1, text="Scissor", command= lambda: RPS("S"))
    ent_l1_b3.pack(in_=ent_l1_f, side="left")




    ent_l2 = ctk.CTkLabel(ent2, text="Cat pictures! Just press the reload button to get new ones!")
    ent_l2.pack()

    ent_l2_l = ctk.CTkLabel(ent2, text="")
    ent_l2_l.pack(pady=15)
    ent_l2_b = ctk.CTkButton(ent2, text="Reload", command=cat_api)
    ent_l2_b.pack(side="bottom", padx=(0, 15))





    subprocess.run(['ollama', 'pull', ans])
    n_model = []
    b = (ollama.list())
    for i in range(len(b['models'])):
      n_model.append(b['models'][i]['name'])
    dropdown.configure(values=n_model)
    m.set(n_model[0])


  button_do.configure(text="Download more models")
  button_do.configure(state='normal')
  print('\n\n')

def delete():
  button_de.configure(text="Check pop-up")
  button_de.configure(state='disabled')
  mod_get = ctk.CTkInputDialog(text="What is the name of the model you want to delete?", title="Model delete")
  ans = mod_get.get_input()
  if ans:
    subprocess.run(['ollama', 'rm', ans])
    n_model = []
    b = (ollama.list())
    for i in range(len(b['models'])):
      n_model.append(b['models'][i]['name'])
    dropdown.configure(values=n_model)
    m.set(n_model[0])

  button_de.configure(text="Delete more models")
  button_de.configure(state='normal')
  print('\n\n')

def Response(app):
    
    
    entry.configure(state='disabled')
    response = ollama.chat(model=m.get(), messages=[
    {
    'role': 'user',
    'content': txt.get(),
    },
    ],
    keep_alive=60)
    answer.configure(text=response['message']['content'])
    txt.set("")
    entry.configure(state="normal")
    



m = ctk.StringVar(value=n_model[0])
dropdown = ctk.CTkOptionMenu(app, values=n_model, variable=m, font=("Arial", 12))
dropdown.pack(pady=(10, 30))

answer = ctk.CTkLabel(app, width=1250, text='', font=('Arial', 18), fg_color='gray', wraplength=1300, corner_radius=5)
answer.pack(pady=5)

butt_frame = ctk.CTkFrame(app)
butt_frame.pack(side="bottom")

button_do = ctk.CTkButton(app, text="Download more models", command=downloader, font=("Arial", 11))
button_do.pack(in_=butt_frame, side="left", pady=(0, 10), padx=(0, 15))

button_de = ctk.CTkButton(app, text="Delete models", command=delete, font=("Arial", 11))
button_de.pack(in_=butt_frame, side="left", pady=(0, 10))

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