import speech_recognition as sr
import simpleaudio as sa
from os import system
from time import sleep

r = sr.Recognizer()

def Voz(ArchivoAudio):
    wave_obj = sa.WaveObject.from_wave_file(ArchivoAudio)
    play_obj = wave_obj.play()
    play_obj.wait_done()

def ReconocimientoDeVoz():
    while(True):
        with sr.Microphone() as source:
            try:
                sleep(0.5)
                Voz('path/to/DigaComando.wav')
                print("Diga un comando: ")

                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
                texto = r.recognize_google(audio, language='es-ES')
                voz = '{}'.format(texto)
                return voz
            except:
                sleep(0.5)
                Voz('path/to/NoEscucho.wav')
                print("No se escucho...")

def Programas(comandoProgramas):
    print("INGRESAMOS al bucle 'PROGRAMA'")
    PalabrasReservadasProg = {'internet', 'multimedia', 'oficina', 'programar'}
    
    while(comandoProgramas not in PalabrasReservadasProg):

        comandoProgramas = ReconocimientoDeVoz()

        if(comandoProgramas == 'internet'):
            Voz('path/to/Internet.wav')
            system('firefox')
        elif(comandoProgramas == 'multimedia'):
            Voz('path/to/Multimedia.wav')
            system('vlc')
        elif(comandoProgramas == 'oficina'):
            Voz('path/to/Oficina.wav')
            system('libreoffice')
        elif(comandoProgramas == 'programar'):
            Voz('path/to/Code.wav')
            system('code')
            
    print("SALIMOS del bucle 'PROGRAMA'")
    return
    
def Volumen(comandoVolumen):
    print("INGRESAMOS al bucle 'VOLUMEN'")
    PalabrasReservadasVol = {'subir', 'bajar', 'silenciar', 'activar'}
    
    while(comandoVolumen not in PalabrasReservadasVol):
        comandoVolumen = ReconocimientoDeVoz()
        if(comandoVolumen == 'subir'):
            Voz('path/to/Subir.wav')
            system('amixer sset Master 10%+')
        elif(comandoVolumen == 'bajar'):
            Voz('path/to/Bajar.wav')
            system('amixer sset Master 10%-')
        elif(comandoVolumen == 'silenciar'):
            Voz('path/to/Silenciar.wav')
            system('amixer sset Master mute')
        elif(comandoVolumen == 'activar'):
            Voz('path/to/Activar.wav')
            system('amixer sset Master unmute')
            
    print("SALIMOS del bucle 'VOLUMEN'")
    return

#Bloque Principal
Voz('path/to/SaludoInicial.wav')

print("""
Lista de comandos ---> Programas --> Internet(Firefox)
                  '             '--> Multimedia(VLC)
                  '             '--> Oficina(LibreOffice)
                  '             '--> Programar(VisualStudio)
                  '
                  '--> Volumen  --> Subir
                               '--> Bajar
                               '--> Silenciar
                               '--> Activar
""")  

while(True):
    comando = ReconocimientoDeVoz()
    print(comando)

    if(comando == 'volumen'):
        Volumen(comando)
    elif(comando == 'programa'):
        Programas(comando)
    elif(comando == 'salir' or comando == 'salió'):
        break

Voz('path/to/SaludoFinal.wav')
print("Fin del siclo")
system('clear')