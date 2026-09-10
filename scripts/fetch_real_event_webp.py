import os
import urllib.request
from PIL import Image

output_dir = os.path.join(os.path.dirname(__file__), "..", "assets", "images")
os.makedirs(output_dir, exist_ok=True)

# High Quality Real Event Photography URLs (Unsplash Public License)
real_event_images = {
    "hero-bg.webp": ("https://images.unsplash.com/photo-1492684223066-81342ee5ff30?w=1200&auto=format&fit=crop&q=80", (1200, 700)),
    "hero-event.webp": ("https://images.unsplash.com/photo-1511795409834-ef04bbd61622?w=900&auto=format&fit=crop&q=80", (800, 500)),
    "corporate.webp": ("https://images.unsplash.com/photo-1511578314322-379afb476865?w=800&auto=format&fit=crop&q=80", (600, 400)),
    "wedding.webp": ("https://images.unsplash.com/photo-1519741497674-611481863552?w=800&auto=format&fit=crop&q=80", (600, 400)),
    "concert.webp": ("https://images.unsplash.com/photo-1470225620780-dba8ba36b745?w=800&auto=format&fit=crop&q=80", (600, 400)),
    "gala.webp": ("https://images.unsplash.com/photo-1519671482749-fd09be7ccebf?w=800&auto=format&fit=crop&q=80", (600, 400)),
    "launch.webp": ("https://images.unsplash.com/photo-1540575467063-178a50c2df87?w=800&auto=format&fit=crop&q=80", (600, 400)),
    "expo.webp": ("https://images.unsplash.com/photo-1475721027785-f74eccf877e2?w=800&auto=format&fit=crop&q=80", (600, 400)),
    "venue-1.webp": ("https://images.unsplash.com/photo-1519167758481-83f550bb49b3?w=800&auto=format&fit=crop&q=80", (600, 400)),
    "venue-2.webp": ("https://images.unsplash.com/photo-1561489413-985b06da5bee?w=800&auto=format&fit=crop&q=80", (600, 400)),
    "venue-3.webp": ("https://images.unsplash.com/photo-1514525253161-7a46d19cd819?w=800&auto=format&fit=crop&q=80", (600, 400)),
    "venue-4.webp": ("https://images.unsplash.com/photo-1527529482837-4698179dc6ce?w=800&auto=format&fit=crop&q=80", (600, 400)),
    "team-1.webp": ("https://images.unsplash.com/photo-1560250097-0b93528c311a?w=400&auto=format&fit=crop&q=80", (400, 400)),
    "team-2.webp": ("https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?w=400&auto=format&fit=crop&q=80", (400, 400)),
    "team-3.webp": ("https://images.unsplash.com/photo-1519085360753-af0119f7cbe7?w=400&auto=format&fit=crop&q=80", (400, 400)),
    "team-4.webp": ("https://images.unsplash.com/photo-1580489944761-15a19d654956?w=400&auto=format&fit=crop&q=80", (400, 400)),
    "blog-1.webp": ("https://images.unsplash.com/photo-1501386761578-eac5c94b800a?w=800&auto=format&fit=crop&q=80", (600, 400)),
    "blog-2.webp": ("https://images.unsplash.com/photo-1464366400600-7168b8af9bc3?w=800&auto=format&fit=crop&q=80", (600, 400)),
    "blog-3.webp": ("https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?w=800&auto=format&fit=crop&q=80", (600, 400)),
    "testimonial-1.webp": ("https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=200&auto=format&fit=crop&q=80", (200, 200)),
    "testimonial-2.webp": ("https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=200&auto=format&fit=crop&q=80", (200, 200)),
    "testimonial-3.webp": ("https://images.unsplash.com/photo-1573497019940-1c28c88b4f3e?w=200&auto=format&fit=crop&q=80", (200, 200)),
    "about-hero.webp": ("https://images.unsplash.com/photo-1511578314322-379afb476865?w=1200&auto=format&fit=crop&q=80", (1200, 500)),
    "contact-hero.webp": ("https://images.unsplash.com/photo-1519671482749-fd09be7ccebf?w=1200&auto=format&fit=crop&q=80", (1200, 500)),
}

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

for filename, (url, target_size) in real_event_images.items():
    try:
        req = urllib.request.Request(url, headers=headers)
        temp_file = os.path.join(output_dir, "temp_download")
        with urllib.request.urlopen(req, timeout=10) as response, open(temp_file, "wb") as f:
            f.write(response.read())

        # Process with PIL: Resize & Convert to WEBP under 100KB
        with Image.open(temp_file) as img:
            img = img.convert("RGB")
            img = img.resize(target_size, Image.Resampling.LANCZOS)
            out_path = os.path.join(output_dir, filename)
            
            # Start at quality 80 and adjust if needed to stay under 100KB
            quality = 80
            img.save(out_path, "WEBP", quality=quality)
            size_kb = os.path.getsize(out_path) / 1024
            
            while size_kb > 95 and quality > 40:
                quality -= 5
                img.save(out_path, "WEBP", quality=quality)
                size_kb = os.path.getsize(out_path) / 1024

            print(f"Downloaded & Saved {filename}: {target_size[0]}x{target_size[1]}, {size_kb:.2f} KB (Quality={quality})")

        if os.path.exists(temp_file):
            os.remove(temp_file)

    except Exception as e:
        print(f"Error processing {filename}: {e}")

print("All real event management system images processed into WebP format under 100KB!")
