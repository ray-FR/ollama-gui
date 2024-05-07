import ollama
import tkinter
import customtkinter as ctk




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

app.mainloop()