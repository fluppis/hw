from proxmoxer import ProxmoxAPI
import tkinter as tk
from cryptography.fernet import Fernet
def decrypt_password(key, encrypted_password):
    cipher_suite = Fernet(key)
    decrypted_password = cipher_suite.decrypt(encrypted_password)
    return decrypted_password.decode()


with open('pass1.txt', 'r') as file:
    lines = file.readlines()
    nodes = lines[0].split(':')[1].strip()

with open('pass2.txt', 'r') as file:
    lines = file.readlines()
    nodes2 = lines[0].split(':')[1].strip()
with open('pass3.txt', 'r') as file:
    lines = file.readlines()
    nodes3 = lines[0].split(':')[1].strip()
def unlock_vm():
    node = node_entry.get()
    node_ip = node_ip_entry.get()
    vmid = vmid_entry.get()
    if node == nodes:
        with open('pass1.txt', 'r') as file:
            lines = file.readlines()
        encryption_key = lines[1].split(':')[1].strip()
        encrypted_password = lines[2].split(':')[1].strip()
        decrypted_password = decrypt_password(encryption_key, encrypted_password)
        proxmox = ProxmoxAPI(
            f"{node_ip}", user="root@pam", password=f"{decrypted_password}", verify_ssl=False
        )
    elif node == nodes2:
        with open('pass2.txt', 'r') as file:
            lines = file.readlines()
        encryption_key = lines[1].split(':')[1].strip()
        encrypted_password = lines[2].split(':')[1].strip()
        decrypted_password = decrypt_password(encryption_key, encrypted_password)
        proxmox = ProxmoxAPI(
            f"{node_ip}", user="root@pam", password=f"{decrypted_password}", verify_ssl=False
        )
    elif node == nodes3:
        with open('pass3.txt', 'r') as file:
            lines = file.readlines()
        encryption_key = lines[1].split(':')[1].strip()
        encrypted_password = lines[2].split(':')[1].strip()
        decrypted_password = decrypt_password(encryption_key, encrypted_password)
        proxmox = ProxmoxAPI(
            f"{node_ip}", user="root@pam", password=f"{decrypted_password}", verify_ssl=False
        )
    proxmox.nodes(node).qemu(vmid).config.post(delete='lock', skiplock='1')


root = tk.Tk()
root.title("Разблокировка виртуальной машины")

node_label = tk.Label(root, text="Имя узла (Node):")
node_label.pack()

node_entry = tk.Entry(root)
node_entry.pack()

node_ip_label = tk.Label(root, text="node ip ")
node_ip_label.pack()

node_ip_entry = tk.Entry(root)
node_ip_entry.pack()

vmid_label = tk.Label(root, text="ID виртуальной машины (VM ID):")
vmid_label.pack()

vmid_entry = tk.Entry(root)
vmid_entry.pack()

unlock_button = tk.Button(root, text="Разблокировать VM", command=unlock_vm)
unlock_button.pack()

def show_message():
    node = node_entry.get()
    node_ip = node_ip_entry.get()
    vmid = vmid_entry.get()
    if node == nodes:
        with open('pass1.txt', 'r') as file:
            lines = file.readlines()
        encryption_key = lines[1].split(':')[1].strip()
        encrypted_password = lines[2].split(':')[1].strip()
        decrypted_password = decrypt_password(encryption_key, encrypted_password)
        proxmox = ProxmoxAPI(
            f"{node_ip}", user="root@pam", password=f"{decrypted_password}", verify_ssl=False
        )
    elif node == nodes2:
        with open('pass2.txt', 'r') as file:
            lines = file.readlines()
        encryption_key = lines[1].split(':')[1].strip()
        encrypted_password = lines[2].split(':')[1].strip()
        decrypted_password = decrypt_password(encryption_key, encrypted_password)
        proxmox = ProxmoxAPI(
            f"{node_ip}", user="root@pam", password=f"{decrypted_password}", verify_ssl=False
        )
    elif node == nodes3:
        with open('pass3.txt', 'r') as file:
            lines = file.readlines()
        encryption_key = lines[1].split(':')[1].strip()
        encrypted_password = lines[2].split(':')[1].strip()
        decrypted_password = decrypt_password(encryption_key, encrypted_password)
        proxmox = ProxmoxAPI(
            f"{node_ip}", user="root@pam", password=f"{decrypted_password}", verify_ssl=False
        )
    vm_config = proxmox.nodes(node).qemu(vmid).config.get()
    lock_status = vm_config.get("lock")
    message = f"Статус: {lock_status}"
    label.config(text=message)

label = tk.Label(root, text="")
label.pack()

button = tk.Button(root, text="Показать статус", command=show_message)
button.pack()

def generate_key():
    return Fernet.generate_key()

# Функция для шифрования пароля
def encrypt_password():
    if file_entry.get() and pass_entry.get():
        original_password = pass_entry.get()
        encryption_key = generate_key()
        cipher_suite = Fernet(encryption_key)
        encrypted_password = cipher_suite.encrypt(original_password.encode())
        nodes_name=nodes_entry.get()
        key_string = encryption_key.decode()
        password_string = encrypted_password.decode()

        with open(file_entry.get(), 'w') as file:
            file.write(f"nodes : {nodes_name}\n")
            file.write(f"Key : {key_string}\n")
            file.write(f"Pass : {password_string}")
nodes_label = tk.Label(root, text="Название ноды:")
nodes_label.pack()

nodes_entry = tk.Entry(root)
nodes_entry.pack()
file_label = tk.Label(root, text="Название файла pass1-3.txt:")
file_label.pack()

file_entry = tk.Entry(root)
file_entry.pack()

pass_label = tk.Label(root, text="Пароль:")
pass_label.pack()

pass_entry = tk.Entry(root, show="*")
pass_entry.pack()

encrypt_button = tk.Button(root, text="Шифровать пароль и записать ноду ", command=encrypt_password)
encrypt_button.pack()

label = tk.Label(root, text="")
label.pack()


root.mainloop()

