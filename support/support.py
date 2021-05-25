import getpass
import os
import smtplib
import socket
import sys
import time
import platform
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from threading import Thread
from pyngrok import ngrok, conf
from support.settings import USER_EMAIL, PASSWORD_EMAIL, SEND_TO

config = conf

if len(USER_EMAIL) == 0:
    with open('settings.py', 'w') as f:
        USER_EMAIL = input('Digite o seu e-mail: ').lower()
        PASSWORD_EMAIL = input('Digite a senha do e-mail: ')
        SEND_TO = input('Digite o e-mail de destino: ').lower()
        text = f"USER_EMAIL = '{USER_EMAIL}'\nPASSWORD_EMAIL = '{PASSWORD_EMAIL}'\nSEND_TO = '{SEND_TO}'\n"
        f.write(text)
        os.system('cls' if os.name == 'nt' else 'clear')


def get_platform():
    platforms = {
        'linux': 'Linux',
        'darwin': 'OS X',
        'win32': 'Windows'
    }
    if sys.platform not in platforms:
        return sys.platform, platform.machine()
    elif platforms[sys.platform] == 'Linux' and platform.machine() == 'armv7l':
        return 'Raspberry', platform.machine()
    elif platforms[sys.platform] == 'Windows':
        print('Desculpe sistema operacional não suportado...')
        sys.exit(0)

    return platforms[sys.platform], platform.machine()


def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


class ShareDesktop(object):

    def __init__(self, client='Test Share Desktop', vnc_port=5900, ssh_port=22):
        self.killed = False
        self.client = client
        self.vnc_port = vnc_port
        self.ssh_port = ssh_port
        self.user = getpass.getuser()

    def get_vnc_url(self):
        self.start_vnc()
        return ngrok.connect(self.vnc_port, "tcp")

    def get_ssh_url(self):
        return ngrok.connect(self.ssh_port, "tcp")

    @staticmethod
    def ngrok_tunnels():
        return ngrok.get_tunnels()

    @staticmethod
    def ngrok_process():
        return ngrok.get_ngrok_process()

    def ngrok_process_pid(self):
        return self.ngrok_process().proc.pid

    def start_vnc(self):
        thread_1 = Thread(target=self.run_x11vnc, args=[])
        thread_1.start()

    def check_vnc(self):
        thread_2 = Thread(target=self.is_port_in_use, args=[])
        thread_2.start()

    def kill_threads(self):
        self.killed = True

    @staticmethod
    def run_x11vnc():
        if get_platform()[0] == 'Raspberry':
            os.system('sudo x11vnc -display :0 -auth /home/pi/.Xauthority -forever > /dev/null 2>&1 &')
        elif get_platform()[0] == 'Linux':
            os.system('x11vnc > /dev/null 2>&1 &')

    def is_port_in_use(self):
        while True:
            if self.killed:
                ngrok.kill()
                os.system('killall x11vnc')
                break
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                if not s.connect_ex(('localhost', 5900)) == 0:
                    ngrok.kill()
                    os.system('killall x11vnc')
                    sys.exit(0)
            time.sleep(5)

    def send_email(self):
        port_ssh = self.get_ssh_url().public_url.split(':')[2]
        host_ssh = self.get_ssh_url().public_url.split(':')[1].replace('//', '')
        server_vnc = self.get_vnc_url().public_url.replace('tcp://', '')
        process_pid = self.ngrok_process_pid()
        print("Desktop sharing.")
        email = USER_EMAIL
        password = PASSWORD_EMAIL
        send_to_email = SEND_TO
        subject = f"CONEXÃO REMOTA AO CLIENTE {self.client}"
        message = f"\nPROCESSO NGROK: {process_pid}\n" \
                  f"COLE ESSE COMANDO EM UM TERMINAL: \n" \
                  f"ssh -p {port_ssh} {self.user}@{host_ssh}\n" \
                  f"CONTROLE DE ÁREA DE TRABALHO: \n" \
                  f"{server_vnc}\n"

        msg = MIMEMultipart()
        msg["From"] = email
        msg["To"] = send_to_email
        msg["Subject"] = subject

        msg.attach(MIMEText(message, 'plain'))

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(email, password)
        str_mail = msg.as_string()
        server.sendmail(email, send_to_email, str_mail)
        server.quit()
        self.check_vnc()
        return self.ngrok_process()
