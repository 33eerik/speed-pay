from PIL import Image, ImageDraw, ImageFont
import os

def create_badge(filename, text):
    img = Image.new('RGB', (200, 100), color = (255, 255, 255))
    d = ImageDraw.Draw(img)
    font = ImageFont.load_default()
    d.text((10,10), text, fill=(0,0,0), font=font)
    
    if not os.path.exists('static/img'):
        os.makedirs('static/img')
    
    img.save(f'static/img/{filename}')

create_badge('security-badge-1.png', 'Security Certification')
create_badge('security-badge-2.png', 'PCI DSS Compliant')
create_badge('trust-seal-1.png', 'Trust Seal')
create_badge('trust-seal-2.png', 'Verified Business')
create_badge('pci-dss.png', 'PCI DSS Compliant')
create_badge('ssl-secure.png', 'SSL Encrypted')

print("Badge images created successfully.")
