from django.apps import AppConfig # Django'nun uygulama yapılandırma sınıfını içe aktarır

# 'Code4Us' adlı Django uygulamasının yapılandırmasını tanımlayan sınıf
class Code4UsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'code4us' # Uygulamanın adını belirler.
