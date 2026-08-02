import json
import os
import urllib.request

# Read the JSON output
with open(r"C:\Users\Home\.gemini\antigravity-ide\brain\7e540840-9e29-41a2-9caa-c218168c2a1e\.system_generated\steps\252\output.txt", "r", encoding="utf-8") as f:
    data = json.load(f)

# File mappings based on screen IDs
file_map = {
    "projects/15755269347752467937/screens/8a67c5d16b8044429ac057939fe8baa9": "index.html",
    "projects/15755269347752467937/screens/276bd39f50f74c97bb14c473cce86428": "about.html",
    "projects/15755269347752467937/screens/11f03adffa5043f1bf0ce2b781978ddb": "agency.html",
    "projects/15755269347752467937/screens/fab89671f101450697761c6bcf87fd30": "companies.html",
    "projects/15755269347752467937/screens/89ac1ebe004f48b784034d8c5fc4b60d": "holding.html",
    "projects/15755269347752467937/screens/12758011898057244444": "assets/images/1.png",
    "projects/15755269347752467937/screens/12758011898057242090": "assets/images/2.png",
    "projects/15755269347752467937/screens/12758011898057243832": "assets/images/3.png"
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
            
        # If it's an image, download screenshot
        elif dest.endswith(".png") and "screenshot" in screen and "downloadUrl" in screen["screenshot"]:
            download_file(screen["screenshot"]["downloadUrl"], dest)

print("Download complete.")
