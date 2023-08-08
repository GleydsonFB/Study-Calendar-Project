from database import *

aux_bd = Database()


class Study_calc:
    def __init__(self, cat_ref, studies, month, year):
        self.cat = cat_ref
        self.studies = studies
        self.month = month
        self.year = year

    def cal_study(self):
        aux_bd.connect()
        search = aux_bd.select_three_search('calendar', 'time', self.cat, self.month, self.year, 'cat_ref', 'month', 'year')
        eff = aux_bd.select_three_search('effectivity', 'efficiency', self.cat, self.month, self.year, 'cat_ref', 'month', 'year')
        aux_bd.disconnect()
        if len(eff) == 0:
            if len(search) != 0:
                eff = 100
                answer = (search[0][0] * eff) / 100
            else:
                answer = ''
        else:
            answer = (search[0][0] * eff[0][0]) / 100
        return answer

