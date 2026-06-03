import os
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle
from kivy.garden.androidbanner import AndroidBanner

# Force a fun mobile aspect ratio for testing
Window.clearcolor = (0.05, 0.1, 0.2, 1) # Deep Space Blue Background

# AdMob Configuration
ADMOB_BANNER_ID = "ca-app-pub-6872596196321341/xxxxxxxx"  # Replace with your banner ad unit ID
ADMOB_INTERSTITIAL_ID = "ca-app-pub-6872596196321341/yyyyyyyy"  # Replace with your interstitial ad unit ID

class SecurityGate:
    @staticmethod
    def verify_pin(input_pin):
        return str(input_pin) == "2408"

class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=40, spacing=20)
        
        # Sparkly Header
        layout.add_widget(Label(
            text="✨ EDULEARN BLOX ✨",
            font_size='35sp',
            bold=True,
            color=(1, 0.8, 0, 1) # Golden Sparkle
        ))
        
        self.pin_input = TextInput(
            hint_text="Enter Admin Secret...",
            password=True,
            multiline=False,
            size_hint=(1, None),
            height='60dp',
            font_size='20sp',
            halign='center'
        )
        layout.add_widget(self.pin_input)
        
        btn = Button(
            text="UNSEAL CORE 🔓",
            size_hint=(1, None),
            height='70dp',
            background_color=(0, 1, 0.5, 1), # Neon Green
            bold=True
        )
        btn.bind(on_press=self.check_auth)
        layout.add_widget(btn)
        
        self.error_lbl = Label(text="", color=(1, 0, 0, 1))
        layout.add_widget(self.error_lbl)
        self.add_widget(layout)

    def check_auth(self, instance):
        if SecurityGate.verify_pin(self.pin_input.text):
            self.manager.current = 'dashboard'
        else:
            self.error_lbl.text = "WRONG KEY! 🚫"

class DashboardScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Main Container
        outer_layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        # Top Logo/Status Space
        outer_layout.add_widget(Label(
            text="🚀 MISSION CONTROL 🚀",
            font_size='28sp',
            bold=True,
            size_hint_y=0.4,
            color=(0, 0.8, 1, 1) # Cyan Blue
        ))

        # Bottom Button Group (Matching your screenshot but with BLOX style)
        button_group = BoxLayout(orientation='vertical', spacing=10, size_hint_y=0.6)

        # START MISSIONS BUTTON
        btn_start = Button(
            text="START MISSIONS (GRADE R-7)",
            font_size='20sp',
            bold=True,
            background_normal='',
            background_color=(0.1, 0.1, 0.1, 1), # Sleek Black
            color=(1, 1, 1, 1)
        )
        
        # UPGRADE BUTTON
        btn_upgrade = Button(
            text="UPGRADE / PAY R150",
            font_size='18sp',
            bold=True,
            background_normal='',
            background_color=(0.15, 0.15, 0.15, 1), # Slightly lighter for contrast
            color=(1, 0.9, 0, 1) # Gold Text
        )

        button_group.add_widget(btn_start)
        button_group.add_widget(btn_upgrade)
        
        outer_layout.add_widget(button_group)
        self.add_widget(outer_layout)

class EduKidsApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(DashboardScreen(name='dashboard'))
        
        # Initialize AdMob banner
        self.init_admob()
        
        return sm
    
    def init_admob(self):
        """Initialize AdMob banner ads"""
        try:
            from jnius import autoclass
            PythonJavaClass = autoclass('org.kivy.android.PythonActivity')
            activity = PythonJavaClass.mActivity
            
            from kivy.garden.androidbanner import AndroidBanner
            self.banner = AndroidBanner(ADMOB_BANNER_ID)
            self.banner.show()
        except Exception as e:
            print(f"AdMob initialization skipped: {e}")

if __name__ == '__main__':
    EduKidsApp().run()
