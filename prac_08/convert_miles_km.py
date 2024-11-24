from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934

class ConvertMilesKmApp(App):
    output_km = StringProperty("0.0")

    def build(self):
        """Build the Kivy app from the kv file."""
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file("convert_miles_km.kv")
        return self.root

    def handle_conversion(self, miles_text):
        """Convert miles to kilometers and update the output label."""
        miles = self.validate_input(miles_text)
        km = miles * MILES_TO_KM
        self.output_km = str(km)

    def handle_increment(self, miles_text, change):
        """Adjust the miles value by a specified increment and update the text input and output."""
        miles = self.validate_input(miles_text) + change
        self.root.ids.input_miles.text = str(miles)  # Update TextInput field
        self.handle_conversion(str(miles))  # Update conversion output

    def validate_input(self, text):
        """Validate the text input, returning 0.0 if input is invalid."""
        try:
            return float(text)
        except ValueError:
            return 0.0


if __name__ == "__main__":
    ConvertMilesKmApp().run()
