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
