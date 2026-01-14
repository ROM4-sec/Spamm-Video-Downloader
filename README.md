# 📥 Video Downloader Funcional (ProjetoSpamm)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![CustomTkinter](https://img.shields.io/badge/GUI-CustomTkinter-blue?style=for-the-badge)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)
![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)

Um baixador de vídeos moderno, multiplataforma e fácil de usar. Desenvolvido em Python, este software automatiza o download e a conversão de mídias para o formato MP4 (H.264) com uma interface gráfica.

## ✨ Funcionalidades

* **Interface Moderna:** Construída com CustomTkinter para suporte a temas Dark/Light.
* **Multiplataforma:** Lógica adaptada para rodar perfeitamente em Windows e Linux.
* **Conversão Automática:** Garante que os vídeos sejam salvos em `.mp4` usando FFmpeg.
* **Organização Inteligente:** Cria automaticamente uma pasta na Área de Trabalho para salvar os arquivos.
* **Processamento em Segundo Plano:** Utiliza *Threading* para evitar que a interface trave durante o download.

---

## 🚀 Como Executar

### 🪟 No Windows (Para usuários finais)
1.  Certifique-se de ter o [Python](https://www.python.org/downloads/) instalado (marque a opção **"Add Python to PATH"**).
2.  Baixe este repositório e extraia a pasta.
3.  Dê dois cliques no arquivo `rodar.bat`. O sistema instalará as dependências e abrirá o programa automaticamente.

### 🐧 No Linux (BigLinux/Arch/Ubuntu)
1.  Instale o suporte ao Tkinter no seu sistema:
    ```bash
    sudo pacman -S tk  # Para Arch/BigLinux
    # ou
    sudo apt install python3-tk  # Para Ubuntu/Debian
    ```
2.  Ative seu ambiente virtual e instale as dependências:
    ```bash
    source venv/bin/activate
    pip install -r requirements.txt
    ```
3.  Execute o programa:
    ```bash
    python main.py
    ```

---

## 🛠️ Requisitos de Sistema
* **FFmpeg:** O executável deve estar dentro da pasta `bin/`.
    * `bin/ffmpeg.exe` (Windows)
    * `bin/ffmpeg` (Linux)
* **Bibliotecas Python:** `yt-dlp` e `customtkinter`.

---

## 📂 Estrutura do Projeto
```text
ProjetoSpamm/
├── bin/                # Binários do FFmpeg
├── main.py             # Código fonte principal
├── requirements.txt    # Dependências do projeto
├── rodar.bat           # Script de inicialização (Windows)
└── .gitignore          # Filtros para o Git
