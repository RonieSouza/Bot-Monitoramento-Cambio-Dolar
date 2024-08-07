import sys
import os
from cx_Freeze import setup, Executable

arquivo = ['icone_dolar.ico']

configuracao = Executable(
    script='gerador_relatorio_cotacao_dolar.py',
    icon='icone_dolar.ico'
)

setup(
    name = 'Gerador de Relatório da Cotação do Dólar',
    version = '1.0',
    description = 'Este programa gera um relatório em pdf com a cotação atual do dólar',
    author = 'Ronie Souza',
    options = {'build_exe': {'include_files': arquivo}},
    executables = [configuracao]
)