import customtkinter as ctk
import os
import tkinter as tk
from threading import Thread
from tkinter import filedialog
from gamatool.decdode import *
from pystray import Icon, MenuItem, Menu
from PIL import Image, ImageDraw
import sys

# Karanlık tema stilini ayarlıyoruz
ctk.set_appearance_mode("dark")  # Karanlık mod
ctk.set_default_color_theme("dark-blue")  # Temanın rengi

# Ana pencereyi oluşturuyoruz
root = ctk.CTk()

# Pencere başlığını belirliyoruz
root.title("Gama Widgets")
root.geometry("1000x600")  # Pencere boyutunu genişlettik

# Data klasöründeki tüm alt klasörleri listeleyen fonksiyon
def get_all_folders(directory):
    folder_list = []
    for root_dir, dirs, _ in os.walk(directory):
        for dir_name in dirs:
            folder_list.append(os.path.relpath(os.path.join(root_dir, dir_name), directory))
    return sorted(folder_list)  # Klasörleri alfabetik sıraya göre sıralıyoruz

# Data klasöründeki tüm klasörleri alıyoruz
data_folder = "data"
folders = get_all_folders(data_folder)

# Sol tarafta bir frame oluşturuyoruz
listbox_frame = ctk.CTkFrame(root, width=200, height=350, corner_radius=10)
listbox_frame.pack(side="left", padx=20, pady=20, fill="y")

# Liste kutusunun başlığını ekliyoruz
listbox_header = ctk.CTkLabel(listbox_frame, text="Klasörler", font=("Arial", 16, "bold"))
listbox_header.pack(pady=10)

# Tkinter Listbox kullanarak, şık bir liste kutusu ekliyoruz
listbox = tk.Listbox(listbox_frame, height=15, width=30, bd=0, font=("Arial", 12), fg="white", bg="#2e2e2e", selectmode=tk.SINGLE)
listbox.pack(side="left", padx=10, pady=10)

# Data klasöründeki tüm klasörleri liste kutusuna ekliyoruz
if folders:
    for folder in folders:
        listbox.insert("end", folder)
else:
    listbox.insert("end", "Klasör bulunamadı.")

# Seçilen klasörü etiket olarak göstermek için bir fonksiyon
def show_selected_folder(event):
    selected_folder = listbox.get(listbox.curselection())  # Seçilen öğeyi alıyoruz
    label.configure(text=f"Seçilen Klasör: {selected_folder}")

# Klasör seçildiğinde etiketin güncellenmesini sağlıyoruz
listbox.bind("<<ListboxSelect>>", show_selected_folder)

# Sağ tarafta bir frame oluşturuyoruz (Klasör adı gösterimi için)
info_frame = ctk.CTkFrame(root, width=300, height=350, corner_radius=10)
info_frame.pack(side="right", padx=20, pady=20)

# Sağ tarafta bir etiket ekliyoruz
label = ctk.CTkLabel(info_frame, text="Klasör seçin...", font=("Arial", 18))
label.pack(pady=50)

# Run fonksiyonu
def run():
    selected_folder = listbox.get(listbox.curselection())  # Seçilen klasörü alıyoruz
    label.configure(text=f"Çalıştırılıyor: {selected_folder}")  # Etiketi güncelliyoruz
    th = Thread(target=os.system, args=(f"python\python\python.exe data\\{selected_folder}\\app.py",)).start()


# Buton ekliyoruz ve Run fonksiyonunu bağlıyoruz
run_button = ctk.CTkButton(info_frame, text="Run", command=run)
run_button.pack(pady=20)

# -----------------------------------------------
# Yükleme Sayfası (Yeni Frame)
# -----------------------------------------------

terminal_frame = ctk.CTkFrame(root, width=10, height=150, corner_radius=30)
terminal_frame.pack(side="right", padx=0, pady=0)

# Yükleme sayfası için yeni bir frame oluşturuyoruz
upload_frame = ctk.CTkFrame(root, width=300, height=350, corner_radius=30)
upload_frame.pack(side="right", padx=20, pady=20)

# Yükleme işlemi için başlık ekliyoruz
upload_header = ctk.CTkLabel(upload_frame, text="Yükleme İşlemi", font=("Arial", 16, "bold"))
upload_header.pack(pady=10)

# Dosya seçme ve yükleme işlemi için bir fonksiyon
def upload_file():
    # Dosya seçme penceresini açıyoruz
    file_path = filedialog.askopenfilename(title="Dosya Seçin", filetypes=(("All Files", "*.*"),))
    
    if file_path:
        # Burada dosya yolu ile işlem yapabilirsiniz, örneğin:
        file_label.configure(text=f"Seçilen Dosya: {file_path}")
        # install fonksiyonunu burada çağırabilirsiniz
        install(file_path)

        # Yükleme işlemi tamamlandıktan sonra listeyi yenile
        update_listbox()

# Yükleme işlemi için install fonksiyonu (içeriğini kendi ihtiyaçlarınıza göre doldurun)
def install(file_path):
    # Yükleme işlemini burada yapabilirsiniz
    print(f"Yükleniyor: {file_path}")
    decode(filename=file_path)  # Örneğin decode fonksiyonu kullanıyoruz

# Listeyi güncelleyen fonksiyon
def update_listbox():
    # Data klasöründeki tüm klasörleri tekrar alıyoruz
    folders = get_all_folders(data_folder)

    # Mevcut listbox'u temizliyoruz
    listbox.delete(0, tk.END)

    # Yeni klasörleri listbox'a ekliyoruz
    if folders:
        for folder in folders:
            listbox.insert("end", folder)
    else:
        listbox.insert("end", "Klasör bulunamadı.")

# Yükle butonunu ekliyoruz
upload_button = ctk.CTkButton(upload_frame, text="Yükle", command=upload_file)
upload_button.pack(pady=20)

def terminal():
    os.startfile("rungamaterminal.bat")

terminal_bt = ctk.CTkButton(terminal_frame, text="Terminal", command=terminal)
terminal_bt.pack(pady=20)
# Dosya yolunun görüntüleneceği bir etiket ekliyoruz
file_label = ctk.CTkLabel(upload_frame, text="Dosya Seçin...", font=("Arial", 14))
file_label.pack(pady=10)

# Sistem tepsisine simge ekleme fonksiyonu
def create_image():
    image = Image.new("RGBA", (64, 64), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    draw.rectangle([0, 0, 64, 64], fill="blue")
    return image

# Uygulamanın tray ikonunu oluşturuyoruz
def on_quit(icon, item):
    icon.stop()  # Stop the tray icon
    root.quit()  # Close the Tkinter window
    root.destroy()  # Make sure the application terminates properly

    

def minimize_to_tray():
    root.withdraw()  # Ana pencereyi gizliyoruz
    image = create_image()
    icon = Icon("Gama Widgets", image, menu=Menu(MenuItem("Büyüt", restore_window), MenuItem("Quit", on_quit)))
    icon.run()

# Tray simgesine tıklanınca uygulamayı geri getirme
def restore_window(icon, item):
    root.deiconify()  # Ana pencereyi gösteriyoruz
    icon.stop()  # Tray simgesini durduruyoruz

# Başlangıçta tray simgesini ekliyoruz
root.protocol("WM_DELETE_WINDOW", minimize_to_tray)  # Pencereyi kapatırken tray'e küçült

# Ana döngüyü başlatıyoruz
root.mainloop()