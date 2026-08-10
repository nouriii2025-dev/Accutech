from django.db import models


class ContactMessage(models.Model):
    """A message submitted through the public contact form."""

    ENQUIRY_CHOICES = [
        ("product", "Product enquiry"),
        ("calibration", "Calibration services"),
        ("partnership", "Partnership / dealership"),
        ("support", "Technical support"),
        ("other", "Other"),
    ]

    name = models.CharField(max_length=120)
    company = models.CharField(max_length=150, blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=40, blank=True)
    enquiry_type = models.CharField(max_length=20, choices=ENQUIRY_CHOICES, default="product")
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} ({self.get_enquiry_type_display()}) - {self.created_at:%Y-%m-%d}"


class Site_Home_Content(models.Model):
    key = models.CharField(max_length=100, unique=True)
    value = models.TextField()

    def __str__(self):
        return self.key
        
class Brand(models.Model):
    name = models.CharField(max_length=150)
    logo = models.ImageField(upload_to="brands/", default="brands/default-logo.png")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Certification(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Site_About_Content(models.Model):
    key = models.CharField(max_length=100, unique=True)
    value = models.TextField()

    def __str__(self):
        return self.key

class About_Milestone_Content(models.Model):
    year = models.CharField(max_length=50)
    title = models.CharField(max_length=250)
    description = models.TextField()
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"{self.year} - {self.title}"

class Site_Solutions_Content(models.Model):
    key = models.CharField(max_length=100, unique=True)
    value = models.TextField()

    def __str__(self):
        return self.key

class Solution(models.Model):
    title = models.CharField(max_length=200)
    summary = models.TextField(blank=True)
    detail = models.TextField(blank=True)
    image = models.ImageField(upload_to="solutions/", blank=True, null=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Site_Project_Content(models.Model):
    key = models.CharField(max_length=100, unique=True)
    value = models.TextField()

    def __str__(self):
        return self.key

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="projects/", blank=True, null=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class TermsandConditions_Content(models.Model):
    key = models.CharField(max_length=100, unique=True)
    value = models.TextField()

    def __str__(self):
        return self.key

class TermsandConditions(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


