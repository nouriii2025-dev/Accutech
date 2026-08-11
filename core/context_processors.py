from .models import Site_Base_Content, Company_Details


def site_base_content(request):

    base_content = {
        item.key: item.value
        for item in Site_Base_Content.objects.all()
    }

    company = {
        item.key: item.value
        for item in Company_Details.objects.all()
    }

    return {
        "base_title": base_content.get("base_title", ""),
        "base_description": base_content.get("base_description", ""),
        "base_bottom_left": base_content.get("base_bottom_left", ""),
        "base_bottom_right": base_content.get("base_bottom_right", ""),
        "company": company,
    }