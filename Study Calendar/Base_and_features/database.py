import sqlite3
# this module is about SQL queries and the construction of SQLite3 DB
# if u feel missing some explains in this module, please contact me thought: https://calendario-estudos.netlify.app/


class Database:
    def __init__(self):
        self.con = None
        self.mouse = None

    def connect(self):
        """
        :return: object to connection and create a bd file if not exists.
        """
        self.con = sqlite3.connect('items_sc.bd')
        self.mouse = self.con.cursor()

    def disconnect(self):
        """
        :return: make interrupt of connection
        """
        self.con.close()

    def table_create(self):
        """
        Creation all tables
        Tables don't have dependence between they (except case of scale and week tables).
        :return: tables creates, but he function can't update any table after of first run.
        """
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
        """
        this method get a simple select query
        :param table: choose any table from bd;
        :param name_col: define someone column to same table;
        :return: two parameters: st: length of tuple; nd: content of tuple.
        """
        sql = f'SELECT {name_col} FROM {table};'
        self.mouse.execute(sql)
        total = []
        for item in self.mouse:
            total.append(item[0])
        return len(total), total

    def choose_one(self, table, name_col, col_search, search):
        """
        choose_one method can make a select with where clause
        :param table: define any table of bd.
        :param name_col: write some column for return datas;
        :param col_search: send a column to use for research;
        :param search: inform one value for find in col_search;
        :return: tuple with all conditions informed.
        """
        sql = F'SELECT {name_col} FROM {table} WHERE {col_search} = "{search}"'
        self.mouse.execute(sql)
        r = []
        for col in self.mouse:
            r.append(col)
        return r

    def choose_two(self, table, name_col, name_col2, col_search, search):
        """
        Here we've the same to choose_one method. The unique different is that we can return two columns to table
        :param table: define any table of bd.
        :param name_col: write some column for return datas;
        :param name_col2: write another some column for return datas;
        :param col_search: send a column to use for research;
        :param search: inform one value for find in col_search;
        :return: tuple with all conditions informed.
        """
        sql = F'SELECT {name_col}, {name_col2} FROM {table} WHERE {col_search} = "{search}"'
        self.mouse.execute(sql)
        r = []
        for col1, col2 in self.mouse:
            r.append(col1)
            r.append(col2)
        return r

    def choose_three(self, table, name_col, name_col2, name_col3, col_search, col_search2, col_search3, *search):
        """
        This method is similar to choose_one and choose_two, but here we can make where clause if three conditions
        :param table: define any table of bd.
        :param name_col: write someone column for return datas;
        :param name_col2: write a second some column for return datas;
        :param name_col3: write a third some column for return datas;
        :param col_search: send a column to use for research;
        :param col_search2: send a second column to use for research;
        :param col_search3: send a third column to use for research;
        :param search: inform one or more values for find in col_searchs, remember use index here;
        :return: tuple with all conditions informed.
        """
        sql = F'SELECT {name_col}, {name_col2}, {name_col3} FROM {table} ' \
              F'WHERE {col_search} = "{search[0]}" AND {col_search2} = "{search[1]}" AND {col_search3} = "{search[2]}";'
        self.mouse.execute(sql)
        cols = []
        for col in self.mouse:
            cols.append(col)
        return cols

    def insert_cat(self, name, color):
        """
        insert_cat only used to insert categories in "category" table
        :param name: here write one name to a category;
        :param color: choose one color for her;
        :return: don't have return, he only writes in database.
        """
        sql = 'INSERT INTO category(name, color) VALUES ("{}", "{}");'.format(name, color)
        self.mouse.execute(sql)
        self.con.commit()

    def show_cat(self):
        """
        this method help to show all categories inserted before
        :return: a tuple with name and color of all categories.
        """
        sql = f'SELECT name, color FROM category;'
        self.mouse.execute(sql)
        cats = []
        for cat in self.mouse:
            cats.append(cat)
        return cats

    def delete_cat(self, choose):
        """
        delete_cat can remove one category to database
        :param choose: inform one name to category.
        :return: don't have return, he only updated db.
        """
        sql = f'DELETE FROM category WHERE name = "{choose}";'
        self.mouse.execute(sql)
        self.con.commit()

    def insert_goal(self, objective, month, year, category, color):
        """
        this method can insert one goal in "goal" table
        :param objective: objective is time to goal;
        :param month: write a month of goal;
        :param year: write one year;
        :param category: insert name of category;
        :param color: send the color of category.
        :return: Here we've two returns: st: return 0 to inform that a new goal is success registry.
        nd: return 1 to inform that the goal previously inserted had updated.
        """
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
        """
        insert_comment can registries commentaries in database
        :param content: content of commentary;
        :param day: write the day of commentary;
        :param month: write one month;
        :param year: write one year.
        :return: don't have return, he only updated database.
        """
        sql = f'INSERT INTO commentary (description, day, month, year) VALUES ("{content}", "{day}", "{month}",' \
              f' "{year}");'
        self.mouse.execute(sql)
        self.con.commit()

    def view_day_comment(self, month, year):
        """
        this method find days with commentaries in any month
        :param month: define one month to filter;
        :param year: write one year.
        :return: two datas: st: one list with days. nd: length of this list.
        """
        sql = f'SELECT day FROM commentary WHERE month = "{month}" AND year = {year};'
        self.mouse.execute(sql)
        days = []
        for day in self.mouse:
            days.append(day[0])
        days.sort()
        return days, len(days)

    def view_content_comment(self, day, month, year):
        """
        similar to view_day_comment. Here we can see content of commentaries in any month
        :param day: choose the day for filter;
        :param month: write one month;
        :param year: write one year.
        :return: tuple with commentaries in this day.
        """
        sql = f'SELECT description FROM commentary WHERE day = {day} AND month = "{month}" AND year = {year};'
        self.mouse.execute(sql)
        desc = []
        for item in self.mouse:
            desc.append(item[0])
        return desc

    def view_id_com(self, day, month, year):
        """
        This method show id of one commentary with conditions previously informed
        :param day: inform the day for filter;
        :param month: write one month;
        :param year: write one year.
        :return: tuple with id of all commentaries with conditions informed.
        """
        sql = f'SELECT id_com FROM commentary WHERE day = {day} AND month = "{month}" AND year = {year};'
        self.mouse.execute(sql)
        r_id = []
        for id_com in self.mouse:
            r_id.append(id_com)
        return r_id

    def del_comment(self, ids):
        """
        Remove one commentary.
        :param ids: insert the id of commentary.
        :return: don't have return, he only updated the database.
        """
        sql = f'DELETE FROM commentary WHERE id_com = {ids};'
        self.mouse.execute(sql)
        self.con.commit()

    def insert_week(self, study_day, day_off, month, year, week):
        """
        This method create one week for bond with month scale
        :param study_day: insert all days that will be study day;
        :param day_off: inform day offs;
        :param month: write one month;
        :param year: write one year;
        :param week: write days with values one or zero (one for study and zero for day off).
        :return: don't have return, he only updated database.
        """
        sql = f'SELECT week FROM scale WHERE month = "{month}" AND year = {year};'
        self.mouse.execute(sql)
        total = []
        for item in self.mouse:
            total.append(item)
        if len(total) == 0:
            sql1 = 'INSERT INTO week(seg, ter, qua, qui, sex, sab, dom) VALUES ' \
                   '("{}", "{}", "{}", "{}", "{}", "{}", "{}")'\
                    .format(week[0], week[1], week[2], week[3], week[4], week[5], week[6])
            self.mouse.execute(sql1)
            id_week = self.mouse.lastrowid
            self.con.commit()
            sql2 = f'INSERT INTO scale (work, off, month, year, week) VALUES ("{study_day}", "{day_off}", "{month}",' \
                   f' "{year}", "{id_week}");'
            self.mouse.execute(sql2)
            self.con.commit()
        else:
            sql1 = 'UPDATE week SET seg = "{}", ter = "{}", qua = "{}", qui = "{}", sex = "{}", sab = "{}", ' \
                   'dom = "{}" WHERE id_wek = "{}";'\
                .format(week[0], week[1], week[2], week[3], week[4], week[5], week[6], total[0][0])
            self.mouse.execute(sql1)
            self.con.commit()
            sql2 = 'UPDATE scale SET work = "{}", off = "{}" WHERE week = "{}";'.format(study_day, day_off, total[0][0])
            self.mouse.execute(sql2)
            self.con.commit()

    def insert_effectivity(self, eff, cat, month, year):
        """
        Method auxiliar for "effectitivy" table
        :param eff: inform efficiency to category;
        :param cat: write the name of category;
        :param month: write one month;
        :param year: write one year.
        :return: return zero if a new effectivity is insert else return one to update effectivity previously inserted.
        """
        sql = f'SELECT id_eff FROM effectivity WHERE cat_ref = "{cat}" AND month = "{month}" AND year = {year};'
        self.mouse.execute(sql)
        unique = []
        for i in self.mouse:
            unique.append(i)
        if len(unique) == 0:
            sql1 = f'INSERT INTO effectivity(efficiency, cat_ref, month, year) VALUES({eff}, "{cat}", "{month}",' \
                   f' {year});'
            self.mouse.execute(sql1)
            self.con.commit()
            return 0
        else:
            sql2 = f'UPDATE effectivity SET efficiency = {eff} WHERE id_eff = {unique[0][0]};'
            self.mouse.execute(sql2)
            self.con.commit()
            return 1

    def insert_calendar(self, time, day, month, year, cat, color):
        """
        Core method. Here we can insert registries and day offs in schedule
        :param time: inform duration of study;
        :param day: write the day that receive the insertion;
        :param month: write one month;
        :param year: write one year;
        :param cat: send name of category (or "Folgas" for day off);
        :param color: define the color of category.
        :return: three cases to return: st: return 0 to a new registry. nd: return one to update previously registry.
        rd: return two to fail in insert because off max limit of registries in one same day.
        """
        sql = f'SELECT id_cal, time FROM calendar WHERE day = {day} AND month = "{month}" AND year = {year} ' \
              f'AND cat_ref = "{cat}";'
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
            sql2 = f'INSERT INTO calendar(time, day, month, year, cat_ref, color_cat) VALUES({time}, {day}, ' \
                   f'"{month}", {year}, "{cat}", "{color}");'
            self.mouse.execute(sql2)
            self.con.commit()
            return 0
        elif len(total) >= 5 and len(unique) == 0:
            return 2
        else:
            if cat == 'Folgas':
                t_offs = 0
                for off in offs:
                    t_offs += off
                sql3 = f'UPDATE calendar SET time = {t_offs} WHERE id_cal = {unique[0]};'
                self.mouse.execute(sql3)
                self.con.commit()
            else:
                sql4 = f'UPDATE calendar SET time = {time} WHERE id_cal = {unique[0]};'
                self.mouse.execute(sql4)
                self.con.commit()
                return 1

    def del_registry(self, selection, day, month, year):
        """
        Remove one registry (study)
        :param selection: this parameter is about position of selector in tree view;
        :param day: inform day to filter;
        :param month: write one month;
        :param year: write one year.
        :return: don't have return, he only updated the database.
        """
        sql = f'SELECT id_cal FROM calendar WHERE day = {day} AND month = "{month}" AND year = {year} AND cat_ref = ' \
              f'"{selection}";'
        ids = []
        self.mouse.execute(sql)
        for i in self.mouse:
            ids.append(i)
        sql2 = f'DELETE FROM calendar WHERE id_cal = {ids[0][0]};'
        self.mouse.execute(sql2)
        self.con.commit()

    def search_goal(self, month, year):
        """
        Method to find goals in "goal" table
        :param month: write the month to filter;
        :param year: write one year.
        :return: tuple with three columns that answer all conditions.
        """
        sql = f'SELECT objective, cat_ref, color_cat FROM goal WHERE month = "{month}" AND year = {year};'
        r = []
        self.mouse.execute(sql)
        for data in self.mouse:
            r.append(data)
        return r

    def select_two_search(self, table, col, search1, search2, col_s, col_s2, order=False):
        """
        selection_two_search can make select query with where clause and order by (default is without)
        :param table: inform a table to filter;
        :param col: choose one column for return;
        :param search1: write first value to search;
        :param search2: write second value;
        :param col_s: send first column to filter where clause;
        :param col_s2: send second column;
        :param order: set False or True to active Order By query.
        :return: tuple with conditions defined.
        """
        if order is False:
            sql = f'SELECT {col} FROM {table} WHERE {col_s} = "{search1}" AND {col_s2} = "{search2}";'
            self.mouse.execute(sql)
            r = []
            for data in self.mouse:
                r.append(data)
            return r
        else:
            sql = f'SELECT {col} FROM {table} WHERE {col_s} = "{search1}" AND {col_s2} = "{search2}" ORDER BY {col} ' \
                  f'ASC;'
            self.mouse.execute(sql)
            r = []
            for data in self.mouse:
                r.append(data)
            return r

    def select_three_search(self, table, col, search1, search2, search3, col_s, col_s2, col_s3):
        """
        Similar to select_two, here we can return one column but with three parameters in where clause
        :param table: define table to filter;
        :param col: inform column for return;
        :param search1: send first value to apply where clause;
        :param search2: send second value;
        :param search3: send third value;
        :param col_s: choose first column for search in where clause;
        :param col_s2: choose second column;
        :param col_s3: choose third column.
        :return: tuple with all conditions informed.
        """
        sql = f'SELECT {col} FROM {table} WHERE {col_s} = "{search1}" AND {col_s2} = "{search2}" AND {col_s3} = ' \
              f'"{search3}";'
        self.mouse.execute(sql)
        r = []
        for data in self.mouse:
            r.append(data)
        return r

    def del_simple(self, table, col_s, search):
        """
        Remove any value in some table
        :param table: write table to filter;
        :param col_s: write column for search;
        :param search: inform the value to apply in column search.
        :return: don't have return, only remove the element from database.
        """
        sql = f'DELETE FROM {table} WHERE {col_s} = "{search}";'
        self.mouse.execute(sql)
        self.con.commit()

    def show_week_scale(self, id_week):
        """
        Method helps to show scale/week
        :param id_week: write the id to one row in "week" table;
        :return: select with id informed.
        """
        sql = f'SELECT seg, ter, qua, qui, sex, sab, dom FROM week WHERE id_wek = {id_week[0]};'
        self.mouse.execute(sql)
        r = []
        for item in self.mouse:
            r.append(item)
        return r

    def insert_off(self, day, month, year):
        """
        This method can insert one day off in schedule
        :param day: write one day to filter;
        :param month: write one month;
        :param year: write one year.
        :return: three types: st: return tuple with select for confirm update. nd: return one to inform that have one
        off in this day. rd: return two to confirm insertion of day off.
        """
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
        """
        remove one day off to schedule
        :param day: inform the day to filter;
        :param month: write one month;
        :param year: write one year.
        :return: don't have return, he only remove the element from database.
        """
        sql = f'DELETE FROM dayOff WHERE day = {day} AND month = "{month}" AND year = {year};'
        self.mouse.execute(sql)
        self.con.commit()

    def confirm_insert_off(self, day, month, year):
        """
        this method is auxiliar of insert_off. He is used for insert day offs
        :param day: write the day of off;
        :param month: write the month;
        :param year: write the year.
        :return: don't have return, only insert day off in "dayOff" table.
        """
        sql = f'INSERT INTO dayOff (day, month, year) VALUES ({day}, "{month}", {year});'
        self.mouse.execute(sql)
        self.con.commit()