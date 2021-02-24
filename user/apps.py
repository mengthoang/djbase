from django.apps import AppConfig

class UserConfig(AppConfig):
    name = 'user'
 
    def ready(self):
        from user.receivers import SignalReceiver
        SignalReceiver.connect()
        AppConfig.ready(self)
    