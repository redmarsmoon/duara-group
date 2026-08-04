import glob
from bs4 import BeautifulSoup

nav_template = """
<nav class="bg-surface dark:bg-inverse-surface fixed top-0 w-full z-50 border-b border-outline-variant dark:border-outline">
    <div class="flex justify-between items-center h-20 px-margin-mobile md:px-margin-desktop max-w-container-max mx-auto">
        <a class="flex items-center" href="index.html">
            <img alt="Duara Group Logo" class="h-12 md:h-16 w-auto object-contain" src="assets/logo.png"/>
        </a>
        <div class="hidden md:flex items-center gap-6">
            <a class="nav-link font-label-md text-label-md font-medium text-on-surface-variant dark:text-on-tertiary-container hover:text-primary dark:hover:text-primary-fixed transition-colors" href="index.html">Home</a>
            <a class="nav-link font-label-md text-label-md font-medium text-on-surface-variant dark:text-on-tertiary-container hover:text-primary dark:hover:text-primary-fixed transition-colors" href="about.html">About</a>
            <a class="nav-link font-label-md text-label-md font-medium text-on-surface-variant dark:text-on-tertiary-container hover:text-primary dark:hover:text-primary-fixed transition-colors" href="companies.html">Our Divisions</a>
            <a class="nav-link font-label-md text-label-md font-medium text-on-surface-variant dark:text-on-tertiary-container hover:text-primary dark:hover:text-primary-fixed transition-colors" href="agency.html">East Africa</a>
            <a class="nav-link font-label-md text-label-md font-medium text-on-surface-variant dark:text-on-tertiary-container hover:text-primary dark:hover:text-primary-fixed transition-colors" href="dev.html">Technology</a>
            <a class="nav-link font-label-md text-label-md font-medium text-on-surface-variant dark:text-on-tertiary-container hover:text-primary dark:hover:text-primary-fixed transition-colors" href="audiovisual.html">Media</a>
            <a class="nav-link font-label-md text-label-md font-medium text-on-surface-variant dark:text-on-tertiary-container hover:text-primary dark:hover:text-primary-fixed transition-colors" href="csr.html">CSR</a>
            <a class="nav-link font-label-md text-label-md font-medium text-on-surface-variant dark:text-on-tertiary-container hover:text-primary dark:hover:text-primary-fixed transition-colors" href="news.html">News</a>
        </div>
        <a class="hidden md:flex bg-primary text-on-primary font-label-md text-label-md px-6 py-2 rounded hover:opacity-90 active:scale-[0.98] transition-all duration-200" href="contact.html">
            Partner With Us
        </a>
        <button class="md:hidden text-primary">
            <span class="material-symbols-outlined">menu</span>
        </button>
    </div>
</nav>
"""

html_files = glob.glob('*.html')

for f in html_files:
    if f == 'sections.html':
        continue
        
    with open(f, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')
        
    old_nav = soup.find('nav')
    if old_nav:
        new_nav_soup = BeautifulSoup(nav_template, 'html.parser')
        new_nav = new_nav_soup.nav
        
        # Set active class for current page
        active_classes = 'text-primary dark:text-primary-fixed font-bold border-b-2 border-primary dark:border-primary-fixed pb-1'.split()
        inactive_classes = 'font-medium text-on-surface-variant dark:text-on-tertiary-container hover:text-primary dark:hover:text-primary-fixed'.split()
        
        current_href = f
        if f == 'index-scroll.html':
            current_href = 'index.html'
            
        for link in new_nav.find_all('a', class_='nav-link'):
            classes = link.get('class', [])
            if link.get('href') == current_href:
                for c in inactive_classes:
                    if c in classes:
                        classes.remove(c)
                classes.extend(active_classes)
                link['aria-current'] = 'page'
            
            link['class'] = classes
            
        old_nav.replace_with(new_nav)
        
        # Write back
        html_content = str(soup)
        with open(f, 'w', encoding='utf-8') as file:
            file.write(html_content)
        print(f'Updated {f}')
