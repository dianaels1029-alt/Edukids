# ======================================================
# EDUKIDS: SOVEREIGN V.1 (CLEAN SYNTAX)
# ARCHITECT: DONOVAN HIEPNER
# R50 GATEKEEPER | OCTO-TUTOR | DYNAMIC THEME ENGINE
# WITH ADMOB MONETIZATION
# ======================================================
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ListProperty, StringProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
import requests
import webbrowser
import os

# Change this to match your live PythonAnywhere domain!
CLOUD_URL = "https://ArchitectDon.pythonanywhere.com/check-license"

# AdMob Configuration
ADMOB_APP_ID = "ca-app-pub-6872596196321341~0000000000"  # Replace with your app ID
ADMOB_BANNER_ID = "ca-app-pub-6872596196321341/xxxxxxxx"  # Replace with your banner ad unit ID
ADMOB_INTERSTITIAL_ID = "ca-app-pub-6872596196321341/yyyyyyyy"  # Replace with your interstitial ad unit ID

KV = '''
#:import utils kivy.utils

<RoundedInput@TextInput>:
    background_color: 0, 0, 0, 0
    font_size: '20sp'
    padding: [20, 15]
    halign: 'center'
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [15,]

<ActionBtn@Button>:
    background_color: 0, 0, 0, 0
    font_size: '22sp'
    bold: True
    canvas.before:
        Color:
            rgba: app.accent_color
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [20,]

WindowManager:
    SplashPage:
    MainHub:

<SplashPage>:
    name: 'splash'
    BoxLayout:
        orientation: 'vertical'
        padding: 30
        spacing: 15
        canvas.before:
            Color:
                rgba: utils.get_color_from_hex("#1E1E2E")
            Rectangle:
                pos: self.pos
                size: self.size
        Label:
            text: 'EDUKIDS: THE VAULT'
            font_size: '40sp'
            bold: True
            color: utils.get_color_from_hex("#F9E2AF")
        RoundedInput:
            id: alias
            hint_text: 'Player Alias...'
            size_hint_y: None
            height: '60dp'
        RoundedInput:
            id: age
            hint_text: 'Age...'
            input_filter: 'int'
            size_hint_y: None
            height: '60dp'
        ActionBtn:
            text: 'ENTER THE PORTAL 🚀'
            on_release: app.process_player(alias.text, age.text)
        Button:
            text: 'PAY R50 FOR ACCESS'
            background_color: 0, 0.5, 0, 1
            on_release: app.open_payment_portal(alias.text)

<MainHub>:
    name: 'hub'
    BoxLayout:
        orientation: 'vertical'
        padding: 20
        spacing: 15
        canvas.before:
            Color:
                rgba: app.bg_color
            Rectangle:
                pos: self.pos
                size: self.size
        Label:
            text: f"PLAYER: {app.player_alias} | LVL: {app.player_level}"
            font_size: '20sp'
            color: 1, 1, 1, 1
        GridLayout:
            cols: 2
            spacing: 10
            ActionBtn:
                text: 'DAILY CHORES'
            ActionBtn:
                text: 'EXPLORER HUB'
            ActionBtn:
                text: 'OCTO-TUTOR AI'
                on_release: webbrowser.open("https://chatgpt.com")
            ActionBtn:
                text: 'MARKETPLACE'
        Label:
            text: 'Ads powered by Google AdMob'
            font_size: '12sp'
            color: 0.7, 0.7, 0.7, 1
            size_hint_y: 0.1
'''

class SplashPage(Screen): pass
class MainHub(Screen): pass
class WindowManager(ScreenManager): pass

class EduKidsApp(App):
    bg_color = ListProperty([0, 0, 0, 1])
    accent_color = ListProperty([0, 0, 0, 1])
    player_alias = StringProperty("GUEST")
    player_level = StringProperty("1")

    def build(self): 
        root = Builder.load_string(KV)
        self.init_admob()
        return root
    
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
            print(f"AdMob initialization note: {e}")

    def open_payment_portal(self, alias):
        if not alias.strip():
            Popup(title='Alert', content=Label(text='Enter Player Alias first!'), size_hint=(None, None), size=(400, 200)).open()
            return
        pay_url = f"https://www.paypal.com/ncp/payment/4W6ECRCNV8KDS?custom={alias.strip().upper()}"
        webbrowser.open(pay_url)

    def process_player(self, name, age_str):
        name_upper = name.upper().strip()
        from kivy.utils import get_color_from_hex as hex_col

        if not name_upper:
            return

        # GHOST DOOR: Master Architect Bypass
        if name_upper == "102829":
            self.player_alias, self.player_level = "THE ARCHITECT", "SOVEREIGN"
            self.bg_color, self.accent_color = hex_col("#0B0C10"), hex_col("#D4AF37")
            self.root.current = 'hub'
            return

        # CLOUD VERIFICATION
        try:
            response = requests.get(f"{CLOUD_URL}?alias={name_upper}", timeout=5)
            if response.status_code != 200 or response.json().get("status") != "UNLOCKED":
                Popup(title='Vault Locked', content=Label(text='No R50 license found for this alias.'), size_hint=(None, None), size=(400, 200)).open()
                return
        except Exception:
            Popup(title='Connection Error', content=Label(text='Cannot reach cloud server.'), size_hint=(None, None), size=(400, 200)).open()
            return
            
        age = int(age_str) if age_str and age_str.isdigit() else 0
        self.player_alias = name_upper
        
        # THEME ENGINE
        if age <= 7:
            self.bg_color, self.accent_color, self.player_level = hex_col("#87CEEB"), hex_col("#FF4500"), "STARTER"
        elif 8 <= age <= 10:
            self.bg_color, self.accent_color, self.player_level = hex_col("#2E2E2E"), hex_col("#39FF14"), "BUILDER"
        else:
            self.bg_color, self.accent_color, self.player_level = hex_col("#191970"), hex_col("#FFCC00"), "MASTER"
        
        self.root.current = 'hub'

if __name__ == '__main__':
    EduKidsApp().run()
