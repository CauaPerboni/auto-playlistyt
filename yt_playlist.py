import pyautogui
import time
import webbrowser

playlist_url = '# Insira a URL'

def abrir_youtube_playlist():
    webbrowser.open(playlist_url)
    
    time.sleep(5)
    
    # Iniciar a reprodução da playlist (ajuste as coordenadas conforme necessário)
    pyautogui.click(x=600, y=400) 
    print("Playlist iniciada.")

abrir_youtube_playlist()
