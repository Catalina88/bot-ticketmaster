import requests
from bs4 import BeautifulSoup
import time


# 🔗 URL a monitorear
url = "https://www.ticketmaster.co/event/bts-world-tour-venta-general-viernes-2-octubre"

headers = {
    "User-Agent": "Mozilla/5.0"
}

# 🔔 TELEGRAM (REEMPLAZA ESTO)
TOKEN = "8252199412:AAFcR5wHf8yAm7-JY_Qp1CKM_ZSyoWbW3cM"
CHAT_ID = "2005993323"

def enviar_telegram(mensaje):
    url_telegram = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    try:
        response = requests.get(url_telegram, params={
            "chat_id": CHAT_ID,
            "text": mensaje
        })
        print("📨 Respuesta Telegram:", response.text)  # 👈 IMPORTANTE
    except Exception as e:
        print("❌ Error enviando a Telegram:", e)

print("🚀 Bot iniciado...")

# 🧪 PRUEBA DE TELEGRAM (NO BORRAR HASTA QUE FUNCIONE)
enviar_telegram("🧪 prueba desde bot")

detectado = False

while True:
    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")

        texto = soup.get_text().lower()

        print("⏳ Revisando...")

        # 🔥 DETECCIÓN MÁS PRECISA
        disponible = (
            "join queue" in texto or
            "find tickets" in texto or
            "seleccionar boletos" in texto
        )

        if disponible and not detectado:
            mensaje = "🔥 ¡Posible disponibilidad de BTS! Corre a Ticketmaster"
            print(mensaje)

        

            # 📱 telegram
            enviar_telegram(mensaje)

            detectado = True

        elif not disponible:
            detectado = False
            print("❌ Nada aún")

    except Exception as e:
        print("❌ Error general:", e)

    time.sleep(10)