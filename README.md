# Scraper de Notebooks Lenovo

Este projeto é uma aplicação de web scraping que coleta dados de notebooks Lenovo do site de teste de e-commerce da [Web Scraper](https://webscraper.io/test-sites/e-commerce/static/computers/laptops). A aplicação raspa todos os notebooks Lenovo disponíveis, ordena-os do mais barato para o mais caro e exibe todos os dados disponíveis dos produtos.

## Funcionalidades

- **Raspagem de Dados**: Coleta informações como título, preço, descrição, avaliações, classificação, imagem e link do produto.
- **Ordenação**: Os notebooks são ordenados do mais barato para o mais caro.
- **API RESTful**: Disponibiliza uma API que retorna os dados raspados em formato JSON.
- **Interface Web**: Exibe os dados em uma tabela interativa no navegador.
- **Download de Dados**: Permite baixar os dados em um arquivo JSON diretamente da interface web.

## Tecnologias Utilizadas

- **Python 3**
- **Flask**: Framework web para criar a API e servir a interface.
- **BeautifulSoup**: Biblioteca para fazer o parsing do HTML e extrair os dados.
- **HTML/CSS/JavaScript**: Para construir a interface web.
- **Virtual Environment (venv)**: Para gerenciar as dependências do projeto.

## Pré-requisitos

- **Python 3.x** instalado.
- **Git** (opcional, para clonar o repositório).

## Como Executar o Projeto

### 1. Clonar o Repositório

```bash
git clone https://github.com/marcinhojazz/crawler-test
cd crawler-test
```

### 2. Criar e Ativar o Ambiente Virtual

```bash
python -m venv venv
```

- Ativar no Windows:

  ```bash
  venv\Scripts\activate
  ```

- Ativar no Linux/MacOS:

  ```bash
  source venv/bin/activate
  ```

### 3. Instalar as Dependências

Crie um arquivo `requirements.txt` com o seguinte conteúdo:

```txt
Flask
requests
beautifulsoup4
```

Então, instale as dependências:

```bash
pip install -r requirements.txt
```

### 4. Executar a Aplicação

```bash
python app.py
```

A aplicação estará rodando em `http://localhost:5000/`.

### 5. Acessar a Interface Web

Abra o navegador e acesse:

```
http://localhost:5000/
```

## Uso da Aplicação

### Interface Web

- **Carregar Dados**: Clique no botão "Carregar Dados" para iniciar a raspagem e exibir os notebooks Lenovo na tabela.
- **Visualizar Produto**: Clique no título do produto para abrir a página original do produto em uma nova aba.
- **Salvar em JSON**: Após carregar os dados, clique em "Salvar em JSON" para baixar um arquivo com os dados raspados.

### API RESTful

- **Endpoint**: `http://localhost:5000/lenovo-notebooks`
- **Descrição**: Retorna os dados dos notebooks Lenovo em formato JSON.
- **Exemplo de Uso**:

  ```bash
  curl http://localhost:5000/lenovo-notebooks
  ```

## Estrutura do Projeto

```
├── app.py
├── requirements.txt
├── templates
│   └── index.html
├── static
    └── css
        └── style.css
```

- **app.py**: Código principal da aplicação Flask com a lógica de raspagem e APIs.
- **requirements.txt**: Lista de dependências Python do projeto.
- **templates/index.html**: Página HTML que exibe os dados e interage com a API.
- **static/css/style.css**: Arquivo CSS para estilização da página.

## Detalhes do Código

### app.py

- **Funções Principais**:
  - `get_total_pages(soup)`: Determina o número total de páginas a serem raspadas.
  - `scrape_lenovo_notebooks()`: Raspa os dados dos notebooks Lenovo e os ordena.
- **Rotas**:
  - `@app.route('/')`: Serve a página inicial com a interface web.
  - `@app.route('/lenovo-notebooks')`: Endpoint da API que retorna os dados em JSON.

### index.html

- **Descrição**: Página que exibe os dados em uma tabela e interage com o usuário.
- **Componentes**:
  - Botão para carregar os dados e exibi-los.
  - Botão para salvar os dados em um arquivo JSON.
  - Tabela para exibir os dados dos notebooks Lenovo.

### style.css

- **Estilização**:
  - Layout responsivo para desktop e dispositivos móveis.
  - Estilos para botões, tabela e texto.
  - Efeitos de hover e transições para melhorar a experiência do usuário.

## Observações

- **Desempenho**: A raspagem pode levar alguns segundos, dependendo da velocidade da conexão.
- **Uso Ético**: Este projeto é para fins educacionais e utiliza um site de testes. Sempre respeite os termos de uso e o arquivo `robots.txt` de sites reais ao fazer web scraping.
- **Contribuição**: Sinta-se à vontade para clonar o repositório e fazer melhorias.

## Autor

- **Márcio Machado Pontes**
- [LinkedIn](https://www.linkedin.com/in/marcio-machado-pontes-2a2661137)
- [GitHub](https://github.com/marcinhojazz)

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

---
