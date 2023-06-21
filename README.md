# 🎓 NotFound Server

## 📘 Sobre o Servidor

O NotFound Server é um projeto desenvolvido com Python e Django que tem como objetivo gerenciar dados acadêmicos de alunos de faculdades. Este servidor foi projetado para ser uma solução robusta e flexível para a gestão de dados acadêmicos, proporcionando uma interface amigável e intuitiva.

## 🔧 Como foi feito o servidor

O servidor foi construído usando Python, uma linguagem de programação de alto nível, junto com o Django, um framework de alto nível em Python que incentiva o desenvolvimento rápido e o design limpo e pragmático. O Django foi escolhido por sua arquitetura baseada em modelo-visão-controlador (MVC), que permite a separação clara entre a lógica de negócios e a interface do usuário.

## 📋 Requisitos para utilizar o sistema

Para rodar o NotFound Server na sua máquina, você precisa ter os seguintes requisitos instalados:

- Python (versão 3.7 ou superior)

Além disso, é necessário que você tenha um conhecimento básico de como usar a linha de comando no seu sistema operacional.

## 🚀 Como usar

Primeiramente, clone o repositório usando o seguinte comando no terminal:

```sh
git clone https://github.com/FacensProjects/Facens-NotFound-Server.git
```

Em seguida, entre na pasta do projeto com o comando:

```sh
cd Facens-NotFound-Server
```

Agora, instale as dependências do projeto usando o pip, o gerenciador de pacotes do Python:

```sh
pip install -r requirements.txt
```

Depois de instalar as dependências, você precisa configurar o banco de dados. O Django facilita essa tarefa com o comando makemigrations:

```sh
python manage.py makemigrations
```

E então, aplique as migrations com o comando:

```sh
python manage.py migrate
```

Agora, crie um superusuário para ter acesso ao painel administrativo:

```sh
python manage.py createsuperuser
```

E finalmente, inicie o servidor com o comando:

```sh
python manage.py runserver
```

Agora você pode acessar o servidor localmente no endereço: http://127.0.0.1:8000/

## 👥 Desenvolvedores
[WhitePoodleMoth](https://github.com/WhitePoodleMoth)

## 📄 Licença
O NotFound Server é licenciado sob a MIT License. Veja o arquivo [LICENSE](https://github.com/FacensProjects/Facens-NotFound-Server/blob/main/LICENSE) para mais detalhes.
