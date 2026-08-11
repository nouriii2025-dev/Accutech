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
    image = models.ImageField(upload_to="site_content/",blank=True,null=True)

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
    image = models.ImageField(upload_to="site_content/",blank=True,null=True)

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
    image = models.ImageField(upload_to="site_content/",blank=True,null=True)

    def __str__(self):
        return self.title

class ProductCategory(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True)
    icon = models.CharField(max_length=100, blank=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order", "name"]
        verbose_name = "Product Category"
        verbose_name_plural = "Product Categories"

    def __str__(self):
        return self.name


class ProductSubCategory(models.Model):
    category = models.ForeignKey(
        ProductCategory,
        on_delete=models.CASCADE,
        related_name="subcategories"
    )
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order", "name"]
        unique_together = ("category", "slug")
        verbose_name = "Product Subcategory"
        verbose_name_plural = "Product Subcategories"

    def __str__(self):
        return f"{self.category.name} → {self.name}"


class ProductType(models.Model):
    subcategory = models.ForeignKey(
        ProductSubCategory,
        on_delete=models.CASCADE,
        related_name="product_types"
    )
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=270)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order", "name"]
        unique_together = ("subcategory", "slug")
        verbose_name = "Product Type"
        verbose_name_plural = "Product Types"

    def __str__(self):
        return (
            f"{self.subcategory.category.name} → "
            f"{self.subcategory.name} → {self.name}"
        )


class Product(models.Model):
    product_type = models.ForeignKey(
        ProductType,
        on_delete=models.CASCADE,
        related_name="products"
    )

    name = models.CharField(max_length=300)
    slug = models.SlugField(max_length=320)

    brand = models.ForeignKey(
        Brand,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="products"
    )

    model_number = models.CharField(max_length=200, blank=True)
    short_description = models.TextField(blank=True)
    description = models.TextField(blank=True)

    image = models.ImageField(
        upload_to="products/",
        blank=True,
        null=True
    )

    datasheet = models.FileField(
        upload_to="product_datasheets/",
        blank=True,
        null=True
    )

    specifications = models.JSONField(
        default=dict,
        blank=True
    )

    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order", "name"]
        unique_together = ("product_type", "slug")
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.name

class Site_Product_Content(models.Model):
    key = models.CharField(max_length=100, unique=True)
    value = models.TextField()

    def __str__(self):
        return self.key

class Site_Calibration_Content(models.Model):
    key = models.CharField(max_length=100, unique=True)
    value = models.TextField()

    def __str__(self):
        return self.key

class Calibration_Service(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to="calibration_services/", blank=True, null=True)

    class Meta:
        ordering = ["order", "title"]
        verbose_name = "Calibration Service"
        verbose_name_plural = "Calibration Services"

    def __str__(self):
        return self.title

class Calibration_Capabilities(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to="calibration_capabilities/", blank=True, null=True)

    class Meta:
        ordering = ["order", "title"]
        verbose_name = "Calibration Capability"
        verbose_name_plural = "Calibration Capabilities"

    def __str__(self):
        return self.title

class Site_Base_Content(models.Model):
    key = models.CharField(max_length=100, unique=True)
    value = models.TextField()

    def __str__(self):
        return self.key

class Company_Details(models.Model):
    key = models.CharField(max_length=100, unique=True)
    value = models.TextField()

    def __str__(self):
        return self.key