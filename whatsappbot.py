from selenium import webdriver
import time

class WhatsappBot:
    def __init__(self):
        self.mensagem = "Oi, tudo bem? Testando bot WhatsApp"
        self.grupos = ["Sisters"]
        options = webdriver.ChromeOptions()
        options.add_argument('lan=pt-br')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')

    def EnviarMensagens(self): 
        # <span dir="auto" title="Sisters" class="_35k-1 _1adfa _3-8er">Sisters</span>
        # <div tabindex="-1" class="_2A8P4">
        # <span data-testid="send" data-icon="send" class="">
        print('dsjdjdl')
        self.driver.get('https://web.whatsapp.com')
        time.sleep(30)
        grupo = self.driver.find_element_by_xpath("//span[@title='Sisters']")
        time.sleep(3)
        grupo.click()
        chat_box = self.driver.find_element_by_class_name('_2A8P4')
        time.sleep(3)
        chat_box.click()
        chat_box.send_keys(self.mensagem)
        botao_enviar = self.driver.find_element_by_xpath("//span[@data-icon='send']")
        time.sleep(3)
        botao_enviar.click()
        time.sleep(3)

bot = WhatsappBot()
bot.EnviarMensagens()

