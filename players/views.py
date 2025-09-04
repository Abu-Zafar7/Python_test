from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Player, Like
from .serializers import PlayerSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, status
from django.db.models import Max
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class PlayerListView(generics.ListAPIView):

    serializer_class = PlayerSerializer

    def get_queryset(self):
        queryset = Player.objects.all()
        club = self.request.query_params.get("club")
        position = self.request.query_params.get("position")

        if club:
            queryset = queryset.filter(club__iexact=club)

        if position:
            queryset = queryset.filter(position__iexact=position)    


        return queryset

class LikePlayerView(APIView):
    
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        try:
            player = Player.objects.get(pk=pk)
        except Player.DoesNotExist:
            return Response({"error": "Player not found"}, status=404)

        if Like.objects.filter(user=request.user, player=player).exists():
            return Response({"error": "You already liked this player"}, status=400)

        Like.objects.create(user=request.user, player=player)
        player.likes += 1
        player.save()

        return Response(PlayerSerializer(player).data)    

class OverallRankingView(generics.ListAPIView):
    serializer_class = PlayerSerializer

    def get_queryset(self):
        return Player.objects.all().order_by("-likes")
    

class PositionRankingView(APIView):

    def get(self,request):
        pos_param = request.query_params.get("position")

        if pos_param:
            players = Player.objects.filter(position__iexact=pos_param).order_by("-likes")
            return Response({pos_param: PlayerSerializer(players, many=True).data})    
        
        positions = {}

        for pos_name, _ in Player.CHOICES:
            players = Player.objects.filter(position__iexact = pos_name).order_by("-likes")
            positions[pos_name] = PlayerSerializer(players, many=True).data

        return Response(positions)


class ClubRankingView(APIView):
    def get(self, request):
        club_param = request.query_params.get("club")

        if club_param:
            players = Player.objects.filter(club__iexact=club_param).order_by("-likes")
            return Response({club_param: PlayerSerializer(players, many=True).data})  

        clubs = Player.objects.values_list("club", flat=True).distinct()  
        result = {}

        for club in clubs:
            players = Player.objects.filter(club__iexact=club).order_by("-likes")
            result[club] = PlayerSerializer(players, many=True).data

        return Response(result)
    

class TopPlayersView(generics.ListAPIView):
    serializer_class = PlayerSerializer

    def get_queryset(self):
        top_n = self.request.query_params.get("top")
        queryset = Player.objects.all().order_by("-likes")
        if top_n and top_n.isdigit():
            return queryset[:int(top_n)]
        return queryset
    
class MostLikedPerClubView(APIView):
    def get(self, request):
        club_param = request.query_params.get("club")

        if club_param:
            max_likes = Player.objects.filter(club__iexact=club_param).aggregate(Max("likes"))["likes__max"]
            if max_likes is None:
                return Response({club_param: []})
            top_players = Player.objects.filter(club__iexact=club_param, likes=max_likes)
            return Response({club_param: PlayerSerializer(top_players, many=True).data})

        result = {}
        clubs = Player.objects.values_list("club", flat=True).distinct()
        for club in clubs:
            max_likes = Player.objects.filter(club__iexact=club).aggregate(Max("likes"))["likes__max"]

            if max_likes is None:
                result[club] = []
                continue

            top_players = Player.objects.filter(club__iexact=club, likes=max_likes)
            result[club] = PlayerSerializer(top_players, many=True).data

        return Response(result)


class RegisterUserView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        if not username or not password:
            return Response({'error': 'Username and password required'}, status=status.HTTP_400_BAD_REQUEST)
        
        if User.objects.filter(username=username).exists():
            return Response({'error': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)
        
        user = User.objects.create_user(username=username, password=password)
        token = Token.objects.create(user=user)
        return Response({'username': user.username, 'token': token.key})