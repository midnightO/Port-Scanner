import socket # for connecting
from colorama import init, Fore

# some colors
init()
GREEN = Fore.GREEN
RESET = Fore.RESET
GRAY = Fore.LIGHTBLACK_EX

def is_port_open(host, port):
    """
    Determina se o Host tem a porta aberta
    """
    # Criando uma conexão socket
    s = socket.socket()
    try:
        # Tentando conectar ao host utilizando a porta
        s.connect((host, port))
        # Limite de tempo (quanto mais rapido, menor a precisão)
        s.settimeout(0.2)
    except:
        # Não foi Possível conectar, Porta fechada
        # return false
        return False
    else:
        # A conexão foi estabelecida, Porta aberta!
        return True

# Pegando o host pelo input do usuário
host = input("Enter the host:")
# Varredura das portas 1 até 1024
for port in range(1, 1025):
    if is_port_open(host, port):
        print(f"{GREEN}[+] {host}:{port} is open      {RESET}")
    else:
        print(f"{GRAY}[!] {host}:{port} is closed    {RESET}", end="\r")