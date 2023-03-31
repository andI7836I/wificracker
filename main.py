import tkinter as tk
import subprocess


class wificracker(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master.geometry("600x800")
        self.master.configure(bg="#1A1A1D")
        self.create_widgets()

    def create_widgets(self):
        self.title = tk.Label(
            self.master,
            text="WIFICRACKER",
            font=("Courier", 30),
            fg="#8AFF33",
            bg="#1A1A1D",
            pady=20,
        )
        self.title.pack()

        self.instructions = tk.Label(
            self.master,
            text="Enter the target network name and interface,\nthen click Scan Networks:",
            font=("Courier", 12),
            fg="#8AFF33",
            bg="#1A1A1D",
            pady=10,
        )
        self.instructions.pack()

        self.target_label = tk.Label(
            self.master,
            text="Target Network:",
            font=("Courier", 14),
            fg="#8AFF33",
            bg="#1A1A1D",
            pady=10,
        )
        self.target_label.pack()

        self.target_input = tk.Entry(
            self.master,
            width=40,
            borderwidth=2,
            fg="#FFFFFF",
            bg="#2C2C32",
            font=("Courier", 14),
        )
        self.target_input.pack(pady=10)

        self.interface_label = tk.Label(
            self.master,
            text="WiFi Interface:",
            font=("Courier", 14),
            fg="#8AFF33",
            bg="#1A1A1D",
            pady=10,
        )
        self.interface_label.pack()

        self.interface_input = tk.Entry(
            self.master,
            width=40,
            borderwidth=2,
            fg="#FFFFFF",
            bg="#2C2C32",
            font=("Courier", 14),
        )
        self.interface_input.pack(pady=10)

        self.scan_button = tk.Button(
            self.master,
            text="SCAN NETWORKS",
            font=("Courier", 16),
            fg="#1A1A1D",
            bg="#8AFF33",
            activebackground="#FF5733",
            padx=20,
            pady=10,
            command=self.scan_networks,
        )
        self.scan_button.pack(pady=10)

        self.button = tk.Button(
            self.master,
            text="CAPTURE",
            font=("Courier", 16),
            fg="#1A1A1D",
            bg="#8AFF33",
            activebackground="#FF5733",
            padx=20,
            pady=10,
            command=self.run_command,
        )
        self.button.pack(pady=10)

        self.output_label = tk.Label(
            self.master,
            text="Output:",
            font=("Courier", 12),
            fg="#8AFF33",
            bg="#1A1A1D",
            pady=10,
        )
        self.output_label.pack()

        self.output = tk.Text(
            self.master,
            height=10,
            width=50,
            fg="#FFFFFF",
            bg="#2C2C32",
            borderwidth=2,
            font=("Courier", 14),
        )
        self.output.pack(padx=20)

    def scan_networks(self):
        target = self.target_input.get()
        interface = self.interface_input.get()
        command = f"sudo NetworkManager stop && sudo airmon-ng check kill && sudo airmon-ng start {interface} && sudo airodump-ng {interface}mon"
        process = subprocess.Popen(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=True,
        )
        output, error = process.communicate()
        if error:
            self.output.insert(tk.END, f"Error:\n\n{error.decode()}")
        else:
            self.output.insert(tk.END, f"Output:\n\n{output.decode()}")

    def run_command(self):
        target = self.target_input.get()
        command = f"sudo aircrack-ng -a2 -b {target} capturefile.cap"
        process = subprocess.Popen(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=True,
        )
        output, error = process.communicate()
        if error:
            self.output.insert(tk.END, f"Error:\n\n{error.decode()}")
        else:
            self.output.insert(tk.END, f"Output:\n\n{output.decode()}")


root = tk.Tk()
root.title("WIFICRACKER")
app = wificracker(master=root)
app.mainloop()

