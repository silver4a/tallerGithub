#!/bin/sh

# Salir inmediatamente si un comando falla
set -e

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar pruebas
pytest