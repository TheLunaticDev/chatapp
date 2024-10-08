# Generated by Django 5.1 on 2024-09-04 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ads", "0009_alter_ad_location"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ad",
            name="category",
            field=models.CharField(
                choices=[
                    (None, ""),
                    ("sp", "Strictly Platonic"),
                    ("ww", "Women seeking Women"),
                    ("wm", "Women seeking Men"),
                    ("mw", "Men seeking Women"),
                    ("mm", "Men seeking Men"),
                    ("mr", "Misc Romance"),
                ],
                max_length=2,
            ),
        ),
        migrations.AlterField(
            model_name="ad",
            name="location",
            field=models.CharField(
                choices=[
                    (None, ""),
                    ("01", "USA-Alabama"),
                    ("02", "USA-Alaska"),
                    ("03", "USA-Arizona"),
                    ("04", "USA-Arkansas"),
                    ("05", "USA-California"),
                    ("06", "USA-Colorado"),
                    ("07", "USA-Connecticut"),
                    ("08", "USA-Delaware"),
                    ("09", "USA-Florida"),
                    ("10", "USA-Georgia"),
                    ("11", "USA-Hawaii"),
                    ("12", "USA-Idaho"),
                    ("13", "USA-Illinois"),
                    ("14", "USA-Indiana"),
                    ("15", "USA-Iowa"),
                    ("16", "USA-Kansas"),
                    ("17", "USA-Kentucky"),
                    ("18", "USA-Louisiana"),
                    ("19", "USA-Maine"),
                    ("20", "USA-Maryland"),
                    ("21", "USA-Massachusetts"),
                    ("22", "USA-Michigan"),
                    ("23", "USA-Minnesota"),
                    ("24", "USA-Mississippi"),
                    ("25", "USA-Missouri"),
                    ("26", "USA-Montana"),
                    ("27", "USA-Nebraska"),
                    ("28", "USA-Nevada"),
                    ("29", "USA-New Hampshire"),
                    ("30", "USA-New Jersey"),
                    ("31", "USA-New Mexico"),
                    ("32", "USA-New York"),
                    ("33", "USA-North Carolina"),
                    ("34", "USA-North Dakota"),
                    ("35", "USA-Ohio"),
                    ("36", "USA-Oklahoma"),
                    ("37", "USA-Oregon"),
                    ("38", "USA-Pennsylvania"),
                    ("39", "USA-Rhode Island"),
                    ("40", "USA-South Carolina"),
                    ("41", "USA-South Dakota"),
                    ("42", "USA-Tennessee"),
                    ("43", "USA-Texas"),
                    ("44", "USA-Utah"),
                    ("45", "USA-Vermont"),
                    ("46", "USA-Virginia"),
                    ("47", "USA-Washington"),
                    ("48", "USA-West Virginia"),
                    ("49", "USA-Wisconsin"),
                    ("50", "USA-Wyoming"),
                    ("51", "Canada-Ontario"),
                    ("52", "Canada-Quebec"),
                    ("53", "Canada-Nova Scotia"),
                    ("54", "Canada-New Brunswick"),
                    ("55", "Canada-Manitoba"),
                    ("56", "Canada-British Columbia"),
                    ("57", "Canada-Prince Edward Island"),
                    ("58", "Canada-Saskatchewan"),
                    ("59", "Canada-Alberta"),
                    ("60", "Canada-Newfoundland and Labrador"),
                    ("84", "Canada-Yukon"),
                    ("85", "Canada-Northwest Territories"),
                    ("86", "Canada-Nunuvut"),
                    ("61", "United Kingdom"),
                    ("62", "Brazil"),
                    ("63", "France"),
                    ("64", "Australia"),
                    ("65", "Germany"),
                    ("66", "Netherlands"),
                    ("67", "Mexico"),
                    ("68", "Spain"),
                    ("69", "Argentina"),
                    ("70", "Belgium"),
                    ("71", "Italy"),
                    ("72", "Ireland"),
                    ("73", "Norway"),
                    ("74", "Denmark"),
                    ("75", "Finland"),
                    ("76", "New Zealand"),
                    ("77", "India"),
                    ("78", "Guyana"),
                    ("79", "China"),
                    ("80", "Switzerland"),
                    ("81", "Philippines"),
                    ("82", "Vietnam"),
                    ("83", "Indonesia"),
                    ("87", "Portugal"),
                ],
                max_length=2,
            ),
        ),
    ]
