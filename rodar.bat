@echo off
title Downloader ProjetoSpamm
cls

echo ================================================
echo    INICIALIZANDO PROJETO SPAMM DOWNLOADER
echo ================================================

:: 1. Verifica se o Python está instalando
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] python nao encontrado! Por favor, instale o Python.
    pause
    exit
)

:: 2. Cria o ambiente virtual se ele não existir
if not exist "venv_win" (
    echo [INFO] Criando ambiente virtual para Windows...
    python -m venv venv_win
)

:: 3. Ativa a venv e instala as dependencias
echo [INFO] Verificando bibliotecas...
call venv_win\Scripts\activate
pip install -r requirements.txt --quiet

:: 4. Roda o Programa
echo [INFO] Abrindo o programa...
python main.py

:: 5. Mantem a janela aberta se o programa fechar sozinho
if %errorlevel% neq 0 (
    echo.
    echo [ERRO] O programa fechou com um problema
    pause
)
