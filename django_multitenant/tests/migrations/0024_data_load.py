# Generated by Django 4.1.5 on 2023-02-20 07:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("tests", "0023_auto_20200412_0603"),
    ]

    def forwards_func(apps, schema_editor):
        db_alias = schema_editor.connection.alias
        Country = apps.get_model("tests", "Country")

        Country.objects.using(db_alias).bulk_create(
            [
                Country(name="USA"),
                Country(name="France"),
                Country(name="Turkiye"),
            ]
        )

        Account = apps.get_model("tests", "Account")
        Account.objects.using(db_alias).bulk_create(
            [
                Account(
                    name="johndoe",
                    domain="domain",
                    subdomain="subdomain",
                    country=Country.objects.get(name="USA"),
                ),
                Account(
                    name="jilldoe",
                    domain="domain",
                    subdomain="subdomain",
                    country=Country.objects.get(name="USA"),
                ),
                Account(
                    name="milldoe",
                    domain="domain",
                    subdomain="subdomain",
                    country=Country.objects.get(name="USA"),
                ),
                Account(
                    name="alidoe",
                    domain="domain",
                    subdomain="subdomain",
                    country=Country.objects.get(name="Turkiye"),
                ),
                Account(
                    name="velidoe",
                    domain="domain",
                    subdomain="subdomain",
                    country=Country.objects.get(name="Turkiye"),
                ),
                Account(
                    name="pierredoe",
                    domain="domain",
                    subdomain="subdomain",
                    country=Country.objects.get(name="France"),
                ),
            ]
        )
        country = Country.objects.get(name="USA")
        accounts = Account.objects.all()

        assert len(accounts) == 6
        assert country is not None

    operations = [migrations.RunPython(forwards_func)]
