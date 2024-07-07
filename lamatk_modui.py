#!/usr/bin/python3
import pathlib
import tkinter as tk
import pygubu

PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "gui.ui"
RESOURCE_PATHS = [PROJECT_PATH]


class lamatkUI:
    def __init__(self, master=None):
        self.builder = pygubu.Builder()
        self.builder.add_resource_paths(RESOURCE_PATHS)
        self.builder.add_from_file(PROJECT_UI)
        # Main widget
        self.mainwindow: tk.Toplevel = self.builder.get_object("toplevel1", master)
        # Main menu
        _main_menu = self.builder.get_object("menu1", self.mainwindow)
        self.mainwindow.configure(menu=_main_menu)
        self.builder.connect_callbacks(self)
        
        self.tv = self.builder.get_object("tv_models")

    def run(self):
        self.mainwindow.mainloop()

    def click_btn_send(self):
        pass

    def click_btn_addfile(self):
        pass

    def item_selected(self, event=None):
        for selected_item in tree.selection():
            item = tree.item(selected_item)
            record = item['values']
            # show a message
            showinfo(title='Information', message=','.join(record))

    def click_btn_info(self):
        pass

    def click_btn_delete(self):
        pass

    def click_btn_update(self):
        contacts = []
        for n in range(1, 100):
            contacts.append((f'ItemA {n}', f'ItemB {n}', f'ItemC {n}'))
        for contact in contacts:
            self.tv.insert('', tk.END, values=contact)
        pass

    def click_btn_clear(self):
        pass

    def click_btn_saveas(self):
        pass


if __name__ == "__main__":
    app = lamatkUI()
    app.run()
