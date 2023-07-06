import datetime
from tkinter import messagebox
from tkinter import *
from tkinter import colorchooser
from database import *

date = datetime.datetime.now()
month = date.month
year = date.year
day = date.day
bd = Database()


class Issue_date:
    def __init__(self):
        self.months = month

    def date_month(self, *back_time):
        if len(back_time) == 0:
            match self.months:
                case 1:
                    return 'janeiro', 31, day
                case 2:
                    return 'fevereiro', 28, day
                case 3:
                    return 'março', 31, day
                case 4:
                    return 'abril', 30, day
                case 5:
                    return 'maio', 31, day
                case 6:
                    return 'junho', 30, day
                case 7:
                    return 'julho', 31, day
                case 8:
                    return 'agosto', 31, day
                case 9:
                    return 'setembro', 30, day
                case 10:
                    return 'outubro', 31, day
                case 11:
                    return 'novembro', 30, day
                case 12:
                    return 'dezembro', 31, day
        else:
            self.months -= back_time
            match self.months:
                case 1:
                    return 'janeiro', 31, day
                case 2:
                    return 'fevereiro', 28, day
                case 3:
                    return 'março', 31, day
                case 4:
                    return 'abril', 30, day
                case 5:
                    return 'maio', 31, day
                case 6:
                    return 'junho', 30, day
                case 7:
                    return 'julho', 31, day
                case 8:
                    return 'agosto', 31, day
                case 9:
                    return 'setembro', 30, day
                case 10:
                    return 'outubro', 31, day
                case 11:
                    return 'novembro', 30, day
                case 12:
                    return 'dezembro', 31, day

    def day_registry(self):
        list_day = []
        for days in range(1, self.date_month()[1] + 1):
            list_day.append(str(days))
        return list_day


def colors(scale):
    match scale:
        case 1:
            return '#224459'
        case 2:
            return '#58788c'
        case 3:
            return '#819ba6'
        case 4:
            return '#a8bbbf'
        case 5:
            return '#c1d4d9'


def max_char(limit, arg, field, parent):
    arg = arg.get()
    if len(arg) >= limit:
        messagebox.showerror('Erro', f'O campo em questão só permite {limit} caracteres', parent=parent)
        field.delete(0, END)


def max_comment(limit, arg, field, parent, days, months, years):
    if len(arg) >= limit:
        messagebox.showerror('Erro', f'O campo em questão só permite {limit} caracteres', parent=parent)
    else:
        bd.connect()
        bd.insert_comment(arg, days, months, years)
        bd.disconnect()
        messagebox.showinfo('Sucesso!', 'comentário inserido no dia desejado!', parent=parent)
        field.delete(1.0, END)


def show_tree(treeview):
    bd.connect()
    total = bd.simple_select('CATEGORY', 'id_cat')
    if total[0] == 0:
        pass
    else:
        items = bd.show_cat()
        for cate in range(0, total[0]):
            treeview.tag_configure(f'{items[cate - 1][1]}', background=colors(1), foreground=items[cate - 1][1])
            treeview.insert('', 'end', values=(items[cate - 1][0], 'a', 'a'), tags=(f'{items[cate - 1][1]}',))
    bd.disconnect()


def insert_combo():
    bd.connect()
    total = bd.simple_select('CATEGORY', 'name')
    if total[0] == 0:
        pass
    else:
        return total[1]
    bd.disconnect()


def month_combo():
    mon = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro',
           'outubro', 'novembro', 'dezembro']
    return mon


def year_combo():
    y = []
    for i in range(year, year + 51):
        y.append(i)
    return y


def insert_goal(arg, field, parent, months, years, category):
    ctg = str(arg.get())
    if ctg.isnumeric():
        bd.connect()
        cat = bd.choose_two('category', 'id_cat', 'name', 'name', category)
        if len(cat) == 0:
            messagebox.showerror('Erro no registro', 'Escolha uma categoria para receber a meta.', parent=parent)
            bd.disconnect()
        else:
            insert = bd.insert_goal(ctg, months, years, cat[0])
            if insert == 1:
                messagebox.showinfo('Sucesso!', f'meta para a categoria {category} no mês {months} de {years} foi definida como'
                                                f' sendo {ctg} minuto(s).', parent=parent)
                bd.disconnect()
            else:
                messagebox.showerror('Erro no registro de meta', 'As informações preenchidas no campo de minutos estão inválidas.'
                                     , parent=parent)
                field.delete(0, END)
                bd.disconnect()
    else:
        messagebox.showerror('Erro no registro dos minutos', 'Valor passado não é composto por um número inteiro.',
                             parent=parent)
        field.delete(0, END)


class Complementar_tree:
    def __init__(self):
        self.hex_col, self.selection = None, None

    def tree_color(self):
        color = colorchooser.askcolor()
        self.hex_col = color[1]

    def tree_insert(self, limit, arg, field, parent, treeview):
        arg = arg.get()
        if len(arg) >= limit:
            messagebox.showerror('Erro', f'O campo em questão só permite {limit} caracteres.', parent=parent)
            field.delete(0, END)
        elif self.hex_col is None:
            messagebox.showerror('Erro', f'Não foi escolhida uma cor para a categoria.', parent=parent)
        else:
            treeview.tag_configure(f'{self.hex_col}', background=colors(1), foreground=self.hex_col)
            treeview.insert('', 'end', values=(arg, 'a', 'a'), tags=(f'{self.hex_col}',))
            bd.connect()
            bd.insert_cat(arg, self.hex_col)
            self.hex_col = None
            bd.disconnect()

    def delete_tree(self, treeview, parent):
        try:
            self.selection = treeview.selection()[0]
        except IndexError:
            messagebox.showerror('Erro', 'Nenhuma categoria selecionada para exclusão.', parent=parent)
        else:
            treeview.delete(self.selection)
            bd.connect()
            bd.delete_cat(self.selection)
            bd.disconnect()
            self.selection = None


class Registry_rule:
    def __init__(self):
        self.choose_s, self.choose_d = None, None
        self.year, self.month = None, None

    def collect_option_default(self, option, parent):
        op = str(option.get())
        if op.isnumeric():
            op = int(op)
            if op == 0:
                messagebox.showerror('Erro na definição do padrão', 'Selecione uma das opções para seguir',
                                     parent=parent)
            if op == 1:
                self.choose_s = 5
                self.choose_d = 2
                messagebox.showinfo('Sucesso!', 'Escolha registrada, siga para definir o mês e ano da regra.',
                                    parent=parent)
                option.set(0)
            elif op == 2:
                self.choose_s = 6
                self.choose_d = 1
                messagebox.showinfo('Sucesso!', 'Escolha registrada, siga para definir o mês e ano da regra.',
                                    parent=parent)
                option.set(0)
            else:
                self.choose_s = 7
                self.choose_d = 0
                messagebox.showinfo('Sucesso!', 'Escolha registrada, siga para definir o mês e ano da regra.',
                                    parent=parent)
                option.set(0)

    def collect_option_style(self, option1, option2, parent, field1, field2):
        op1 = str(option1.get())
        op2 = str(option2.get())
        if op1.isnumeric() and op2.isnumeric():
            op1, op2 = int(op1), int(op2)
            if (op1 + op2) == 7:
                self.choose_s = op1
                self.choose_d = op2
                messagebox.showinfo('Sucesso!', 'Escolhas registradas, siga para definir o mês e ano da regra.',
                                    parent=parent)
                field1.delete(0, END)
                field2.delete(0, END)
            else:
                messagebox.showerror('Escolha inválida', 'A somatória dos dias de estudo e de folga devem totalizar 7.',
                                     parent=parent)
                field1.delete(0, END)
                field2.delete(0, END)

        else:
            messagebox.showerror('Erro na definição', 'Opção enviada contém caracteres não permitidos ou esta vazia.',
                                 parent=parent)
            field1.delete(0, END)
            field2.delete(0, END)

    def return_choose(self):
        return self.choose_s, self.choose_d, self.month, self.year

    def open_scale(self, parent, new_window, mon, yea):
        self.month = mon.get()
        self.year = yea.get()
        if self.choose_s == 7:
            messagebox.showinfo('Escala definida!', 'Tudo certo agora, aproveite seus estudos (7 dias direto é para pessoas estudiosas mesmo hein!)',
                                parent=parent)
            week = [1, 1, 1, 1, 1, 1, 1]
            bd.connect()
            bd.insert_week(self.choose_s, 0, self.month, self.year, week)
            self.choose_s = None
            bd.disconnect()
            self.month, self.year = None, None
        elif self.choose_s is None or self.choose_d is None:
            messagebox.showerror('Erro', 'Escolha primeiro a quantia de dias para estudo e folga', parent=parent)
        else:
            new_window()


class Choose_scale:
    def __init__(self):
        self.study, self.check = [], []
        self.variables, self.days = [], ['Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sab', 'Dom']
        self.week = []

    def scale_default(self, parent):
        move_button = 0.04
        move_days = 0
        for item in range(0, 7):
            self.variables.append(IntVar(master=parent))
        for check in range(0, 7):
            self.check.append(check)
            self.check[check] = Checkbutton(parent, text=self.days[move_days], variable=self.variables[check],
                                            onvalue=check + 1, offvalue=0, font=('Calibri', 10, 'bold'), bg=colors(2),
                                            fg=colors(4))
            self.check[check].place(relx=move_button, rely=0.50)
            move_button += 0.13
            move_days += 1

    def set_study(self, parent, choose_s, choose_d, choose_m, choose_y):
        for variable in range(0, len(self.variables)):
            if self.variables[variable].get() == 0:
                self.week.append(0)
            else:
                self.week.append(1)
                self.study.append(self.variables[variable].get())
        if choose_s < len(self.study) or choose_s > len(self.study):
            messagebox.showerror('Erro na escolha', 'Quantidade dias definidos é diferente do definido na janela anterior.',
                                 parent=parent)
            self.study = []
        else:
            messagebox.showinfo('Dias registrados', 'O(s) dia(s) de folga é(são) o(s) não escolhido(s).',
                                parent=parent)
            bd.connect()
            bd.insert_week(choose_s, choose_d, choose_m, choose_y, self.week)
            bd.disconnect()
            parent.destroy()
            self.study = []
            for variable in range(0, len(self.variables)):
                self.variables[variable].set(0)


def registry_condition(parent, mon, yea, eff, field, cat):
    if cat == '':
        messagebox.showerror('Erro no cadastro da condição',
                             'Não foi informada uma categoria para aplicar a efetividade.',
                             parent=parent)
    elif eff == '':
        messagebox.showerror('Erro no cadastro da condição',
                             f'Não foi passado um valor para a efetividade da categoria {cat}.',
                             parent=parent)
        field.delete(0, END)
    else:
        v_eff = str(eff)
        v_eff = v_eff.replace(',', '.')
        try:
            verify = float(v_eff)
        except:
            messagebox.showerror('Erro no cadastro da condição',
                                 'Valor inserido no campo de efetividade não é um número inteiro ou real.',
                                 parent=parent)
            field.delete(0, END)
        else:
            bd.connect()
            bd.insert_effectivity(v_eff, cat, mon.get(), yea.get())
            bd.disconnect()
            messagebox.showinfo('Sucesso!',
                                f'Efetividade de {v_eff}% para a categoria {cat.upper()} durante o período do mês {mon.get()} de {yea.get()} inserida com sucesso!',
                                parent=parent)
            field.delete(0, END)
