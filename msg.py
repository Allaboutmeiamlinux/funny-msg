import tkinter as tk

def say_hello():
    while True:
        
        app = tk.Tk()
        app.title("linux")
    
        label = tk.Label(app, text="iam linux")
        label.pack(pady=10)
    
        app.mainloop()


app = tk.Tk()
app.title("linux")

label = tk.Label(app, text="iam linux!")
label.pack(pady=10)

button = tk.Button(app, text="ok", command=say_hello)
button.pack()

app.mainloop()
