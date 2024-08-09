# Bot de Monitoramento de Câmbio (Dólar) 💹

## Descrição do Projeto 📋

Este projeto é um bot em Python criado para monitorar a cotação do dólar (USD) em relação ao Real Brasileiro (BRL) no site [Google Finance](https://www.google.com/finance/quote/USD-BRL). O bot automatiza a coleta do valor da cotação, registra a data e a hora, salva o URL da página e faz uma captura de tela da cotação. Todos esses dados são organizados em um relatório, que é gerado em formato PDF.

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

## Configuração para Usuários 🔧

### Requisitos

- O instalador incluirá todas as dependências necessárias.

### Instruções para Execução ▶️

1. Faça o download do instalador `mysetup.exe` disponível no repositório.
2. Execute o instalador para instalar o programa em seu sistema.
3. Após a instalação, abra o programa para iniciar a execução.

## Configuração para Desenvolvedores 🔧

### Requisitos

- Python 3.x 🐍
- Bibliotecas: `selenium`, `docx`, `docx2pdf`, `pytz`, `os`, `datetime`

### Instalação das Dependências

1. Clone o repositório:

   ```bash
   git clone https://github.com/RonieSouza/Bot-Monitoramento-Cambio-Dolar.git
   cd Bot-Monitoramento-Cambio-Dolar
   ```
   
2. Configure um ambiente virtual (opcional, mas recomendado):

   ```bash
   python -m venv venv
   # No Linux use `source venv/bin/activate`
   # No Windows use `venv\Scripts\activate`
   ```

3. Instale as dependências usando o arquivo requirements.txt:

   ```bash
   pip install -r requirements.txt
   ```

## Exemplo de Uso 💡

Após instalar o programa, você precisará executá-lo manualmente. O bot então começará a coletar e registrar os dados. O relatório gerado em PDF estará disponível com as informações atualizadas.

## Problemas Conhecidos ⚠️

- **Falhas na Coleta de Dados:** A coleta de dados pode falhar se o site alvo estiver fora do ar ou se houver mudanças significativas na estrutura da página.
- **Problemas de Permissão:** Se o programa for instalado em um diretório protegido, como `C:\Program Files`, pode haver problemas na criação de arquivos devido à falta de permissões adequadas. Para resolver, execute o programa como administrador.
- **Erro de Conversão para PDF:** Se o Microsoft Office não estiver instalado, a conversão do arquivo Word para PDF pode falhar. Embora o arquivo Word seja criado normalmente, a conversão para PDF pode não funcionar. Se isso ocorrer, você pode **converter manualmente** o arquivo utilizando serviços de conversão online ou outras ferramentas de software para transformar o arquivo `.docx` em `.pdf`.

    
## Licença 📝

Este projeto está licenciado sob a Licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.
