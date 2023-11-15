### Requisitos para desenvolvimento:
- Python 3.12.0

### Configuração do ambiente
Para conseguir contribuir com o projeto, é necessário algumas configurações iniciais.
- Adicione a [chave de API da Geocoding API](https://console.cloud.google.com/apis/library) no .env do projeto. Dentro da raiz do repositório você consegue achar um arquivo chamado ```.env.example```, copie o conteúdo desse arquivo e substitua os valores coringas pelo valores reais.
- Rode o seguinte comando para instalar as dependências do projeto.

    ```bash
    pip install -r requirements.txt
    ```

### Para rodar o projeto localmente:
Verificar se cumpre com os requisitos para o desenvolvimento, se sim basta rodar o comando abaixo e para iniciar o projeto em modo debug.

```bash
flask --app api/index.py --debug run
```

### Instalar uma nova dependência ao projeto:
Caso uma nova feature precisou de uma nova dependência para ser instalada, rode o seguinte comando para atualizar o ```requirements.txt``` do projeto:
```bash
pip freeze > requirements.txt
```
