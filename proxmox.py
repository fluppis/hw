from proxmoxer import ProxmoxAPI
import tkinter as tk

def unlock_vm():
    node = node_entry.get()
    node_ip = node_ip_entry.get()
    vmid = vmid_entry.get()
    proxmox = ProxmoxAPI(
        f"{node_ip}", user="root@pam", password="YOUR_PASSWORD", verify_ssl=False
    )
    proxmox.nodes(node).qemu(vmid).config.post(delete='lock',skiplock='1')

root = tk.Tk()
root.title("Разблокировка виртуальной машины")

node_label = tk.Label(root, text="Имя узла (Node):"
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
    proxmox = ProxmoxAPI(
        f"{node_ip}", user="root@pam", password="YOUR_PASSWORK", verify_ssl=False
    )
    vm_config = proxmox.nodes(node).qemu(vmid).config.get()
    lock_status = vm_config.get("lock")
    message = f"Статус: {lock_status}"
    label.config(text=message)

label = tk.Label(root, text="")
label.pack()

button = tk.Button(root, text="Показать статус", command=show_message)
button.pack()

root.mainloop()

