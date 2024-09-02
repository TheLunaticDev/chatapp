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

    category_mapping = {
        categories.STRICTLY_PLATONIC: "Strictly Platonic",
        categories.WOMEN_SEEKING_WOMEN: "Women seeking Women",
        categories.WOMEN_SEEKING_MEN: "Women seeking Men",
        categories.MEN_SEEKING_WOMEN: "Men seeking Women",
        categories.MEN_SEEKING_MEN: "Men seeking Men",
    }

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

    location_mapping = {
        locations.ALABAMA: "United States - Alabama",
        locations.ALASKA: "United States - Alaska",
        locations.ARIZONA: "United States - Arizona",
        locations.ARKANSAS: "United States - Arkansas",
        locations.CALIFORNIA: "United States - California",
        locations.COLORADO: "United States - Colorado",
        locations.CONNECTICUT: "United States - Connecticut",
        locations.DELAWARE: "United States - Delaware",
        locations.FLORIDA: "United States - Florida",
        locations.GEORGIA: "United States - Georgia",
        locations.HAWAII: "United States - Hawaii",
        locations.IDAHO: "United States - Idaho",
        locations.ILLINOIS: "United States - Illinois",
        locations.INDIANA: "United States - Indiana",
        locations.IOWA: "United States - Iowa",
        locations.KANSAS: "United States - Kansas",
        locations.KENTUCKY: "United States - Kentucky",
        locations.LOUISIANA: "United States - Louisiana",
        locations.MAINE: "United States - Maine",
        locations.MARYLAND: "United States - Maryland",
        locations.MASSACHUSETTS: "United States - Massachusetts",
        locations.MICHIGAN: "United States - Michigan",
        locations.MINNESOTA: "United States - Minnesota",
        locations.MISSISSIPPI: "United States - Mississippi",
        locations.MISSOURI: "United States - Missouri",
        locations.MONTANA: "United States - Montana",
        locations.NEBRASKA: "United States - Nebraska",
        locations.NEVADA: "United States - Nevada",
        locations.NEW_HAMPSHIRE: "United States - New Hampshire",
        locations.NEW_JERSEY: "United States - New Jersey",
        locations.NEW_MEXICO: "United States - New Mexico",
        locations.NEW_YORK: "United States - New York",
        locations.NORTH_CAROLINA: "United States - North Carolina",
        locations.NORTH_DAKOTA: "United States - North Dakota",
        locations.OHIO: "United States - Ohio",
        locations.OKLAHOMA: "United States - Oklahoma",
        locations.OREGON: "United States - Oregon",
        locations.PENNSYLVANIA: "United States - Pennsylvania",
        locations.RHODE_ISLAND: "United States - Rhode Island",
        locations.SOUTH_CAROLINA: "United States - South Carolina",
        locations.SOUTH_DAKOTA: "United States - South Dakota",
        locations.TENNESSEE: "United States - Tennessee",
        locations.TEXAS: "United States - Texas",
        locations.UTAH: "United States - Utah",
        locations.VERMONT: "United States - Vermont",
        locations.VIRGINIA: "United States - Virginia",
        locations.WASHINGTON: "United States - Washington",
        locations.WEST_VIRGINIA: "United States - West Virginia",
        locations.WISCONSIN: "United States - Wisconsin",
        locations.WYOMING: "United States - Wyoming",
        locations.ONTARIO: "Canada - Ontario",
        locations.QUEBEC: "Canada - Quebec",
        locations.NOVA_SCOTIA: "Canada - Nova Scotia",
        locations.NEW_BRUNSWICK: "Canada - New Brunswick",
        locations.MANITOBA: "Canada - Manitoba",
        locations.BRITISH_COLUMBIA: "Canada - British Columbia",
        locations.PRINCE_EDWARD_ISLAND: "Canada - Prince Edward Island",
        locations.SASKATCHEWAN: "Canada - Saskatchewan",
        locations.ALBERTA: "Canada - Alberta",
        locations.NEWFOUNDLAND_AND_LABRADOR: "Canada - Newfoundland and Labrador",
        locations.UNITED_KINGDOM: "United Kingdom",
        locations.BRAZIL: "Brazil",
        locations.FRANCE: "France",
        locations.AUSTRALIA: "Australia",
        locations.GERMANY: "Germany",
        locations.NETHERLANDS: "Netherlands",
        locations.MEXICO: "Mexico",
        locations.SPAIN: "Spain",
        locations.ARGENTINA: "Argentina",
        locations.BELGIUM: "Belgium",
        locations.ITALY: "Italy",
        locations.IRELAND: "Ireland",
        locations.NORWAY: "Norway",
        locations.DENMARK: "Denmark",
        locations.FINLAND: "Finland",
        locations.NEW_ZEALAND: "New Zealand",
        locations.INDIA: "India",
        locations.GUYANA: "Guyana",
        locations.CHINA: "China",
        locations.SWITZERLAND: "Switzerland",
        locations.PHILIPPINES: "Philippines",
        locations.VIETNAM: "Vietnam",
        locations.INDONESIA: "Indonesia",
    }

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
