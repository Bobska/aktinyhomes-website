from django.db import models

class TinyHomeLayout(models.Model):
    """Model for different tiny home layouts and designs"""
    name = models.CharField(max_length=100)
    description = models.TextField()
    size = models.CharField(max_length=50)
    price_range = models.CharField(max_length=50, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class TinyHomeImage(models.Model):
    """Model for tiny home images"""
    layout = models.ForeignKey(TinyHomeLayout, on_delete=models.CASCADE, related_name='images', null=True, blank=True)
    title = models.CharField(max_length=100)
    image_url = models.URLField(blank=True, null=True)  # For external URLs
    image_file = models.ImageField(upload_to='tiny_homes/', blank=True, null=True)  # For local files
    description = models.TextField(blank=True)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    @property
    def image_src(self):
        """Return the image source - either local file or external URL"""
        if self.image_file:
            return self.image_file.url
        elif self.image_url:
            return self.image_url
        return None
    
    def __str__(self):
        return self.title

class BlogPost(models.Model):
    """Model for blog posts"""
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

class FAQ(models.Model):
    """Model for frequently asked questions"""
    question = models.CharField(max_length=300)
    answer = models.TextField()
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['order', 'created_at']
    
    def __str__(self):
        return self.question
