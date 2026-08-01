import os
from bs4 import BeautifulSoup

def update_seo(file_path, title, description):
    if not os.path.exists(file_path):
        return
    with open(file_path, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')
    
    # Update title
    if soup.title:
        soup.title.string = title
    else:
        title_tag = soup.new_tag('title')
        title_tag.string = title
        soup.head.append(title_tag)
        
    # Update or add meta description
    meta_desc = soup.find('meta', attrs={'name': 'description'})
    if meta_desc:
        meta_desc['content'] = description
    else:
        meta_tag = soup.new_tag('meta', attrs={'name': 'description', 'content': description})
        soup.head.append(meta_tag)
        
    # Inject sections into index.html if it's the index file
    if file_path == 'index.html':
        with open('sections.html', 'r', encoding='utf-8') as sf:
            sections_html = sf.read()
            
        sections_soup = BeautifulSoup(sections_html, 'html.parser')
        
        # Find where to insert (before the footer)
        footer = soup.find('footer')
        if footer:
            for element in sections_soup.contents:
                footer.insert_before(element)
    
    # Save back
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(str(soup))
    print(f"Updated {file_path}")

# Data for pages
pages = [
    {
        'file': 'index.html',
        'title': 'Duara Group | Building Africa Through Technology & Innovation',
        'desc': 'Duara Group is a premier East African holding company driving sustainable growth and technological advancement across the continent. Discover our companies.'
    },
    {
        'file': 'about.html',
        'title': 'About Us | Duara Group',
        'desc': 'Learn about Duara Group\'s vision, mission, and core values. We are an East African company investing in technology, business development, and education.'
    },
    {
        'file': 'companies.html',
        'title': 'Our Companies | Duara Group',
        'desc': 'Explore Duara Group subsidiaries: Duara Tech, Duara Agency, and Duara Audiovisual, offering technology, marketing, and media solutions across East Africa.'
    },
    {
        'file': 'presence.html',
        'title': 'East Africa Presence | Duara Group',
        'desc': 'Headquartered in Nairobi, Kenya, Duara Group serves businesses across East Africa including Uganda, Tanzania, Rwanda, Burundi, and more.'
    },
    {
        'file': 'csr.html',
        'title': 'Corporate Social Responsibility | Duara Group',
        'desc': 'Our CSR initiative focuses on Technology for Education, providing free digital learning resources and AI education to communities across Africa.'
    },
    {
        'file': 'news.html',
        'title': 'Media & News | Duara Group',
        'desc': 'Stay updated with the latest news, press releases, events, and company updates from Duara Group and its subsidiaries.'
    },
    {
        'file': 'careers.html',
        'title': 'Careers | Duara Group',
        'desc': 'Join Duara Group and help us build Africa through technology and innovation. Explore careers, internships, and employee benefits.'
    },
    {
        'file': 'contact.html',
        'title': 'Contact Us | Duara Group',
        'desc': 'Get in touch with Duara Group for corporate, partnership, media, and career enquiries at our headquarters in Nairobi, Kenya.'
    }
]

for p in pages:
    update_seo(p['file'], p['title'], p['desc'])
