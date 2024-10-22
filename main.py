import json
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.core.window import Window
import random

learned_verbs = set()

# Load irregular verbs from JSON file
def load_irregular_verbs(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

class VerbLearningApp(App):
    def build(self):
        # Set window background color to a light theme
        Window.clearcolor = (0.95, 0.95, 0.95, 1)  # Light grey background

        # Load the irregular verbs into an instance variable
        self.irregular_verbs = load_irregular_verbs('irregular_verbs.json')
        self.current_verb = None
        self.current_form = None

        # Main layout
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Define the background color for inputs
        input_background_color = (0.9, 0.9, 0.9, 1)  # Light gray

        # Text input for the verb (user-fillable)
        self.verb_input = TextInput(hint_text="Verb (user input)", multiline=False, font_size=22,
                        background_color=input_background_color, foreground_color=(0, 0, 0, 1))
        self.layout.add_widget(self.verb_input)

        # Text input for Präteritum form
        self.prateritum_input = TextInput(hint_text="Präteritum", multiline=False, font_size=22,
                          background_color=input_background_color, foreground_color=(0, 0, 0, 1))
        self.layout.add_widget(self.prateritum_input)

        # Text input for Perfect form
        self.perfect_input = TextInput(hint_text="Perfect", multiline=False, font_size=22,
                           background_color=input_background_color, foreground_color=(0, 0, 0, 1))
        self.layout.add_widget(self.perfect_input)

        # Text input for Meaning (shown for learning mode)
        self.meaning_input = TextInput(hint_text="Meaning", multiline=False, font_size=22,
                           readonly=True, background_color=input_background_color, foreground_color=(0, 0, 0, 1))
        self.layout.add_widget(self.meaning_input)

        # Set the padding for each TextInput after they've been created
        self.set_input_padding()

        # Button to check the answer
        self.check_button = Button(text="Check Answer", font_size=22, background_color=(0.1, 0.6, 0.8, 1), color=(1, 1, 1, 1))
        self.check_button.bind(on_press=self.check_answer)
        self.layout.add_widget(self.check_button)

        # Button to mark the verb as learned
        self.learn_button = Button(text="I Learned the Verb", font_size=22, background_color=(0.1, 0.7, 0.3, 1), color=(1, 1, 1, 1))
        self.learn_button.bind(on_press=self.learn_verb)
        self.layout.add_widget(self.learn_button)

        # Button to move to the next verb
        self.next_button = Button(text="Next Verb", font_size=22, background_color=(0.8, 0.4, 0.4, 1), color=(1, 1, 1, 1))
        self.next_button.bind(on_press=self.next_verb)
        self.layout.add_widget(self.next_button)

        # Start by showing the first verb
        self.next_verb()

        return self.layout

    def set_input_padding(self):
        """Set the padding for the TextInput fields to align text."""
        for input_field in [self.verb_input, self.prateritum_input, self.perfect_input, self.meaning_input]:
            input_field.padding_y = [(input_field.height - input_field.line_height) / 2, 0]

    def next_verb(self, instance=None):
        if len(learned_verbs) < len(self.irregular_verbs):
            self.current_verb = random.choice([verb for verb in self.irregular_verbs if verb not in learned_verbs])
        else:
            self.current_verb = random.choice(list(self.irregular_verbs.keys()))  # Practice mode

        self.current_form = random.choice(["Präteritum", "Perfect"])

        # Update the display with the new verb and its meaning
        self.verb_input.text = self.current_verb
        self.meaning_input.text = f"{self.irregular_verbs[self.current_verb]['meaning']}"

        # Fill the input fields with the correct answers
        self.prateritum_input.text = self.irregular_verbs[self.current_verb]["Präteritum"]
        self.perfect_input.text = self.irregular_verbs[self.current_verb]["Perfect"]

        # Reset input fields' background color and disable all fields
        self.prateritum_input.disabled = True
        self.perfect_input.disabled = True
        self.meaning_input.disabled = True  # Disable Meaning field
        self.prateritum_input.background_color = (0.9, 0.9, 0.9, 1)  # Light gray
        self.perfect_input.background_color = (0.9, 0.9, 0.9, 1)  # Light gray
        self.meaning_input.background_color = (0.9, 0.9, 0.9, 1)  # Light gray

        # Enable only the user input field based on the current form
        if self.current_form == "Präteritum":
            self.prateritum_input.text = ""  # Clear field for user input
            self.prateritum_input.disabled = False  # Enable user input field
            self.prateritum_input.background_color = (1, 1, 1, 1)  # White
        elif self.current_form == "Perfect":
            self.perfect_input.text = ""  # Clear field for user input
            self.perfect_input.disabled = False  # Enable user input field
            self.perfect_input.background_color = (1, 1, 1, 1)  # White

    def check_answer(self, instance):
        correct_prateritum = self.irregular_verbs[self.current_verb]["Präteritum"]
        correct_perfect = self.irregular_verbs[self.current_verb]["Perfect"]

        # Get the user input
        user_prateritum = self.prateritum_input.text.strip().lower()
        user_perfect = self.perfect_input.text.strip().lower()

        # Check if the answer is correct based on the enabled field
        if not self.prateritum_input.disabled and user_prateritum == correct_prateritum.lower():
            self.show_popup("Correct!", f"Correct: {correct_prateritum}")
        elif not self.perfect_input.disabled and user_perfect == correct_perfect.lower():
            self.show_popup("Correct!", f"Correct: {correct_perfect}")
        else:
            correct_form = ""
            if not self.prateritum_input.disabled:
                correct_form = correct_prateritum
            elif not self.perfect_input.disabled:
                correct_form = correct_perfect

            self.show_popup("Incorrect", f"The correct answer was: {correct_form}")

        self.next_verb()

    def learn_verb(self, instance):
        learned_verbs.add(self.current_verb)
        self.show_popup("Learned", f"{self.current_verb} added to learned verbs.")
        self.next_verb()

    def show_popup(self, title, message):
        popup = Popup(title=title, content=Label(text=message, halign='center', valign='middle'), size_hint=(0.6, 0.4))

        # Close the popup when it is touched
        popup.bind(on_touch_down=lambda instance, touch: popup.dismiss() if popup.collide_point(*touch.pos) else None)

        popup.open()

if __name__ == '__main__':
    VerbLearningApp().run()
