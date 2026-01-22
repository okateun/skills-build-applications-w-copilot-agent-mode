from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models
from octofit_tracker import models as app_models

from django.db import connection

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()
        # Clear all collections
        User.objects.all().delete()
        app_models.Team.objects.all().delete()
        app_models.Activity.objects.all().delete()
        app_models.Leaderboard.objects.all().delete()
        app_models.Workout.objects.all().delete()

        # Create Teams
        marvel = app_models.Team.objects.create(name='Marvel')
        dc = app_models.Team.objects.create(name='DC')

        # Create Users
        tony = User.objects.create_user(username='tony', email='tony@stark.com', password='ironman', team=marvel)
        steve = User.objects.create_user(username='steve', email='steve@rogers.com', password='captain', team=marvel)
        bruce = User.objects.create_user(username='bruce', email='bruce@wayne.com', password='batman', team=dc)
        clark = User.objects.create_user(username='clark', email='clark@kent.com', password='superman', team=dc)

        # Create Activities
        app_models.Activity.objects.create(user=tony, type='run', duration=30, calories=300)
        app_models.Activity.objects.create(user=steve, type='cycle', duration=45, calories=400)
        app_models.Activity.objects.create(user=bruce, type='swim', duration=60, calories=500)
        app_models.Activity.objects.create(user=clark, type='run', duration=50, calories=450)

        # Create Workouts
        app_models.Workout.objects.create(name='Morning Cardio', description='Cardio for all heroes', duration=40)
        app_models.Workout.objects.create(name='Strength Training', description='Strength for all heroes', duration=60)

        # Create Leaderboard
        app_models.Leaderboard.objects.create(team=marvel, points=700)
        app_models.Leaderboard.objects.create(team=dc, points=950)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
