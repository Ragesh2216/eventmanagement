import os
import math
from PIL import Image, ImageDraw, ImageFont, ImageFilter

output_dir = os.path.join(os.path.dirname(__file__), "..", "assets", "images")
os.makedirs(output_dir, exist_ok=True)

def try_font(size):
    try:
        return ImageFont.truetype("arial.ttf", size=size)
    except Exception:
        return ImageFont.load_default()

def draw_spotlight_beam(draw, start_pt, end_width, height, color):
    # Draw trapezoidal glowing light beam
    sx, sy = start_pt
    pts = [
        (sx - 15, sy),
        (sx + 15, sy),
        (sx + end_width // 2, height),
        (sx - end_width // 2, height)
    ]
    draw.polygon(pts, fill=color)

def generate_corporate_img(w=600, h=400, filename="corporate.webp"):
    img = Image.new("RGBA", (w, h), (15, 23, 42, 255))
    draw = ImageDraw.Draw(img)

    # Gradient background
    for y in range(h):
        r = int(15 + (30 - 15) * (y / h))
        g = int(23 + (58 - 23) * (y / h))
        b = int(42 + (138 - 42) * (y / h))
        draw.line([(0, y), (w, y)], fill=(r, g, b, 255))

    # Stage spotlights
    draw_spotlight_beam(draw, (w * 0.3, 0), 200, h, (59, 130, 246, 40))
    draw_spotlight_beam(draw, (w * 0.7, 0), 200, h, (99, 102, 241, 40))

    # Large Presentation Screen backdrop
    draw.rectangle([w * 0.15, h * 0.15, w * 0.85, h * 0.65], fill=(30, 41, 59, 230), outline=(99, 102, 241, 255), width=3)
    draw.rectangle([w * 0.18, h * 0.18, w * 0.82, h * 0.62], fill=(15, 23, 42, 255))
    
    # Screen chart graphic
    draw.line([(w * 0.22, h * 0.5), (w * 0.35, h * 0.35), (w * 0.48, h * 0.42), (w * 0.62, h * 0.25), (w * 0.78, h * 0.3)], fill=(59, 130, 246, 255), width=4)
    for x_p in [w * 0.22, w * 0.35, w * 0.48, w * 0.62, w * 0.78]:
        draw.ellipse([x_p - 5, h * 0.5 - 5, x_p + 5, h * 0.5 + 5], fill=(212, 175, 55, 255))

    # Speaker Podium
    draw.rectangle([w * 0.43, h * 0.6, w * 0.57, h * 0.85], fill=(30, 41, 59, 255), outline=(212, 175, 55, 255), width=2)
    draw.polygon([(w * 0.41, h * 0.6), (w * 0.59, h * 0.6), (w * 0.57, h * 0.64), (w * 0.43, h * 0.64)], fill=(212, 175, 55, 255))

    # Audience seating silhouettes
    for i in range(12):
        cx = (i + 0.5) * (w / 12)
        draw.ellipse([cx - 15, h * 0.88, cx + 15, h * 0.98], fill=(10, 15, 26, 255))

    # Text overlay
    font = try_font(24)
    font_sub = try_font(14)
    draw.text((30, 30), "CORPORATE SUMMIT & KEYNOTE", fill=(212, 175, 55, 255), font=font_sub)
    draw.text((30, h - 50), "Enterprise Leadership 2026", fill=(255, 255, 255, 255), font=font)

    filepath = os.path.join(output_dir, filename)
    img.convert("RGB").save(filepath, "WEBP", quality=85)
    print(f"Generated field image {filename}: {os.path.getsize(filepath)/1024:.2f} KB")

def generate_wedding_img(w=600, h=400, filename="wedding.webp"):
    img = Image.new("RGBA", (w, h), (40, 15, 30, 255))
    draw = ImageDraw.Draw(img)

    # Warm pinkish gold gradient
    for y in range(h):
        r = int(70 + (131 - 70) * (y / h))
        g = int(25 + (24 - 25) * (y / h))
        b = int(45 + (67 - 45) * (y / h))
        draw.line([(0, y), (w, y)], fill=(r, g, b, 255))

    # Floral Archway Structure
    cx, cy = w // 2, int(h * 0.55)
    rx, ry = int(w * 0.28), int(h * 0.38)
    draw.arc([cx - rx, cy - ry, cx + rx, cy + ry], start=180, end=360, fill=(212, 175, 55, 255), width=6)

    # Glowing Fairy Lights along Arch
    for angle in range(180, 361, 15):
        rad = math.radians(angle)
        lx = cx + rx * math.cos(rad)
        ly = cy + ry * math.sin(rad)
        draw.ellipse([lx - 6, ly - 6, lx + 6, ly + 6], fill=(254, 240, 138, 230))
        draw.ellipse([lx - 3, ly - 3, lx + 3, ly + 3], fill=(255, 255, 255, 255))

    # Aisle Runner & Candles
    draw.polygon([(w * 0.35, h), (w * 0.65, h), (w * 0.58, h * 0.55), (w * 0.42, h * 0.55)], fill=(255, 245, 235, 60))
    for step in range(5):
        y_c = h * 0.95 - step * 25
        x_left = w * 0.33 + step * 4
        x_right = w * 0.67 - step * 4
        draw.rectangle([x_left, y_c - 10, x_left + 8, y_c], fill=(254, 240, 138, 255))
        draw.rectangle([x_right - 8, y_c - 10, x_right, y_c], fill=(254, 240, 138, 255))

    # Text overlay
    font = try_font(24)
    font_sub = try_font(14)
    draw.text((30, 30), "LUXURY DESTINATION WEDDING", fill=(212, 175, 55, 255), font=font_sub)
    draw.text((30, h - 50), "Royal Opulence Celebrations", fill=(255, 255, 255, 255), font=font)

    filepath = os.path.join(output_dir, filename)
    img.convert("RGB").save(filepath, "WEBP", quality=85)
    print(f"Generated field image {filename}: {os.path.getsize(filepath)/1024:.2f} KB")

def generate_concert_img(w=600, h=400, filename="concert.webp"):
    img = Image.new("RGBA", (w, h), (10, 10, 25, 255))
    draw = ImageDraw.Draw(img)

    # Deep violet backdrop
    for y in range(h):
        r = int(20 + (88 - 20) * (y / h))
        g = int(10 + (28 - 10) * (y / h))
        b = int(45 + (135 - 45) * (y / h))
        draw.line([(0, y), (w, y)], fill=(r, g, b, 255))

    # Laser Beams
    colors = [(236, 72, 153, 120), (6, 182, 212, 120), (168, 85, 247, 120), (234, 179, 8, 120)]
    for i, col in enumerate(colors):
        sx = w * (0.2 + i * 0.2)
        draw.line([(sx, h * 0.3), (0, h)], fill=col, width=3)
        draw.line([(sx, h * 0.3), (w, h)], fill=col, width=3)
        draw.line([(sx, h * 0.3), (w * 0.5, h)], fill=col, width=4)

    # Trussing Grid Top
    draw.rectangle([w * 0.1, h * 0.08, w * 0.9, h * 0.15], fill=(40, 40, 60, 255), outline=(168, 85, 247, 255), width=2)

    # Audience Hands raised silhouette
    for i in range(25):
        hx = (i + 0.5) * (w / 25)
        hy = h - 20 - (i % 5) * 8
        draw.rectangle([hx - 4, hy, hx + 4, h], fill=(5, 5, 12, 255))
        draw.ellipse([hx - 7, hy - 10, hx + 7, hy + 4], fill=(5, 5, 12, 255))

    # Text overlay
    font = try_font(24)
    font_sub = try_font(14)
    draw.text((30, 30), "CONCERT & MUSIC FESTIVAL", fill=(236, 72, 153, 255), font=font_sub)
    draw.text((30, h - 50), "Neon Electric Arena Live", fill=(255, 255, 255, 255), font=font)

    filepath = os.path.join(output_dir, filename)
    img.convert("RGB").save(filepath, "WEBP", quality=85)
    print(f"Generated field image {filename}: {os.path.getsize(filepath)/1024:.2f} KB")

def generate_gala_img(w=600, h=400, filename="gala.webp"):
    img = Image.new("RGBA", (w, h), (30, 20, 10, 255))
    draw = ImageDraw.Draw(img)

    for y in range(h):
        r = int(67 + (120 - 67) * (y / h))
        g = int(40 + (53 - 40) * (y / h))
        b = int(16 + (15 - 16) * (y / h))
        draw.line([(0, y), (w, y)], fill=(r, g, b, 255))

    # Chandelier Crystal Strands
    cx = w // 2
    for ring in [80, 50, 25]:
        draw.ellipse([cx - ring, 20, cx + ring, 20 + ring], outline=(212, 175, 55, 200), width=2)
    for i in range(15):
        ang = i * (360 / 15)
        rad = math.radians(ang)
        lx = cx + 80 * math.cos(rad)
        ly = 25 + 40 * math.sin(rad)
        draw.line([(lx, ly), (lx, ly + 40)], fill=(254, 240, 138, 180), width=2)
        draw.ellipse([lx - 3, ly + 40, lx + 3, ly + 46], fill=(255, 255, 255, 255))

    # Gala Dining Round Tables
    for t in range(4):
        tx = w * (0.2 + t * 0.2)
        ty = h * 0.75
        draw.ellipse([tx - 40, ty - 15, tx + 40, ty + 15], fill=(255, 255, 255, 200), outline=(212, 175, 55, 255), width=2)
        # Centerpiece flower glow
        draw.ellipse([tx - 8, ty - 6, tx + 8, ty + 6], fill=(212, 175, 55, 255))

    # Text overlay
    font = try_font(24)
    font_sub = try_font(14)
    draw.text((30, 30), "CHARITY & PRIVATE GALA", fill=(212, 175, 55, 255), font=font_sub)
    draw.text((30, h - 50), "Crystal Ball Grand Evening", fill=(255, 255, 255, 255), font=font)

    filepath = os.path.join(output_dir, filename)
    img.convert("RGB").save(filepath, "WEBP", quality=85)
    print(f"Generated field image {filename}: {os.path.getsize(filepath)/1024:.2f} KB")

def generate_launch_img(w=600, h=400, filename="launch.webp"):
    img = Image.new("RGBA", (w, h), (6, 40, 35, 255))
    draw = ImageDraw.Draw(img)

    for y in range(h):
        r = int(6 + (4 - 6) * (y / h))
        g = int(78 + (120 - 78) * (y / h))
        b = int(59 + (87 - 59) * (y / h))
        draw.line([(0, y), (w, y)], fill=(r, g, b, 255))

    # Holographic 3D Pedestal
    cx, cy = w // 2, int(h * 0.6)
    draw.polygon([(cx - 70, cy), (cx + 70, cy), (cx + 90, cy + 50), (cx - 90, cy + 50)], fill=(16, 185, 129, 180), outline=(52, 211, 153, 255), width=3)
    
    # Floating Hologram Product Cube
    cube_y = cy - 80
    draw.rectangle([cx - 35, cube_y - 35, cx + 35, cube_y + 35], outline=(52, 211, 153, 255), width=3)
    draw.rectangle([cx - 20, cube_y - 20, cx + 20, cube_y + 20], outline=(254, 240, 138, 255), width=2)
    draw.line([(cx - 35, cube_y - 35), (cx - 20, cube_y - 20)], fill=(52, 211, 153, 255), width=2)
    draw.line([(cx + 35, cube_y - 35), (cx + 20, cube_y - 20)], fill=(52, 211, 153, 255), width=2)
    draw.line([(cx + 35, cube_y + 35), (cx + 20, cube_y + 20)], fill=(52, 211, 153, 255), width=2)
    draw.line([(cx - 35, cube_y + 35), (cx - 20, cube_y + 20)], fill=(52, 211, 153, 255), width=2)

    # Vertical light ray
    draw.rectangle([cx - 45, 0, cx + 45, h], fill=(52, 211, 153, 30))

    # Text overlay
    font = try_font(24)
    font_sub = try_font(14)
    draw.text((30, 30), "PRODUCT LAUNCH & ACTIVATION", fill=(52, 211, 153, 255), font=font_sub)
    draw.text((30, h - 50), "NextGen Tech Reveal 2026", fill=(255, 255, 255, 255), font=font)

    filepath = os.path.join(output_dir, filename)
    img.convert("RGB").save(filepath, "WEBP", quality=85)
    print(f"Generated field image {filename}: {os.path.getsize(filepath)/1024:.2f} KB")

def generate_expo_img(w=600, h=400, filename="expo.webp"):
    img = Image.new("RGBA", (w, h), (20, 30, 45, 255))
    draw = ImageDraw.Draw(img)

    for y in range(h):
        r = int(30 + (51 - 30) * (y / h))
        g = int(41 + (65 - 41) * (y / h))
        b = int(59 + (85 - 59) * (y / h))
        draw.line([(0, y), (w, y)], fill=(r, g, b, 255))

    # Trade show booth frames
    draw.rectangle([w * 0.1, h * 0.2, w * 0.45, h * 0.8], outline=(148, 163, 184, 255), width=3)
    draw.rectangle([w * 0.55, h * 0.2, w * 0.9, h * 0.8], outline=(99, 102, 241, 255), width=3)
    
    draw.line([(w * 0.1, h * 0.35), (w * 0.45, h * 0.35)], fill=(212, 175, 55, 255), width=2)
    draw.line([(w * 0.55, h * 0.35), (w * 0.9, h * 0.35)], fill=(212, 175, 55, 255), width=2)

    # Text overlay
    font = try_font(24)
    font_sub = try_font(14)
    draw.text((30, 30), "GLOBAL HYBRID EXPO", fill=(148, 163, 184, 255), font=font_sub)
    draw.text((30, h - 50), "International Trade Exhibition", fill=(255, 255, 255, 255), font=font)

    filepath = os.path.join(output_dir, filename)
    img.convert("RGB").save(filepath, "WEBP", quality=85)
    print(f"Generated field image {filename}: {os.path.getsize(filepath)/1024:.2f} KB")

# Generate all field images
generate_corporate_img()
generate_wedding_img()
generate_concert_img()
generate_gala_img()
generate_launch_img()
generate_expo_img()

print("All field-specific WebP images successfully updated!")
