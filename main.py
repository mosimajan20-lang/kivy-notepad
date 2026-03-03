import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.utils import platform

# Dark background
Window.clearcolor = (0.1, 0.1, 0.1, 1)


class AndroidNotepad(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", **kwargs)

        # Get safe app storage path (works on Android + PC)
        if platform == "android":
            from android.storage import app_storage_path
            self.storage_path = app_storage_path()
        else:
            self.storage_path = os.getcwd()

        self.file_path = os.path.join(self.storage_path, "note.txt")

        # ===== Top Buttons =====
        top_bar = BoxLayout(size_hint_y=None, height=50)

        btn_new = Button(text="New")
        btn_save = Button(text="Save")

        btn_new.bind(on_press=self.new_file)
        btn_save.bind(on_press=self.save_file)

        top_bar.add_widget(btn_new)
        top_bar.add_widget(btn_save)

        self.add_widget(top_bar)

        # ===== Text Editor =====
        self.editor = TextInput(
            multiline=True,
            font_size=18,
            background_color=(0.15, 0.15, 0.15, 1),
            foreground_color=(1, 1, 1, 1),
            cursor_color=(1, 1, 1, 1)
        )

        self.add_widget(self.editor)

        # ===== Status =====
        self.status = Label(
            text="Ready",
            size_hint_y=None,
            height=30
        )
        self.add_widget(self.status)

        # Load existing note if exists
        self.load_file()

    # =======================
    # Core Functions
    # =======================

    def new_file(self, instance):
        self.editor.text = ""
        self.status.text = "New note"

    def save_file(self, instance):
        try:
            with open(self.file_path, "w", encoding="utf-8") as f:
                f.write(self.editor.text)
            self.status.text = "Saved successfully"
        except Exception as e:
            self.status.text = f"Error: {e}"

    def load_file(self):
        if os.path.exists(self.file_path):
            try:
                with open(self.file_path, "r", encoding="utf-8") as f:
                    self.editor.text = f.read()
                self.status.text = "Loaded saved note"
            except:
                self.status.text = "Could not load file"


class NotepadApp(App):
    def build(self):
        return AndroidNotepad()


if __name__ == "__main__":
    NotepadApp().run()