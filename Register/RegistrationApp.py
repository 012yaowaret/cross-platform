from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout

class FirstScreen(Screen):
    pass

class SecondScreen(Screen):
    def submit_registration(self):
        username = self.ids.username.text
        email = self.ids.email.text
        password = self.ids.password.text
        # ตรวจสอบข้อมูลที่กรอกและดำเนินการต่อไป
        print(f'Username: {username}, Email: {email}, Password: {password}')
        # สามารถเพิ่มโค้ดส่วนนี้เพื่อบันทึกข้อมูลหรือทำการลงทะเบียนในฐานข้อมูลได้

class RegistrationApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(FirstScreen(name='first'))
        sm.add_widget(SecondScreen(name='second'))
        return sm

if __name__ == '__main__':
    RegistrationApp().run()
