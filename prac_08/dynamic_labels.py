from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    def __init__(self):
        super().__init__()
        self.names = ["Timmy", "Bob", "Roger", "Tilly", "Jim"]

    def build(self):
        """Build the Kivy app and add labels dynamically."""
        self.root = Builder.load_file("dynamic_labels.kv")
        for name in self.names:
            label = Label(text=name, font_size=24)
            self.root.ids.main.add_widget(label)
        return self.root


if __name__ == "__main__":
    DynamicLabelsApp().run()
