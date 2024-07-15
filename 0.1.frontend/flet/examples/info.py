import flet as ft
import platform
import socket
from kivy.core.window import Window

def get_android_version():
    return platform.system(), platform.release()

def get_ip_address():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address

def get_screen_size():
    return Window.size

def main(page: ft.Page):
    page.title = "Device Information"
    
    android_version = get_android_version()
    ip_address = get_ip_address()
    screen_size = get_screen_size()
    
    page.add(ft.Text(f"Android Version: {android_version}"))
    page.add(ft.Text(f"IP Address: {ip_address}"))
    page.add(ft.Text(f"Screen Size: {screen_size}"))

ft.app(target=main)
