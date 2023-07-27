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
        sql = f'SELECT name, color FROM category;'
        self.mouse.execute(sql)
        cats = []
        total = []
        for cat in self.mouse:
            cats.append(cat)
            total.append(cat[0])
        choose = int(choose[1:]) - 1
        sql1 = f'DELETE FROM category WHERE name = "{cats[choose][0]}";'
        self.mouse.execute(sql1)
        self.con.commit()

    def insert_goal(self, objective, month, year, category, color):
        sql1 = f'SELECT id_goa FROM goal WHERE month = "{month}" AND year = "{year}" AND cate_ref = {category};'
        self.mouse.execute(sql1)
        unique = []
        for item in self.mouse:
            unique.append(item)
        if len(unique) == 0:
            sql = 'INSERT INTO goal(objective, month, year, cate_ref, color) VALUES("{}", "{}", "{}", "{}", "{}")' \
                .format(objective, month, year, category, color)
            try:
                self.mouse.execute(sql)
                self.con.commit()
            except:
                pass
            else:
                return 1
        else:
            sql = 'UPDATE goal SET objective = "{}" WHERE month = "{}" AND year = "{}" AND cate_ref = "{}";'\
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
        sql = 'INSERT INTO week(seg, ter, qua, qui, sex, sab, dom) VALUES ("{}", "{}", "{}", "{}", "{}", "{}", "{}")'\
            .format(week[0], week[1], week[2], week[3], week[4], week[5], week[6])
        self.mouse.execute(sql)
        id_week = self.mouse.lastrowid
        self.con.commit()
        sql1 = f'INSERT INTO scale (work, off, month, year, week) VALUES ("{study_day}", "{day_off}", "{month}", "{year}", "{id_week}");'
        self.mouse.execute(sql1)
        self.con.commit()

    def insert_effectivity(self, eff, cat, month, year):
        sql = f'SELECT id_cat FROM category WHERE name = "{cat}";'
        self.mouse.execute(sql)
        id_cat = 0
        for ids in self.mouse:
            id_cat = ids[0]
        sql1 = f'INSERT INTO effectivity(efficiency, id_cat, month, year) VALUES({eff}, {id_cat}, "{month}", {year});'
        self.mouse.execute(sql1)
        self.con.commit()

    def insert_calendar(self, time, day, month, year, cat, color):
        sql = f'SELECT id_cal, time FROM calendar WHERE day = {day} AND month = "{month}" AND year = {year} AND cat_ref = "{cat}";'
        self.mouse.execute(sql)
        unique = []
        times = []
        time = int(time)
        for i, t in self.mouse:
            unique.append(i)
            times.append(t)
        if len(unique) == 0:
            sql1 = f'INSERT INTO calendar(time, day, month, year, cat_ref, color_cat) VALUES({time}, {day}, "{month}", {year}, "{cat}", "{color}");'
            self.mouse.execute(sql1)
            self.con.commit()
            return 0
        else:
            new_time = 0
            for t in times:
                new_time += t
            new_time += time
            sql2 = f'UPDATE calendar SET time = {new_time} WHERE id_cal = {unique[0]};'
            self.mouse.execute(sql2)
            self.con.commit()
            return 1