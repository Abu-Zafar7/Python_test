import json
from django.core.management.base import BaseCommand
from players.models import Player

class Command(BaseCommand):
    help = 'Load players from a JSON file into the database'

    def handle(self, *args, **kwargs):

        with open('players.json', 'r') as f:
            players_data = json.load(f)

        for player_data in players_data:
            player, created = Player.objects.get_or_create(
                name=player_data['name'],
                club=player_data['club'],
                position=player_data['position'],
                defaults={'likes': player_data.get('likes', 0)}
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Added player: {player.name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Player already exists: {player.name}'))
        
      