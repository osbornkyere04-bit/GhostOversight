from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
import socket

class GhostLink(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        # 1. UI Elements
        self.label = Label(text="GhostLink: Phone to Laptop", font_size='20sp')
        
        self.ip_input = TextInput(hint_text="Enter Laptop IP (e.g. 192.168.43.15)", multiline=False)
        self.msg_input = TextInput(hint_text="Type your message here...", multiline=True)
        
        self.send_btn = Button(text="SEND TO LAPTOP", background_color=(0, 0.7, 0.9, 1))
        self.send_btn.bind(on_press=self.send_message)

        # 2. Add to Layout
        self.layout.add_widget(self.label)
        self.layout.add_widget(self.ip_input)
        self.layout.add_widget(self.msg_input)
        self.layout.add_widget(self.send_btn)

        return self.layout

    def send_message(self, instance):
        laptop_ip = self.ip_input.text
        message = self.msg_input.text
        port = 5555

        if not laptop_ip:
            self.label.text = "Error: Enter Laptop IP first!"
            return

        try:
            # Create the socket connection
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.settimeout(5) # Don't freeze the app if IP is wrong
            client.connect((laptop_ip, port))
            client.send(message.encode())
            client.close()
            self.label.text = "✅ Message Sent Successfully!"
        except Exception as e:
            self.label.text = f"❌ Error: {str(e)}"

if __name__ == "__main__":
    GhostLink().run()
