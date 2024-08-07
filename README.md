# Bot de Monitoramento de Câmbio (Dólar) 💹

## Descrição do Projeto 📋

Este projeto é um bot em Python criado para monitorar a cotação do dólar (USD) em relação ao Real Brasileiro (BRL) em um site de câmbio. O bot automatiza a coleta do valor da cotação, registra a data e a hora, salva o URL da página e faz uma captura de tela da cotação. Todos esses dados são organizados em um relatório, que é gerado em formato PDF.

## Funcionalidades ⚙️

1. **Consulta Automatizada:**
   - Acessa um site de câmbio e coleta o valor atual do dólar.
   - Registra a data e o horário da cotação.
   - Salva o URL do site onde a cotação foi realizada.
   - Captura uma imagem da tela com a cotação.

2. **Criação de Relatório Word:**
   - Organiza os dados coletados em um documento Word, incluindo a captura de tela.

3. **Conversão para PDF:**
   - Converte o relatório Word gerado em um arquivo PDF.

4. **Entrega como Executável:**
   - O projeto inclui um instalador para facilitar a distribuição e uso do programa.

## Configuração do Ambiente 🔧

### Requisitos

- Python 3.x 🐍
- Bibliotecas: `selenium`, `docx`, `docx2pdf`, `pytz`, `os`, `datetime`

### Instruções para Execução ▶️

1. Faça o download do instalador disponível no repositório.
2. Execute o instalador para instalar o programa em seu sistema.
3. Após a instalação, abra o programa para iniciar a execução automática.

## Exemplo de Uso 💡

Após instalar o programa, você precisará executá-lo manualmente. O bot então começará a coletar e registrar as cotações. O relatório gerado em PDF estará disponível com as informações atualizadas.

## Problemas Conhecidos ⚠️

- A coleta de dados pode falhar se o site alvo estiver fora do ar ou se houver mudanças significativas na estrutura da página.

## Licença 📝

Este projeto está licenciado sob a Licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.
