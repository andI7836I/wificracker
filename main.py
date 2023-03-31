#import tkinter and subprocess modules
import tkinter as tk
import subprocess

#create a class Application which inherits from tk.Frame
class wificracker(tk.Frame):
    #initialize the frame
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    #create widgets for the application
    def create_widgets(self):
        self.hello = tk.Label(self, text="hello, this is wificracker \n lets start")
        self.hello.pack()
        self.text = tk.Text(self)
        self.text.pack()
        self.button = tk.Button(self, text="start capture handshake", 
                                command=self.run_command)
        self.button.pack()

    #define the run_command function to execute a shell command
    def run_command(self):
        command = "ls -l"
        process = subprocess.Popen(command, stdout=subprocess.PIPE,  
                                    stderr=subprocess.PIPE, shell=True) 
        output, error = process.communicate() 
        #check if there is an error in executing the command
        if error: 
            self.text.insert(tk.END, error.decode()) 
        else: 
            self.text.insert(tk.END, output.decode()) 
 
#create a root window and an instance of the Application class
root = tk.Tk() 
root.title("wificracker")
app = wificracker(master=root) 
#start the main loop
app.mainloop()