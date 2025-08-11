# Teste automatizado utilizando Cypress

## Avaliação Técnica 
Projeto realizado para verificação de funcionamento de um botão em página simples por teste E2E empregando o framework Cypress. O uso de .click() simula a interação do usuário e de .contains() verifica o resultado esperado.
Ambiente configurado com Visual Studio Code, Node.js e Git.

## Método
O projeto foi iniciado pelo VScode utilizando o terminal para abrir o cypress com o comando "npx cypress open";
Ao clicar para realizar um teste E2E (end-to-end) na aba que se abre, podemos criar um novo spec, que se encontra dentro da pasta "e2e" já no VScode;
No código, foi identificado a linha de comando cy.visit e o site indicado dentro das aspas foi substituído pela URL da página que iremos testar o botão (é importante salvar o arquivo em cada etapa das alterações do código para que possamos visualizar as atualizações descritar a partir do próximo passo);
Voltando à página do cypress que se abriu, o site com o botão que será testado aparece na tela de visualização;
Utilizando a ferramenta de "mira" localizada no topo da página, conseguimos clicar nos elementos contidos na página que estamos trabalhando, neste caso, ao clicar no botão "Enviar", temos acesso ao código que se refere à este campo;
Ao copiar e colar o código na linha de comando logo abaixo do cy.visit, utilizamos .click() no final do código para a simulação de que este elemento seja clicado ao rodar o teste na página do cypress;
O teste de automação é iniciado ao clicar no botão ao ládo da ferramenta de mira;
Ao clicar no botão 'Enviar" a mensagem "Enviado com sucesso!" aparece na tela, assim, utilizamos a ferramenta de mira para copiar as informações contidas no campo da mensagem, ao colar na linha de código, concluímos a linha com .contains() para verificar se este elemento contém a mensagem esperada;
Rodar o teste novamente inclui todas as ações anteriores e finaliza sem erros, indicando o clique no botão e a verificação de que a mensagem aparece na tela.

## Tecnologias utilizas
Este projeto foi construído com:
- Visual Studio Code - editor de código.
- Git - sistema de controle.
- Node.js - ambiente de execução.
- Cypress - framework de testes.

## Instalação
Node
- Acesse https://nodejs.org/pt;
- Clique em “Download” na versão LTS;
- Abra o arquivo .msi baixado e clique em next em todas as etapas, mantendo as opções padrão marcadas (incluindo npm);
finalize clicando em "Install"
- Verifique a intalação abrindo o prompt de comando e digite: "node --version" e também "npm --version", as versões instaladas deverão aparecer na tela.

Git
- Acesse https://git-scm.com/downloads;
- Escolha o sistema operacional indicado para sua máquina e realize o download.

Cypress
- Acesse https://docs.cypress.io/app/get-started/install-cypress;
- Copie o comando "npm install cypress --save-dev" no início da página;
- Abra o terminal do VScode e clique no ícone "Launch Profile" e clique em "Git Bash";
- Cole o comando e aperte enter para finalizar a instalação.

## Site utilizado para teste do botão: https://matheusmontanari.github.io/botao-enviar/

## Readme a respeito do arquivo "spec.cy.js" incluído neste repositório.
