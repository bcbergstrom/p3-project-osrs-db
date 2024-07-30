import requests
from bs4 import BeautifulSoup
import re
from mmm_obj import MMM_Obj

class ScrapeMMM:
    def __init__(self):
        URL = "https://oldschool.runescape.wiki/w/Money_making_guide"
        self.page = requests.get(URL)
        self.soup = BeautifulSoup(self.page.content, "html.parser")
        
    def get_data(self):
        
        table = self.soup.find("tbody")
        for each in table.find_all("tr"):
            temp_method = each.find('a')
            continuer = False
            temp_coins = each.find('span', {"class":"coins coins-pos"})
            temp_list_of_skills = each.find_all('span', {'class': "scp"})
            if temp_method == None and temp_coins == None:
                continue
            else:
                temp_method = temp_method.get('title')
                temp_coins = float(temp_coins.text.replace(",",""))
                for skill in temp_list_of_skills:
                    if skill == None or skill == []:
                        continuer = True
                        continue
                    else: 
                        print(skill)
                if continuer:
                    continue
            # temp_coins = each.find('span', class_="coins coins-pos")
        # results = self.soup.find_all("a")
        # for each in results:
        #     q = each.get('title')
        #     if q != None and "Money making guide/" in q:
                
if __name__ == "__main__":
    q = ScrapeMMM()
    q.get_data()