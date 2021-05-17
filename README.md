BEXS BANCO - TESTE
=======================

Introdução
------------

Está é uma simples aplicação teste baseada em [Python] (https://www.python.org) para empresa BEXS BANCO.

Instalação
------------

Primeiramente, certifique-se de possuir a instalação das ferramentas [pyenv](https://github.com/pyenv/pyenv#installation) e [pip](https://pip.pypa.io/en/stable/installing/), a partir disso, pode-se clonar ou baixar uma cópia da branch `main`.

Através de um terminal, acesse a raíz do projeto e execute o comando:

    $ make install

A instalação irá resolver todas as dependências do projeto, criar ambiente prórpio para aplicação (pyenv), executar testes unitários, de integração e code convention.

Caso deseje visualizar todas as ações pré-configuradas, execute o comando:

    $ make

A seguinte lista de comandos deve ser exibida:

    test                Run tests
    code-convention     Run code convention
    install             Create venv, install dev requirements, run tests and code-convention
    run-console         Run CLI application
    run-http-server     Run HTTP server application

Armazenamento de dados
----------------

Esta aplicação utiliza .csv como fonte de armazenamento e leitura de dados. Diferentemente da proposta inicial, não é necessário setar o arquivo ao executar a aplicação, caso o arquivo não exista, ele será criado no diretório `data` e será usado a partir de então. 

OBS: Havendo necessidade na utilização de backups, basta colocá-lo no diretório `data` sob o nome `routes.csv`.

Testes unitários, de integração e code convention
----------------

Todos os testes são executados na instalação da aplicação, ainda assim, é possível executá-los sempre que necessário através dos comandos:

    $ make test
    $ make code-convention

OBS: É possível acompanhar o resultado dos testes no prórpio terminal onde os comandos forão executados, porém, pode-se também acessar de forma navegável abrindo em um navegador o arquivo abaixo, que é gerado a cada execução:

    {{application-path}}/htmlcov/index.html

Execução da aplicação
----------------

Por se tratar de uma api, a aplicação não possui interface `GUI` e deve ser inicializada a partir de um web server. Para executar operações, utilize comandos `CURL` ou softwares como o [Postman](https://www.postman.com/). Uma cópia da collection contendo exemplos de execução para uso no Postman pode ser [importada](https://learning.postman.com/docs/getting-started/importing-and-exporting-data/#importing-data-into-postman) através do arquivo abaixo:

    {{application-path}}/docs/Bexs-Banco.postman_collection.json

OBS: Caso o Postman seja utilizado, crie uma variável global contendo o host e a porta para que as requests sejam realizadas corretamente:

    VARIABLE        INITIAL VALUE          CURRENT VALUE
    bexs-banco-api  http://localhost:5000  http://localhost:5000

Para a inicialização do web server, execute o comando:

    $ make run-http-server

OBS: O web server por padrão irá ser iniciado no host `http://127.0.0.1` utilizando a porta `5000`, podendo ser alterado a partir do arquivo:

    {{application-path}}/app/constants.py

Por outro lado, também é possível interagir com a aplicação através de interface `CLI`, para isso, execute o comando:

    $ make run-console

OBS: Por não considerar a interface `CLI` a execução prioritária, seus retornos em relação a erros são simplificados em comparação a api, porém, conta com os mesmos recursos.
