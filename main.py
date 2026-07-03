from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.utils import platform

class HereIAmApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20)
        self.status_label = Label(
            text="برنامه 'من اینجام' فعال است.\nدر حال بررسی دسترسی‌ها...", 
            font_size='18sp',
            halign='center'
        )
        layout.add_widget(self.status_label)
        return layout

    def on_start(self):
        if platform == 'android':
            self.request_android_permissions()

    def request_android_permissions(self):
        from android.permissions import request_permissions, Permission
        permissions = [
            Permission.ACCESS_FINE_LOCATION,
            Permission.ACCESS_COARSE_LOCATION,
            Permission.RECEIVE_SMS,
            Permission.READ_SMS
        ]
        request_permissions(permissions, self.permission_callback)

    def permission_callback(self, permissions, results):
        if all(results):
            self.status_label.text = "✅ تمام دسترسی‌ها داده شد.\nآماده برای قدم بعدی!"
        else:
            self.status_label.text = "❌ خطا: برای کارکرد درست برنامه،\nباید همه دسترسی‌ها را تایید کنید."

if __name__ == '__main__':
    HereIAmApp().run()
