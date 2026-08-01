import os
import glob
from bs4 import BeautifulSoup

# The mapping from menu text to URLs
LINK_MAP = {
    'Home': 'index.html',
    'About': 'about.html',
    'Companies': 'companies.html',
    'East Africa': 'presence.html',
    'CSR': 'csr.html',
    'News': 'news.html',
    'Careers': 'careers.html',
    'Contact': 'contact.html',
}

ABOUT_EXTRA = """
<!-- Our Story -->
<section class="py-section-padding px-margin-mobile md:px-margin-desktop max-w-container-max mx-auto reveal">
    <h2 class="font-headline-lg text-headline-md md:text-headline-lg text-primary mb-stack-md">Our Story</h2>
    <p class="font-body-lg text-body-lg text-on-surface-variant max-w-3xl">
        Founded in Nairobi, Duara Group began with a simple but profound belief: that East Africa's potential is boundless when supported by the right technology and strategic investment. Over the years, we have grown from a local enterprise into a regional powerhouse, bridging the gap between local insights and global standards.
    </p>
</section>

<!-- Core Values -->
<section class="py-section-padding px-margin-mobile md:px-margin-desktop bg-surface-container-low reveal">
    <div class="max-w-container-max mx-auto text-center">
        <h2 class="font-headline-lg text-headline-md md:text-headline-lg text-primary mb-stack-lg">Core Values</h2>
        <div class="grid grid-cols-2 md:grid-cols-5 gap-4">
            <div class="p-6 bg-surface rounded-xl shadow-sm border border-outline-variant/30">
                <h3 class="font-label-bold text-lg text-secondary mb-2">Innovation</h3>
            </div>
            <div class="p-6 bg-surface rounded-xl shadow-sm border border-outline-variant/30">
                <h3 class="font-label-bold text-lg text-secondary mb-2">Integrity</h3>
            </div>
            <div class="p-6 bg-surface rounded-xl shadow-sm border border-outline-variant/30">
                <h3 class="font-label-bold text-lg text-secondary mb-2">Excellence</h3>
            </div>
            <div class="p-6 bg-surface rounded-xl shadow-sm border border-outline-variant/30">
                <h3 class="font-label-bold text-lg text-secondary mb-2">Collaboration</h3>
            </div>
            <div class="p-6 bg-surface rounded-xl shadow-sm border border-outline-variant/30">
                <h3 class="font-label-bold text-lg text-secondary mb-2">Sustainability</h3>
            </div>
        </div>
    </div>
</section>

<!-- Leadership -->
<section class="py-section-padding px-margin-mobile md:px-margin-desktop max-w-container-max mx-auto reveal">
    <div class="text-center mb-stack-lg">
        <h2 class="font-headline-lg text-headline-md md:text-headline-lg text-primary">Leadership</h2>
        <p class="font-body-md text-on-surface-variant max-w-2xl mx-auto mt-4">Guided by seasoned executives with deep roots in East Africa and a global perspective.</p>
    </div>
    <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
        <div class="text-center">
            <div class="w-32 h-32 bg-surface-variant rounded-full mx-auto mb-4 border border-outline-variant"></div>
            <h3 class="font-headline-md text-lg text-primary">Executive Director</h3>
        </div>
        <div class="text-center">
            <div class="w-32 h-32 bg-surface-variant rounded-full mx-auto mb-4 border border-outline-variant"></div>
            <h3 class="font-headline-md text-lg text-primary">Head of Technology</h3>
        </div>
        <div class="text-center">
            <div class="w-32 h-32 bg-surface-variant rounded-full mx-auto mb-4 border border-outline-variant"></div>
            <h3 class="font-headline-md text-lg text-primary">Head of Operations</h3>
        </div>
    </div>
</section>

<!-- Company Timeline -->
<section class="py-section-padding px-margin-mobile md:px-margin-desktop bg-surface-container-lowest border-t border-outline-variant/20 reveal">
    <div class="max-w-container-max mx-auto">
        <h2 class="font-headline-lg text-headline-md md:text-headline-lg text-primary mb-stack-lg text-center">Company Timeline</h2>
        <div class="space-y-8 max-w-3xl mx-auto">
            <div class="flex gap-4">
                <div class="font-label-bold text-secondary w-24 flex-shrink-0">2015</div>
                <div class="font-body-md text-on-surface-variant">Founding of Duara Group in Nairobi, Kenya.</div>
            </div>
            <div class="flex gap-4">
                <div class="font-label-bold text-secondary w-24 flex-shrink-0">2018</div>
                <div class="font-body-md text-on-surface-variant">Launch of Duara Tech to drive digital innovation across our portfolio.</div>
            </div>
            <div class="flex gap-4">
                <div class="font-label-bold text-secondary w-24 flex-shrink-0">2020</div>
                <div class="font-body-md text-on-surface-variant">Expansion into Uganda and Tanzania with strategic logistics hubs.</div>
            </div>
            <div class="flex gap-4">
                <div class="font-label-bold text-secondary w-24 flex-shrink-0">2023</div>
                <div class="font-body-md text-on-surface-variant">Initiated the Technology for Education CSR program across East Africa.</div>
            </div>
            <div class="flex gap-4">
                <div class="font-label-bold text-secondary w-24 flex-shrink-0">2025</div>
                <div class="font-body-md text-on-surface-variant">Reached $1.2B in managed asset base with 24 active subsidiaries.</div>
            </div>
        </div>
    </div>
</section>
"""

PRESENCE_EXTRA = """
<!-- Expanded Regional Reach -->
<section class="py-section-padding px-margin-mobile md:px-margin-desktop bg-surface reveal">
    <div class="max-w-container-max mx-auto text-center">
        <h2 class="font-headline-lg text-headline-md md:text-headline-lg text-primary mb-stack-lg">Our Expanded Reach</h2>
        <p class="font-body-lg text-body-lg text-on-surface-variant max-w-3xl mx-auto mb-stack-lg">
            We are actively driving enterprise, infrastructure, and technology across the entire East African and Horn of Africa region, including:
        </p>
        <div class="flex flex-wrap justify-center gap-4">
            <span class="bg-primary text-on-primary px-6 py-3 rounded-full font-label-bold shadow-sm">Kenya</span>
            <span class="bg-primary text-on-primary px-6 py-3 rounded-full font-label-bold shadow-sm">Uganda</span>
            <span class="bg-primary text-on-primary px-6 py-3 rounded-full font-label-bold shadow-sm">Tanzania</span>
            <span class="bg-primary text-on-primary px-6 py-3 rounded-full font-label-bold shadow-sm">Rwanda</span>
            <span class="bg-primary text-on-primary px-6 py-3 rounded-full font-label-bold shadow-sm">Burundi</span>
            <span class="bg-primary text-on-primary px-6 py-3 rounded-full font-label-bold shadow-sm">South Sudan</span>
            <span class="bg-primary text-on-primary px-6 py-3 rounded-full font-label-bold shadow-sm">Ethiopia</span>
            <span class="bg-primary text-on-primary px-6 py-3 rounded-full font-label-bold shadow-sm">Somalia</span>
            <span class="bg-primary text-on-primary px-6 py-3 rounded-full font-label-bold shadow-sm">Djibouti</span>
        </div>
    </div>
</section>
"""


def process_html_files():
    html_files = glob.glob('*.html')
    for file_path in html_files:
        with open(file_path, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f, 'html.parser')
        
        # Update Nav Links
        nav_links = soup.find_all('a')
        for a in nav_links:
            text = a.get_text(strip=True)
            if text in LINK_MAP:
                a['href'] = LINK_MAP[text]
            
            # also update buttons mimicking links
            if 'Partner With Us' in text:
                a['href'] = 'contact.html'
                
        # Fix buttons that are <button> instead of <a>
        buttons = soup.find_all('button')
        for btn in buttons:
            text = btn.get_text(strip=True)
            if 'Partner With Us' in text:
                btn.name = 'a'
                btn['href'] = 'contact.html'
            elif 'Explore Our Companies' in text:
                btn.name = 'a'
                btn['href'] = 'companies.html'

        # Special processing for specific files
        if file_path == 'index.html':
            # Remove background image in hero section and replace with solid color
            hero_div = soup.find('div', attrs={'data-alt': lambda x: x and 'African metropolis' in x})
            if hero_div:
                if hero_div.has_attr('style'):
                    del hero_div['style']
                hero_div['class'] = ['absolute', 'inset-0', 'z-0', 'bg-surface-variant']

            # Update the floating image
            float_img = soup.find('img', class_=lambda c: c and 'animate-float' in c)
            if float_img:
                float_img['src'] = 'assets/images/logistics.png'
                classes = float_img.get('class', [])
                if 'animate-float' in classes:
                    classes.remove('animate-float')
                float_img['class'] = classes
                float_img['data-alt'] = 'East Africa Shipping and Logistics'
                
        elif file_path == 'about.html':
            # Inject about sections before footer
            footer = soup.find('footer')
            if footer:
                about_soup = BeautifulSoup(ABOUT_EXTRA, 'html.parser')
                for elem in about_soup.contents:
                    footer.insert_before(elem)
                    
        elif file_path == 'presence.html':
            # Inject presence sections before footer
            footer = soup.find('footer')
            if footer:
                presence_soup = BeautifulSoup(PRESENCE_EXTRA, 'html.parser')
                for elem in presence_soup.contents:
                    footer.insert_before(elem)
                    
            # Fix generic stat
            stat_div = soup.find('div', string='12M+')
            if stat_div:
                stat_div.string = '9'
                label = stat_div.find_next_sibling('div')
                if label:
                    label.string = 'REGIONAL MARKETS'

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(str(soup))
        print(f"Updated {file_path}")

if __name__ == '__main__':
    process_html_files()
