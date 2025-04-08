#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from pymongo import MongoClient

def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "octofit_tracker.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

def initialize_octofit_db():
    """Initialize the octofit_db MongoDB database."""
    client = MongoClient("mongodb://localhost:27017/")  # Adjust connection string if needed
    db = client["octofit_db"]

    # Create collections
    db.create_collection("users", capped=False)
    db.create_collection("teams", capped=False)
    db.create_collection("activity", capped=False)
    db.create_collection("leaderboard", capped=False)
    db.create_collection("workouts", capped=False)

    # Ensure unique index for users collection
    db.users.create_index([("email", 1)], unique=True)

    # List collections to verify
    collections = db.list_collection_names()
    print("Collections in octofit_db:", collections)

if __name__ == "__main__":
    main()
    if "initdb" in sys.argv:
        initialize_octofit_db()
