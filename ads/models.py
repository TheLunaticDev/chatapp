from django.db import models
from django.contrib.auth.models import User


class tag(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class ad(models.Model):
    class categories:
        STRICTLY_PLATONIC = "sp"
        WOMEN_SEEKING_WOMEN = "ww"
        WOMEN_SEEKING_MEN = "wm"
        MEN_SEEKING_WOMEN = "mw"
        MEN_SEEKING_MEN = "mm"
        MISC_ROMANCE = "mr"

    category_mapping = [
        (None, ""),
        (categories.STRICTLY_PLATONIC, "Strictly Platonic ($5)"),
        (categories.WOMEN_SEEKING_WOMEN, "Women seeking Women ($5)"),
        (categories.WOMEN_SEEKING_MEN, "Women seeking Men (Free)"),
        (categories.MEN_SEEKING_WOMEN, "Men seeking Women ($5)"),
        (categories.MEN_SEEKING_MEN, "Men seeking Men ($5)"),
        (categories.MISC_ROMANCE, "Misc Romance ($5)"),
    ]

    class locations:
        ALABAMA = "01"
        ALASKA = "02"
        ARIZONA = "03"
        ARKANSAS = "04"
        CALIFORNIA = "05"
        COLORADO = "06"
        CONNECTICUT = "07"
        DELAWARE = "08"
        FLORIDA = "09"
        GEORGIA = "10"
        HAWAII = "11"
        IDAHO = "12"
        ILLINOIS = "13"
        INDIANA = "14"
        IOWA = "15"
        KANSAS = "16"
        KENTUCKY = "17"
        LOUISIANA = "18"
        MAINE = "19"
        MARYLAND = "20"
        MASSACHUSETTS = "21"
        MICHIGAN = "22"
        MINNESOTA = "23"
        MISSISSIPPI = "24"
        MISSOURI = "25"
        MONTANA = "26"
        NEBRASKA = "27"
        NEVADA = "28"
        NEW_HAMPSHIRE = "29"
        NEW_JERSEY = "30"
        NEW_MEXICO = "31"
        NEW_YORK = "32"
        NORTH_CAROLINA = "33"
        NORTH_DAKOTA = "34"
        OHIO = "35"
        OKLAHOMA = "36"
        OREGON = "37"
        PENNSYLVANIA = "38"
        RHODE_ISLAND = "39"
        SOUTH_CAROLINA = "40"
        SOUTH_DAKOTA = "41"
        TENNESSEE = "42"
        TEXAS = "43"
        UTAH = "44"
        VERMONT = "45"
        VIRGINIA = "46"
        WASHINGTON = "47"
        WEST_VIRGINIA = "48"
        WISCONSIN = "49"
        WYOMING = "50"
        ONTARIO = "51"
        QUEBEC = "52"
        NOVA_SCOTIA = "53"
        NEW_BRUNSWICK = "54"
        MANITOBA = "55"
        BRITISH_COLUMBIA = "56"
        PRINCE_EDWARD_ISLAND = "57"
        SASKATCHEWAN = "58"
        ALBERTA = "59"
        NEWFOUNDLAND_AND_LABRADOR = "60"
        UNITED_KINGDOM = "61"
        BRAZIL = "62"
        FRANCE = "63"
        AUSTRALIA = "64"
        GERMANY = "65"
        NETHERLANDS = "66"
        MEXICO = "67"
        SPAIN = "68"
        ARGENTINA = "69"
        BELGIUM = "70"
        ITALY = "71"
        IRELAND = "72"
        NORWAY = "73"
        DENMARK = "74"
        FINLAND = "75"
        NEW_ZEALAND = "76"
        INDIA = "77"
        GUYANA = "78"
        CHINA = "79"
        SWITZERLAND = "80"
        PHILIPPINES = "81"
        VIETNAM = "82"
        INDONESIA = "83"
        YUKON = "84"
        NORTHWEST_TERRITORIES = "85"
        NUNUVUT = "86"
        PORTUGAL = "87"

    location_mapping = [
        (None, ""),
        (locations.ALABAMA, "USA-Alabama"),
        (locations.ALASKA, "USA-Alaska"),
        (locations.ARIZONA, "USA-Arizona"),
        (locations.ARKANSAS, "USA-Arkansas"),
        (locations.CALIFORNIA, "USA-California"),
        (locations.COLORADO, "USA-Colorado"),
        (locations.CONNECTICUT, "USA-Connecticut"),
        (locations.DELAWARE, "USA-Delaware"),
        (locations.FLORIDA, "USA-Florida"),
        (locations.GEORGIA, "USA-Georgia"),
        (locations.HAWAII, "USA-Hawaii"),
        (locations.IDAHO, "USA-Idaho"),
        (locations.ILLINOIS, "USA-Illinois"),
        (locations.INDIANA, "USA-Indiana"),
        (locations.IOWA, "USA-Iowa"),
        (locations.KANSAS, "USA-Kansas"),
        (locations.KENTUCKY, "USA-Kentucky"),
        (locations.LOUISIANA, "USA-Louisiana"),
        (locations.MAINE, "USA-Maine"),
        (locations.MARYLAND, "USA-Maryland"),
        (locations.MASSACHUSETTS, "USA-Massachusetts"),
        (locations.MICHIGAN, "USA-Michigan"),
        (locations.MINNESOTA, "USA-Minnesota"),
        (locations.MISSISSIPPI, "USA-Mississippi"),
        (locations.MISSOURI, "USA-Missouri"),
        (locations.MONTANA, "USA-Montana"),
        (locations.NEBRASKA, "USA-Nebraska"),
        (locations.NEVADA, "USA-Nevada"),
        (locations.NEW_HAMPSHIRE, "USA-New Hampshire"),
        (locations.NEW_JERSEY, "USA-New Jersey"),
        (locations.NEW_MEXICO, "USA-New Mexico"),
        (locations.NEW_YORK, "USA-New York"),
        (locations.NORTH_CAROLINA, "USA-North Carolina"),
        (locations.NORTH_DAKOTA, "USA-North Dakota"),
        (locations.OHIO, "USA-Ohio"),
        (locations.OKLAHOMA, "USA-Oklahoma"),
        (locations.OREGON, "USA-Oregon"),
        (locations.PENNSYLVANIA, "USA-Pennsylvania"),
        (locations.RHODE_ISLAND, "USA-Rhode Island"),
        (locations.SOUTH_CAROLINA, "USA-South Carolina"),
        (locations.SOUTH_DAKOTA, "USA-South Dakota"),
        (locations.TENNESSEE, "USA-Tennessee"),
        (locations.TEXAS, "USA-Texas"),
        (locations.UTAH, "USA-Utah"),
        (locations.VERMONT, "USA-Vermont"),
        (locations.VIRGINIA, "USA-Virginia"),
        (locations.WASHINGTON, "USA-Washington"),
        (locations.WEST_VIRGINIA, "USA-West Virginia"),
        (locations.WISCONSIN, "USA-Wisconsin"),
        (locations.WYOMING, "USA-Wyoming"),
        (locations.ONTARIO, "Canada-Ontario"),
        (locations.QUEBEC, "Canada-Quebec"),
        (locations.NOVA_SCOTIA, "Canada-Nova Scotia"),
        (locations.NEW_BRUNSWICK, "Canada-New Brunswick"),
        (locations.MANITOBA, "Canada-Manitoba"),
        (locations.BRITISH_COLUMBIA, "Canada-British Columbia"),
        (locations.PRINCE_EDWARD_ISLAND, "Canada-Prince Edward Island"),
        (locations.SASKATCHEWAN, "Canada-Saskatchewan"),
        (locations.ALBERTA, "Canada-Alberta"),
        (locations.NEWFOUNDLAND_AND_LABRADOR, "Canada-Newfoundland and Labrador"),
        (locations.YUKON, "Canada-Yukon"),
        (locations.NORTHWEST_TERRITORIES, "Canada-Northwest Territories"),
        (locations.NUNUVUT, "Canada-Nunuvut"),
        (locations.UNITED_KINGDOM, "United Kingdom"),
        (locations.BRAZIL, "Brazil"),
        (locations.FRANCE, "France"),
        (locations.AUSTRALIA, "Australia"),
        (locations.GERMANY, "Germany"),
        (locations.NETHERLANDS, "Netherlands"),
        (locations.MEXICO, "Mexico"),
        (locations.SPAIN, "Spain"),
        (locations.ARGENTINA, "Argentina"),
        (locations.BELGIUM, "Belgium"),
        (locations.ITALY, "Italy"),
        (locations.IRELAND, "Ireland"),
        (locations.NORWAY, "Norway"),
        (locations.DENMARK, "Denmark"),
        (locations.FINLAND, "Finland"),
        (locations.NEW_ZEALAND, "New Zealand"),
        (locations.INDIA, "India"),
        (locations.GUYANA, "Guyana"),
        (locations.CHINA, "China"),
        (locations.SWITZERLAND, "Switzerland"),
        (locations.PHILIPPINES, "Philippines"),
        (locations.VIETNAM, "Vietnam"),
        (locations.INDONESIA, "Indonesia"),
        (locations.PORTUGAL, "Portugal"),
    ]

    title = models.CharField(max_length=255)
    description = models.CharField(max_length=2000)
    category = models.CharField(max_length=2, choices=category_mapping)
    location = models.CharField(
        max_length=2,
        choices=location_mapping,
    )
    tags = models.ManyToManyField("ads.tag", blank=True)
    poster = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    flags = models.ManyToManyField(User, related_name="flagged_ads", blank=True)
    is_active = models.BooleanField(default=True)
    is_paid = models.BooleanField(default=False)

    def flag_count(self):
        return self.flags.count()

    def check_flags(self, flag_threshold=5):
        if self.flag_count() >= flag_threshold:
            self.is_active = False
            self.save()

    def __str__(self):
        return self.title


class Payment(models.Model):
    linked_ad = models.OneToOneField(ad, on_delete=models.CASCADE)
    payment_status = models.CharField(max_length=20, default="pending")
    invoice_id = models.CharField(max_length=100, blank=True, null=True)
