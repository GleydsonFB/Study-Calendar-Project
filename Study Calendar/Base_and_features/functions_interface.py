import datetime
from tkinter import messagebox
from tkinter import *
from tkinter import ttk
from tkinter import colorchooser
from database import *
from PIL import Image, ImageTk
from auxiliar_math import *

date = datetime.datetime.now()
month = date.month
year = date.year
day = date.day
bd = Database()
calc_study = Study_calc(None, None, None, None)


class Issue_date:
    def __init__(self):
        self.months = month
        self.future, self.back, self.name_month_back, self.name_month_future = 0, 0, 0, 0
        self.year = year
        self.change_or_not, self.choose_now = False, month

    def date_month(self, back_time=0, advance_time=0, change_or_not=False):
        self.change_or_not = change_or_not
        if back_time == 0 and advance_time == 0:
            match self.months:
                case 1:
                    return 'janeiro', 31, day, self.months
                case 2:
                    if (self.year % 4 == 0 and self.year % 100 != 0) or self.year % 4 == 0:
                        return 'fevereiro', 29, day, self.months
                    else:
                        return 'fevereiro', 28, day, self.months
                case 3:
                    return 'março', 31, day, self.months
                case 4:
                    return 'abril', 30, day, self.months
                case 5:
                    return 'maio', 31, day, self.months
                case 6:
                    return 'junho', 30, day, self.months
                case 7:
                    return 'julho', 31, day, self.months
                case 8:
                    return 'agosto', 31, day, self.months
                case 9:
                    return 'setembro', 30, day, self.months
                case 10:
                    return 'outubro', 31, day, self.months
                case 11:
                    return 'novembro', 30, day, self.months
                case 12:
                    return 'dezembro', 31, day, self.months
        elif back_time >= 1 and advance_time == 0:
            if self.change_or_not is True:
                self.back += back_time
                self.choose_now = self.months + self.future - self.back
            else:
                self.name_month_back += back_time
                self.choose_now = self.months + self.name_month_future - self.name_month_back
            if 12 >= self.choose_now >= 1:
                match self.choose_now:
                    case 1:
                        return 'janeiro', 31, day, self.choose_now
                    case 2:
                        if (self.year % 4 == 0 and self.year % 100 != 0) or self.year % 4 == 0:
                            return 'fevereiro', 29, day, self.choose_now
                        else:
                            return 'fevereiro', 28, day, self.choose_now
                    case 3:
                        return 'março', 31, day, self.choose_now
                    case 4:
                        return 'abril', 30, day, self.choose_now
                    case 5:
                        return 'maio', 31, day, self.choose_now
                    case 6:
                        return 'junho', 30, day, self.choose_now
                    case 7:
                        return 'julho', 31, day, self.choose_now
                    case 8:
                        return 'agosto', 31, day, self.choose_now
                    case 9:
                        return 'setembro', 30, day, self.choose_now
                    case 10:
                        return 'outubro', 31, day, self.choose_now
                    case 11:
                        return 'novembro', 30, day, self.choose_now
                    case 12:
                        return 'dezembro', 31, day, self.choose_now
            else:
                if self.choose_now >= 13:
                    self.year += 1
                elif self.choose_now <= 0:
                    self.year -= 1
                self.months = 12
                self.back, self.name_month_back, self.future, self.name_month_future = -1, 0, 0, 0
                return 'dezembro', 31, day, self.choose_now
        else:
            if change_or_not is True:
                self.future += advance_time
                self.choose_now = self.months + self.future - self.back
            else:
                self.name_month_future += advance_time
                self.choose_now = self.months + self.name_month_future - self.name_month_back
            if 12 >= self.choose_now >= 1:
                match self.choose_now:
                    case 1:
                        return 'janeiro', 31, day, self.choose_now
                    case 2:
                        if (self.year % 4 == 0 and self.year % 100 != 0) or self.year % 4 == 0:
                            return 'fevereiro', 29, day, self.choose_now
                        else:
                            return 'fevereiro', 28, day, self.choose_now
                    case 3:
                        return 'março', 31, day, self.choose_now
                    case 4:
                        return 'abril', 30, day, self.choose_now
                    case 5:
                        return 'maio', 31, day, self.choose_now
                    case 6:
                        return 'junho', 30, day, self.choose_now
                    case 7:
                        return 'julho', 31, day, self.choose_now
                    case 8:
                        return 'agosto', 31, day, self.choose_now
                    case 9:
                        return 'setembro', 30, day, self.choose_now
                    case 10:
                        return 'outubro', 31, day, self.choose_now
                    case 11:
                        return 'novembro', 30, day, self.choose_now
                    case 12:
                        return 'dezembro', 31, day, self.choose_now
            else:
                if self.choose_now >= 13:
                    self.year += 1
                elif self.choose_now <= 1:
                    self.year -= 1
                self.months = 1
                self.future, self.name_month_future, self.back, self.name_month_back = -1, 0, 0, 0
                return 'janeiro', 31, day, self.choose_now

    def day_registry(self):
        list_day = []
        for days in range(1, self.date_month()[1] + 1):
            list_day.append(str(days))
        return list_day

    def reset_all(self):
        self.__init__()


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


def show_tree(treeview):
    bd.connect()
    total = bd.simple_select('CATEGORY', 'id_cat')
    if total[0] == 0:
        pass
    else:
        items = bd.show_cat()
        for cate in range(0, total[0]):
            treeview.tag_configure(f'{items[cate - 1][1]}', background=items[cate - 1][1], foreground='white')
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


def insert_goal(arg, field, parent, months, years, category, goal_status):
    ctg = str(arg.get())
    if ctg.isnumeric():
        bd.connect()
        cat = bd.choose_two('category', 'color', 'name', 'name', category)
        if len(cat) == 0:
            messagebox.showerror('Erro no registro', 'Escolha uma categoria para receber a meta.', parent=parent)
            bd.disconnect()
        else:
            insert = bd.insert_goal(ctg, months, years, cat[1], cat[0])
            if insert == 0:
                messagebox.showinfo('Sucesso!',
                                    f'meta para a categoria {category} no mês {months} de {years} foi definida como'
                                    f' sendo {ctg} hora(s).', parent=parent)
                field.delete(0, END)
                bd.disconnect()
                goal_status.clear_frame()
                goal_status.show_data()
            elif insert == 1:
                messagebox.showinfo('Sucesso!',
                                    f'meta para a categoria {category} no mês {months} de {years} foi atualizada para'
                                    f' {ctg} hora(s).', parent=parent)
                field.delete(0, END)
                bd.disconnect()
                goal_status.clear_frame()
                goal_status.show_data()
            else:
                messagebox.showerror('Erro no registro de meta',
                                     'As informações preenchidas no campo de horas estão inválidas.'
                                     , parent=parent)
                field.delete(0, END)
                bd.disconnect()
    else:
        messagebox.showerror('Erro no registro dos minutos', 'Valor passado não é composto por um número inteiro.',
                             parent=parent)
        field.delete(0, END)
        bd.disconnect()


def delete_goal(parent, months, years, category, goal_status):
    bd.connect()
    registries = bd.select_three_search('goal', 'id_goa', category, months, years, 'cat_ref', 'month', 'year')
    if len(registries) == 0:
        messagebox.showerror('Retorno da busca', f'Não foi localizado uma meta para a categoria {category} em {months} de {years}.', parent=parent)
        bd.disconnect()
    else:
        bd.del_simple('goal', 'id_goa', registries[0][0])
        messagebox.showinfo('Retorno da busca', f'Foi removida a meta cadastrada em {months} de {years} na categoria {category}.', parent=parent)
        goal_status.clear_frame()
        goal_status.show_data()
        bd.disconnect()


class Complementar_tree:
    def __init__(self):
        self.hex_col, self.selection = None, None

    def tree_color(self):
        color = colorchooser.askcolor()
        self.hex_col = color[1]

    def tree_insert(self, limit, arg, field, parent, treeview):
        arg = arg.get()
        if len(arg) >= limit:
            messagebox.showerror('Erro', f'O campo em questão só permite {limit - 1} caracteres.', parent=parent)
            field.delete(0, END)
        elif self.hex_col is None:
            messagebox.showerror('Erro', f'Não foi escolhida uma cor para a categoria.', parent=parent)
        else:
            bd.connect()
            test_name = bd.simple_select('category', 'name')
            result = 0
            bd.disconnect()
            for name in test_name[1]:
                arg = arg.lstrip()
                arg = arg.strip()
                if arg == name:
                    messagebox.showerror('Erro', 'O nome da categoria informado já existe, escolha outro', parent=parent)
                    field.delete(0, END)
                    result = 1
                    break
                else:
                    pass
            arg = arg.lstrip()
            arg = arg.strip()
            if arg == '':
                messagebox.showerror('Erro', 'Campo de categoria vazio.', parent=parent)
                field.delete(0, END)
                result = 1
            if result == 0:
                treeview.tag_configure(f'{self.hex_col}', background=self.hex_col, foreground='white')
                treeview.insert('', 'end', values=(arg, 'a', 'a'), tags=(f'{self.hex_col}',))
                bd.connect()
                bd.insert_cat(arg, self.hex_col)
                self.hex_col = None
                bd.disconnect()
                messagebox.showinfo('Sucesso!', f'A categoria {arg} foi cadastrada no programa!', parent=parent)
                field.delete(0, END)
            else:
                pass

    def delete_tree(self, treeview, parent):
        try:
            self.selection = treeview.item(treeview.focus())
            bd.connect()
            bd.delete_cat(self.selection['tags'][0])
            bd.disconnect()
        except IndexError:
            if self.selection is None:
                messagebox.showerror('Erro', 'Nenhum registro selecionado para remoção.', parent=parent)
                self.selection = None
            else:
                messagebox.showerror('Erro de execução', 'Ocorreu um pequeno erro na solicitação, por favor, feche e abra novamente esta janela.', parent=parent)
                self.selection = None
        else:
            messagebox.showinfo('Sucesso!', 'Categoria selecionada foi removida, o histórico dela no calendário será preservado (se houver)', parent=parent)
            treeview.delete(treeview.focus())
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
            messagebox.showinfo('Escala definida!',
                                'Tudo certo agora, aproveite seus estudos (7 dias direto é para pessoas estudiosas mesmo hein!)',
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
            messagebox.showerror('Erro na escolha',
                                 'Quantidade dias definidos é diferente do definido na janela anterior.',
                                 parent=parent)
            self.study = []
        else:
            messagebox.showinfo('Dias registrados', 'O(s) dia(s) de folga é(são) o(s) não escolhido(s).',
                                parent=parent)
            bd.connect()
            bd.insert_week(choose_s, choose_d, choose_m, choose_y, self.week)
            bd.disconnect()
            parent.destroy()
            self.study, self.week = [], []
            for variable in range(0, len(self.variables)):
                self.variables[variable].set(0)


def registry_condition(parent, mon, yea, eff, field, cat):
    if cat == '':
        messagebox.showerror('Erro no cadastro da condição',
                             'Não foi informada uma categoria para aplicar a efetividade.',
                             parent=parent)
        field.delete(0, END)
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
            v_eff = float(v_eff)
            if v_eff < 0:
                messagebox.showerror('Erro no registro da efetividade',
                                     'Valor passado é negativo, não sendo possível o uso.',
                                     parent=parent)
                field.delete(0, END)
            elif v_eff > 100:
                messagebox.showerror('Erro no registro da efetividade',
                                     'Valor informado é maior que 100%', parent=parent)
                field.delete(0, END)
            else:
                bd.connect()
                confirm = bd.insert_effectivity(v_eff, cat, mon.get(), yea.get())
                bd.disconnect()
                if confirm == 0:
                    messagebox.showinfo('Sucesso!',
                                        f'Efetividade de {v_eff}% para a categoria {cat.upper()} durante o período do mês {mon.get()} de {yea.get()} inserida com sucesso!',
                                        parent=parent)
                    field.delete(0, END)
                else:
                    messagebox.showinfo('Sucesso!',
                                        f'A efetividade para a categoria {cat.upper()} durante o período do mês {mon.get()} de {yea.get()} foi atualizad para {v_eff}%!',
                                        parent=parent)
                    field.delete(0, END)


dates = Issue_date()


class Comment_show_window:
    def __init__(self):
        self.window, self.frame1, self.scroll = None, None, None
        self.label1, self.actual_day = None, None
        self.button = []

    def screen(self):
        self.window.title('Comentários')
        self.window.configure(background=colors(1))
        self.window.geometry('300x300+400+50')
        self.window.resizable(False, False)
        self.window.maxsize(width=300, height=300)
        self.window.minsize(width=300, height=300)
        self.window.iconbitmap('images/girl.ico')

    def frame(self):
        self.frame1 = Frame(self.window, bg=colors(2))
        self.frame1.place(relx=0.04, rely=0.04, relwidth=0.92, relheight=0.92)

    def scroll_bar(self):
        self.scroll = Scrollbar(self.frame1, orient=VERTICAL)
        self.scroll.pack(side=RIGHT, fill=Y)

    def label(self):
        self.label1 = Label(self.frame1, text=f'Comentários do dia {self.actual_day}', font=('Calibri', 13, 'bold'), bg=colors(2),
                            fg=colors(1))
        self.label1.place(relx=0.20, rely=0.03, relwidth=0.60)

    def editable_label(self, content, ids, actual_month, day_reg, class_month=None, frame_month=None):
        self.window = Toplevel()
        self.actual_day = day_reg
        self.screen()
        self.frame()
        self.label()
        self.scroll_bar()
        self.button = []
        rely, rely_button = 0.15, 0.15
        #list to insert comments and working scrollbar
        my_list = Text(self.frame1, yscrollcommand=self.scroll.set, bg=colors(3), fg=colors(1), font=('Calibri', 11), borderwidth=2, relief='groove', wrap=WORD)
        my_list.tag_configure('center', justify='center')
        #-
        if len(content) > 1:
            for item in range(0, len(content)):
                # button for deletion of comment if actual month is same to system
                if actual_month == month and dates.year == year:
                    self.button.append(Button(my_list, text=f'{item + 1}', fg=colors(2), font=('calibri', 9), bg=colors(5),
                                              command=lambda i=ids[item][0], p=item + 1: self.del_comments(i, p, class_month, frame_month)))
                    my_list.window_create('end', window=self.button[item])
                #-
                else:
                    pass
                my_list.insert(END, '° comentário:\n')
                my_list.insert(END, content[item] + '\n\n')
                my_list.place(relx=0.125, rely=rely, relwidth=0.75, relheight=0.85)
                my_list.tag_add('center', 1.0, 'end')
        else:
            self.label1['text'] = f'Comentário do dia {self.actual_day}'
            my_list.insert(END, content[0])
            my_list.place(relx=0.125, rely=rely + 0.175, relwidth=0.75, relheight=0.35)
            my_list.tag_add('center', 1.0, 'end')
            # button for deletion of comment if actual month is same to system
            if actual_month == month and dates.year == year:
                button = Button(self.frame1, text='x', fg=colors(2), font=('calibri', 9), bg=colors(5),
                                command=lambda i=ids[0][0], p=1: self.del_comments(i, p, class_month, frame_month))
                button.place(relx=0.06, relwidth=0.05, relheight=0.05, rely=rely + 0.18)
            else:
                pass
            #-
        my_list.configure(state='disabled')
        self.scroll.config(command=my_list.yview)
        self.window.mainloop()

    def del_comments(self, ids, pos, class_up, frame):
        answer = messagebox.askyesno('Confirme a ação', f'Você tem certeza que deseja deletar o comentário de número {pos} deste dia?', parent=self.window)
        if answer:
            bd.connect()
            bd.del_comment(ids)
            bd.disconnect()
            messagebox.showinfo('Sucesso!', 'Comentário foi excluído do programa.', parent=self.window)
            self.window.destroy()
            if class_up is None or frame is None:
                pass
            else:
                class_up.day_month_system(frame=frame, original_obj=class_up)
        else:
            messagebox.showinfo('Ação não executada', 'Comentário foi preservado conforme desejado', parent=self.window)


window_aux = Comment_show_window()


class Days_month:
    def __init__(self, window):
        self.window_parent = window
        self.all_days, self.number_day, self.name_day = [], [], []
        self.com_button, self.cal_reg = [], []
        self.week_day, self.week_day_name = [], ['seg', 'ter', 'qua', 'qui', 'sex', 'sab', 'dom']
        self.advance_right, self.control_cal = 0, 0
        self.img_view, self.base_obj = None, None

    def day_month_system(self, frame, original_obj):
        self.base_obj = original_obj
        self.all_days, self.number_day, self.name_day, self.com_button, self.cal_reg, self.control_cal = [], [], [], [], [], 0
        self.week_day = []
        control, relx, rely = 0, 0.02, 0.02
        max_width = 100
        aux_button = 0
        unique_day, sup_unique = [], 0
        actual_month = dates.date_month()[0:4]
        bd.connect()
        check_scale = bd.select_two_search('scale', 'week', actual_month[0], year, 'month', 'year')
        if len(check_scale) == 0:
            messagebox.showinfo('Notificação', 'Você ainda não definiu uma escala de estudo, faça isso o quanto antes para melhor aproveitamento!', parent=self.window_parent)
        else:
            pass
        check_scale = bd.show_week_scale(check_scale[0][0])
        print(check_scale[0][7])
        calc_study.month = actual_month[0]
        calc_study.year = year
        verify_com = bd.view_day_comment(dates.date_month()[0], year)
        bd.disconnect()
        img = Image.open('images/comentary_ico.png')
        img_res = img.resize((10, 10))
        self.img_view = ImageTk.PhotoImage(img_res)
        if verify_com[1] == 0:
            pass
        else:
            for item in range(0, verify_com[1]):
                if verify_com[0][sup_unique] not in unique_day:
                    unique_day.append(verify_com[0][sup_unique])
                    sup_unique += 1
                else:
                    sup_unique += 1
            for item in range(0, len(unique_day)):
                bd.connect()
                desc = bd.view_content_comment(unique_day[item], actual_month[0], year)
                ids = bd.view_id_com(unique_day[item], actual_month[0], year)
                bd.disconnect()
                self.com_button.append(Button(frame, image=self.img_view, bg=colors(3), borderwidth=0,
                                              command=lambda c=desc, i=ids, f=frame, d=unique_day[item]: window_aux.editable_label(c, i, actual_month[3], d, self.base_obj, f)))
        for days in range(1, dates.date_month()[1] + 1):
            self.number_day.append(days)
            self.name_day.append(days)
            self.week_day.append(datetime.date(year, actual_month[3], days).weekday())
        for number in range(len(self.number_day)):
            self.all_days.append(number)
            self.all_days[number] = Frame(frame, bd=1, bg=colors(4))
        while True:
            if control >= len(self.all_days):
                break
            else:
                if max_width >= 2:
                    self.name_day[control] = Label(frame, text=f'{self.week_day_name[self.week_day[control]]} - Dia {self.number_day[control]}', fg=colors(5),
                                                   bg=colors(3),
                                                   font=('Calibri', 10, 'bold'))
                    self.name_day[control].place(relx=relx + 0.035, rely=rely - 0.015, relheight=0.03)
                    self.all_days[control].place(relx=relx, rely=rely + 0.015, relwidth=0.10, relheight=0.20)
                    if aux_button < len(unique_day) and len(unique_day) > 0:
                        if self.number_day[control] == unique_day[aux_button]:
                            self.com_button[aux_button].place(relx=relx + 0.02, rely=rely - 0.010)
                            aux_button += 1
                    bd.connect()
                    verify_calendar = bd.choose_three('calendar', 'time', 'cat_ref', 'color_cat', 'day', 'month',
                                                      'year',
                                                      self.number_day[control], actual_month[0], year)
                    bd.disconnect()
                    rely_cal = 0
                    aux_cal = 0
                    if len(verify_calendar) != 0:
                        while True:
                            if aux_cal < len(verify_calendar):
                                self.cal_reg.append(Label(self.all_days[control],
                                                          text=f'{verify_calendar[aux_cal][1]} - {verify_calendar[aux_cal][0]}',
                                                          font=('calibri', 10, 'bold'),
                                                          fg=verify_calendar[aux_cal][2], bg=colors(4), anchor='center', highlightthickness=1, highlightbackground=verify_calendar[aux_cal][2]))
                                self.cal_reg[self.control_cal].place(relx=0.005, rely=rely_cal, relwidth=0.99)
                                self.control_cal += 1
                                aux_cal += 1
                                rely_cal += 0.20
                            else:
                                break
                    max_width -= 14
                    relx += 0.12
                    control += 1
                else:
                    max_width = 100
                    rely += 0.24
                    relx = 0.02
        dates.reset_all()

    def change_month_back(self, hidden_object, label, frame):
        for number in range(0, len(self.all_days)):
            self.all_days[number].place_forget()
            self.name_day[number].place_forget()
        for button in range(0, len(self.com_button)):
            self.com_button[button].place_forget()
        self.all_days, self.number_day, self.name_day, self.com_button, self.week_day = [], [], [], [], []
        control, relx, rely = 0, 0.02, 0.02
        unique_day, sup_unique = [], 0
        max_width = 100
        changing = 1
        bd.connect()
        aux_button = 0
        name_month = dates.date_month(back_time=changing)[0:4]
        verify_com = bd.view_day_comment(name_month[0], dates.year)
        calc_study.month = name_month[0]
        calc_study.year = dates.year
        bd.disconnect()
        img = Image.open('images/comentary_ico.png')
        img_res = img.resize((10, 10))
        self.img_view = ImageTk.PhotoImage(img_res)
        if verify_com[1] == 0:
            pass
        else:
            for item in range(0, verify_com[1]):
                if verify_com[0][sup_unique] not in unique_day:
                    unique_day.append(verify_com[0][sup_unique])
                    sup_unique += 1
                else:
                    sup_unique += 1
            for item in range(0, len(unique_day)):
                bd.connect()
                desc = bd.view_content_comment(unique_day[item], name_month[0], dates.year)
                ids = bd.view_id_com(unique_day[item], name_month[0], dates.year)
                bd.disconnect()
                self.com_button.append(Button(frame, image=self.img_view, bg=colors(3), borderwidth=0,
                                              command=lambda c=desc, i=ids, f=frame, d=unique_day[item]: window_aux.editable_label(c, i, name_month[3], d, self.base_obj, f)))
        label.config(text=f'Agenda de {name_month[0]}/{dates.year}!')
        for days in range(1, dates.date_month(back_time=changing, change_or_not=True)[1] + 1):
            self.number_day.append(days)
            self.name_day.append(days)
            self.week_day.append(datetime.date(dates.year, name_month[3], days).weekday())
        for number in range(len(self.number_day)):
            self.all_days.append(number)
            self.all_days[number] = Frame(frame, bd=1, bg=colors(4))
        while True:
            if control >= len(self.all_days):
                break
            else:
                if max_width >= 2:
                    self.name_day[control] = Label(frame,
                                                   text=f'{self.week_day_name[self.week_day[control]]} - Dia {self.number_day[control]}',
                                                   fg=colors(5),
                                                   bg=colors(3),
                                                   font=('Calibri', 10, 'bold'))
                    self.name_day[control].place(relx=relx + 0.035, rely=rely - 0.015, relheight=0.03)
                    self.all_days[control].place(relx=relx, rely=rely + 0.015, relwidth=0.10, relheight=0.20)
                    if aux_button < len(unique_day) and len(unique_day) > 0:
                        if self.number_day[control] == unique_day[aux_button]:
                            self.com_button[aux_button].place(relx=relx - 0.10, rely=rely - 0.010)
                            aux_button += 1
                    bd.connect()
                    verify_calendar = bd.choose_three('calendar', 'time', 'cat_ref', 'color_cat', 'day', 'month',
                                                      'year',
                                                      self.number_day[control], name_month[0], dates.year)
                    bd.disconnect()
                    rely_cal = 0
                    aux_cal = 0
                    if len(verify_calendar) != 0:
                        while True:
                            if aux_cal < len(verify_calendar):
                                self.cal_reg.append(Label(self.all_days[control],
                                                          text=f'{verify_calendar[aux_cal][1]} - {verify_calendar[aux_cal][0]}',
                                                          font=('calibri', 10, 'bold'),
                                                          fg=verify_calendar[aux_cal][2], bg=colors(4), anchor='center',
                                                          highlightthickness=1,
                                                          highlightbackground=verify_calendar[aux_cal][2]))
                                self.cal_reg[self.control_cal].place(relx=0.005, rely=rely_cal, relwidth=0.99)
                                self.control_cal += 1
                                aux_cal += 1
                                rely_cal += 0.20
                            else:
                                break
                    max_width -= 14
                    relx += 0.12
                    control += 1
                else:
                    max_width = 100
                    rely += 0.24
                    relx = 0.02
        if dates.year == year and (dates.months + dates.future - dates.back) == month:
            hidden_object[0].place(relx=0.85, rely=0.95, relwidth=0.03)
            hidden_object[1].place(relx=0.03, rely=0.945, relwidth=0.10)
            hidden_object[2].place(relx=0.89, rely=0.945, relwidth=0.08)
            hidden_object[3].place(relx=0.50, rely=0.945, relwidth=0.10)
            hidden_object[4].place(relx=0.40, rely=0.945, relwidth=0.10)
            hidden_object[5].place(relx=0.70, rely=0.945)
        else:
            for item in range(0, len(hidden_object)):
                hidden_object[item].place_forget()

    def change_month_future(self, hidden_object, label, frame):
        for number in range(0, len(self.all_days)):
            self.all_days[number].place_forget()
            self.name_day[number].place_forget()
        self.all_days, self.number_day, self.name_day, self.com_button, self.week_day = [], [], [], [], []
        control, relx, rely = 0, 0.02, 0.02
        max_width = 100
        unique_day, sup_unique = [], 0
        changing = 1
        bd.connect()
        aux_button = 0
        name_month = dates.date_month(advance_time=changing)[0:4]
        verify_com = bd.view_day_comment(name_month[0], dates.year)
        calc_study.month = name_month[0]
        calc_study.year = dates.year
        bd.disconnect()
        img = Image.open('images/comentary_ico.png')
        img_res = img.resize((10, 10))
        self.img_view = ImageTk.PhotoImage(img_res)
        if verify_com[1] == 0:
            pass
        else:
            for item in range(0, verify_com[1]):
                if verify_com[0][sup_unique] not in unique_day:
                    unique_day.append(verify_com[0][sup_unique])
                    sup_unique += 1
                else:
                    sup_unique += 1
            for item in range(0, len(unique_day)):
                bd.connect()
                desc = bd.view_content_comment(unique_day[item], name_month[0], dates.year)
                ids = bd.view_id_com(unique_day[item], name_month[0], dates.year)
                bd.disconnect()
                self.com_button.append(Button(frame, image=self.img_view, bg=colors(3), borderwidth=0,
                                              command=lambda c=desc, i=ids, f=frame, d=unique_day[item]: window_aux.editable_label(c, i, name_month[3], d, self.base_obj, f)))
        label.config(text=f'Agenda de {name_month[0]}/{dates.year}!')
        for days in range(1, dates.date_month(advance_time=changing, change_or_not=True)[1] + 1):
            self.number_day.append(days)
            self.name_day.append(days)
            self.week_day.append(datetime.date(dates.year, name_month[3], days).weekday())
        for number in range(len(self.number_day)):
            self.all_days.append(number)
            self.all_days[number] = Frame(frame, bd=1, bg=colors(4))
        while True:
            if control >= len(self.all_days):
                break
            else:
                if max_width >= 2:
                    self.name_day[control] = Label(frame,
                                                   text=f'{self.week_day_name[self.week_day[control]]} - Dia {self.number_day[control]}',
                                                   fg=colors(5),
                                                   bg=colors(3),
                                                   font=('Calibri', 10, 'bold'))
                    self.name_day[control].place(relx=relx + 0.035, rely=rely - 0.015, relheight=0.03)
                    self.all_days[control].place(relx=relx, rely=rely + 0.015, relwidth=0.10, relheight=0.20)
                    if aux_button < len(unique_day) and len(unique_day) > 0:
                        if self.number_day[control] == unique_day[aux_button]:
                            self.com_button[aux_button].place(relx=relx - 0.10, rely=rely - 0.010)
                            aux_button += 1
                    bd.connect()
                    verify_calendar = bd.choose_three('calendar', 'time', 'cat_ref', 'color_cat', 'day', 'month',
                                                      'year',
                                                      self.number_day[control], name_month[0], dates.year)
                    bd.disconnect()
                    rely_cal = 0
                    aux_cal = 0
                    if len(verify_calendar) != 0:
                        while True:
                            if aux_cal < len(verify_calendar):
                                self.cal_reg.append(Label(self.all_days[control],
                                                          text=f'{verify_calendar[aux_cal][1]} - {verify_calendar[aux_cal][0]}',
                                                          font=('calibri', 10, 'bold'),
                                                          fg=verify_calendar[aux_cal][2], bg=colors(4), anchor='center',
                                                          highlightthickness=1,
                                                          highlightbackground=verify_calendar[aux_cal][2]))
                                self.cal_reg[self.control_cal].place(relx=0.005, rely=rely_cal, relwidth=0.99)
                                self.control_cal += 1
                                aux_cal += 1
                                rely_cal += 0.20
                            else:
                                break
                    max_width -= 14
                    relx += 0.12
                    control += 1
                else:
                    max_width = 100
                    rely += 0.24
                    relx = 0.02
        if dates.year == year and (dates.months + dates.future - dates.back) == month:
            hidden_object[0].place(relx=0.85, rely=0.95, relwidth=0.03)
            hidden_object[1].place(relx=0.03, rely=0.945, relwidth=0.10)
            hidden_object[2].place(relx=0.89, rely=0.945, relwidth=0.08)
            hidden_object[3].place(relx=0.50, rely=0.945, relwidth=0.10)
            hidden_object[4].place(relx=0.40, rely=0.945, relwidth=0.10)
            hidden_object[5].place(relx=0.70, rely=0.945)
        else:
            for item in range(0, len(hidden_object)):
                hidden_object[item].place_forget()


class content_schedule:
    def __init__(self, base_obj, frame_obj):
        self.base = base_obj
        self.frame = frame_obj
        self.selection, self.search, self.current_day = None, None, None

    def max_char(self, limit, arg, field, cat, days, parent):
        arg = str(arg.get())
        if arg.isnumeric():
            if len(arg) >= limit:
                messagebox.showerror('Erro', f'O campo em questão só permite {limit - 1} números (e do tipo inteiro)', parent=parent)
                field.delete(0, END)
            else:
                bd.connect()
                color = bd.choose_one('category', 'color', 'name', cat)
                if len(color) == 0:
                    messagebox.showerror('Erro', 'Não há uma categoria cadastrada ainda para inserção', parent=parent)
                    field.delete(0, END)
                    bd.disconnect()
                else:
                    confirm = bd.insert_calendar(arg, days, dates.date_month()[0], year, cat, color[0][0])
                    bd.disconnect()
                    if confirm == 0:
                        messagebox.showinfo('Sucesso!', f'Registro da categoria {cat} no dia {days} realizado com sucesso!',
                                            parent=parent)
                        field.delete(0, END)
                        self.base.day_month_system(frame=self.frame, original_obj=self.base)
                    elif confirm == 1:
                        messagebox.showinfo('Atualizado com sucesso',
                                            f'O registro já existente para a categoria {cat} no dia {days} foi atualizado!',
                                            parent=parent)
                        field.delete(0, END)
                        self.base.day_month_system(frame=self.frame, original_obj=self.base)
                    else:
                        messagebox.showerror('Erro no registro', 'Para este dia, já existem 5 categorias cadastras, por esse motivo, '
                                                                 'não será possível cadastrar outra sem remover algum registro.', parent=parent)
                        field.delete(0, END)

        else:
            messagebox.showerror('Erro no campo', 'Só é permitido inserir valores numéricos', parent=parent)
            field.delete(0, END)

    def max_comment(self, limit, arg, field, parent, days, months, years):
        verify_content = ''
        if len(arg) == 0 or arg == '':
            messagebox.showerror('Erro', 'O campo está vazio', parent=parent)
            field.delete(1.0, END)
        elif len(arg) >= limit:
            messagebox.showerror('Erro', f'O campo em questão só permite {limit - 1} caracteres', parent=parent)
            field.delete(1.0, END)
        else:
            for letter in arg:
                if letter == ' ':
                    verify_content = ''
                else:
                    verify_content = 1
            if verify_content == '':
                messagebox.showerror('Erro', 'O campo está vazio preenchido apenas com espaços', parent=parent)
                field.delete(1.0, END)
            else:
                bd.connect()
                bd.insert_comment(arg, days, months, years)
                bd.disconnect()
                messagebox.showinfo('Sucesso!', 'comentário inserido no dia desejado!', parent=parent)
                field.delete(1.0, END)
                self.base.day_month_system(frame=self.frame, original_obj=self.base)

    def delete_registry(self, treeview, days, window):
        try:
            self.selection = treeview.item(treeview.focus())
            bd.connect()
            bd.del_registry(self.selection['tags'][0], days.get(), dates.date_month()[0], year)
            bd.disconnect()
        except IndexError:
            if self.selection is None:
                messagebox.showerror('Erro', 'Nenhum registro selecionado para remoção.', parent=window)
                self.selection = None
            else:
                messagebox.showerror('Erro de execução', 'Ocorreu um pequeno erro na solicitação, por favor, feche e abra novamente esta janela.', parent=window)
                self.selection = None
        else:
            messagebox.showinfo('Sucesso', 'Registro removido!', parent=window)
            treeview.delete(treeview.focus())
            self.selection = None
            self.base.day_month_system(frame=self.frame, original_obj=self.base)

    def find_element(self, treeview, days, window):
        if self.search == 1 and self.current_day == days:
            messagebox.showerror('Ação repetida', f'Os registros do dia {days} já estão na tela (caso exista).', parent=window)
        else:
            self.search = None
            bd.connect()
            cat_day = bd.choose_three('calendar', 'time', 'cat_ref', 'color_cat', 'day', 'month', 'year', days,
                                      dates.date_month()[0], year)
            bd.disconnect()
            if len(cat_day) == 0:
                for item in treeview.get_children():
                    treeview.delete(item)
                messagebox.showerror('Retorno da busca',
                                     f'Nenhum registro localizado para o dia {days} de {dates.date_month()[0]}.',
                                     parent=window)
            else:
                for item in range(0, len(cat_day)):
                    treeview.tag_configure(f'{cat_day[item][1]}', foreground=cat_day[item][2], background=colors(5))
                    treeview.insert('', 'end', values=(cat_day[item][0], cat_day[item][1]), tags=(f'{cat_day[item][1]}',))
        self.search = 1
        self.current_day = days


class Goal_status_window:
    def __init__(self, parent):
        self.frame1, self.label1 = None, None
        self.actual_m, self.window = None, None
        self.parent = parent
        self.view_status()

    def screen(self):
        self.window.title('Status das metas do mês')
        self.window.configure(background=colors(1))
        self.window.geometry('500x300+700+100')
        self.window.resizable(False, False)
        self.window.maxsize(width=500, height=300)
        self.window.minsize(width=500, height=300)
        self.window.iconbitmap('images/girl.ico')

    def frame(self):
        self.frame1 = Frame(self.window, background=colors(2))
        self.frame1.place(relx=0.04, rely=0.04, relwidth=0.92, relheight=0.92)

    def view_status(self):
        match dates.choose_now:
            case 1:
                self.actual_m = 'janeiro'
            case 2:
                self.actual_m = 'fevereiro'
            case 3:
                self.actual_m = 'março'
            case 4:
                self.actual_m = 'abril'
            case 5:
                self.actual_m = 'maio'
            case 6:
                self.actual_m = 'junho'
            case 7:
                self.actual_m = 'julho'
            case 8:
                self.actual_m = 'agosto'
            case 9:
                self.actual_m = 'setembro'
            case 10:
                self.actual_m = 'outubro'
            case 11:
                self.actual_m = 'novembro'
            case 12:
                self.actual_m = 'dezembro'

        bd.connect()
        result = bd.search_goal(self.actual_m, dates.year)
        bd.disconnect()
        if len(result) == 0:
            messagebox.showerror('Erro na execução', 'Para o mês e ano selecionados não há registros de meta para apresentar.', parent=self.parent)
        else:
            self.window = Toplevel()
            self.screen()
            self.frame()
            style = ttk.Style()
            style.configure("Treeview.Heading", background=colors(5), foreground=colors(1))
            style.configure('Treeview', fieldbackground=colors(1), font=('calibri', 12, 'bold'))
            style.map('Treeview', background=[('selected', colors(3))], foreground=[('selected', colors(1))])
            style.configure('Scrollbar')
            tree = ttk.Treeview(self.frame1, height=2, columns=('Categoria', 'Meta', 'Estudado', '% completa'), selectmode='browse', show='headings')
            tree.heading('#0', text='')
            tree.heading('Categoria', text='Categoria')
            tree.heading('Meta', text='Meta')
            tree.heading('Estudado', text='Estudado')
            tree.heading('% completa', text='% completa')
            tree.column('#0', width=1, minwidth=1, stretch=NO)
            tree.column('Categoria', width=120, minwidth=120, stretch=NO, anchor='c')
            tree.column('Estudado', width=100, minwidth=100, stretch=NO, anchor='c')
            tree.column('% completa', width=100, minwidth=100, stretch=NO, anchor='c')
            tree.column('Meta', width=100, minwidth=100, stretch=NO, anchor='c')
            tree.place(relx=0.04, rely=0.04, relheight=0.92, relwidth=0.92)
            tree.bind('<Motion>', 'break')
            for item in range(0, len(result)):
                calc_study.cat = result[item][1]
                actual_time = calc_study.cal_study()
                tree.tag_configure(f'{result[item][1]}', foreground='white', background=result[item][2])
                tree.insert('', 'end', values=(result[item][1], result[item][0], actual_time[0], actual_time[1]), tags=(f'{result[item][1]}',))
            self.window.mainloop()


class Goal_main_view:
    def __init__(self, frame, a_month):
        self.frame = frame
        self.a_month = a_month
        self.actual_m = None

    def show_data(self):
        match self.a_month:
            case 1:
                self.actual_m = 'janeiro'
            case 2:
                self.actual_m = 'fevereiro'
            case 3:
                self.actual_m = 'março'
            case 4:
                self.actual_m = 'abril'
            case 5:
                self.actual_m = 'maio'
            case 6:
                self.actual_m = 'junho'
            case 7:
                self.actual_m = 'julho'
            case 8:
                self.actual_m = 'agosto'
            case 9:
                self.actual_m = 'setembro'
            case 10:
                self.actual_m = 'outubro'
            case 11:
                self.actual_m = 'novembro'
            case 12:
                self.actual_m = 'dezembro'

        bd.connect()
        result = bd.search_goal(self.actual_m, dates.year)
        bd.disconnect()

        if len(result) == 0:
            label = Label(self.frame, text='Ainda não há metas para visualização, por favor, cadastre alguma!', bg=colors(2), fg=colors(5), font=('Calibri', 15, 'underline'),
                          wraplength=200)
            label.place(relx=0.10, rely=0.10)
        else:
            style = ttk.Style()
            style.configure("Treeview.Heading", background=colors(5), foreground=colors(1))
            style.configure('Treeview', fieldbackground=colors(1), font=('calibri', 12, 'bold'))
            style.map('Treeview', background=[('selected', colors(3))], foreground=[('selected', colors(1))])
            style.configure('Scrollbar')
            tree = ttk.Treeview(self.frame, height=2, columns=('Categoria', 'Meta', 'Estudado', '% completa'),
                                selectmode='browse', show='headings')
            tree.heading('#0', text='')
            tree.heading('Categoria', text='Categoria')
            tree.heading('Meta', text='Meta')
            tree.heading('Estudado', text='Feito')
            tree.heading('% completa', text='%')
            tree.column('#0', width=1, minwidth=1)
            tree.column('Categoria', width=87, anchor='c')
            tree.column('Estudado', width=50, anchor='c')
            tree.column('% completa', width=50, anchor='c')
            tree.column('Meta', width=50, anchor='c')
            tree.place(relx=0.04, rely=0.04, relheight=0.92, relwidth=0.92)
            tree.bind('<Motion>', 'break')
            for item in range(0, len(result)):
                calc_study.cat = result[item][1]
                actual_time = calc_study.cal_study()
                tree.tag_configure(f'{result[item][1]}', foreground='white', background=result[item][2])
                tree.insert('', 'end', values=(result[item][1], result[item][0], actual_time[0], actual_time[1]),
                            tags=(f'{result[item][1]}',))

    def clear_frame(self):
        for widget in self.frame.winfo_children():
            widget.destroy()