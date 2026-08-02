import glob
import os
from bs4 import BeautifulSoup

def update_nav():
    html_files = glob.glob('*.html')
    
    # 1. Remove presence.html
    if 'presence.html' in html_files:
        os.remove('presence.html')
        html_files.remove('presence.html')
        print("Removed presence.html")

    for file_path in html_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                soup = BeautifulSoup(f, 'html.parser')
            
            navs = soup.find_all('nav')
            if not navs:
                continue
            
            # Find the main nav links container
            # Usually it's a div containing the 'Home' and 'About' links
            for nav in navs:
                about_link = None
                east_africa_link = None
                
                # find all a tags in nav
                a_tags = nav.find_all('a')
                for a in a_tags:
                    text = a.get_text(strip=True)
                    if text == 'About':
                        about_link = a
                    elif text == 'East Africa':
                        east_africa_link = a
                        
                if east_africa_link and about_link:
                    # Update East Africa link
                    east_africa_link['href'] = 'agency.html'
                    
                    # Check if Technology already exists to avoid duplicates
                    has_tech = any(a.get_text(strip=True) == 'Technology' for a in a_tags)
                    if not has_tech:
                        # Create Technology link
                        tech_link = soup.new_tag('a', href='tech.html')
                        tech_link.string = 'Technology'
                        # Copy classes from about_link (which is usually inactive)
                        if 'class' in about_link.attrs:
                            tech_link['class'] = about_link['class']
                        east_africa_link.insert_after(tech_link)
                        
                        # Create Media link
                        media_link = soup.new_tag('a', href='audiovisual.html')
                        media_link.string = 'Media'
                        if 'class' in about_link.attrs:
                            media_link['class'] = about_link['class']
                        tech_link.insert_after(media_link)
                        
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(str(soup))
            print(f"Updated nav in {file_path}")
            
        except Exception as e:
            print(f"Error processing {file_path}: {e}")

if __name__ == '__main__':
    update_nav()
