import sqlite3


class Database:
    def __init__(self):
        self.con = None
        self.mouse = None

    def connect(self):
        self.con = sqlite3.connect('items_sc.bd')
        self.mouse = self.con.cursor()

    def disconnect(self):
        self.con.close()

    def table_create(self):
        self.mouse.execute('CREATE TABLE IF NOT EXISTS category('
                           'id_cat integer NOT NULL PRIMARY KEY AUTOINCREMENT,'
                           'name TEXT UNIQUE NOT NULL,'
                           'color VARCHAR(255) NOT NULL);')

        self.mouse.execute('CREATE TABLE IF NOT EXISTS effectivity('
                           'id_eff integer NOT NULL PRIMARY KEY AUTOINCREMENT,'
                           'efficiency FLOAT NOT NULL,'
                           'cat_ref TEXT NOT NULL,'
                           'month TEXT NOT NULL,'
                           'year INT NOT NULL);')

        self.mouse.execute('CREATE TABLE IF NOT EXISTS dayOff('
                           'id_day integer NOT NULL PRIMARY KEY AUTOINCREMENT,'
                           'month TEXT NOT NULL,'
                           'day INT NOT NULL,'
                           'year INT NOT NULL);')

        self.mouse.execute('CREATE TABLE IF NOT EXISTS commentary('
                           'id_com integer NOT NULL PRIMARY KEY AUTOINCREMENT,'
                           'description VARCHAR(255),'
                           'day INT NOT NULL,'
                           'month TEXT NOT NULL,'
                           'year INT NOT NULL);')

        self.mouse.execute('CREATE TABLE IF NOT EXISTS calendar('
                           'id_cal integer NOT NULL PRIMARY KEY AUTOINCREMENT,'
                           'time INT NOT NULL,'
                           'day INT NOT NULL,'
                           'month TEXT NOT NULL,'
                           'year INT NOT NULL,'
                           'cat_ref TEXT NOT NULL,'
                           'color_cat VARCHAR(255) NOT NULL);')

        self.mouse.execute('CREATE TABLE IF NOT EXISTS goal('
                           'id_goa integer NOT NULL PRIMARY KEY AUTOINCREMENT,'
                           'objective INT NOT NULL,'
                           'month TEXT NOT NULL,'
                           'year INT NOT NULL,'
                           'cat_ref TEXT NOT NULL,'
                           'color_cat VARCHAR(255) NOT NULL);')

        self.mouse.execute('CREATE TABLE IF NOT EXISTS week('
                           'id_wek integer NOT NULL PRIMARY KEY AUTOINCREMENT,'
                           'seg INT NOT NULL,'
                           'ter INT NOT NULL,'
                           'qua INT NOT NULL,'
                           'qui INT NOT NULL,'
                           'sex INT NOT NULL,'
                           'sab INT NOT NULL,'
                           'dom INT NOT NULL)')

        self.mouse.execute('CREATE TABLE IF NOT EXISTS scale('
                           'id_sca integer NOT NULL PRIMARY KEY AUTOINCREMENT,'
                           'work INT NOT NULL,'
                           'off INT NOT NULL,'
                           'month TEXT NOT NULL,'
                           'year INT NOT NULL,'
                           'week INT,'
                           'FOREIGN KEY(week) REFERENCES week(id_wek));')

    def simple_select(self, table, name_col):
        sql = f'SELECT {name_col} FROM {table};'
        self.mouse.execute(sql)
        total = []
        for item in self.mouse:
            total.append(item[0])
        return len(total), total

    def choose_one(self, table, name_col, col_search, search):
        sql = F'SELECT {name_col} FROM {table} WHERE {col_search} = "{search}"'
        self.mouse.execute(sql)
        r = []
        for col in self.mouse:
            r.append(col)
        return r

    def choose_two(self, table, name_col, name_col2, col_search, search):
        sql = F'SELECT {name_col}, {name_col2} FROM {table} WHERE {col_search} = "{search}"'
        self.mouse.execute(sql)
        r = []
        for col1, col2 in self.mouse:
            r.append(col1)
            r.append(col2)
        return r

    def choose_three(self, table, name_col, name_col2, name_col3, col_search, col_search2, col_search3, *search):
        sql = F'SELECT {name_col}, {name_col2}, {name_col3} FROM {table} ' \
              F'WHERE {col_search} = "{search[0]}" AND {col_search2} = "{search[1]}" AND {col_search3} = "{search[2]}";'
        self.mouse.execute(sql)
        cols = []
        for col in self.mouse:
            cols.append(col)
        return cols

    def insert_cat(self, name, color):
        sql = 'INSERT INTO category(name, color) VALUES ("{}", "{}");'.format(name, color)
        self.mouse.execute(sql)
        self.con.commit()

    def show_cat(self):
        sql = f'SELECT name, color FROM category;'
        self.mouse.execute(sql)
        cats = []
        for cat in self.mouse:
            cats.append(cat)
        return cats

    def delete_cat(self, choose):
        sql = f'DELETE FROM category WHERE name = "{choose}";'
        self.mouse.execute(sql)
        self.con.commit()

    def insert_goal(self, objective, month, year, category, color):
        sql1 = f'SELECT id_goa FROM goal WHERE month = "{month}" AND year = "{year}" AND cat_ref = "{category}";'
        self.mouse.execute(sql1)
        unique = []
        for item in self.mouse:
            unique.append(item)
        if len(unique) == 0:
            sql = 'INSERT INTO goal(objective, month, year, cat_ref, color_cat) VALUES("{}", "{}", "{}", "{}", "{}")' \
                .format(objective, month, year, category, color)
            try:
                self.mouse.execute(sql)
                self.con.commit()
            except:
                pass
            else:
                return 0
        else:
            sql = 'UPDATE goal SET objective = "{}" WHERE month = "{}" AND year = "{}" AND cat_ref = "{}";'\
                .format(objective, month, year, category)
            self.mouse.execute(sql)
            self.con.commit()
            return 1

    def insert_comment(self, content, day, month, year):
        sql = f'INSERT INTO commentary (description, day, month, year) VALUES ("{content}", "{day}", "{month}", "{year}");'
        self.mouse.execute(sql)
        self.con.commit()

    def view_day_comment(self, month, year):
        sql = f'SELECT day FROM commentary WHERE month = "{month}" AND year = {year};'
        self.mouse.execute(sql)
        days = []
        for day in self.mouse:
            days.append(day[0])
        days.sort()
        return days, len(days)

    def view_content_comment(self, day, month, year):
        sql = f'SELECT description FROM commentary WHERE day = {day} AND month = "{month}" AND year = {year};'
        self.mouse.execute(sql)
        desc = []
        for item in self.mouse:
            desc.append(item[0])
        return desc

    def view_id_com(self, day, month, year):
        sql = f'SELECT id_com FROM commentary WHERE day = {day} AND month = "{month}" AND year = {year};'
        self.mouse.execute(sql)
        r_id = []
        for id_com in self.mouse:
            r_id.append(id_com)
        return r_id

    def del_comment(self, ids):
        sql = f'DELETE FROM commentary WHERE id_com = {ids};'
        self.mouse.execute(sql)
        self.con.commit()

    def insert_week(self, study_day, day_off, month, year, week):
        sql = f'SELECT week FROM scale WHERE month = "{month}" AND year = {year};'
        self.mouse.execute(sql)
        total = []
        for item in self.mouse:
            total.append(item)
        if len(total) == 0:
            sql1 = 'INSERT INTO week(seg, ter, qua, qui, sex, sab, dom) VALUES ("{}", "{}", "{}", "{}", "{}", "{}", "{}")'\
                .format(week[0], week[1], week[2], week[3], week[4], week[5], week[6])
            self.mouse.execute(sql1)
            id_week = self.mouse.lastrowid
            self.con.commit()
            sql2 = f'INSERT INTO scale (work, off, month, year, week) VALUES ("{study_day}", "{day_off}", "{month}", "{year}", "{id_week}");'
            self.mouse.execute(sql2)
            self.con.commit()
        else:
            sql1 = 'UPDATE week SET seg = "{}", ter = "{}", qua = "{}", qui = "{}", sex = "{}", sab = "{}", dom = "{}" WHERE id_wek = "{}";'\
                .format(week[0], week[1], week[2], week[3], week[4], week[5], week[6], total[0][0])
            self.mouse.execute(sql1)
            self.con.commit()
            sql2 = 'UPDATE scale SET work = "{}", off = "{}" WHERE week = "{}";'.format(study_day, day_off, total[0][0])
            self.mouse.execute(sql2)
            self.con.commit()

    def insert_effectivity(self, eff, cat, month, year):
        sql = f'SELECT id_eff FROM effectivity WHERE cat_ref = "{cat}" AND month = "{month}" AND year = {year};'
        self.mouse.execute(sql)
        unique = []
        for i in self.mouse:
            unique.append(i)
        if len(unique) == 0:
            sql1 = f'INSERT INTO effectivity(efficiency, cat_ref, month, year) VALUES({eff}, "{cat}", "{month}", {year});'
            self.mouse.execute(sql1)
            self.con.commit()
            return 0
        else:
            sql2 = f'UPDATE effectivity SET efficiency = {eff} WHERE id_eff = {unique[0][0]};'
            self.mouse.execute(sql2)
            self.con.commit()
            return 1

    def insert_calendar(self, time, day, month, year, cat, color):
        sql = f'SELECT id_cal, time FROM calendar WHERE day = {day} AND month = "{month}" AND year = {year} AND cat_ref = "{cat}";'
        self.mouse.execute(sql)
        unique, total, offs = [], [], []
        for i, o in self.mouse:
            unique.append(i)
            offs.append(o)
        sql1 = f'SELECT id_cal FROM calendar WHERE day = {day} AND month = "{month}" AND year = {year};'
        self.mouse.execute(sql1)
        for i in self.mouse:
            total.append(i)
        if len(unique) == 0 and len(total) < 5:
            sql2 = f'INSERT INTO calendar(time, day, month, year, cat_ref, color_cat) VALUES({time}, {day}, "{month}", {year}, "{cat}", "{color}");'
            self.mouse.execute(sql2)
            self.con.commit()
            return 0
        elif len(total) >= 5 and len(unique) == 0:
            return 2
        else:
            t_offs = 0
            for off in offs:
                t_offs += off
            sql3 = f'UPDATE calendar SET time = {t_offs} WHERE id_cal = {unique[0]};'
            self.mouse.execute(sql3)
            self.con.commit()

    def del_registry(self, selection, day, month, year):
        sql = f'SELECT id_cal FROM calendar WHERE day = {day} AND month = "{month}" AND year = {year} AND cat_ref = "{selection}";'
        ids = []
        self.mouse.execute(sql)
        for i in self.mouse:
            ids.append(i)
        sql2 = f'DELETE FROM calendar WHERE id_cal = {ids[0][0]};'
        self.mouse.execute(sql2)
        self.con.commit()

    def search_goal(self, month, year):
        sql = f'SELECT objective, cat_ref, color_cat FROM goal WHERE month = "{month}" AND year = {year};'
        r = []
        self.mouse.execute(sql)
        for data in self.mouse:
            r.append(data)
        return r

    def select_two_search(self, table, col, search1, search2, col_s, col_s2, order=False):
        if order is False:
            sql = f'SELECT {col} FROM {table} WHERE {col_s} = "{search1}" AND {col_s2} = "{search2}";'
            self.mouse.execute(sql)
            r = []
            for data in self.mouse:
                r.append(data)
            return r
        else:
            sql = f'SELECT {col} FROM {table} WHERE {col_s} = "{search1}" AND {col_s2} = "{search2}" ORDER BY {col} ASC;'
            self.mouse.execute(sql)
            r = []
            for data in self.mouse:
                r.append(data)
            return r

    def select_three_search(self, table, col, search1, search2, search3, col_s, col_s2, col_s3):
        sql = f'SELECT {col} FROM {table} WHERE {col_s} = "{search1}" AND {col_s2} = "{search2}" AND {col_s3} = "{search3}";'
        self.mouse.execute(sql)
        r = []
        for data in self.mouse:
            r.append(data)
        return r

    def del_simple(self, table, col_s, search):
        sql = f'DELETE FROM {table} WHERE {col_s} = "{search}";'
        self.mouse.execute(sql)
        self.con.commit()

    def show_week_scale(self, id_week):
        sql = f'SELECT seg, ter, qua, qui, sex, sab, dom FROM week WHERE id_wek = {id_week[0]};'
        self.mouse.execute(sql)
        r = []
        for item in self.mouse:
            r.append(item)
        return r

    def insert_off(self, day, month, year):
        sql = f'SELECT id_day FROM dayOff WHERE day = {day} AND month = "{month}" AND year = {year};'
        self.mouse.execute(sql)
        total = []
        for item in self.mouse:
            total.append(item)
        if len(total) == 0:
            sql1 = f'SELECT id_cal FROM calendar WHERE day = {day} AND month = "{month}" AND year = {year};'
            self.mouse.execute(sql1)
            for ids in self.mouse:
                total.append(ids)
            if len(total) == 0:
                sql2 = f'INSERT INTO dayOff (day, month, year) VALUES ({day}, "{month}", {year});'
                self.mouse.execute(sql2)
                self.con.commit()
                return 2
            else:
                return total
        else:
            return 1

    def del_off(self, day, month, year):
        sql = f'DELETE FROM dayOff WHERE day = {day} AND month = "{month}" AND year = {year};'
        self.mouse.execute(sql)
        self.con.commit()

    def confirm_insert_off(self, day, month, year):
        sql = f'INSERT INTO dayOff (day, month, year) VALUES ({day}, "{month}", {year});'
        self.mouse.execute(sql)
        self.con.commit()