from urllib.parse import quote
import webbrowser
from time import sleep
import datetime
import pyautogui

#message 
telefone = "558198680775"
mensagem = "meu mano bala"
encoded_message = quote(mensagem)

link_mensagem = f"https://wa.me/{telefone}?text={encoded_message}"



#open whatsapp
webbrowser.open(link_mensagem)
sleep(5)

webbrowser.open(link_mensagem)
sleep(2)

#click to send message
seta_centro = pyautogui.locateCenterOnScreen("icone2.png", confidence=0.6)
sleep(5)
if datetime.datetime.now() == 
    if seta_centro is not None:
        pyautogui.click(seta_centro[0], seta_centro[1], clicks=1, interval=1)
    else:
        print("Icon not found on the screen.")

#close whatsapp screen
pyautogui.hotkey("alt", 'f4')

