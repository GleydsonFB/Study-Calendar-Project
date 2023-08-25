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
        goal = aux_bd.select_three_search('goal', 'objective', self.cat, self.month, self.year, 'cat_ref', 'month', 'year')
        off = aux_bd.select_two_search('dayOff', 'id_day', self.month, self.year, 'month', 'year')
        aux_bd.disconnect()
        if self.cat == 'Folgas':
            if len(off) == 0:
                answer = 'N/A'
                percentual = 'N/A'
                return answer, percentual
            else:
                answer = 0
                for registry in off:
                    answer += 1
                if goal[0][0] == 0:
                    percentual = '-'
                else:
                    percentual = answer * 100 / goal[0][0]
                    if percentual > 100:
                        percentual = '-'
                return answer, percentual
        elif len(eff) == 0:
            if len(search) != 0:
                eff = 100
                answer, answer_cal = 0, 0
                for data in range(0, len(search)):
                    answer += ((search[data][0] * eff) / 100) / 60
                    answer_cal += search[data][0] * eff / 100
                percentual = answer_cal * 100 / goal[0][0]
            else:
                answer = 'N/A'
                percentual = 'N/A'
                return answer, percentual
        else:
            if len(search) != 0:
                answer, answer_cal = 0, 0
                for data in range(0, len(search)):
                    answer += ((search[data][0] * eff[0][0]) / 100) / 60
                    answer_cal += search[data][0] * eff / 100
                percentual = answer_cal * 100 / goal[0][0]
            else:
                answer = 'N/A'
                percentual = 'N/A'
                return answer, percentual
        return round(answer, 2), round(percentual, 2)

    def cal_goal(self, id_week):
        aux_bd.connect()
        total_study_day = aux_bd.show_week_scale(id_week[0])
        count = 0
        for day in range(0, len(total_study_day[0])):
            if total_study_day[0][day] == 1:
                count += 1
            else:
                pass
        if self.month == 'fevereiro':
            if (self.year % 4 == 0 and self.year % 100 != 0) or self.year % 4 == 0:
                count_fev = count * 3.857
                return round(count_fev, 0)
            else:
                count_fev = count * 3.714
                return round(count_fev, 0)
        else:
            return count * 4


