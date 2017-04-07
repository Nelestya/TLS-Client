#!/usr/bin/python3.4

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import tlsconnect



class App():

    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file("TLS_Client.glade")
        self.builder.connect_signals(self)
        self.window = self.builder.get_object("window1")
        self.entry1 = self.builder.get_object("entry1")
        self.textview1 = self.builder.get_object("textview1")


        self.window.show_all()

    def on_imagemenuitem10_activate(self, widget):
        self.dialog1 = self.builder.get_object("aboutdialog1")
        self.dialog1.show_all()

    def on_button2_clicked(self, widget):
        print(self.entry1.get_text())

        self.textbuffer = self.textview1.get_buffer()
        self.request = tlsconnect.HTTPclient(self.entry1.get_text())
        self.response = self.request.getconnection()
        print(self.response)
        self.textbuffer.set_text(str(self.response))

    def on_window1_delete_event(self, *args):
        Gtk.main_quit(*args)

    def on_button1_clicked(self, button):
        print(delete)




if __name__ == "__main__":
    App()
    Gtk.main()
