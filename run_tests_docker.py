#!/usr/bin/env python3
"""
Script para executar testes da API WATT Filmes usando Docker
"""

import subprocess
import sys
import os


def run_docker_command(command, description):
    """Executa um comando Docker e exibe o resultado"""
    print(f"\n{'='*60}")
    print(f"🚀 {description}")
    print(f"{'='*60}")
    
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Erro ao executar: {e}")
        print(f"Stderr: {e.stderr}")
        return False


def main():
    """Função principal"""
    print("🧪 EXECUTOR DE TESTES - WATT FILMES API (DOCKER)")
    print("=" * 60)
    
    # Verificar se estamos no diretório correto
    if not os.path.exists("tests"):
        print("❌ Diretório 'tests' não encontrado!")
        print("   Execute este script no diretório raiz do projeto.")
        sys.exit(1)
    
    # Verificar se o Docker está disponível
    try:
        subprocess.run(["docker", "--version"], check=True, capture_output=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("❌ Docker não encontrado! Instale o Docker primeiro.")
        sys.exit(1)
    
    # Lista de comandos para executar
    commands = [
        ("docker compose run --rm watt-tests python -m pytest --version", "Verificando versão do pytest"),
        ("docker compose run --rm watt-tests python -m pytest -v --tb=short", "Executando todos os testes"),
        ("docker compose run --rm watt-tests python -m pytest tests/test_auth.py -v", "Testes de autenticação"),
        ("docker compose run --rm watt-tests python -m pytest tests/test_filmes.py -v", "Testes de filmes"),
        ("docker compose run --rm watt-tests python -m pytest tests/test_usuarios.py -v", "Testes de usuários"),
        ("docker compose run --rm watt-tests python -m pytest tests/test_crud.py -v", "Testes CRUD"),
        ("docker compose run --rm watt-tests python -m pytest tests/test_auth_jwt.py -v", "Testes JWT"),
    ]
    
    success_count = 0
    total_commands = len(commands)
    
    for command, description in commands:
        if run_docker_command(command, description):
            success_count += 1
        else:
            print(f"⚠️  Falha em: {description}")
    
    # Resumo final
    print(f"\n{'='*60}")
    print("📊 RESUMO DOS TESTES")
    print(f"{'='*60}")
    print(f"✅ Comandos executados com sucesso: {success_count}/{total_commands}")
    
    if success_count == total_commands:
        print("🎉 Todos os testes foram executados com sucesso!")
        sys.exit(0)
    else:
        print("⚠️  Alguns testes falharam. Verifique os erros acima.")
        sys.exit(1)


if __name__ == "__main__":
    main() 