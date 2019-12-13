from user_interface import UI
# from backend_app import process

def process(data):
    print(data)
    
app = UI(process_fn=process)
app.mainloop()