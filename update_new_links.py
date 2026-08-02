import glob
from bs4 import BeautifulSoup

LINK_MAP = {
    'Home': 'index.html',
    'About': 'about.html',
    'Our Divisions': 'companies.html',
    'East Africa': 'presence.html',
    'CSR': 'csr.html',
    'News': 'news.html',
}

def update_links():
    html_files = ['index.html', 'about.html', 'agency.html', 'companies.html', 'holding.html']
    for file_path in html_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                soup = BeautifulSoup(f, 'html.parser')
            
            nav_links = soup.find_all('a')
            for a in nav_links:
                text = a.get_text(strip=True)
                if text in LINK_MAP:
                    a['href'] = LINK_MAP[text]
                
            buttons = soup.find_all('button')
            for btn in buttons:
                text = btn.get_text(strip=True)
                if 'Partner With Us' in text:
                    btn.name = 'a'
                    btn['href'] = 'contact.html'
                    
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(str(soup))
            print(f"Updated {file_path}")
        except FileNotFoundError:
            print(f"Skipping {file_path}, not found.")

if __name__ == '__main__':
    update_links()
