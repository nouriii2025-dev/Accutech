from django.contrib import messages
from django.shortcuts import redirect, render

from .content import (
    BRAND_ROSTER,
    BRANDS,
    CERTIFICATIONS,
    COMPANY,
    PRODUCT_CATEGORIES,
    PROJECT_CATEGORIES,
    SOLUTIONS,
    STATS,
)
from .forms import ContactForm


def home(request):
    context = {
        "solutions": SOLUTIONS[:6],
        "brands": BRANDS,
        "stats": STATS,
        "certifications": CERTIFICATIONS,
        "company": COMPANY,
    }
    return render(request, "core/home.html", context)


def about(request):
    context = {
        "stats": STATS,
        "certifications": CERTIFICATIONS,
        "company": COMPANY,
    }
    return render(request, "core/about.html", context)


def solutions(request):
    context = {
        "solutions": SOLUTIONS,
        "company": COMPANY,
    }
    return render(request, "core/solutions.html", context)


def products(request):
    context = {
        "product_categories": PRODUCT_CATEGORIES,
        "brand_roster": BRAND_ROSTER,
        "company": COMPANY,
    }
    return render(request, "core/products.html", context)


def projects(request):
    context = {
        "project_categories": PROJECT_CATEGORIES,
        "company": COMPANY,
    }
    return render(request, "core/projects.html", context)


def brands(request):
    context = {
        "brands": BRANDS,
        "brand_roster": BRAND_ROSTER,
        "company": COMPANY,
    }
    return render(request, "core/brands.html", context)

def terms(request):
    context = {"company": COMPANY}
    return render(request, "core/terms.html", context)



def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Thanks — your enquiry has been logged. Our engineering team "
                "will be in touch shortly.",
            )
            return redirect("core:contact")
    else:
        form = ContactForm()

    context = {"form": form, "company": COMPANY}
    return render(request, "core/contact.html", context)
