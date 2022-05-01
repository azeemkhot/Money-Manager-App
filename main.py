from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDFlatButton, MDRaisedButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import ThreeLineIconListItem, OneLineIconListItem
from kivymd.uix.list import IconLeftWidget
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.picker import MDThemePicker
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.menu import MDDropdownMenu
from kivy.properties import StringProperty
from kivy.lang import Builder
from kivy.clock import Clock

from kvfile import navigation_helper


import matplotlib.pyplot as plt
from datetime import date, datetime

fl = []
icondict = {
    'Books': 'book-open-page-variant',
    'Clothing': 'tshirt-crew',
    'Education': 'school',
    'Entertainment': 'movie-open',
    'Food': 'food',
    'Groceries': 'cart-variant',
    'Healthcare': 'hospital-box',
    'Personal': 'account-plus',
    'Stationery': 'printer',
    'Travel': 'train-car',
    'Utilities': 'tools',
    'Others': 'plus-circle',
}


class ContentNavigationDrawer(BoxLayout):
    pass


class HomeScreen(Screen):
    def on_pre_enter(self, *args):

        def on_enterh(interval):
            fig = plt.figure(figsize=(3, 3))
            ax = fig.add_axes([0, 0, 1, 1])
            ax.axis('equal')
            f = open("rec.txt", "r+")
            amtcount = {}
            maxamtcount = '-'
            last30 = 0
            thism = 0
            fl = []
            for i in f:
                temp = i.split(" ")
                fl.append(temp)
                if temp[0] in amtcount:
                    amtcount[temp[0]] += int(temp[2])
                else:
                    amtcount[temp[0]] = int(temp[2])

                rdate = temp[3].split('-')
                rdate.reverse()
                cdate = str(datetime.now()).split()[0].split('-')
                date1 = date(int(rdate[0]), int(rdate[1]), int(rdate[2]))
                date2 = date(int(cdate[0]), int(cdate[1]), int(cdate[2]))
                if (date2 - date1).days <= 30:
                    last30 += int(temp[2])
                    if rdate[1] == cdate[1]:
                        thism += int(temp[2])
            f.close()
            if amtcount:
                maxamtcount = max(amtcount, key=amtcount.get)

            self.ids.ltd.text = "₹ " + str(last30)
            self.ids.thm.text = "₹ " + str(thism)
            self.ids.mec.text = str(maxamtcount)

            items = list(amtcount.keys())
            amount = list(amtcount.values())

            ax.pie(amount, labels=items, autopct='%1.2f%%')
            fig.savefig("catamt.png", bbox_inches='tight')  # save the figure to file
            plt.close(fig)
            self.ids.pchimg.reload()

        Clock.schedule_once(on_enterh)


class ViewScreen(Screen):

    def on_enter(self, *args):

        def on_enterv(interval):
            f = open("rec.txt", "r")
            self.ids.selection_list.clear_widgets()
            fl = []
            for i in f:
                temp = i.split(" ")[:-1]
                fl.append(temp)

            if fl:
                self.ids.noreclabel.text = ''
            else:
                self.ids.noreclabel.text = 'No Records to display'

            for recline in fl[::-1]:
                item = ThreeLineIconListItem(text=recline[1], secondary_text="Amount : " + recline[2],
                                             tertiary_text="Date : " + recline[3])
                icon = IconLeftWidget(icon=icondict[recline[0]])
                item.add_widget(icon)
                self.ids.selection_list.add_widget(item)
            f.close()

        Clock.schedule_once(on_enterv)


class ContentNameDialog(BoxLayout):
    pass


class ContentEmailDialog(BoxLayout):
    pass


class ContentNewRecordDialog(BoxLayout):
    pass


class IconListItem(OneLineIconListItem):
    icon = StringProperty()


class DemoApp(MDApp):

    def on_start(self):
        a_file = open("nameemailrec.txt", "r")
        list_of_lines = a_file.readlines()
        self.root.ids.cnd.nameid.text = list_of_lines[0][:-1]
        self.root.ids.cnd.emailid.text = list_of_lines[1][:-1]
        self.theme_cls.primary_palette, self.theme_cls.accent_palette, self.theme_cls.theme_style = list_of_lines[
            2].split()
        a_file.close()

    def on_stop(self):
        a_file = open("nameemailrec.txt", "r")
        list_of_lines = a_file.readlines()
        list_of_lines[2] = self.theme_cls.primary_palette + ' ' + \
                           self.theme_cls.accent_palette + ' ' + \
                           self.theme_cls.theme_style

        a_file = open("nameemailrec.txt", "w")
        a_file.writelines(list_of_lines)
        a_file.close()

    def build(self):

        menu_items = [
            {
                "viewclass": "IconListItem",
                "icon": "help",
                "text": "FAQ",
                "height": dp(56),
                "on_release": lambda x='1': self.menu_callback(x),
            },
            {
                "viewclass": "IconListItem",
                "icon": "exit-to-app",
                "text": "Exit",
                "height": dp(56),
                "on_release": lambda x='2': self.menu_callback(x),
            }
        ]
        self.menu = MDDropdownMenu(
            items=menu_items,
            width_mult=3,
        )

        return Builder.load_string(navigation_helper)

    def callback(self, button):
        self.menu.caller = button
        self.menu.open()

    def menu_callback(self, text_item):
        self.menu.dismiss()
        if text_item == '1':
            self.faq()
        elif text_item == '2':
            self.close()

    def faq(self):
        snackbar = Snackbar(text='Nothing to show',
                            snackbar_x="10dp", snackbar_y="20dp")
        snackbar.size_hint_x = (Window.width - (dp(10) * 2)) / Window.width
        snackbar.open()

    def close(self):
        self.dialog = MDDialog(
            title="Exit Application?",
            text="Are you sure you want to exit the application?",
            buttons=[
                MDFlatButton(
                    text="CANCEL", text_color=self.theme_cls.primary_color, on_release=self.close_dialog,
                ),
                MDFlatButton(
                    text="EXIT", text_color=self.theme_cls.primary_color, on_release=MDApp.get_running_app().stop,
                ),
            ],
        )
        self.dialog.open()

    def show_theme_picker(self):
        theme_dialog = MDThemePicker()
        theme_dialog.open()

    def show_name_dialog(self):
        self.dialog = MDDialog(title='Change Name',
                               type="custom",
                               content_cls=ContentNameDialog(),
                               buttons=[MDRaisedButton(text='Save Changes', on_release=self.change_name),
                                        MDFlatButton(text='Close', on_release=self.close_dialog)])
        self.dialog.open()

    def show_email_dialog(self):
        self.dialog = MDDialog(title='Change Email',
                               type="custom",
                               content_cls=ContentEmailDialog(),
                               buttons=[MDRaisedButton(text='Save Changes', on_release=self.change_email),
                                        MDFlatButton(text='Close', on_release=self.close_dialog)])
        self.dialog.open()

    def change_name(self, obj):

        name = self.dialog.content_cls.name.text

        if name == '':
            snackbar = Snackbar(text='Invalid Text',
                                snackbar_x="10dp", snackbar_y="20dp")
            snackbar.size_hint_x = (Window.width - (dp(10) * 2)) / Window.width
            snackbar.open()
        else:
            self.dialog.dismiss()
            a_file = open("nameemailrec.txt", "r")
            list_of_lines = a_file.readlines()
            list_of_lines[0] = name + "\n"

            a_file = open("nameemailrec.txt", "w")
            a_file.writelines(list_of_lines)
            a_file.close()
            self.root.ids.cnd.nameid.text = name
            self.show_snackbar()

    def change_email(self, obj):

        email = self.dialog.content_cls.email.text

        if email == '':
            snackbar = Snackbar(text='Invalid Text',
                                snackbar_x="10dp", snackbar_y="20dp")
            snackbar.size_hint_x = (Window.width - (dp(10) * 2)) / Window.width
            snackbar.open()
        else:
            self.dialog.dismiss()
            a_file = open("nameemailrec.txt", "r")
            list_of_lines = a_file.readlines()
            list_of_lines[1] = email + "\n"

            a_file = open("nameemailrec.txt", "w")
            a_file.writelines(list_of_lines)
            a_file.close()
            self.root.ids.cnd.emailid.text = email
            self.show_snackbar()

    def show_new_record_dialog(self, category):
        self.dialog = MDDialog(title=category,
                               type="custom",
                               content_cls=ContentNewRecordDialog(),
                               buttons=[MDRaisedButton(text='Save Changes', on_release=self.save_record),
                                        MDFlatButton(text='Close', on_release=self.close_dialog)])
        self.dialog.open()

    def show_snackbar(self):
        self.dialog.dismiss()
        snackbar = Snackbar(text='Changes Saved Successfully',
                            snackbar_x="10dp", snackbar_y="20dp")
        snackbar.size_hint_x = (Window.width - (dp(10) * 2)) / Window.width
        snackbar.open()

    def show_newrec_snackbar(self):
        snackbar = Snackbar(text='New Record Added Successfully',
                            snackbar_x="10dp", snackbar_y="20dp")
        snackbar.size_hint_x = (Window.width - (dp(10) * 2)) / Window.width
        snackbar.open()

    def save_record(self, obj):
        category = self.dialog.title
        rtext = self.dialog.content_cls.rname.text
        amttext = self.dialog.content_cls.amt.text
        dmy = self.dialog.content_cls.dmy.text

        if rtext == '' or amttext == '' or dmy == '':
            snackbar = Snackbar(text='Invalid Text',
                                snackbar_x="10dp", snackbar_y="20dp")
            snackbar.size_hint_x = (Window.width - (dp(10) * 2)) / Window.width
            snackbar.open()
        else:
            self.dialog.dismiss()
            self.show_newrec_snackbar()

            f = open("rec.txt", "a")
            f.write(category + " " + rtext + " " + amttext + " " + dmy + " " + "\n")
            f.close()

            f = open("rec.txt", "r")
            f.close()

    def delete_records(self):
        print("Incomplete")
        self.dialog = MDDialog(title='Delete Records',
                               text="Are you sure you want to delete all records?[/color]",
                               size_hint=(0.9, 0.9),
                               buttons=[MDFlatButton(text="CANCEL", text_color=self.theme_cls.primary_color,
                                                     on_release=self.close_dialog),
                                        MDFlatButton(text="DELETE", text_color=self.theme_cls.primary_color,
                                                     on_release=self.confirm_delete)])
        self.dialog.open()

    def confirm_delete(self, obj):
        self.dialog.dismiss()
        file = open("rec.txt", "r+")
        file.truncate(0)
        file.close()

        snackbar = Snackbar(text='All Records Deleted Successfully',
                            snackbar_x="10dp", snackbar_y="20dp")
        snackbar.size_hint_x = (Window.width - (dp(10) * 2)) / Window.width
        snackbar.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()


DemoApp().run()
