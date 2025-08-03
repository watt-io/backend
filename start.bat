@echo off
echo 🚀 Iniciando WATT Filmes API...
echo.

REM Adicionar Docker ao PATH
set PATH=%PATH%;C:\Program Files\Docker\Docker\resources\bin

REM Verificar se Docker está funcionando
docker --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Docker não encontrado!
    pause
    exit /b 1
)

echo ✅ Docker funcionando!
echo 📦 Executando docker compose up --build...
echo.

REM Executar docker compose
docker compose up --build

pause 