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

    class locations:
        ALABAMA = "AL"
        ALASKA = "AK"
        ARIZONA = "AZ"
        ARKANSAS = "AR"
        CALIFORNIA = "CA"
        COLORADO = "CO"
        CONNECTICUT = "CT"
        DELAWARE = "DE"
        FLORIDA = "FL"
        GEORGIA = "GA"
        HAWAII = "HI"
        IDAHO = "ID"
        ILLINOIS = "IL"
        INDIANA = "IN"
        IOWA = "IA"
        KANSAS = "KS"
        KENTUCKY = "KY"
        LOUISIANA = "LA"
        MAINE = "ME"
        MARYLAND = "MD"
        MASSACHUSETTS = "MA"
        MICHIGAN = "MI"
        MINNESOTA = "MN"
        MISSISSIPPI = "MS"
        MISSOURI = "MO"
        MONTANA = "MT"
        NEBRASKA = "NE"
        NEVADA = "NV"
        NEW_HAMPSHIRE = "NH"
        NEW_JERSEY = "NJ"
        NEW_MEXICO = "NM"
        NEW_YORK = "NY"
        NORTH_CAROLINA = "NC"
        NORTH_DAKOTA = "ND"
        OHIO = "OH"
        OKLAHOMA = "OK"
        OREGON = "OR"
        PENNSYLVANIA = "PA"
        RHODE_ISLAND = "RI"
        SOUTH_CAROLINA = "SC"
        SOUTH_DAKOTA = "SD"
        TENNESSEE = "TN"
        TEXAS = "TX"
        UTAH = "UT"
        VERMONT = "VT"
        VIRGINIA = "VA"
        WASHINGTON = "WA"
        WEST_VIRGINIA = "WV"
        WISCONSIN = "WI"
        WYOMING = "WY"
        ONTARIO = "ON"
        QUEBEC = "QC"
        NOVA_SCOTIA = "NS"
        NEW_BRUNSWICK = "NB"
        MANITOBA = "MB"
        BRITISH_COLUMBIA = "BC"
        PRINCE_EDWARD_ISLAND = "PE"
        SASKATCHEWAN = "SK"
        ALBERTA = "AB"
        NEWFOUNDLAND_AND_LABRADOR = "NL"

    category_mapping = {
        categories.STRICTLY_PLATONIC: "Strictly Platonic",
        categories.WOMEN_SEEKING_WOMEN: "Women seeking Women",
        categories.WOMEN_SEEKING_MEN: "Women seeking Men",
        categories.MEN_SEEKING_WOMEN: "Men seeking Women",
        categories.MEN_SEEKING_MEN: "Men seeking Men",
    }

    location_mapping = {
        locations.ALABAMA: "Alabama",
        locations.ALASKA: "Alaska",
        locations.ARIZONA: "Arizona",
        locations.ARKANSAS: "Arkansas",
        locations.CALIFORNIA: "California",
        locations.COLORADO: "Colorado",
        locations.CONNECTICUT: "Connecticut",
        locations.DELAWARE: "Delaware",
        locations.FLORIDA: "Florida",
        locations.GEORGIA: "Georgia",
        locations.HAWAII: "Hawaii",
        locations.IDAHO: "Idaho",
        locations.ILLINOIS: "Illinois",
        locations.INDIANA: "Indian",
        locations.IOWA: "Iowa",
        locations.KANSAS: "Kansas",
        locations.KENTUCKY: "Kentucky",
        locations.LOUISIANA: "Louisiana",
        locations.MAINE: "Maine",
        locations.MARYLAND: "Maryland",
        locations.MASSACHUSETTS: "Massachusetts",
        locations.MICHIGAN: "Michigan",
        locations.MINNESOTA: "Minnesota",
        locations.MISSISSIPPI: "Mississippi",
        locations.MISSOURI: "Missouri",
        locations.MONTANA: "Montana",
        locations.NEBRASKA: "Nebraska",
        locations.NEVADA: "Nevada",
        locations.NEW_HAMPSHIRE: "New Hampshire",
        locations.NEW_JERSEY: "New Jersey",
        locations.NEW_MEXICO: "New Mexico",
        locations.NEW_YORK: "New York",
        locations.NORTH_CAROLINA: "North Carolina",
        locations.NORTH_DAKOTA: "North Dakota",
        locations.OHIO: "Ohio",
        locations.OKLAHOMA: "Oklahoma",
        locations.OREGON: "Oregon",
        locations.PENNSYLVANIA: "Pennsylvania",
        locations.RHODE_ISLAND: "Rhode Island",
        locations.SOUTH_CAROLINA: "South Carolina",
        locations.SOUTH_DAKOTA: "South Dakota",
        locations.TENNESSEE: "Tennessee",
        locations.TEXAS: "Texas",
        locations.UTAH: "Utah",
        locations.VERMONT: "Vermont",
        locations.VIRGINIA: "Virginia",
        locations.WASHINGTON: "Washington",
        locations.WEST_VIRGINIA: "West Virginia",
        locations.WISCONSIN: "Wisconsin",
        locations.WYOMING: "Wyoming",
        locations.ONTARIO: "Ontario",
        locations.QUEBEC: "Quebec",
        locations.NOVA_SCOTIA: "Nova Scotia",
        locations.NEW_BRUNSWICK: "New Brunswick",
        locations.MANITOBA: "Manitoba",
        locations.BRITISH_COLUMBIA: "British Columbia",
        locations.PRINCE_EDWARD_ISLAND: "Prince Edward Island",
        locations.SASKATCHEWAN: "Saskatchewan",
        locations.ALBERTA: "Alberta",
        locations.NEWFOUNDLAND_AND_LABRADOR: "Newfoundland and Labrador",
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
    favorites = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
