import subprocess

def criar_exe():
    comando = ['pyinstaller', '--onefile', 'yt_playlist.py']

    try:
        subprocess.run(comando, check=True)
        print("Executável criado com sucesso na pasta 'dist'.")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao criar o executável: {e}")

if __name__ == "__main__":
    criar_exe()
