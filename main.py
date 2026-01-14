import os
import platform
import yt_dlp
import sys
import customtkinter as ctk
from threading import Thread
import subprocess

#configurações de aparência
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

def verificar_setup():
    #verifica se a estrutura de pastas e os bínarios necessários existem
    
    #pega o diretório do scrip
    diretorio_raiz = os.path.dirname(os.path.abspath(__file__))
    pasta_bin = os.path.join(diretorio_raiz, "bin")
    
    #verifica se a pasta 'bin' existe
    if not os.path.exists(pasta_bin):
        return False, f"Pasta 'bin' não encontrada em: {pasta_bin}"
    
    #identifica o S.O.
    sistema = platform.system()
    ffmepeg_nome = "ffmpeg.exe" if sistema == "Windows" else "ffmpeg"
    caminho_completo_ffmpeg = os.path.join(pasta_bin, ffmepeg_nome)
    
    #verifica se o arquivo do FFmpeg esta no loca
    if not os.path.exists(caminho_completo_ffmpeg):
        return False, f"FFmpeg ({sistema}) não encontrado na pasta bin."
    
    return True, caminho_completo_ffmpeg     

def baixar_video(url, caminho_ffmpeg, callback_status):
    
    try:
            #Pastas na area de trabalho
            home = os.path.expanduser("~")
            sistema = platform.system()
            desktop = ""
            
            if sistema == "Windows":
                desktop = os.path.join(home, "Desktop")
            
            else:
                #No linux, verifica no sistema qual a pasta correta
                
                try:
                    #o comando 'xdg-user-dir' retorna o caminho exato da área de trabalho
                    process = subprocess.Popen(['xdg-user-dir', 'DESKTOP'], stdout=subprocess.PIPE)
                    desktop = process.communicate()[0].decode('utf-8').strip()
                except:
                    #caso o comando falhe, tentamos usar os nomes comuns
                    desktop = os.path.join(home,"Desktop")
                    if not os.path.exist(desktop):
                        desktop = os.path.join(home, "Área de Trabalho")
                        
            #cria o caminho final
            pasta_destino = os.path.join(desktop, "Projeto Spamm Videos")
            
            #garante que a pasta seja criada no local certo
            os.makedirs(pasta_destino, exist_ok=True)
        
            opcoes = {
                
                #define o formato: melhor vídeo + melhor áudio disponível
                'format': 'bestvideo+bestaudio/best',
                
                #define onde salvar e o nome: pasta Downloads do usuário / título do vídeo
                'outtmpl': os.path.join(pasta_destino, "%(title)s.%(ext)s"),
                
                #aqui passamos o caminho do FFmpeg que detectamos acima
                'ffmpeg_location': caminho_ffmpeg,
                
                #avisa para não baixar playlisys inteiras caso o link seja de uma playlista
                'noplaylist': True,
                
                #mantem o terminal limpo
                'quiet': True,
                
                #faz a conversão para MP4 caso o download não venha em MP4
                'postprocessors': [{
                    'key': 'FFmpegVideoConvertor',
                    'preferedformat': 'mp4',
                }],
            }

            callback_status("Baixando...", "yellow")
            with yt_dlp.YoutubeDL(opcoes) as ydl:
                ydl.download([url])
                
            callback_status("Sucesso! Verifique seus Downloads.", "green")
            
    except Exception as e:
        callback_status(f"Erro: {str(e)[:40]}...", "red")
        
class App(ctk.CTk):
    def __init__(self,ffmpeg_path):
        super().__init__()
        self.ffmpeg_path = ffmpeg_path
        
        #configuração da janela
        self.title("ProjetoSpamm - Downloader")
        self.geometry("900x525")
        self.configure(fg_Color='#1a1a1a') #fundo escuro
        
        #Texto topo
        self.label = ctk.CTkLabel(
            self, text="ADICIONE O LINK ABAIXO",
            font=("Arial Bold", 26), text_color="white"
        )
        self.label.pack(pady=(60,20))
        
        #Entry
        self.entry = ctk.CTkEntry(
            self, width=700, height=55, corner_radius=25,
            fg_color="#8c8c8c", text_color="black",
            placeholder_text="Cole a URL aqui...", border_width=0,
            font=("Arial", 16)
        )
        self.entry.pack(pady=20) #espaçando para não sumir
        
        #botão de baixar
        self.btn = ctk.CTkButton(
            self, text='BAIXAR VIDEO', command=self.iniciar_download,
            width=350, height=80, corner_radius=40,
            fg_color="#b3b3b3", hover_color="#999999",
            text_color="white", font=("Arial Bold", 24)
        )
        self.btn.pack(pady=(50,20))
        
        #label de status para feedback do usuario
        self.status_label = ctk.CTkLabel(self,text="", font=("Arial",14))
        self.status_label.pack(pady=10)
        
    def atualizar_status(self, mensagem, cor):
        self.status_label.configure(text=mensagem, text_color=cor)
        self.btn.configure(state="normal")
        
    def iniciar_download(self):
        url = self.entry.get()
        if not url:
            self.atualizar_status("Por Favor, cole um link!","red")
            return
        
        self.btn.configure(state="disabled") #para evitar cliques duplos
        self.status_label.configure(text="Iniciando...", text_color="white")
        
        Thread(target=baixar_video, args=(url, self.ffmpeg_path, self.atualizar_status)).start()
        
if __name__ == "__main__":
    #verifica antes de tudo
    sucesso, resultado = verificar_setup()
    
    if sucesso:
        app = App(resultado)
        app.mainloop()
    else:
        print(f"Erro de Setup: {resultado}")
        input("Pressione Enter para sair...")