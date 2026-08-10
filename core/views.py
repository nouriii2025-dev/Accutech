from django.contrib import messages
from django.shortcuts import redirect, render
from .models import *

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


# All views in this file are for the public-facing website.
#All the site content is stored in the get_site_content() function, which retrieves the content from the SiteContent model. 
# This allows for easy editing of the site content without having to modify the code.
def get_site_content():
    return {
        item.key: item.value
        for item in Site_Home_Content.objects.all()
    }
def home(request):
    content = get_site_content()
    context = {
        "hero_title": content.get("home_hero_title"),
        "hero_eyebrow": content.get("home_hero_eyebrow"),
        "hero_description": content.get("home_hero_description"),
        "solutions_eyebrow": content.get("home_solutions_eyebrow"),
        "solutions_title": content.get("home_solutions_title"),
        "solutions_description": content.get("home_solutions_description"),
        "product_card_title": content.get("home_product_card_title"),
        "product_card_description": content.get("home_product_card_description"),
        "project_card_title": content.get("home_project_card_title"),
        "project_card_description": content.get("home_project_card_description"),
        "brand_card_eyebrow": content.get("home_brand_card_eyebrow"),
        "certificate_card_eyebrow": content.get("home_certificate_card_eyebrow"),
        "certificate_card_title": content.get("home_certificate_card_title"),
        "certificate_card_description": content.get("home_certificate_card_description"),
        "contact_card_title": content.get("home_contact_card_title"),
        "contact_card_subtitle": content.get("home_contact_card_subtitle"),

        "solutions": SOLUTIONS[:6],
        "brands": Brand.objects.filter(is_active=True),
        "stats": STATS,
        "certifications": Certification.objects.all(),
        "company": COMPANY,
    }
    return render(request, "core/home.html", context)


def get_about_content():
    return {
        item.key: item.value
        for item in Site_About_Content.objects.all()
    }
def about(request):
    content = get_about_content()
    context = {
        "about_eyebrow": content.get("about_hero_eyebrow"),
        "about_title": content.get("about_hero_title"),
        "about_description": content.get("about_hero_description"),
        "left_column_eyebrow": content.get("about_left_column_eyebrow"),
        "left_column_title": content.get("about_left_column_title"),
        "left_column_description": content.get("about_left_column_description"),
        "right_column_eyebrow": content.get("about_right_column_eyebrow"),
        "right_column_title": content.get("about_right_column_title"),
        "right_column_description": content.get("about_right_column_description"),
        "milestone_eyebrow": content.get("about_milestone_eyebrow"),
        "milestone_title": content.get("about_milestone_title"),
        "milestones": About_Milestone_Content.objects.filter(is_active=True).order_by("order"),
        "last_content_eyebrow": content.get("about_last_content_eyebrow"),
        "last_content_title": content.get("about_last_content_title"),  
        "last_content_description": content.get("about_last_content_description"),

        "stats": STATS,
        "certifications": CERTIFICATIONS,
        "company": COMPANY,
    }
    return render(request, "core/about.html", context)


def get_solutions_content():
    return {
        item.key: item.value
        for item in Site_Solutions_Content.objects.all()
    }
def solutions(request):
    content = get_solutions_content()
    context = {
        "solution_eyebrow": content.get("solution_eyebrow"),
        "solution_title": content.get("solution_title"),
        "solution_description": content.get("solution_description"),
        "solution_bottom_title": content.get("solution_bottom_card_title"),
        "solution_bottom_subtitle": content.get("solution_bottom_card_subtitle"),

        "solutions": Solution.objects.filter(is_active=True).order_by("order"),
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


def get_projects_content():
    return {
        item.key: item.value
        for item in Site_Project_Content.objects.all()
    }
def projects(request):
    content = get_projects_content()
    context = {
        "project_eyebrow": content.get("project_eyebrow"),
        "project_title": content.get("project_title"),
        "project_description": content.get("project_description"),
        "project_bottomleft_eyebrow": content.get("project_bottomleft_eyebrow"),
        "project_bottomleft_title": content.get("project_bottomleft_title"),
        "project_bottomleft_description": content.get("project_bottomleft_description"),
        "project_bottomright_eyebrow": content.get("project_bottomright_eyebrow"),
        "project_bottomright_title": content.get("project_bottomright_title"),
        "project_bottomright_description": content.get("project_bottomright_description"),
        "project_bottom_title": content.get("project_bottom_card_title"),
        "project_bottom_subtitle": content.get("project_bottom_card_subtitle"),

        "project_categories": Project.objects.filter(is_active=True).order_by("order"),
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

def get_terms_content():
    return {
        item.key: item.value
        for item in TermsandConditions_Content.objects.all()
    }
def terms(request):
    content = get_terms_content()
    context = {
        "terms_eyebrow": content.get("terms_eyebrow"),
        "terms_title": content.get("terms_title"),  
        "terms_description": content.get("terms_description"),
        "terms": TermsandConditions.objects.filter(is_active=True).order_by("order"),
        "company": COMPANY,
        }
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
