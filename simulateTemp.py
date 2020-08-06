from random import randint
import pyowm

location = {
    "id": 3388368,
    "name": "Sao Luis",
    "country": "BR",
    "coord": {
        "lon": -44.30278,
        "lat": -2.52972
    }
}


class Openwinterface():
    def __init__(self, idioma, cidade, pais, chave):

        # retorna um dicionário com os dados do openweather

        self.retorno = {}
        self.idioma = idioma
        # self.cidade = cidade
        # self.pais = pais
        self.chave = chave
        # aqui criamos a nossa interface com a biblioteca
        self.owm = pyowm.OWM(self.chave, language=self.idioma)
        # só continua se a chave for uma chave válida
        if self.chave[0] == 'x':
            return

        self.get_weather()

    def get_weather(self):
       
        self.observation = self.owm.weather_at_id(location['id'])
        # lemos todos os dados disponíveis
        self.dados_clima = self.observation.get_weather()
        # aqui convertemos os dados em um dicionario para retornamos todos os dados disponíveis.
        self.retorno['temperatura'] = self.dados_clima.get_temperature('celsius')
        self.retorno['vento'] = self.dados_clima.get_wind()
        self.retorno['umidade'] = self.dados_clima.get_humidity()
        self.retorno['chuva'] = self.dados_clima.get_rain()
        self.retorno['pressao'] = self.dados_clima.get_pressure()
        self.retorno['nascer_sol'] = self.dados_clima.get_sunrise_time('iso')
        self.retorno['por_sol'] = self.dados_clima.get_sunset_time('iso')
        return self.retorno

    def updateTemp(self):
        self.dados_clima = self.observation.get_weather()
        return self.dados_clima

def readTemp():
    weather = Openwinterface(
        'pt-br', 'Sao Luis', 'BR', 'e4c3021c2f52bb971a2c68e6b43ab43f').get_weather()
    return weather

