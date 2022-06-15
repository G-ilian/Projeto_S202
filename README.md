<h1 align ="center">Loja de Ferramentas - Projeto S202</h1>

<p>A aplicação em questão se trata de um sistema de fácil utilização para compras em uma loja de ferramentas, que é capaz de realizar um CRUD completo. Foi totalmente desenvolvida com Python e o banco de dados escolhido para armazenamento dos dados foi o MongoDB</p>

<p>O projeto foi desenvolvido para o projeto prático da disciplina de Banco de Dados 2 - S202 </p>


### 💻 Funcionalidades
- Cadastrar produtos em um carrinho de compras.
- Lista os produtos que estão cadastrados no carrinho.
- Atualizar dados do produto.
- Deletar produtos.

### 🚀 Começando
Para obter uma cópia do projeto a fim de operá-lo/testá-lo em sua máquina,clone o repositório em uma pasta na sua máquina:
```
$ git clone git@github.com:G-ilian/Projeto_S202.git
```
### 📋 Pré-requisitos para execução
- IDE para execução de códigos Python (ex: Visual Studio Code,PyCharm)
- MongoDB Atlas ou Mongo DB Compass

### 🔧 Instalação e execução
-Venv 
<p>Para uma melhor experiência ao executar a aplicação é recomendado a criação de um ambiente virtual (venv), que possibilitará isolar a aplicação e sua execução do nosso sistema operacional</p>
<p>Para a criação e ativação da venv siga os seguintes comandos: </p>
- Criação
<p>Obs: O nome da venv deve estar fora das aspas duplas</p> 

```
$ python -m venv "Nome da venv que você deseja criar"
```

- Ativação
Para windows(Lembrar sempre de verificar se está na raiz do projeto):

- Acessar a pasta venv

```
$ cd venv
```

- Acessar Scripts

```
$ cd Scripts
```

- Ativar a venv

```
$ activate
```

<p>
Posteriormente a esta ativação da venv volte até a pasta de origem de nome 'Projeto - S202'.Será necessário para isso executar o seguinte código por duas vezes:
</p>

```
$ cd ..
```

- Linux ou MacOS
```
$ source tutorial-env/bin/activate
```

**Preparação**
<p>Após termos feito a configuração e ativado nosso ambiente virtural, podemos então partir para a preparação para a execução do código</p>
<p>Para isto é necessário fazer a instalação do pré requisitos que permitem a execução, esta instalação pode ser feita através do comando no terminal</p>

```
$ pip install -r requirements.txt
```

### ⚙️ Executando os testes

<p>Após ter instalado todos os pré requisitos, podemos partir para a execução da aplicação, para isto será necessário executar alguns comandos pelo terminal, estando na pasta raiz do projeto execute os seguinter códigos </p>

```
$ python main.py
```

<p>Não se esqueça de trocar as informações do BD, tais como url de conexão, usuário e senha para as suas informações :)</p>

## ✒️ Autor

***Gabriel Ilian Fonseca Barboza*** - [Gabriel](https://github.com/G-ilian)