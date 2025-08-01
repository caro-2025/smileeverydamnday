#!/usr/bin/env python3
"""
Script to create favicon files from the logo
"""

from PIL import Image
import os

def create_favicons():
    # Input logo file
    logo_path = "Logo Film ohne Hintergrund.JPEG"
    
    # Check if logo exists
    if not os.path.exists(logo_path):
        print(f"Error: {logo_path} not found!")
        return
    
    try:
        # Open the logo
        logo = Image.open(logo_path)
        print(f"Original logo size: {logo.size}")
        
        # Convert to RGBA if not already (for transparency support)
        if logo.mode != 'RGBA':
            logo = logo.convert('RGBA')
        
        # Define favicon sizes
        sizes = [
            (32, 32, "favicon-32x32.png"),
            (16, 16, "favicon-16x16.png"),
            (180, 180, "apple-touch-icon.png")
        ]
        
        # Create each favicon size
        for width, height, filename in sizes:
            # Resize with high quality
            favicon = logo.resize((width, height), Image.Resampling.LANCZOS)
            
            # Save as PNG
            favicon.save(filename, "PNG", optimize=True)
            print(f"✅ Created {filename} ({width}x{height})")
        
        print("\n🎉 All favicons created successfully!")
        print("\nFiles created:")
        for _, _, filename in sizes:
            if os.path.exists(filename):
                file_size = os.path.getsize(filename)
                print(f"  - {filename} ({file_size} bytes)")
    
    except Exception as e:
        print(f"Error creating favicons: {e}")

if __name__ == "__main__":
    create_favicons()