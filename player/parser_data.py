# import sqlite3
# import requests
# import datetime
# from bs4 import BeautifulSoup
# from .models import Players


# def get_player_data():
#     HEADERS = {
#         'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'}

#     go_that_url = requests.get(
#         'https://www.championat.com/football/_england/tournament/5467/teams/242829/players/', headers=HEADERS)
#     parse_that_page = BeautifulSoup(go_that_url.text, 'html.parser')
#     # get_nums = parse_that_page.find_all(
#     #     'td', class_="table-responsive__row-item _order_3 _order_mobile_2 _desktop _num-right")
#     # get_names = parse_that_page.find_all(
#     #     'td', class_="table-responsive__row-item _order_1 _left-padding-cell _w-45 _nowrap")
#     # get_positions = parse_that_page.find_all(
#     #     'td', class_="table-responsive__row-item _order_2 _order_mobile_3 _tablet")
#     get_birthdays = parse_that_page.find_all(
#         'td', attrs={"class": "table-responsive__row-item _order_4 _desktop"})
#     # get_height = parse_that_page.find_all(
#     #     'td', attrs={"class": "table-responsive__row-item _order_5 _desktop"})
#     # get_weight = parse_that_page.find_all(
#     #     'td', attrs={"class": "table-responsive__row-item _order_6 _desktop"})
#     # get_price = parse_that_page.find_all(
#     #     'td', attrs={"class": "table-responsive__row-item _order_7 _desktop"})
#     # nums = [i.text.strip() for i in get_nums]
#     # names = [i.text.strip() for i in get_names]
#     # pos = [c.text.strip() for c in get_positions]
#     birth = [d.text.strip() for d in get_birthdays] 
#     # height = [e.text.strip() for e in get_height]
#     # weight = [f.text.strip() for f in get_weight]
#     # price = [g.text.strip() for g in get_price]
#     count = 0
#     year = datetime.date.today().year 
#     for a in range(0, 35):
#         count += 1
#         date = "-".join(birth[count].split(".")[::-1])
#         # heights = height[count] if height[count] else 170
#         # weights = weight[count] if weight[count] else 75
#         # prices= price[count] if price[count] else 100000
#         # print(height)
#         year_pl = date.split('-')
#         all_pls =  Players.objects.all()
#         for player in all_pls:
#             player.age = year - int(year_pl[count[0]])
#             player.save()
# get_player_data()
        