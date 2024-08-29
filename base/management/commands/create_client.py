import pickle
from django.core.management.base import BaseCommand
from btcpay import BTCPayClient
from base.models import BTCPayClientModel


class Command(BaseCommand):
    help = "Create a BTCPay client and store it in the database"

    def add_arguments(self, parser):
        parser.add_argument("--host", type=str, help="BTCPay server hostname")
        parser.add_argument("--code", type=str, help="Pairing code for BTCPay")

    def handle(self, *args, **options):
        host = options["host"] or input(
            "Enter the BTCPay server hostname (e.g., https://btcpay.example.com): "
        )
        pairing_code = options["code"] or input(
            "Enter the BTCPay server pairing code: "
        )

        try:
            client = BTCPayClient.create_client(host=host, code=pairing_code)
            self.stdout.write(self.style.SUCCESS("BTCPay client created successfully."))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"Failed to create BTCPay client: {e}"))
            return

        client_pickled = pickle.dumps(client)

        btcpay_client_model = BTCPayClientModel(client_data=client_pickled)
        btcpay_client_model.save()

        self.stdout.write(
            self.style.SUCCESS("BTCPay client saved to the database successfully.")
        )
