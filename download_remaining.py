import json
import os
import urllib.request

# Read the JSON output
with open(r"C:\Users\Home\.gemini\antigravity-ide\brain\7e540840-9e29-41a2-9caa-c218168c2a1e\.system_generated\steps\318\output.txt", "r", encoding="utf-8") as f:
    data = json.load(f)

# File mappings based on screen IDs
file_map = {
    "projects/15755269347752467937/screens/eed794273885480aa4fc8fca20a54b23": "contact.html",
    "projects/15755269347752467937/screens/47d4af8e8f5d42aab9ba0c7bbac6ed42": "presence.html",
    "projects/15755269347752467937/screens/c8455a4d0ceb43babfd2029fd46fec70": "careers.html",
    "projects/15755269347752467937/screens/a12abac68d834969bfd7a9ebbb9394fa": "csr.html",
    "projects/15755269347752467937/screens/7aeb922fa75c43dc85dd731a18fd2362": "news.html",
    "projects/15755269347752467937/screens/388c205594564d63953d4c6d98b08a59": "tech.html",
    "projects/15755269347752467937/screens/d98405f531c74c90ae3cd77bc2ff5949": "audiovisual.html"
}

def download_file(url, dest_path):
    print(f"Downloading to {dest_path}")
    os.makedirs(os.path.dirname(os.path.abspath(dest_path)), exist_ok=True)
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req) as response, open(dest_path, 'wb') as out_file:
            out_file.write(response.read())
    except Exception as e:
        print(f"Error downloading {url}: {e}")

for screen in data.get("screens", []):
    screen_name = screen.get("name")
    
    if screen_name in file_map:
        dest = file_map[screen_name]
        
        # If it's an HTML file, download htmlCode
        if dest.endswith(".html") and "htmlCode" in screen and "downloadUrl" in screen["htmlCode"]:
            download_file(screen["htmlCode"]["downloadUrl"], dest)

print("Download complete.")
