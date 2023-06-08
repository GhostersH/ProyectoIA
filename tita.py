import pyttsx3 # pip install pyttsx3    
import datetime    
import speech_recognition as sr # pip install SpeechRecognition    
import wikipedia # pip install wikipedia    
import smtplib    
import webbrowser as wb    
import os    
import pyautogui # pip install pyautogui    
import psutil # pip install psutil    
import pyjokes    
  
# Configurar el reconocimiento de voz en español  
r = sr.Recognizer()  
mic = sr.Microphone(device_index=1) # indice del microfono  
  
engine = pyttsx3.init()    
    
def hablar(audio):    
    engine.say(audio)    
    engine.runAndWait()    
    
def hora():    
    tiempo = datetime.datetime.now().strftime("%I:%M:%S")    
    hablar("La hora actual es")    
    hablar(tiempo)    
    
def fecha():    
    year = int(datetime.datetime.now().year)    
    month = int(datetime.datetime.now().month)    
    date = int(datetime.datetime.now().day)  
    hablar("La fecha actual es")    
    hablar(date)    
    hablar(month)    
    hablar(year)    
  
def bienvenida():    
    hablar("¡Bienvenido de nuevo!")    
    hora()    
    fecha()    
    hora_actual = datetime.datetime.now().hour    
    if hora_actual >= 6 and hora_actual < 12:    
        hablar("¡Buenos días!")    
    elif hora_actual >=12 and hora_actual < 18:    
        hablar("¡Buenas tardes!")    
    elif hora_actual >= 18 and hora_actual < 24:    
        hablar("¡Buenas noches!")    
    else:    
        hablar("¡Buenas noches!")    
  
    hablar("Soy el sistema automatizado que funciona mediante energia solar para el ensamblaje de autos, la primera maquina realiza la recoleccion de piezas necesarias, la segunda maquina utiliza la piezas previamente recolectadas para ensamblar el vehiculo, y por ultimo se evalua el carro ensamblado, y todo funciona mediante energia solar")    
    
def tomar_comando():    
    with mic as source:  
        r.adjust_for_ambient_noise(source) # Evitar problemas de ruido en el audio  
        audio = r.listen(source)    
        print("Escuchando...")    
        try:    
            print("Reconociendo...")    
            query = r.recognize_google(audio, language='es-ES')  # reconocimiento de voz en español  
            print(query)  
            hablar(query)  
    
        except Exception as e:    
            print(e)    
            hablar("Lo siento, no te he entendido. ¿Puedes repetirlo, por favor?")    
            return "None"    
        return query     
    
def enviar_email(to, contenido):    
    servidor = smtplib.SMTP('smtp.gmail.com', 587)    
    servidor.ehlo()    
    servidor.starttls()    
    servidor.login('tu_email@gmail.com', 'tu_contraseña')    
    servidor.sendmail('tu_email@gmail.com', to, contenido)    
    servidor.close()    
    
def captura_pantalla():    
    imagen = pyautogui.screenshot()    
    imagen.save("C:/Users/gteran/Desktop/Universidad/IA/proyectoIA/capturas/screenshot.png")    
    
def cpu():  
    uso = str(psutil.cpu_percent())  
    hablar('La CPU está al ' + uso + ' por ciento')  
    bateria = psutil.sensors_battery()  
    hablar("La batería está al " + str(bateria.percent) + " por ciento")     
    
def chistes():    
    hablar(pyjokes.get_joke(language='es', category= 'all'))    
    
if __name__ == "__main__":    
	bienvenida()    
while True:    
		query = tomar_comando().lower()    
		if 'hora' in query:    
			hora()    
		elif 'fecha' in query:    
			fecha()    
		elif 'buscar en wikipedia' in query:    
			hablar("Buscando en wikipedia...")    
			query = query.replace("buscar en wikipedia","")    
			wikipedia.set_lang("es")  
			resultado = wikipedia.summary(query, sentences=2)    
			print(resultado)    
			hablar(resultado)    
		elif 'enviar correo' in query:    
			try:    
				hablar("¿Qué debo poner en el correo?")    
				contenido = tomar_comando()  
				hablar("¿A quién quieres enviar el correo?")    
				para = 'destinatario@gmail.com'    
				enviar_email(para,contenido)    
				hablar("¡Correo enviado!")    
			except Exception as e:    
				print(e)    
				hablar("Lo siento, no puedo enviar el correo en este momento. Por favor, inténtalo más tarde.")    
    
		elif 'buscar en internet' in query:    
			hablar("¿Qué debo buscar?")    
			ruta_chrome = 'C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe %s' # Directorio del navegador Chrome en Windows  
			busqueda = tomar_comando().lower()    
			wb.get(ruta_chrome).open_new_tab(busqueda + '.com')    
		    
		elif 'cerrar sesión' in query:    
			os.system("shutdown -l")    
    
		elif 'apagar' in query:    
			os.system("shutdown /s /t 1")    
    
		elif 'reiniciar' in query:    
			os.system("shutdown /r /t 1")    
		    
		elif 'reproducir música' in query:    
			directorio_musica = 'C:/Users/gteran/Desktop/Universidad/IA/proyectoIA/musica'    
			canciones = os.listdir(directorio_musica)    
			os.startfile(os.path.join(directorio_musica, canciones[0]))    
    
		elif 'recuerda esto' in query:    
			hablar("¿Qué quieres que recuerde?")    
			datos = tomar_comando()    
			hablar("Me has pedido que recuerde "+datos)    
			recordar = open('datos.txt','w')    
			recordar.write(datos)    
			recordar.close()    
			    
		elif 'sabes algo' in query:    
			recordar =open('datos.txt', 'r')    
			hablar("Me has pedido que recuerde "+recordar.read())    
		elif 'capturar pantalla' in query:  
			captura_pantalla()  
			hablar("Captura realizada.")    
		elif 'cpu' in query:    
			cpu()    
		elif 'chiste' in query:    
			chistes()    
		elif 'apagar' in query:  
			hablar('Hasta pronto!')  
			quit()  
