#################
# LIBRARY IMPORTS
#################
import tkinter as tk
import tkinter.ttk as ttk

from collections import OrderedDict
from PIL import ImageTk, Image
import time

##############
# FRONT END UI
##############
"""Creation of front end frame with various object components"""
class UI(tk.Tk):
    """
    Main Class that initiates and control the UI
    """
    def __init__(self, process_fn, *args, **kwargs) :
        tk.Tk.__init__(self, *args, **kwargs)
        self.process_fn = process_fn
        # self.attributes('-fullscreen', True)

        # Create a container frame to hold all the pages inside it
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = OrderedDict()
        self.current_frame = None

        self.create_frames(container)

        self.frames_list = list(self.frames.keys())
        self.current_frame_index = 0
        self.show_frame('StartPage')

    def create_frames(self, container):
        start_page_frame = StartPage(container, self)
        self.frames['StartPage'] = start_page_frame
        start_page_frame.grid(row=0, column=0, sticky="nsew")

    def show_frame(self, cont, data=None):
        """
        Display the given frame
        :param cont:
        :return:
        """
        frame = self.frames[cont]
        self.current_frame = cont
        print("current frame is", cont)
        frame.tkraise()
        return frame

    def reset(self):
        self.show_frame(self.frames_list[0])


class StartPage(tk.Frame):
    """
    Start page frame Class
    """
    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent)

        menubar = MenuBar(self, controller)
        controller.config(menu=menubar)

        head_frame = HeadFrame(self, controller)
        self.body_frame = BodyFrame(self, controller)
        head_frame.pack()
        self.body_frame.pack(fill=tk.BOTH, expand=True)

        optimize_btn = tk.Button(self, text="SELECT PORTFOLIO", bg='green', fg='white', command=self.optimize)
        optimize_btn.pack(pady=10)

    def optimize(self):
        print("Getting Values")
        data = {}
        data['time'] = time.strftime("%H-%M")
        data['sector'] = self.body_frame.dropdown1_cmd.get()
        data['index'] = self.body_frame.dropdown2_cmd.get()
        data['asset_class'] = self.body_frame.dropdown3_cmd.get()
        data['no_of_instruments'] = self.body_frame.dropdown4_cmd.get()
        data['risk_profile'] = self.body_frame.radiocmd.get()
        print(data)
        self.controller.withdraw()
        self.controller.process_fn(data)
        self.controller.deiconify()


class HeadFrame(tk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        self.parent = parent
        tk.Frame.__init__(self, parent)

        self.title_label = tk.Label(self, text="PORTFOLIO SELECTOR\nSector specific", font=('Cambria', 20, 'bold'))

        self.watch_label = tk.Label(self, font=('times', 12))
        self.update_watch()

        logo = Image.open("images/logo.jpg")
        self.logo = ImageTk.PhotoImage(logo)
        self.logo_label = tk.Label(self, image=self.logo)

        self.columnconfigure(0, weight=4)
        self.columnconfigure(1, weight=1)

        self.title_label.grid(row=0, column=0, sticky='s')
        self.watch_label.grid(row=1, column=0, sticky='n')
        self.logo_label.grid(row=0, rowspan=2, column=1, sticky='n')


    def update_watch(self): 
        time_string = "Date: " + time.strftime('%d-%m-%Y') + "  Time: " + time.strftime('%H:%M:%S')
        self.watch_label.configure(text=time_string)
        self.controller.after(200, self.update_watch) #it'll call itself continuously


class BodyFrame(tk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        self.parent = parent
        tk.Frame.__init__(self, parent)

        label_1 = tk.Label(self, text="SECTOR", borderwidth=2, relief="solid", height=3)
        label_2 = tk.Label(self, text="RISK PROFILE", borderwidth=2, relief="solid", height=3)
        label_3 = tk.Label(self, text="INDEX", borderwidth=2, relief="solid", height=3)
        label_4 = tk.Label(self, text="ASSET CLASS", borderwidth=2, relief="solid", height=3)
        label_5 = tk.Label(self, text="NO OF STOCKS", borderwidth=2, relief="solid", height=3)

        label_1.grid(row=0, column=0, rowspan=2, sticky='nswe', pady=10, padx=(15, 75))
        label_2.grid(row=2, column=0, rowspan=2, sticky='nswe', pady=10, padx=(15, 75))
        label_3.grid(row=4, column=0, rowspan=2, sticky='nswe', pady=10, padx=(15, 75))
        label_4.grid(row=6, column=0, rowspan=2, sticky='nswe', pady=10, padx=(15, 75))
        label_5.grid(row=8, column=0, rowspan=2, sticky='nswe', pady=10, padx=(15, 75))


        # Sector elements
        sectors_list = ["Information Tech", "Insurance"]
        self.dropdown1_cmd = tk.StringVar()
        self.dropdown1_cmd.set(sectors_list[0]) # default value
        dropdown1 = tk.OptionMenu(self, self.dropdown1_cmd, *sectors_list)
        dropdown1.grid(row=0, column=1, columnspan=3, sticky='ws')

        # Risk profile elements
        self.radiocmd = tk.IntVar()
        radio1 = tk.Radiobutton(self, text="High", variable=self.radiocmd, value=1)
        radio2 = tk.Radiobutton(self, text="Medium", variable=self.radiocmd, value=2)
        radio3 = tk.Radiobutton(self, text="Low", variable=self.radiocmd, value=3)
        radio1.grid(row=2, column=1, sticky='sw')
        radio2.grid(row=2, column=2, sticky='sw')
        radio3.grid(row=2, column=3, sticky='sw')

        # INDEX elements
        INDEX_list = ["S&P 500", "NASDAQ"]
        self.dropdown2_cmd = tk.StringVar()
        self.dropdown2_cmd.set(INDEX_list[0]) # default value
        dropdown2 = tk.OptionMenu(self, self.dropdown2_cmd, *INDEX_list)
        dropdown2.grid(row=4, column=1, columnspan=3, sticky='ws')

        # ASSET CLASS elements
        assets_list = ["Stocks", "Commodities"]
        self.dropdown3_cmd = tk.StringVar()
        self.dropdown3_cmd.set(assets_list[0]) # default value
        dropdown3 = tk.OptionMenu(self, self.dropdown3_cmd, *assets_list)
        dropdown3.grid(row=6, column=1, columnspan=3, sticky='ws')

        # NO OF STOCKS elements
        no_of_stocks_list = ["3", "5", "10"]
        self.dropdown4_cmd = tk.StringVar()
        self.dropdown4_cmd.set(no_of_stocks_list[0]) # default value
        dropdown4 = tk.OptionMenu(self, self.dropdown4_cmd, *no_of_stocks_list)
        dropdown4.grid(row=8, column=1, columnspan=3, sticky='ws')    

        
class MenuBar(tk.Menu):
    def __init__(self,master,controller, **kw):
        tk.Menu.__init__(self, master, kw)

        filemenu = FileMenu(self, controller)
        self.add_cascade(label="File", menu=filemenu)

        windowsmenu = WindowsMenu(self, controller)
        self.add_cascade(label="Windows", menu=windowsmenu)

        version = VersionMenu(self, controller)
        self.add_cascade(label="Version", menu=version)


class FileMenu(tk.Menu):
    def __init__(self, master, controller, **kw):
        tk.Menu.__init__(self, master, kw, tearoff=0)

        self.add_command(label="New", command=self.new)
        self.add_command(label="Open", command=self.open)
        self.add_separator()
        self.add_command(label="Exit", command=controller.quit)

    def new(self):
        print("new")

    def open(self):
        print("open")

class WindowsMenu(tk.Menu):
    def __init__(self, master, controller, **kw):
        tk.Menu.__init__(self, master, kw, tearoff=0)

        self.add_command(label="window 1", command=self.window_one)
        self.add_separator()
        self.add_command(label="window 2", command=self.window_two)

    def window_one(self):
        print("window one")

    def window_two(self):
        print("window two")

class VersionMenu(tk.Menu):
    def __init__(self, master, controller, **kw):
        tk.Menu.__init__(self, master, kw, tearoff=0)

        self.add_command(label="Help Index", command=self.help_index)
        self.add_command(label="About...", command=self.about)

    def help_index(self):
        print("Help Index")
        self.entryconfig(0, label = "Clicked!", command=self.about)

    def about(self):
        print("about")
