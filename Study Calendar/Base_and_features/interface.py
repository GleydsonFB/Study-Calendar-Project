from functions_interface import *
from tkinter import *
from tkinter import ttk
from database import *
from PIL import Image, ImageTk
import webbrowser

# Here that the magic happen. Different to another modules, here i only focus to explain classes.
# The reason for it because all methods don't work alone and is necessary summon class complete.

# This block is about all classes summoned for database or functions_interface modules.
color_helper = Complementar_tree()
base = Database()
base.connect()
base.table_create()
dats = Issue_date()
rr = Registry_rule()
cs = Choose_scale()
dm = Days_month()
content_s = content_schedule(dm)
goal_main_v = Goal_main_view(None, None)
# -


class Main_window:
    """
    The core of program. Main_window keeps work program (if u close she, all windows come down).
    """
    def __init__(self):
        window = Tk()
        self.frame1, self.category, self.frame2 = None, None, None
        self.label1, self.label2, self.frame3 = None, None, None
        self.window = window
        self.frame()
        self.screen()
        self.button()
        style = ttk.Style()
        style.theme_use('clam')
        goal_main_v.frame = self.frame2
        goal_main_v.a_month = month
        goal_main_v.show_data()
        cs.goal_m = goal_main_v
        rr.goal_m = goal_main_v
        self.additional()
        self.window.mainloop()

    def screen(self):
        self.window.title('Organizador de estudos')
        self.window.configure(background=colors(1))
        self.window.geometry('321x532+50+50')
        self.window.maxsize(width=321, height=532)
        self.window.minsize(width=321, height=532)
        self.window.resizable(False, False)
        self.window.iconbitmap('images/girl.ico')

    def frame(self):
        self.frame1 = Frame(self.window, bd=1, bg=colors(2), highlightbackground=colors(3), highlightthickness=2)
        self.frame1.place(relx=0.04, rely=0.04, relwidth=0.92, relheight=0.70)
        self.frame2 = Frame(self.window, bd=1, bg=colors(2), highlightbackground=colors(3), highlightthickness=2)
        self.frame2.place(relx=0.08, rely=0.76, relwidth=0.84, relheight=0.22)
        self.frame3 = Frame(self.frame1, bd=1, bg=colors(3), highlightbackground=colors(4), highlightthickness=2)
        self.frame3.place(relx=0.20, rely=0.38, relwidth=0.60, relheight=0.61)

    def button(self):
        self.category = Button(self.frame1, text='Gerenciar categorias', bd=2, bg=colors(4), fg=colors(1),
                               font=('Calibri', 10, 'bold'), command=Category_window)
        self.category.place(relx=0.225, rely=0.40, relwidth=0.55)
        self.category = Button(self.frame1, text='Consultar agenda', bd=2, bg=colors(4), fg=colors(1),
                               font=('Calibri', 10, 'bold'),
                               command=Schedule_window)
        self.category.place(relx=0.225, rely=0.50, relwidth=0.55)
        self.category = Button(self.frame1, text='Definir metas', bd=2, bg=colors(4), fg=colors(1),
                               font=('Calibri', 10, 'bold'), command=Goal_window)
        self.category.place(relx=0.225, rely=0.60, relwidth=0.55)
        self.category = Button(self.frame1, text='Escolher regras', bd=2, bg=colors(4), fg=colors(1),
                               font=('Calibri', 10, 'bold'), command=Rule_window)
        self.category.place(relx=0.225, rely=0.70, relwidth=0.55)
        self.category = Button(self.frame1, text='Feedback/FAQ', bd=2, bg=colors(4), fg=colors(1),
                               font=('Calibri', 10, 'bold'), command=lambda: webbrowser.open('https://calendario-estudos.netlify.app/', new=2))
        self.category.place(relx=0.225, rely=0.80, relwidth=0.55)
        self.category = Button(self.frame1, text='LinkedIn do desenvolvedor', bd=2, bg=colors(4), fg=colors(1),
                               font=('Calibri', 10, 'bold'),
                               command=lambda: webbrowser.open('https://www.linkedin.com/in/gleydsonfreitas/', new=2))
        self.category.place(relx=0.225, rely=0.90, relwidth=0.55)

    def additional(self):
        self.label1 = Label(self.frame1,
                            text=f'BEM VINDO(A) AO \nAPLICATIVO QUE TE AJUDA A\nORGANIZAR SUA \nVIDA ACADÊMICA!',
                            fg=colors(5), bg=colors(2),
                            font=('Calibri', 15, 'bold'))
        self.label1.place(relx=0.05, rely=0.01)
        self.label2 = Label(self.frame1, text='Selecione uma das opções abaixo', fg=colors(5), bg=colors(2),
                            font=('Calibri', 12))
        self.label2.place(relx=0.12, rely=0.30)


class Schedule_window:
    """
    The class of schedule, with she, we can see our studies and another elements.
    """
    def __init__(self):
        self.all_days, self.number_day, self.name_day = None, None, None
        self.frame1, self.label1, self.frame2 = None, None, None
        self.bt_left, self.bt_right, self.label2 = None, None, None
        window1 = Toplevel()
        self.window = window1
        self.screen()
        self.frame()
        self.label()
        dm.window_parent = self.window
        dm.principal_frame = self.frame2
        dates.reset_all()
        dm.day_month_system(dm)
        cs.parent = self.window
        cs.base = dm
        dm.off_system = cs
        content_s.goal_m = goal_main_v
        cs.frame = self.frame2
        self.button()
        self.window.mainloop()

    def screen(self):
        self.window.title('Agenda de acompanhamento')
        self.window.configure(background=colors(1))
        largura = self.window.winfo_screenwidth()
        altura = self.window.winfo_screenheight()
        self.window.geometry(f'{largura}x{altura}')
        self.window.state('zoomed')
        self.window.minsize(width=largura, height=altura)
        self.window.iconbitmap('images/girl.ico')

    def frame(self):
        self.frame1 = Frame(self.window, bd=1, bg=colors(2), highlightbackground=colors(3), highlightthickness=2)
        self.frame1.place(relx=0.04, rely=0.04, relwidth=0.92, relheight=0.92)
        self.frame2 = Frame(self.frame1, bd=1, bg=colors(3), highlightbackground=colors(4), highlightthickness=2)
        self.frame2.place(relx=0.04, rely=0.06, relwidth=0.92, relheight=0.88)

    def label(self):
        self.label1 = Label(self.frame1, text=f'Agenda de {dats.date_month()[0]}/{year}!', fg=colors(5),
                            font=('Calibri', 15, 'bold'),
                            bg=colors(2))
        self.label1.place(relx=0.35, relwidth=0.30)
        self.label2 = Label(self.frame1, text='Registre uma folga para o dia', fg=colors(5),
                            font=('Calibri', 11, 'bold'),
                            bg=colors(2))
        self.label2.place(relx=0.70, rely=0.945)

    def button(self):
        #images for buttons
        load_img1 = Image.open('images/b_left_schudule.png')
        resize_img1 = load_img1.resize((40, 40))
        self.bt_left = ImageTk.PhotoImage(resize_img1)
        load_img2 = Image.open('images/b_right_schedule.png')
        resize_img2 = load_img2.resize((40, 40))
        self.bt_right = ImageTk.PhotoImage(resize_img2)

        #simple buttons
        button1 = Button(self.frame1, text='Registrar estudo', fg=colors(5), font=('Calibri', 11, 'bold'),
                         bg=colors(2), command=Registry_window)
        button1.place(relx=0.40, rely=0.945, relwidth=0.10)
        button2 = Button(self.frame1, text='Apagar estudo', fg=colors(5), font=('Calibri', 11, 'bold'),
                         bg=colors(2), command=Remove_elem_window)
        button2.place(relx=0.50, rely=0.945, relwidth=0.10)
        button5 = Button(self.frame1, text='Inserir folga', fg=colors(5), font=('Calibri', 9, 'bold'),
                         bg=colors(2), command=lambda: cs.insert_off(int(combo.get())))
        button5.place(relx=0.89, rely=0.945, relwidth=0.08)
        button6 = Button(self.frame1, text='Inserir comentário', fg=colors(5), font=('Calibri', 9, 'bold'),
                         bg=colors(2), command=Commentary_window)
        button6.place(relx=0.03, rely=0.945, relwidth=0.10)
        button7 = Button(self.frame1, text='Metas', fg=colors(5), font=('Calibri', 12, 'bold'),
                         bg=colors(2), command=lambda: Goal_status_window(self.window))
        button7.place(relx=0.86, rely=0.75)
        #custom buttons
        button3 = Button(self.window, image=self.bt_left, bg=colors(2), borderwidth=0,
                         command=lambda: dm.change_month_back((combo, button6, button5, button2, button1,
                                                               self.label2), self.label1))
        button3.place(relx=0.045, rely=0.042)
        button4 = Button(self.window, image=self.bt_right, bg=colors(2), borderwidth=0,
                         command=lambda: dm.change_month_future((combo, button6, button5, button2, button1,
                                                                 self.label2), self.label1))
        button4.place(relx=0.925, rely=0.042)

        # combo days for day offs
        list_day = dats.day_registry()
        combo = ttk.Combobox(self.frame1, values=list_day, state='readonly', background=colors(5))
        combo.set(list_day[dats.date_month()[2] - 1])
        combo.place(relx=0.85, rely=0.95, relwidth=0.03)


class Category_window:
    """
    Class to insert and remove categories.
    """
    def __init__(self):
        window2 = Toplevel()
        self.hex_col, self.frame1, self.listt = None, None, None
        self.var = StringVar()
        self.window = window2
        self.frame()
        self.tree_view()
        self.field()
        self.entry_button()
        self.screen()
        self.window.mainloop()

    def screen(self):
        self.window.title('Categorias')
        self.window.configure(background=colors(1))
        self.window.geometry('321x321+400+50')
        self.window.maxsize(width=321, height=321)
        self.window.minsize(width=321, height=321)
        self.window.resizable(False, False)
        self.window.iconbitmap('images/girl.ico')

    def frame(self):
        self.frame1 = Frame(self.window, bg=colors(1))
        self.frame1.place(relx=0.10, rely=0.10, relwidth=0.80, relheight=0.80)

    def tree_view(self):
        style = ttk.Style()
        style.configure("Treeview.Heading", background=colors(5), foreground=colors(1))
        style.configure('Treeview', fieldbackground=colors(1), font=('calibri', 12, 'bold'))
        style.map('Treeview', background=[('selected', colors(3))], foreground=[('selected', colors(1))])
        style.configure('Scrollbar')
        self.listt = ttk.Treeview(self.frame1, height=3, columns=('Nome da categoria', 'vazio'), selectmode='browse',
                                  show='headings')
        self.listt.heading('#0', text='')
        self.listt.heading('Nome da categoria', text='Categorias cadastradas')
        self.listt.heading('vazio', text='')
        self.listt.column('#0', width=1, minwidth=1)
        self.listt.column('Nome da categoria', width=231, minwidth=231, anchor='c')
        self.listt.column('vazio', width=1, minwidth=1)
        self.listt.place(relx=0.04, rely=0.35, relwidth=0.92, relheight=0.58)
        self.listt.bind('<Motion>', 'break')
        show_tree(self.listt)

    def field(self):
        label = Label(self.frame1, text='Digite o nome da nova categoria', font=('Calibri', 10, 'bold'),
                      fg=colors(5), bg=colors(1))
        label.place(relx=0.04, rely=0.10)
        label1 = Label(self.window, text='Gerenciamento de categorias', font=('Calibri', 12, 'bold'),
                       fg=colors(5), bg=colors(1))
        label1.place(relx=0.125, relwidth=0.75, rely=0.05)

    def entry_button(self):
        entry1 = Entry(self.frame1, textvariable=self.var, bg=colors(5))
        entry1.place(relx=0.05, rely=0.20, relwidth=0.30, relheight=0.10)
        button2 = Button(self.frame1, text='Escolha a cor', command=color_helper.tree_color,
                         bg=colors(2), fg=colors(5), font=('Calibri', 9, 'bold'))
        button2.place(relx=0.40, rely=0.20, relheight=0.10)
        button1 = Button(self.frame1, text='Insira', bg=colors(2), fg=colors(5), font=('Calibri', 9, 'bold'),
                         command=lambda: color_helper.tree_insert(13, self.var, entry1, self.window, self.listt))
        button1.place(relx=0.75, rely=0.20, relheight=0.10)
        button3 = Button(self.window, text='Remover selecionada', bg=colors(2), fg=colors(5),
                         font=('Calibri', 9, 'bold'),
                         command=lambda: color_helper.delete_tree(self.listt, self.window))
        button3.place(relx=0.20, rely=0.90, relwidth=0.60)


class Registry_window:
    """
    Auxiliar class to Schedule_window, she is responsible for registry any studies.
    """
    def __init__(self):
        window3 = Toplevel()
        self.frame1 = None
        self.var = StringVar()
        self.window = window3
        self.screen()
        self.frame()
        dats.months = dates.choose_now
        self.insert_time()
        self.label()
        self.window.mainloop()

    def screen(self):
        self.window.title('Registrar estudo')
        self.window.configure(background=colors(1))
        width = (self.window.winfo_screenwidth() * 0.5)
        self.window.geometry(f'321x321+{width:.0f}+50')
        self.window.maxsize(width=321, height=321)
        self.window.minsize(width=321, height=321)
        self.window.resizable(False, False)
        self.window.iconbitmap('images/girl.ico')

    def frame(self):
        self.frame1 = Frame(self.window, bd=1, bg=colors(2), highlightbackground=colors(3), highlightthickness=2)
        self.frame1.place(relx=0.04, rely=0.06, relwidth=0.92, relheight=0.88)

    def insert_time(self):
        content_category = insert_combo()
        if content_category is None:
            content_category = ['Nenhuma inserida']
        #combo and entry
        combo = ttk.Combobox(self.frame1, values=content_category, state='readonly', background=colors(5))
        combo.set(content_category[0])
        combo.place(relx=0.25, rely=0.18, relwidth=0.50)
        entry = Entry(self.frame1, textvariable=self.var, bg=colors(5))
        entry.place(relx=0.375, rely=0.38, relwidth=0.25)

        #date registry
        list_day = dats.day_registry()
        combo1 = ttk.Combobox(self.frame1, values=list_day, state='readonly', background=colors(5))
        if dats.months == month:
            combo1.set(list_day[dats.date_month()[2] - 1])
        else:
            combo1.set(1)
        combo1.place(relx=0.25, rely=0.60, relwidth=0.15)

        button = Button(self.frame1, text='Inserir',
                        command=lambda: content_s.insert_study(4, self.var, entry, combo.get(), combo1.get(),
                                                               self.window),
                        bg=colors(2), fg=colors(5), font=('Calibri', 13, 'bold'))
        button.place(relx=0.375, rely=0.80, relwidth=0.25)

    def label(self):
        label1 = Label(self.frame1, text='Escolha a categoria', font=('Calibri', 12, 'bold'), fg=colors(5),
                       bg=colors(2))
        label1.place(relx=0.25, relwidth=0.50, rely=0.05)
        label2 = Label(self.frame1, text='Defina o tempo estudado em minutos', font=('Calibri', 12, 'bold'),
                       fg=colors(5),
                       bg=colors(2))
        label2.place(relx=0.05, rely=0.30, relwidth=0.90)
        label3 = Label(self.frame1, text='Determine a data do estudo', font=('Calibri', 12, 'bold'),
                       fg=colors(5), bg=colors(2))
        label3.place(relx=0.15, rely=0.50)
        label4 = Label(self.frame1, text=f'/{dats.date_month()[0]}/{dates.year}', font=('Calibri', 12, 'bold'),
                       fg=colors(5), bg=colors(2))
        label4.place(relx=0.40, rely=0.60)


class Commentary_window:
    """
    Class support to Schedule_window, she allows insert commentaries.
    """
    def __init__(self):
        window3 = Toplevel()
        self.frame1 = None
        self.var = StringVar()
        self.window = window3
        self.screen()
        self.frame()
        dats.months = dates.choose_now
        self.insert_comment()
        self.label()
        self.window.mainloop()

    def screen(self):
        self.window.title('Comentar estudo')
        self.window.configure(background=colors(1))
        width = (self.window.winfo_screenwidth() * 0.5)
        self.window.geometry(f'321x321+{width:.0f}+50')
        self.window.maxsize(width=321, height=321)
        self.window.minsize(width=321, height=321)
        self.window.resizable(False, False)
        self.window.iconbitmap('images/girl.ico')

    def frame(self):
        self.frame1 = Frame(self.window, bd=1, bg=colors(2), highlightbackground=colors(3), highlightthickness=2)
        self.frame1.place(relx=0.04, rely=0.06, relwidth=0.92, relheight=0.88)

    def insert_comment(self):
        #combo and entry
        day_list = dats.day_registry()
        combo = ttk.Combobox(self.frame1, values=day_list, state='readonly', background=colors(5))
        combo.set(dats.day_registry()[day - 1])
        combo.place(relx=0.425, rely=0.18, relwidth=0.15)
        comment_text = Text(self.frame1, bg=colors(5), font=('calibri', 10), foreground='green')
        comment_text.place(relx=0.10, rely=0.38, relwidth=0.80, relheight=0.41)
        button = Button(self.frame1, text='Inserir',
                        command=lambda: content_s.max_comment(254, comment_text.get(1.0, 'end-1c'),
                                                              comment_text, self.window, combo.get(),
                                                              dats.date_month()[0], dates.year),
                        bg=colors(2), fg=colors(5), font=('Calibri', 13, 'bold'))
        button.place(relx=0.375, rely=0.80, relwidth=0.25)

    def label(self):
        label1 = Label(self.frame1, text='Escolha o dia para registrar o comentário', font=('Calibri', 12, 'bold'),
                       fg=colors(5), bg=colors(2))
        label1.place(relx=0.00, rely=0.05)
        label2 = Label(self.frame1, text='Faça seu comentário', font=('Calibri', 12, 'bold'), fg=colors(5),
                       bg=colors(2))
        label2.place(relx=0.125, rely=0.25, relwidth=0.75)


class Remove_elem_window:
    """
    Similar to Registry_window, she is focus on remove studies.
    """
    def __init__(self):
        window4 = Toplevel()
        self.frame1, self.tree, self.combo = None, None, None
        self.var = StringVar()
        self.window = window4
        self.screen()
        self.frame()
        dats.months = dates.choose_now
        self.label_button()
        self.tree_view()
        content_s.search = None
        self.window.mainloop()

    def screen(self):
        self.window.title('Apagar estudo')
        self.window.configure(background=colors(1))
        width = (self.window.winfo_screenwidth() * 0.5) + 322
        self.window.geometry(f'321x321+{width:.0f}+50')
        self.window.maxsize(width=321, height=321)
        self.window.minsize(width=321, height=321)
        self.window.resizable(False, False)
        self.window.iconbitmap('images/girl.ico')

    def frame(self):
        self.frame1 = Frame(self.window, bd=1, bg=colors(2), highlightbackground=colors(3), highlightthickness=2)
        self.frame1.place(relx=0.04, rely=0.06, relwidth=0.92, relheight=0.88)

    def label_button(self):
        label = Label(self.frame1, text='escolha o dia do mês', font=('Calibri', 12, 'bold'), fg=colors(5),
                      bg=colors(2))
        label.place(relx=0.25, rely=0.06, relwidth=0.50)
        label1 = Label(self.frame1, text=f'/{dats.date_month()[0]}/{year}', font=('Calibri', 12, 'bold'), fg=colors(5),
                       bg=colors(2))
        label1.place(relx=0.40, rely=0.20)
        list_day = dats.day_registry()
        self.combo = ttk.Combobox(self.frame1, values=list_day, state='readonly', background=colors(5))
        self.combo.set(list_day[dats.date_month()[2] - 1])
        self.combo.place(relx=0.25, rely=0.20, relwidth=0.15)
        button = Button(self.frame1, text='Buscar', bg=colors(2), fg=colors(5), font=('Calibri', 10, 'bold'),
                        command=lambda: content_s.find_study(self.tree, self.combo.get(), self.window))
        button.place(relx=0.40, rely=0.30, relwidth=0.20)

    def tree_view(self):
        style = ttk.Style()
        style.configure("Treeview.Heading", background=colors(3), foreground=colors(1))
        style.configure('Treeview', fieldbackground=colors(5), font=('calibri', 12, 'bold'))
        style.map('Treeview', background=[('selected', colors(1))], foreground=[('selected', colors(5))])
        style.configure('Scrollbar')
        self.tree = ttk.Treeview(self.frame1, height=3, columns=('Duração', 'Categoria'), selectmode='browse',
                                 show='headings')
        self.tree.heading('#0', text='')
        self.tree.heading('Duração', text='Minutos')
        self.tree.heading('Categoria', text='Categoria')
        self.tree.column('#0', width=1, minwidth=1)
        self.tree.column('Duração', width=60, minwidth=60, anchor='c')
        self.tree.column('Categoria', width=201, minwidth=200, anchor='c')
        self.tree.place(relx=0.04, rely=0.40, relwidth=0.92, relheight=0.50)
        self.tree.bind('<Motion>', 'break')
        button_tree = Button(self.frame1, text='Remover registro', bg=colors(2), fg=colors(5),
                             font=('Calibri', 10, 'bold'),
                             command=lambda: content_s.delete_study(self.tree, self.combo, self.window))
        button_tree.place(relx=0.30, rely=0.905, relwidth=0.40)


class Goal_window:
    """
    Window to insert and remove goals.
    """
    def __init__(self):
        window5 = Toplevel()
        self.frame1, self.frame2 = None, None
        self.var, self.category, self.month, self.year = StringVar(), StringVar(), StringVar(), StringVar()
        self.month2, self.year2, self.category2 = StringVar(), StringVar(), StringVar()
        self.window = window5
        self.var_r = IntVar(self.window)
        self.screen()
        self.frame()
        self.label()
        self.button_remove_goal()
        self.window.mainloop()

    def screen(self):
        self.window.title('Definir metas')
        self.window.configure(background=colors(1))
        self.window.geometry(f'300x300+400+50')
        self.window.maxsize(width=600, height=321)
        self.window.minsize(width=600, height=321)
        self.window.resizable(False, False)
        self.window.iconbitmap('images/girl.ico')

    def frame(self):
        self.frame1 = Frame(self.window, bd=1, bg=colors(2), highlightbackground=colors(3), highlightthickness=2)
        self.frame1.place(relx=0.04, rely=0.04, relwidth=0.42, relheight=0.92)
        self.frame2 = Frame(self.window, bd=1, bg=colors(2), highlightthickness=2, highlightbackground=colors(3))
        self.frame2.place(relx=0.54, rely=0.04, relwidth=0.42, relheight=0.92)

    def label(self):
        #Registry feature
        label = Label(self.frame1, text='Registrar', font=('Calibri', 12, 'bold'), fg=colors(5), bg=colors(2))
        label.place(relx=0.375, rely=0.01, relwidth=0.25)
        info = Label(self.frame1, text='Escolha como quer fazer o cálculo da meta (manual ou automaticamente)',
                     font=('Calibri', 11, 'bold'), fg=colors(5), bg=colors(2), wraplength=200)
        info.place(relx=0.10, rely=0.20)
        info1 = Label(self.frame1, text='Se tiver alguma dúvida quanto ao procedimento, por favor, consulte a FAQ.',
                      font=('Calibri', 11, 'bold'), fg=colors(5), bg=colors(2), wraplength=200)
        info1.place(relx=0.10, rely=0.65)
        # choose type registry
        radio = Radiobutton(self.frame1, text='Automático', bg=colors(5), fg=colors(2), font=('Calibri', 10, 'bold'),
                            variable=self.var_r, value=1)
        radio.place(relx=0.10, rely=0.50)
        radio1 = Radiobutton(self.frame1, text='Manual', bg=colors(5), fg=colors(2), font=('Calibri', 10, 'bold'),
                             variable=self.var_r, value=2)
        radio1.place(relx=0.65, rely=0.50)
        button = Button(self.frame1, text='Confirmar', bg=colors(2), fg=colors(5), font=('Calibri', 11, 'bold'),
                        command=lambda: self.new_frame_content(self.var_r.get()))
        button.place(relx=0.35, rely=0.88, relwidth=0.30)

        # -

        #delete feature
        label5 = Label(self.frame2, text='Remover', font=('Calibri', 12, 'bold'), fg=colors(5), bg=colors(2))
        label5.place(relx=0.375, rely=0.01, relwidth=0.25)
        label6 = Label(self.frame2, text='Selecione a categoria', font=('Calibri', 12, 'bold'),
                       fg=colors(5), bg=colors(2))
        label6.place(relx=0.10, rely=0.15)
        label7 = Label(self.frame2, text='Escolha o mês e ano', font=('Calibri', 12, 'bold'), fg=colors(5),
                       bg=colors(2))
        label7.place(relx=0.10, rely=0.40)
        label8 = Label(self.frame2, text='Por fim clique no botão para buscar um registro',
                       font=('Calibri', 12, 'bold'), fg=colors(5), bg=colors(2), wraplength=200)
        label8.place(relx=0.15, rely=0.65)

    def button_remove_goal(self):
        mon = month_combo()
        yea = year_combo()
        content_combo2 = insert_combo_choose('goal', 'cat_ref')
        combo3 = ttk.Combobox(self.frame2, values=content_combo2, state='readonly', background=colors(5),
                              textvariable=self.category2)
        combo3.place(relx=0.10, rely=0.25)
        combo4 = ttk.Combobox(self.frame2, values=mon, state='readonly', background=colors(5), textvariable=self.month2)
        combo4.set(mon[month - 1])
        combo4.place(relx=0.10, rely=0.50, relwidth=0.30)
        combo5 = ttk.Combobox(self.frame2, values=yea, state='readonly', background=colors(5), textvariable=self.year2)
        combo5.set(yea[year - 2023])
        combo5.place(relx=0.45, rely=0.50, relwidth=0.20)
        button2 = Button(self.frame2, text='Buscar', bg=colors(2), fg=colors(5),
                         font=('Calibri', 11, 'bold'),
                         command=lambda: delete_goal(self.window, self.month2.get(), self.year2.get(),
                                                     self.category2.get(), goal_main_v))
        button2.place(relx=0.30, relwidth=0.40, rely=0.85)

    def new_frame_content(self, option):
        def clear_frame(frame):
            for widget in frame.winfo_children():
                widget.destroy()
        clear_frame(self.frame1)
        # if choose is automatic:
        if option == 1:
            label = Label(self.frame1, text='Registrar', font=('Calibri', 12, 'bold'), fg=colors(5), bg=colors(2))
            label.place(relx=0.375, rely=0.01, relwidth=0.25)
            label1 = Label(self.frame1, text='Escolha a categoria', font=('Calibri', 12, 'bold'), fg=colors(5),
                           bg=colors(2))
            label1.place(relx=0.10, rely=0.15)
            label2 = Label(self.frame1, text='Quanto tempo quer estudar por dia?', font=('Calibri', 12, 'bold'),
                           fg=colors(5), bg=colors(2), wraplength=200)
            label2.place(relx=0.05, rely=0.35)
            label3 = Label(self.frame1, text='em minutos', font=('Calibri', 12, 'bold'), fg=colors(5), bg=colors(2))
            label3.place(relx=0.21, rely=0.50)
            label4 = Label(self.frame1, text='Escolha o mês e o ano', font=('Calibri', 12, 'bold'), fg=colors(5),
                           bg=colors(2))
            label4.place(relx=0.10, rely=0.63)
            content_combo = insert_combo()
            combo = ttk.Combobox(self.frame1, values=content_combo, state='readonly', background=colors(5),
                                 textvariable=self.category)
            combo.place(relx=0.10, rely=0.25)
            entry = Entry(self.frame1, bg=colors(5), textvariable=self.var)
            entry.place(relx=0.10, rely=0.50, relwidth=0.10)
            mon = month_combo()
            combo2 = ttk.Combobox(self.frame1, values=mon, state='readonly', background=colors(5),
                                  textvariable=self.month)
            combo2.set(mon[month - 1])
            combo2.place(relx=0.10, rely=0.73, relwidth=0.30)
            yea = year_combo()
            combo3 = ttk.Combobox(self.frame1, values=yea, state='readonly', background=colors(5),
                                  textvariable=self.year)
            combo3.set(yea[year - 2023])
            combo3.place(relx=0.45, rely=0.73, relwidth=0.20)
            button = Button(self.frame1, text='Registrar meta', bg=colors(2), fg=colors(5),
                            font=('Calibri', 11, 'bold'),
                            command=lambda: insert_goal(self.var, entry, self.window, self.month.get(), self.year.get()
                                                        , self.category.get(), goal_main_v))
            button.place(relx=0.30, relwidth=0.40, rely=0.88)
        # -
        # if is manual:
        else:
            label = Label(self.frame1, text='Registrar', font=('Calibri', 12, 'bold'), fg=colors(5), bg=colors(2))
            label.place(relx=0.375, rely=0.01, relwidth=0.25)
            label1 = Label(self.frame1, text='Escolha a categoria', font=('Calibri', 12, 'bold'), fg=colors(5),
                           bg=colors(2))
            label1.place(relx=0.10, rely=0.15)
            label2 = Label(self.frame1, text='Defina a meta de estudo', font=('Calibri', 12, 'bold'),
                           fg=colors(5), bg=colors(2), wraplength=200)
            label2.place(relx=0.05, rely=0.35)
            label3 = Label(self.frame1, text='em minutos', font=('Calibri', 12, 'bold'), fg=colors(5), bg=colors(2))
            label3.place(relx=0.21, rely=0.50)
            label4 = Label(self.frame1, text='Escolha o mês e o ano', font=('Calibri', 12, 'bold'), fg=colors(5),
                           bg=colors(2))
            label4.place(relx=0.10, rely=0.63)
            content_combo = insert_combo()
            combo = ttk.Combobox(self.frame1, values=content_combo, state='readonly', background=colors(5),
                                 textvariable=self.category)
            combo.place(relx=0.10, rely=0.25)
            entry = Entry(self.frame1, bg=colors(5), textvariable=self.var)
            entry.place(relx=0.10, rely=0.50, relwidth=0.10)
            mon = month_combo()
            combo2 = ttk.Combobox(self.frame1, values=mon, state='readonly', background=colors(5),
                                  textvariable=self.month)
            combo2.set(mon[month - 1])
            combo2.place(relx=0.10, rely=0.73, relwidth=0.30)
            yea = year_combo()
            combo3 = ttk.Combobox(self.frame1, values=yea, state='readonly', background=colors(5),
                                  textvariable=self.year)
            combo3.set(yea[year - 2023])
            combo3.place(relx=0.45, rely=0.73, relwidth=0.20)
            button = Button(self.frame1, text='Registrar meta', bg=colors(2), fg=colors(5),
                            font=('Calibri', 11, 'bold'),
                            command=lambda: insert_goal(self.var, entry, self.window, self.month.get(), self.year.get()
                                                        , self.category.get(), goal_main_v, type='Manu'))
            button.place(relx=0.30, relwidth=0.40, rely=0.88)


class Rule_window:
    """
    This class helps to create scales and effectivity.
    """
    def __init__(self):
        window5 = Toplevel()
        self.window = window5
        self.frame1, self.frame_rules, self.frame_conditions, self.frame4 = None, None, None, None
        self.var, self.text, self.text1 = IntVar(self.window), StringVar(), StringVar()
        self.year, self.month, self.category = StringVar(), StringVar(), StringVar()
        self.effectivity, self.yearc, self.monthc = StringVar(), StringVar(), StringVar()
        self.screen()
        self.frame()
        self.label()
        self.radio_combo()
        self.button_entry()
        self.window.mainloop()

    def screen(self):
        self.window.title('Estabelecer regras')
        self.window.configure(background=colors(1))
        self.window.geometry(f'600x600+725+50')
        self.window.maxsize(width=600, height=600)
        self.window.minsize(width=600, height=600)
        self.window.resizable(False, False)
        self.window.iconbitmap('images/girl.ico')

    def frame(self):
        self.frame1 = Frame(self.window, bd=1, bg=colors(2), highlightbackground=colors(3), highlightthickness=2)
        self.frame1.place(relx=0.04, rely=0.04, relwidth=0.92, relheight=0.92)
        self.frame_rules = Frame(self.frame1, bd=1, bg=colors(5), highlightbackground=colors(2), highlightthickness=2)
        self.frame_rules.place(relx=0.02, rely=0.04, relwidth=0.45, relheight=0.92)
        self.frame_conditions = Frame(self.frame1, bd=1, bg=colors(5), highlightbackground=colors(2),
                                      highlightthickness=2)
        self.frame_conditions.place(relx=0.53, rely=0.04, relwidth=0.45, relheight=0.92)
        self.frame4 = Frame(self.frame1, bd=1, bg=colors(1), highlightbackground=colors(2), highlightthickness=2)
        self.frame4.place(relx=0.45, rely=0.04, relwidth=0.09, relheight=1)

    def label(self):
        label = Label(self.window, text='Regras e condições',  bg=colors(2), fg=colors(5), font=('Calibri', 12, 'bold'))
        label.place(relx=0.375, rely=0.045, relwidth=0.25, relheight=0.03)

        #labels rule frame
        label_rule1 = Label(self.frame_rules, text='Escolha o modelo de estudo ideal\n(padrão ou personalizado)',
                            bg=colors(5), fg=colors(2),
                            font=('Calibri', 11, 'bold'))
        label_rule1.place(relx=0.02, rely=0.05)
        label_rule2 = Label(self.frame_rules, text='Opções padrão', bg=colors(5), fg=colors(2),
                            font=('Calibri', 11, 'bold'))
        label_rule2.place(relx=0.10, rely=0.17)
        label_rule3 = Label(self.frame_rules, text='Crie seu próprio formato', bg=colors(5), fg=colors(2),
                            font=('Calibri', 11, 'bold'))
        label_rule3.place(relx=0.10, rely=0.52)
        label_rule4 = Label(self.frame_rules, text='X', bg=colors(5), fg=colors(2), font=('Calibri', 11, 'bold'))
        label_rule4.place(relx=0.35, rely=0.58)
        label_rule5 = Label(self.frame_rules, text='Estudos', bg=colors(5), fg=colors(2), font=('Calibri', 11, 'bold'))
        label_rule5.place(relx=0.09, rely=0.62)
        label_rule6 = Label(self.frame_rules, text='Folgas', bg=colors(5), fg=colors(2), font=('Calibri', 11, 'bold'))
        label_rule6.place(relx=0.46, rely=0.62)
        label_rule7 = Label(self.frame_rules, text='Escolha o mês e ano da rotina', bg=colors(5), fg=colors(2),
                            font=('Calibri', 11, 'bold'))
        label_rule7.place(relx=0.04, rely=0.77)

        #labels condition frame
        label_condition1 = Label(self.frame_conditions,
                                 text='Defina a efetividade do estudo\n\n*Dúvidas sobre os nomes e siglas?\n'
                                      'Consulte a FAQ!',
                                 bg=colors(5), fg=colors(2),
                                 font=('Calibri', 11, 'bold'))
        label_condition1.place(relx=0.05, rely=0.05)
        label_condition2 = Label(self.frame_conditions, text='Primeiro defina uma categoria', bg=colors(5),
                                 fg=colors(2),
                                 font=('Calibri', 11, 'bold'))
        label_condition2.place(relx=0.10, rely=0.25)
        label_condition3 = Label(self.frame_conditions, text='Agora informe a porcentagem\nda efetividade',
                                 bg=colors(5),
                                 fg=colors(2), font=('Calibri', 11, 'bold'))
        label_condition3.place(relx=0.10, rely=0.45)
        label_condition4 = Label(self.frame_conditions, text='%', bg=colors(5), fg=colors(2),
                                 font=('Calibri', 11, 'bold'))
        label_condition4.place(relx=0.57, rely=0.565)
        label_condition5 = Label(self.frame_conditions, text='Escolha também o mês e ano\nde validade',
                                 bg=colors(5), fg=colors(2),
                                 font=('Calibri', 11, 'bold'))
        label_condition5.place(relx=0.10, rely=0.70)

    def radio_combo(self):
        padrao1 = Radiobutton(self.frame_rules, text='5x2 (ExF)', bg=colors(5),
                              fg=colors(2), font=('Calibri', 10, 'bold'),
                              variable=self.var, value=1)
        padrao1.place(relx=0.15, rely=0.23)
        padrao2 = Radiobutton(self.frame_rules, text='6x1 (ExF)', bg=colors(5),
                              fg=colors(2), font=('Calibri', 10, 'bold'),
                              variable=self.var, value=2)
        padrao2.place(relx=0.15, rely=0.29)
        padrao3 = Radiobutton(self.frame_rules, text='7x0 (ExF)', bg=colors(5),
                              fg=colors(2), font=('Calibri', 10, 'bold'),
                              variable=self.var, value=3)
        padrao3.place(relx=0.15, rely=0.35)

        #combos_rule
        mon = month_combo()
        combo2 = ttk.Combobox(self.frame_rules, values=mon, state='readonly',
                              background=colors(5), textvariable=self.month)
        combo2.set(mon[month - 1])
        combo2.place(relx=0.10, rely=0.83, relwidth=0.30)
        yea = year_combo()
        combo3 = ttk.Combobox(self.frame_rules, values=yea, state='readonly',
                              background=colors(5), textvariable=self.year)
        combo3.set(yea[year - 2023])
        combo3.place(relx=0.45, rely=0.83, relwidth=0.20)

        #combo_condition
        content_category = insert_combo()
        combo = ttk.Combobox(self.frame_conditions, values=content_category, state='readonly', background=colors(5),
                             textvariable=self.category)
        combo.place(relx=0.20, rely=0.35)
        mon = month_combo()
        combo2 = ttk.Combobox(self.frame_conditions, values=mon, state='readonly',
                              background=colors(5), textvariable=self.monthc)
        combo2.set(mon[month - 1])
        combo2.place(relx=0.20, rely=0.80, relwidth=0.30)
        yea = year_combo()
        combo3 = ttk.Combobox(self.frame_conditions, values=yea, state='readonly',
                              background=colors(5), textvariable=self.yearc)
        combo3.set(yea[year - 2023])
        combo3.place(relx=0.55, rely=0.80, relwidth=0.20)

    def button_entry(self):
        #content for rule frame
        entry_rule1 = Entry(self.frame_rules, bg=colors(1), fg=colors(5), textvariable=self.text)
        entry_rule1.place(relx=0.15, rely=0.58, relwidth=0.10)
        entry_rule2 = Entry(self.frame_rules, bg=colors(1), fg=colors(5), textvariable=self.text1)
        entry_rule2.place(relx=0.50, rely=0.58, relwidth=0.10)
        button_rule1 = Button(self.frame_rules, text='Aplicar padrão', bg=colors(2), fg=colors(5),
                              font=('Calibri', 9, 'bold'),
                              command=lambda: rr.collect_option_default(self.var, self.window))
        button_rule1.place(relx=0.20, rely=0.43)
        button_rule2 = Button(self.frame_rules, text='Aplicar criação', bg=colors(2), fg=colors(5),
                              font=('Calibri', 9, 'bold'),
                              command=lambda:
                              rr.collect_option_style(self.text, self.text1, self.window, entry_rule1, entry_rule2))
        button_rule2.place(relx=0.20, rely=0.70)
        button_rule3 = Button(self.frame_rules, text='Registrar escolhas', bg=colors(2), fg=colors(5),
                              font=('Calibri', 9, 'bold'),
                              command=lambda: rr.open_scale(self.window, Scale_off_window, self.month, self.year))
        button_rule3.place(relx=0.18, rely=0.92)

        #content for condition frame
        entry_condition1 = Entry(self.frame_conditions, bg=colors(1), fg=colors(5), textvariable=self.effectivity)
        entry_condition1.place(relx=0.45, rely=0.57, relwidth=0.10)
        button_condition = Button(self.frame_conditions, text='Capturar efetividade', bg=colors(2), fg=colors(5),
                                  font=('Calibri', 9, 'bold'), command=lambda:
                                  registry_condition(self.window, self.monthc, self.yearc,
                                                     self.effectivity.get(), entry_condition1, self.category.get()))
        button_condition.place(relx=0.25, rely=0.90)


class Scale_off_window:
    """
    Class support to Rule_window, she allows to choose days to study.
    """
    def __init__(self):
        window6 = Toplevel()
        self.window = window6
        self.frame1, self.variables, self.checkbox = None, [], []
        self.button1, self.button2, self.label2 = None, None, None
        self.screen()
        self.frame()
        self.label()
        cs.scale_default(self.window)
        self.button()
        self.window.mainloop()

    def screen(self):
        self.window.title('Escala de folga')
        self.window.configure(background=colors(1))
        self.window.geometry('400x200+400+50')
        self.window.resizable(False, False)
        self.window.maxsize(width=400, height=200)
        self.window.minsize(width=400, height=200)
        self.window.iconbitmap('images/girl.ico')

    def frame(self):
        self.frame1 = Frame(self.window, bg=colors(2))
        self.frame1.place(relx=0.04, rely=0.04, relwidth=0.92, relheight=0.92)

    def label(self):
        label1 = Label(self.frame1, text='Escolha os dias de estudo e folga', bg=colors(2), fg=colors(1),
                       font=('calibri', 13, 'bold'))
        label1.place(relx=0.15, rely=0.05, relwidth=0.70)
        self.label2 = Label(self.frame1, text='Dias de estudo', bg=colors(2), fg=colors(1),
                            font=('calibri', 12, 'bold'))
        self.label2.place(relx=0.25, rely=0.30, relwidth=0.50)

    def button(self):
        self.button1 = Button(self.frame1, text='Definir', bg=colors(2), fg=colors(1), font=('calibri', 11, 'bold'),
                              command=lambda: cs.set_study(self.window, rr.return_choose()[0], rr.return_choose()[1],
                                                           rr.return_choose()[2], rr.return_choose()[3]))
        self.button1.place(relx=0.40, rely=0.70, relwidth=0.20)


# object "a" open the program.
a = Main_window()
base.disconnect()

# if u feel missing some explains in this module, please contact me thought: https://calendario-estudos.netlify.app/