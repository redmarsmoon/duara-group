import json
import os
import urllib.request

# Read the JSON output
with open(r"C:\Users\Home\.gemini\antigravity-ide\brain\7e540840-9e29-41a2-9caa-c218168c2a1e\.system_generated\steps\24\output.txt", "r", encoding="utf-8") as f:
    data = json.load(f)

# The screens we want to download
# 1. Contact Us - Duara Group (Scroll Reveal) ID: efc131ee956d4208a00b1801a2952d53
# 2. Careers - Duara Group (Scroll Reveal) ID: f1eb2ef1fa654ea49be9f4c468e74971
# 3. CSR - Duara Group (Scroll Reveal) ID: 76a78a53f2004e35b5f0995d9f177b19
# 4. News - Duara Group (Scroll Reveal) ID: 52a9979d5d424402bba823cda25c0616
# 5. East Africa Presence - Duara Group (Scroll Reveal) ID: 16fc97a57b1648d1af440200d74a30e4
# 6. Our Companies - Duara Group (Scroll Reveal) ID: 148537bbe3ac4fe896150448d2a819a2
# 7. About - Duara Group (Scroll Reveal) ID: 851cca4eb7bc4b30ad169a99e0e88a9c
# 8. Home - Duara Group (Full Scroll Reveal) ID: e761b7b348434d968a305b9f96fb3d53
# 9. Home - Duara Group (Animated Hero) ID: eb868409e9974c409146475bbe7964ea

screen_mapping = {
    "efc131ee956d4208a00b1801a2952d53": "contact",
    "f1eb2ef1fa654ea49be9f4c468e74971": "careers",
    "76a78a53f2004e35b5f0995d9f177b19": "csr",
    "52a9979d5d424402bba823cda25c0616": "news",
    "16fc97a57b1648d1af440200d74a30e4": "presence",
    "148537bbe3ac4fe896150448d2a819a2": "companies",
    "851cca4eb7bc4b30ad169a99e0e88a9c": "about",
    "e761b7b348434d968a305b9f96fb3d53": "index-scroll",
    "eb868409e9974c409146475bbe7964ea": "index",
}

os.makedirs("assets/images", exist_ok=True)

for screen in data.get("screens", []):
    screen_name = screen.get("name", "")
    screen_id = screen_name.split("/")[-1]
    if screen_id in screen_mapping:
        filename = screen_mapping[screen_id]
        print(f"Processing {filename}...")
        
        # HTML
        html_obj = screen.get("htmlCode", {})
        html_url = html_obj.get("downloadUrl")
        if html_url:
            print(f"Downloading HTML for {filename}...")
            urllib.request.urlretrieve(html_url, f"{filename}.html")
            
        # Screenshot
        screenshot_obj = screen.get("screenshot", {})
        screenshot_url = screenshot_obj.get("downloadUrl")
        if screenshot_url:
            print(f"Downloading Screenshot for {filename}...")
            urllib.request.urlretrieve(screenshot_url, f"assets/images/{filename}.png")

print("Done downloading assets!")
