from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from .models import Player

class PlayerTests(TestCase):
    def setUp(self):
    
        self.client = APIClient()
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        self.player = Player.objects.create(name="Messi", club="PSG", position="Forward")

    
    def test_like_player(self):
        response = self.client.post(f"/api/players/{self.player.id}/like/")
        self.assertEqual(response.status_code, 200)
        self.player.refresh_from_db()
        self.assertEqual(self.player.likes, 1)

    
    def test_prevent_double_like(self):
        self.client.post(f"/api/players/{self.player.id}/like/")
        response = self.client.post(f"/api/players/{self.player.id}/like/")
        self.assertEqual(response.status_code, 400)
        self.assertIn("error", response.data)

    
    def test_overall_ranking(self):
        Player.objects.create(name="Ronaldo", club="Al Nassr", position="Forward", likes=5)
        Player.objects.create(name="Mbappe", club="PSG", position="Forward", likes=10)
        response = self.client.get("/api/rankings/overall/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['results'][0]["name"], "Mbappe")

    def test_position_ranking_filter(self):
        Player.objects.create(name="Buffon", club="Juventus", position="Goalkeeper", likes=7)
        response = self.client.get("/api/rankings/position/?position=Goalkeeper")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Goalkeeper", response.data)
        self.assertEqual(response.data["Goalkeeper"][0]["name"], "Buffon")


    def test_most_liked_per_club(self):
        Player.objects.create(name="Xavi", club="Barcelona", position="Midfielder", likes=12)
        Player.objects.create(name="Iniesta", club="Barcelona", position="Midfielder", likes=15)
        response = self.client.get("/api/rankings/club/top/?club=Barcelona")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["Barcelona"][0]["name"], "Iniesta")

    
    def test_top_players_view(self):
        Player.objects.create(name="Neymar", club="PSG", position="Forward", likes=30)
        Player.objects.create(name="Suarez", club="Atletico", position="Forward", likes=25)
        response = self.client.get("/api/rankings/top/?top=1")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]["name"], "Neymar")


    def test_club_ranking_all(self):
        Player.objects.create(name="Chiellini", club="Juventus", position="Defender", likes=8)
        response = self.client.get("/api/rankings/club/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Juventus", response.data)
