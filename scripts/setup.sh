#!/bin/bash
# Script de configuração inicial para o ambiente de desenvolvimento

echo "Iniciando configuração do ambiente de desenvolvimento..."

# Criar diretórios adicionais se necessário
mkdir -p build
mkdir -p temp
mkdir -p logs

# Verificar dependências
echo "Verificando dependências..."

# Verificar se git está instalado
if ! command -v git &> /dev/null; then
    echo "Git não encontrado. Por favor, instale o Git para continuar."
    exit 1
fi

# Verificar se python está instalado
if ! command -v python3 &> /dev/null; then
    echo "Python 3 não encontrado. Por favor, instale o Python 3 para continuar."
    exit 1
fi

echo "Todas as dependências estão instaladas."

# Configuração do git local
echo "Configurando Git..."
git config core.autocrlf input
git config core.fileMode false

# Mensagem de conclusão
echo "Configuração concluída com sucesso!"
echo "O ambiente de desenvolvimento está pronto para uso."
