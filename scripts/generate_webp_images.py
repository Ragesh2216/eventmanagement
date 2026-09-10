import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

output_dir = os.path.join(os.path.dirname(__file__), "..", "assets", "images")
os.makedirs(output_dir, exist_ok=True)

def create_gradient_image(filename, width, height, color1, color2, color3=None, text="", category=""):
    img = Image.new("RGB", (width, height), color1)
    draw = ImageDraw.Draw(img)
    
    # Draw smooth gradient layers
    for y in range(height):
        r = int(color1[0] + (color2[0] - color1[0]) * (y / height))
        g = int(color1[1] + (color2[1] - color1[1]) * (y / height))
        b = int(color1[2] + (color2[2] - color1[2]) * (y / height))
        draw.line([(0, y), (width, y)], fill=(r, g, b))
        
    if color3:
        # Add diagonal ambient lighting sphere
        overlay = Image.new("RGBA", (width, height), (0, 0, 0, 0))
        ol_draw = ImageDraw.Draw(overlay)
        cx, cy = int(width * 0.7), int(height * 0.3)
        radius = int(max(width, height) * 0.6)
        ol_draw.ellipse([cx - radius, cy - radius, cx + radius, cy + radius], fill=(color3[0], color3[1], color3[2], 90))
        overlay = overlay.filter(ImageFilter.GaussianBlur(radius=40))
        img = Image.alpha_composite(img.convert("RGBA"), overlay).convert("RGB")
        draw = ImageDraw.Draw(img)

    # Decorative geometric patterns & glow rings
    draw.ellipse([width*0.1, height*0.1, width*0.4, height*0.7], outline=(255, 255, 255, 40), width=3)
    draw.rectangle([width*0.65, height*0.5, width*0.9, height*0.85], outline=(255, 255, 255, 30), width=2)
    
    # Add typography overlay
    try:
        font_large = ImageFont.truetype("arial.ttf", size=int(height * 0.08))
        font_small = ImageFont.truetype("arial.ttf", size=int(height * 0.04))
    except Exception:
        font_large = ImageFont.load_default()
        font_small = ImageFont.load_default()
        
    if category:
        draw.text((40, 40), category.upper(), fill=(212, 175, 55), font=font_small) # Gold text
    if text:
        draw.text((40, height - 90), text, fill=(255, 255, 255), font=font_large)

    filepath = os.path.join(output_dir, filename)
    # Save as WebP with high quality compression
    img.save(filepath, "WEBP", quality=82)
    size_kb = os.path.getsize(filepath) / 1024
    print(f"Generated {filename}: {width}x{height}, {size_kb:.2f} KB")

# Image configurations (all saved in WebP, kept under 100KB)
images_to_generate = [
    ("hero-bg.webp", 1200, 700, (15, 23, 42), (30, 41, 59), (99, 102, 241), "LUXURY EVENT MANAGEMENT", "EVENTCRAFT EXCLUSIVE"),
    ("hero-event.webp", 800, 500, (30, 27, 75), (76, 29, 149), (236, 72, 153), "Grand Gala & Light Engineering", "SPOTLIGHT"),
    ("corporate.webp", 600, 400, (15, 23, 42), (30, 58, 138), (59, 130, 246), "Global Leadership Summit 2026", "CORPORATE"),
    ("wedding.webp", 600, 400, (70, 25, 45), (131, 24, 67), (244, 114, 182), "Royal Opulence Wedding", "LUXURY WEDDING"),
    ("concert.webp", 600, 400, (46, 16, 101), (88, 28, 135), (168, 85, 247), "Neon Electric Music Fest", "CONCERT & FESTIVAL"),
    ("gala.webp", 600, 400, (67, 40, 16), (120, 53, 15), (245, 158, 11), "Charity Crystal Ball Gala", "PRIVATE GALA"),
    ("launch.webp", 600, 400, (6, 78, 59), (4, 120, 87), (16, 185, 129), "NextGen Tech Launch", "BRAND ACTIVATION"),
    ("expo.webp", 600, 400, (30, 41, 59), (51, 65, 85), (148, 163, 184), "Global Hybrid Trade Expo", "EXHIBITION"),
    ("venue-1.webp", 600, 400, (17, 24, 39), (31, 41, 55), (99, 102, 241), "The Diamond Ballroom - NY", "EXCLUSIVE VENUE"),
    ("venue-2.webp", 600, 400, (24, 24, 27), (39, 39, 42), (234, 179, 8), "Skyline Glass Arena - London", "EXCLUSIVE VENUE"),
    ("venue-3.webp", 600, 400, (15, 23, 42), (30, 41, 59), (236, 72, 153), "Palace Bay Pavilion - Dubai", "EXCLUSIVE VENUE"),
    ("venue-4.webp", 600, 400, (20, 83, 45), (22, 101, 52), (34, 197, 94), "Grand Garden Estate - Paris", "EXCLUSIVE VENUE"),
    ("team-1.webp", 400, 400, (30, 27, 75), (67, 56, 202), (129, 140, 248), "Alexander Vance", "CHIEF EVENT ARCHITECT"),
    ("team-2.webp", 400, 400, (70, 25, 45), (157, 23, 77), (251, 113, 133), "Sophia Reynolds", "CREATIVE DIRECTOR"),
    ("team-3.webp", 400, 400, (6, 78, 59), (6, 95, 70), (52, 211, 153), "Marcus Sterling", "HEAD OF OPERATIONS"),
    ("team-4.webp", 400, 400, (67, 40, 16), (146, 64, 14), (251, 191, 36), "Elena Rostova", "VIP CONCIERGE LEAD"),
    ("blog-1.webp", 600, 400, (15, 23, 42), (40, 50, 90), (99, 102, 241), "Top 10 Event Lighting Trends 2026", "DESIGN TRENDS"),
    ("blog-2.webp", 600, 400, (24, 24, 27), (50, 40, 80), (236, 72, 153), "Mastering Sustainable Event Tech", "SUSTAINABILITY"),
    ("blog-3.webp", 600, 400, (17, 24, 39), (30, 60, 70), (59, 130, 246), "Budgeting Luxury Corporate Galas", "INSIGHTS"),
    ("testimonial-1.webp", 200, 200, (30, 41, 59), (71, 85, 105), (148, 163, 184), "Sarah Jenkins", "VP MARKETING"),
    ("testimonial-2.webp", 200, 200, (46, 16, 101), (107, 33, 168), (192, 132, 252), "David Chen", "FOUNDER & CEO"),
    ("testimonial-3.webp", 200, 200, (6, 78, 59), (13, 148, 136), (45, 212, 191), "Victoria Croft", "GALA CHAIRPERSON"),
    ("about-hero.webp", 1200, 500, (15, 23, 42), (30, 41, 59), (168, 85, 247), "Crafting Unforgettable Moments", "ABOUT EVENTCRAFT"),
    ("contact-hero.webp", 1200, 500, (15, 23, 42), (30, 41, 59), (59, 130, 246), "Let's Plan Your Masterpiece", "GET IN TOUCH"),
]

for filename, w, h, c1, c2, c3, txt, cat in images_to_generate:
    create_gradient_image(filename, w, h, c1, c2, c3, txt, cat)

print("All 24 WebP images created successfully!")
