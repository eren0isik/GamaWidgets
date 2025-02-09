import base64
import json
import os

def code(input_data):
    # Veriyi base64 olarak encode et
    encoded_data = base64.b64encode(input_data.encode('utf-8')).decode('utf-8')
    return encoded_data

def getdata(file="build.gws"):
    with open(file=file) as f:
        data = json.load(f)
        return data  # Veriyi döndür


def decode(filename="build.gws"):
    a = getdata(file=filename)
    for i in a['iddata']:
        name = a['iddata'][i]
        break

    # 'files' içindeki her bir öğeyi döngü ile işleyelim
    for file_path, encoded_content in a['files'].items():
        if file_path:
            file_path = f"data\\{name}\\"+file_path
            # Dosya yolunun dizin kısmını al
            dir_path = os.path.dirname(file_path)

            # Eğer dizin mevcut değilse, oluştur
            if dir_path and not os.path.exists(dir_path):
                os.makedirs(dir_path)

            # Base64 ile encoded içeriği çöz
            decoded_content = base64.b64decode(encoded_content).decode('utf-8')

            # Dosyayı oluştur ve içerik yaz
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(decoded_content)  # Dosyaya tam içeriği yaz

            print(f"File path: {file_path} oluşturuldu.")
            print("-" * 30)  # Ayırıcı çizgi
        else:
            print("Geçersiz dosya yolu tespit edildi!")
