# # Метод для присвоения приза игроку

# from django.utils import timezone
# from django.core.exceptions import ObjectDoesNotExist

# class Player(models.Model):
#     player_id = models.CharField(max_length=100)

#     def assign_prize(self, level):
#         try:
#             player_level = PlayerLevel.objects.get(player=self, level=level)
#             if player_level.is_completed:
                
#                 level_prize = LevelPrize.objects.get(level=level)
                
#                 print(f"Игрок {self.player_id} получил приз: {level_prize.prize.title}")
#                 return level_prize.prize
#             else:
#                 print(f"Уровень {level.title} не завершен для игрока {self.player_id}.")
#                 return None
#         except ObjectDoesNotExist:
#             print("Игрок или уровень не найдены.")
#             return None

# # Метод для выгрузки данных в CSV

# import csv
# from django.http import HttpResponse

# def export_player_levels_to_csv():
    
#     response = HttpResponse(content_type='text/csv')
#     response['Content-Disposition'] = 'attachment; filename="player_levels.csv"'

#     writer = csv.writer(response)
#     writer.writerow(['Player ID', 'Level Title', 'Is Completed', 'Prize Title'])

    
#     player_levels = PlayerLevel.objects.select_related('player', 'level', 'level__levelprize__prize').all()

#     for player_level in player_levels:
#         prize_title = player_level.level.levelprize.prize.title if player_level.level.levelprize else 'Нет приза'
#         writer.writerow([
#             player_level.player.player_id,
#             player_level.level.title,
#             player_level.is_completed,
#             prize_title
#         ])

#     return response