Instruções de como rodar o projeto: 
- Com o Python e o Pip instalado, rode o comando "python -m venv venv" no diretorio principal (path/Github/prova-m5-semana9)
- Ative o ambiente virtual rodando (no mesmo diretório) "./venv/Scripts/activate"
- Com o Venv rodando, rode o comando "pip install -r requirements.txt"
- No diretório central rode "python main.py"

A partir de agora o projeto está rodando 100%

Requisições Fornecidas:
- Rota GET /ping -> Retorna um json {"resposta": "pong"}
- Rota POST /echo -> Deve receber um body no formato {"dados": "texto"} -> Retorna um json {"resposta": Informação enviada no body}
- Rota GET /info -> Retorna por mídia HTML os logs de todas as requisições feitas desde o início do programa com data e hora.
NOTA: Tudo isso é armazenado em memória e não em um banco de dados, portanto quando o sistema for reiniciado tudo será perdido. 
- Rota /dash -> Disponibiliza uma página Html para conferir todos os logs
