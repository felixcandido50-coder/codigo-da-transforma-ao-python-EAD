Aqui está a versão adaptada do **README.md** especificamente para o código do **Sistema de Agendamento de Barbearia**:

---

# 🏗️ Panorama Geral do README.md

O documento foi projetado para destacar o seu projeto de **Barbearia** utilizando a biblioteca gráfica `Tkinter`. Ele contém:

* **Título Atrativo:** Alinhado com a temática de barbearia ( Barber Shop).
* **Descrição do Projeto:** O que o sistema faz de forma clara.
* **Funcionalidades:** Explicação visual do fluxo do programa e navegação por telas.
* **Instruções de Implementação/Execução:** Como o professor ou colegas podem rodar o código na máquina deles.
* **Destaque de Conceitos de Programação:** Explicação didática de como a Orientação a Objetos (Classes), listas, dicionários e a interface gráfica trabalham juntos.

---

# 💈 Sistema de Vendas e Gerenciamento - Barbearia (Barber Shop System)

Bem-vindo ao repositório do **Sistema de Agendamento e Gerenciamento de Barbearia**! Este projeto foi desenvolvido em Python utilizando a biblioteca gráfica `Tkinter` (com suporte a `ttk`) para fornecer uma interface de usuário (UI) moderna, intuitiva e temática para o agendamento de serviços, controle de vagas/estoque e configuração de serviços.

---

## 🚀 Funcionalidades Principais

O sistema foi desenhado para organizar a rotina de atendimento de uma barbearia real, contando com as seguintes ferramentas:

1. **📝 Agendamento de Horários:**
* Visualização dos serviços disponíveis com preço, duração e vagas restantes.
* Seleção interativa do profissional (barbeiro) responsável através de uma janela modal (*pop-up*).
* Baixa automática no número de vagas/estoque ao confirmar o agendamento.
* Bloqueio automático de agendamentos caso as vagas fiquem esgotadas.


2. **🛠️ Gerenciamento e Edição de Serviços (CRUD):**
* Seleção dinâmica de serviços existentes via menu suspenso (`Combobox`).
* Carregamento automático das informações no formulário para edição.
* Atualização de nome, profissionais habilitados, preço, duração, descrição e vagas.


3. **📊 Status do Estoque e Vagas:**
* Painel informativo em tempo real mostrando a quantidade de vagas disponíveis para cada serviço.
* Alerta visual com destaque de cor diferenciada quando um serviço está esgotado.


4. **📍 Localização, Contato e Sobre:**
* Informações completas sobre endereço, horários de funcionamento e canais de contato com os clientes.


5. **🛡️ Validação de Erros e Segurança:**
* Tratamento de exceções com `try/except` para garantir que campos numéricos (como Preço e Vagas) recebam dados válidos, evitando falhas repentinas no aplicativo.



---

## 🛠️ Tecnologias e Estruturas Utilizadas

* **Python 3**: Linguagem base do projeto.
* **Tkinter & TTK**: Bibliotecas padrão do Python para criação da interface gráfica (GUI), janelas modais (`Toplevel`), seletores (`Combobox`) e mensagens de alerta (`messagebox`).
* **Programação Orientada a Objetos (POO)**: Organização do sistema na classe `BarbeariaApp`, facilitando a manutenção e alternância dinâmica entre as telas.
* **Estruturas de Dados Dinâmicas**:
* **Listas (`[]`)**: Para armazenar e iterar sobre o catálogo de serviços.
* **Dicionários (`{}`)**: Para mapear as propriedades de cada serviço individualmente (nome, barbeiros, preço, duração, descrição, estoque).


* **Tratamento de Exceções (`try/except`)**: Utilizado no formulário de edição para tratar erros de conversão de dados (`ValueError`).

---

## 💻 Como Executar o Projeto

Para rodar este sistema na sua máquina, você só precisa ter o Python instalado. **Não é necessária a instalação de nenhuma dependência externa!**

1. Clone este repositório ou baixe o código fonte.
2. Abra o terminal na pasta onde o arquivo `.py` está salvo.
3. Execute o comando:
```bash
python nome_do_teu_arquivo.py

```


*(Substitua `nome_do_teu_arquivo.py` pelo nome real do arquivo salvo na sua máquina).*

---

## 📚 Método Educativo: O que aprendemos aqui?

Este projeto demonstra a aplicação prática de vários conceitos fundamentais de desenvolvimento de software:

### 🧩 Interface Gráfica (GUI) vs Interface de Linha de Comando (CLI)

Diferente de scripts executados no terminal, o uso do `Tkinter` introduz o conceito de **Programação Orientada a Eventos**. O sistema permanece em um *loop* contínuo (`mainloop()`) aguardando ações do usuário (cliques de botões, seleção em listas) para acionar as funções correspondentes.

### 🔄 Manipulação de Dados em Memória

Os serviços são gerenciados em tempo de execução usando uma estrutura composta (lista de dicionários):

```python
# Exemplo da estrutura utilizada:
servicos = [
    {
        "nome": "Corte",
        "barbeiros": "Gustavo, Nicolas, Felipe, Victor",
        "preco": 30.00,
        "validade": "7 dias",
        "descricao": "O melhor corte da região.",
        "estoque": 10
    }
]

```

---

## 👥 Participantes e Organização

* **Projeto Desenvolvido por:** [Insere o teu Nome / Gustavo, Nicolas, Felipe, Victor]
* **Disciplina:** Pensamento Computacional / Projeto Código da Transformação

---

## ⚙️ Instruções de Implementação

1. **Crie um arquivo** chamado `README.md` na raiz do seu projeto local.
2. **Copie e cole** o texto acima dentro desse arquivo.
3. Altere a seção `👥 Participantes e Organização` com o seu nome e os integrantes do seu grupo.
4. Faça o `commit` e o `push` para o seu repositório no GitHub antes da apresentação para garantir uma apresentação profissional do projeto!