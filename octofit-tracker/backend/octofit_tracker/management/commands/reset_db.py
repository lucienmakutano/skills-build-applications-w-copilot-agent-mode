from django.core.management.base import BaseCommand
from pymongo import MongoClient

class Command(BaseCommand):
    help = "Reset the octofit_db MongoDB database"

    def handle(self, *args, **kwargs):
        # Connect to MongoDB
        client = MongoClient("mongodb://localhost:27017/")  # Adjust connection string if needed
        db_name = "octofit_db"

        # Drop the database
        client.drop_database(db_name)
        self.stdout.write(self.style.SUCCESS(f"Database '{db_name}' has been deleted."))

        # Recreate the database by running the populate_db command
        from django.core.management import call_command
        call_command("populate_db")
        self.stdout.write(self.style.SUCCESS(f"Database '{db_name}' has been recreated and populated with test data."))
