import requests
import base64
import json

def decode(base64_encoded):
    try:
        padding = len(base64_encoded) % 4
        if padding != 0:
            base64_encoded += "=" * (4 - padding)

        decoded_bytes = base64.b64decode(base64_encoded)
        decoded_str = decoded_bytes.decode('utf-8')
        return decoded_str
    except Exception as e:
        print(f"Erro ao decodificar Base64: {e}")
        return None

def getApps():

    url = "https://ws75.aptoide.com/api/7/apps/get/store_name=apps/q=bWF4U2RrPTE5Jm1heFNjcmVlbj1ub3JtYWwmbWF4R2xlcz0yLjA/group_name=games/limit=10/offset=0/mature=false"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        q = "bWF4U2RrPTE5Jm1heFNjcmVlbj1ub3JtYWwmbWF4R2xlcz0yLjA"

        decoded_q = decode(q)

        print("Decoded 'q' parameter:", decoded_q)

        list_apps = data.get('datalist', {}).get('list', [])

        if list_apps:
            print("\nList of Apps")
            for app in list_apps:
                app_name = app.get('name', 'Unknown')
                print(f"App name: {app_name}")
        else:
            print("No apps found")
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")

def getDescription():

    url = "https://ws75.aptoide.com/api/7/app/get/store_name=apps/q=bWF4U2RrPTE5Jm1heFNjcmVlbj1ub3JtYWwmbWF4R2xlcz0yLjA/package_name=com.fun.lastwar.gp/language=pt_PT/"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        app_description = data.get('nodes', {}).get('meta', {}).get('data', {}).get('media', {}).get('description', 'No description available')

        print(f"\nApp Description: {app_description}")

    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")

def download_apk():
    url = "https://aptoide-mmp.aptoide.com/api/v1/download/b2VtaWQ9VGVjaENoYWxsZW5nZVB5dGhvbiZwYWNrYWdlX25hbWU9Y29tLmZ1bi5sYXN0d2FyLmdwJnJlZGlyZWN0X3VybD1odHRwczovL3Bvb2wuYXBrLmFwdG9pZGUuY29tL2FwcHMvY29tLWZ1bi1sYXN0d2FyLWdwLTk5OTk5LTY2NjEyOTMwLWE3MThmOWZlMjE5OGM1Y2EyYzIwMmUwNDYzZTVkZDk1LmFwaw==?resolution=1080x1776&aptoide_uid=testchallenge"
    
    save_path = 'download.apk'

    response = requests.get(url, stream=True)
    
    # Verificando se a resposta foi bem-sucedida (status code 200)
    if response.status_code == 200:
        # Abrindo o arquivo no modo binário para salvar o APK
        with open(save_path, 'wb') as apk_file:
            for chunk in response.iter_content(chunk_size=8192):
                # Escrevendo os dados no arquivo
                apk_file.write(chunk)
        print(f"\nAPK baixado com sucesso! Arquivo salvo em: {save_path}")
    else:
        print(f"\nFalha no download. Status code: {response.status_code}")



getApps()
getDescription()
download_apk()