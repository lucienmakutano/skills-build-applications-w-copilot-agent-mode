from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = "Populate the octofit_db database with test data"

    def handle(self, *args, **kwargs):
        # Force delete existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Populate Users
        users = [
            {"email": "john.doe@example.com", "name": "John Doe"},
            {"email": "jane.smith@example.com", "name": "Jane Smith"},
        ]
        user_instances = [User.objects.create(**user_data) for user_data in users]

        # Populate Teams
        teams = [
            {"name": "Team Alpha", "members": [user_instances[0].email, user_instances[1].email]},
        ]
        for team_data in teams:
            Team.objects.create(**team_data)

        # Populate Activities
        activities = [
            {"user": user_instances[0], "type": "Running", "duration": 30},
            {"user": user_instances[1], "type": "Cycling", "duration": 45},
        ]
        for activity_data in activities:
            Activity.objects.create(**activity_data)

        # Populate Leaderboard
        leaderboard = [
            {"user": user_instances[0], "score": 100},
            {"user": user_instances[1], "score": 80},
        ]
        for leaderboard_data in leaderboard:
            Leaderboard.objects.create(**leaderboard_data)

        # Populate Workouts
        workouts = [
            {"name": "Morning Run", "description": "A quick morning run to start the day."},
            {"name": "Evening Yoga", "description": "Relaxing yoga session in the evening."},
        ]
        for workout_data in workouts:
            Workout.objects.create(**workout_data)

        self.stdout.write(self.style.SUCCESS("Successfully populated the database with test data."))
