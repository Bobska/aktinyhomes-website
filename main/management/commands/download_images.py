import os
import requests
from urllib.parse import urlparse
from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from main.models import TinyHomeImage


class Command(BaseCommand):
    help = 'Download all external images and store them locally'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Starting image download process...'))
        
        # Get all images with external URLs
        images = TinyHomeImage.objects.all()
        
        for image in images:
            if image.image_url and image.image_url.startswith('http'):
                try:
                    self.stdout.write(f'Downloading: {image.title}')
                    
                    # Download the image
                    response = requests.get(image.image_url, timeout=30)
                    response.raise_for_status()
                    
                    # Extract file extension from URL
                    parsed_url = urlparse(image.image_url)
                    path = parsed_url.path
                    
                    # Get file extension, default to .jpg if not found
                    if '.' in path:
                        ext = path.split('.')[-1].lower()
                        if ext not in ['jpg', 'jpeg', 'png', 'gif', 'webp']:
                            ext = 'jpg'
                    else:
                        ext = 'jpg'
                    
                    # Create safe filename
                    safe_title = "".join(c for c in image.title if c.isalnum() or c in (' ', '-', '_')).rstrip()
                    safe_title = safe_title.replace(' ', '_')
                    filename = f"tiny_homes/{safe_title[:50]}.{ext}"
                    
                    # Save the image
                    image_content = ContentFile(response.content)
                    saved_path = default_storage.save(filename, image_content)
                    
                    # Update the model to use local path
                    image.image_url = f'/media/{saved_path}'
                    image.save()
                    
                    self.stdout.write(self.style.SUCCESS(f'✓ Downloaded and saved: {saved_path}'))
                    
                except requests.exceptions.RequestException as e:
                    self.stdout.write(self.style.ERROR(f'✗ Failed to download {image.title}: {str(e)}'))
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f'✗ Error processing {image.title}: {str(e)}'))
            else:
                self.stdout.write(f'Skipping {image.title} - already local or no URL')
        
        self.stdout.write(self.style.SUCCESS('Image download complete!'))
        self.stdout.write(self.style.SUCCESS('All images are now stored locally in the media/tiny_homes/ folder'))
