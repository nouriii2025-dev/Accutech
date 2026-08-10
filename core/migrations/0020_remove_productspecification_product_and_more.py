from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0019_productcategory_product_productspecification_and_more"),
    ]

    operations = [
        migrations.DeleteModel(
            name="ProductSpecification",
        ),
        migrations.DeleteModel(
            name="ProductType",
        ),
        migrations.DeleteModel(
            name="ProductSubcategory",
        ),
        migrations.DeleteModel(
            name="ProductCategory",
        ),
        migrations.DeleteModel(
            name="Product",
        ),
    ]