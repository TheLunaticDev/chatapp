from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import ad


def show_ads_view(request, page_no=1):
    ad_list = ad.objects.filter(is_active=True).order_by("-created_on")
    paginator = Paginator(ad_list, 50)

    try:
        ads = paginator.page(page_no)
    except PageNotAnInteger:
        ads = paginator.page(1)
    except EmptyPage:
        ads = paginator.page(paginator.num_pages)

    context = {
        "ad_list": ads,
    }
    return render(request, "ads/show_ads.html", context)


@login_required
def create_ads_view(request):
    context = {}
    return render(request, "ads/create_ads.html", context)


def ads_info_view(request, id):
    try:
        requested_ad = ad.objects.get(id=id)
    except ad.DoesNotExist:
        requested_ad = None
    except ad.MultipleObjectsReturned:
        requested_ad = None

    if requested_ad is not None:
        ad_tags = []
        ad_tags_available = requested_ad.tags.all()

        for tags in ad_tags_available:
            ad_tags.append(tags.name)

        requested_ad = {
            "id": requested_ad.id,
            "title": requested_ad.title,
            "description": requested_ad.description,
            "category": requested_ad.get_category_display(),
            "location": requested_ad.get_location_display(),
            "poster": requested_ad.poster.username,
            "created_on": requested_ad.created_on,
            "last_updated": requested_ad.updated_on,
            "favorite": requested_ad.favorites,
            "tags": ad_tags,
        }
    else:
        requested_ad = None

    context = {
        "ad": requested_ad,
    }

    return render(request, "ads/ads_info.html", context)


@login_required
def edit_ads_view(request):
    context = {}
    return render(request, "ads/edit_ads.html", context)
