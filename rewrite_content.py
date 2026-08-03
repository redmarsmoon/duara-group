import glob
import re

replacements = {
    # index.html & about.html
    "Building Africa Through Technology, Innovation &amp; Enterprise": "Technology, Business, and Audiovisual Solutions in East Africa",
    "Building Africa Through Technology, Innovation & Enterprise": "Technology, Business, and Audiovisual Solutions in East Africa",
    "Duara Group is a premier East African holding company driving sustainable growth and technological advancement across the continent. We invest in the future of Africa through robust infrastructure, digital solutions, and strategic partnerships.": "Duara Group is a holding company based in Nairobi. We operate Duara Dev, Duara Agency, and Duara Audiovisual to provide services to businesses across 9 countries.",
    "Driving innovation and enterprise across East Africa through specialized subsidiaries.": "Our companies provide technology, marketing, and media solutions.",
    
    # about.html
    "Building East Africa's Future": "About Duara Group",
    "Duara Group is a leading holding company committed to long-term sustainability, robust governance, and solving the region's most complex challenges through strategic investment and operational excellence.": "We are an East African company that provides technology, market expansion, and audiovisual services to businesses.",
    "To be the definitive catalyst for sustainable economic growth and institutional excellence across East Africa, setting the global standard for responsible regional investment.": "To provide reliable technology and business services to companies across East Africa.",
    "We invest in and operate transformative enterprises. By marrying local insights with global best practices, we create enduring value for our stakeholders and the communities we serve.": "We build and operate businesses that solve practical problems in tech, market expansion, and event production.",
    "Founded in Nairobi, Duara Group began with a simple but profound belief: that East Africa's potential is boundless when supported by the right technology and strategic investment. Over the years, we have grown from a local enterprise into a regional powerhouse, bridging the gap between local insights and global standards.": "Duara Group was founded in Nairobi, Kenya in 2015. We have since expanded into 9 East African countries, providing businesses with technology, consulting, and event services.",
    "Guided by seasoned executives with deep roots in East Africa and a global perspective.": "Our leadership team oversees our operations across the region.",
    
    # presence.html
    "Powering East Africa's Future": "Our East Africa Presence",
    "A deeply rooted presence across the region, driving sustainable growth through strategic investments in critical infrastructure, industry, and innovation.": "We operate across 9 East African countries, providing local businesses with technology, market entry support, and audiovisual services.",
    "Regional Reach": "Our Locations",
    "Our operational footprint spans key economic hubs, providing a robust platform for scalable enterprise solutions and cross-border synergy.": "We have offices and operations in 9 countries to support businesses across East Africa.",
    "Strategic Operations": "Key Operations",
    "Tailored enterprise strategies executing across distinct regulatory and economic landscapes.": "Our main operational hubs and their primary focus areas.",
    "Our regional headquarters, focusing on advanced logistics, fintech integration, and sustainable energy projects driving the national grid.": "Our regional headquarters for all operations.",
    "Spearheading agribusiness innovations and high-yield processing facilities to maximize export potential.": "Market expansion and business development hub.",
    "Maritime logistics and coastal infrastructure development.": "Audiovisual and event production services.",
    "Tech incubator investments and smart-city infrastructure.": "Technology and software development hub.",
    "We are actively driving enterprise, infrastructure, and technology across the entire East African and Horn of Africa region, including:": "We provide services in the following countries:",
    
    # csr.html
    "Empowering the Future Through Digital Education": "Technology for Education",
    "Bridging the digital divide in East Africa by providing access, infrastructure, and skills for the next generation of innovators.": "We provide free digital learning resources and technology training to students in East Africa.",
    
    # Contact & Careers & News generic text
    "Connecting Enterprise Across the Continent": "Contact Duara Group",
    "Whether you are looking to scale operations, explore joint ventures, or integrate next-generation tech solutions, our team is ready to facilitate your growth in East Africa.": "Contact us for general, media, career, and partnership enquiries.",
    "Shaping the Future of African Enterprise": "Careers at Duara Group",
    "Join a culture of excellence. We are looking for visionary thinkers and relentless executors to drive our pan-African initiatives forward.": "Join our team. We offer job openings, internships, and employee benefits.",
    "Insights &amp; Innovations": "News and Press Releases",
    "Insights & Innovations": "News and Press Releases",
    "Stay informed on our latest strategic investments, technological breakthroughs, and regional economic impact.": "Stay updated with our latest news articles and press releases."
}

def rewrite_content():
    html_files = glob.glob('*.html')
    for file_path in html_files:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Apply strict replacements
        for old, new in replacements.items():
            content = content.replace(old, new)
            
        # Write back
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {file_path}")

if __name__ == '__main__':
    rewrite_content()
