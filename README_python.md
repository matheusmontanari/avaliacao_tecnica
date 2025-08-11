# Verificador de palíndromos

## Visão Técnica
O projeto consiste em um script realizado em Python que identifica se uma palavra é ou não um palíndromo, ou seja, se pode ser lida da mesma forma de trás para frente.
A entrada é capturada por input(), é realizada a conversão dos caracteres digitados para letras minúsculas com .lower(),
a comparação da palavra digitada com a sua versão invertida é realizada utilizando slicing( [::-1] ), para retornar o resultado da verificação é utilizada a estrutura condicional if/else e conta com o uso de f-strings para um código mais legível.
O projeto foi desenvolvido no Visual Studio Code, utilizando Python 3.8 como linguagem.

## Método
Utilização da função def para iniciar um bloco onde foi atribuído uma função à uma palavra;
Com .lower consegui fazer com que qualquer caractere que será digitado após a solicitação, seja convertido em letras minúsculas, padronizando a visualização do resultado;
Finalizo o bloco com return, ele vai comparar a palavra com a "versão" invertida dela (consigo realizar essa inversão utilizando slicing [::-1]) e finalizar a função;
Como o teste necessita de uma entrada pelo usuário para ser verificada, utilizo input para receber a palavra;
Finalizo o código com if else, uma vez que essa condicional consegue me retornar o objetivo desta tarefa, informando se a palavra digitada é ou não um palíndromo.
Utilizo f-string que me permite inserir o valor da variável que criei no início do código diretamente dentro da frase utilizando chaves. Considerei essa maneira menos "poluída" visualmente do que com uma concatenação.

## Tecnologias utilizadas
Este projeto foi construído com:
- Visual Studio Code - editor de código-fonte.
- Python 3.8.10 - linguagem de programação.
- Node.js - ambiente de execução.

## Instalação
Python
- Acesse o site oficial https://www.python.org/downloads/ e baixe a versão mais recente;
- Execute o instalador e marque a opção "Add Python to PATH" antes de clicar em "Install Now".
- Aguarde a instalação terminar;
- Abra o prompt de comando e digite: "python --version", clique enter e a mensagem com a versão instalada deverá aparecer.
Node
- Acesse https://nodejs.org/pt;
- Clique em “Download” na versão LTS;
- Abra o arquivo .msi baixado e clique em next em todas as etapas, mantendo as opções padrão marcadas (incluindo npm);
finalize clicando em "Install"
- Verifique a intalação abrindo o prompt de comando e digite: "node --version" e também "npm --version", as versões instaladas deverão aparecer na tela.

## Readme a respeito do arquivo "teste1palindromo.py" incluído neste repositório.
