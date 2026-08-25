# 🚕 Urban Routes — Automação de Testes E2E de Solicitação de Táxi (Tarifa Comfort)
![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Selenium](https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=selenium&logoColor=white)
![Caso de Testes](https://img.shields.io/badge/Caso_de_Testes-0052CC?style=for-the-badge&logo=testrail&logoColor=white)
![PyCharm](https://img.shields.io/badge/PyCharm-000000?style=for-the-badge&logo=pycharm&logoColor=white)

Uma solução completa de Automação de Testes End-to-End (E2E) desenvolvida em Python e Selenium WebDriver para validar todo o fluxo de pedido de táxi na tarifa "Comfort" do aplicativo Urban Routes.

---

## 📌 O que é o projeto?
Em plataformas de transporte e mobilidade urbana, falhas durante o fluxo de reserva, seleção de tarifa, adição de cartão ou pedido de serviços adicionais impactam diretamente a conversão e a experiência do usuário.

Este projeto foca na automação do fluxo completo de solicitação de táxi na tarifa "Comfort", validando desde a inserção dos endereços de origem e destino até a confirmação do pedido e busca pelo motorista. A suíte automatizada cobre as seguintes etapas sequenciais da aplicação:

- Definição de Rota: Inserção automatizada dos endereços de origem ("De") e destino ("Para").

- Seleção de Tarifa: Seleção do modo de transporte e ativação da tarifa Comfort.

- Autenticação de Telefone: Inserção do número do celular e captura/preenchimento automático do código SMS de confirmação.

- Método de Pagamento: Adição e vinculação de um novo cartão de crédito (número, código CVV e perda de foco para validação).

- Comentários ao Motorista: Envio de mensagem personalizada para o condutor.

- Requisitos Adicionais: Ativação do pedido de mantas e lenços.

- Adição de Itens: Solicitação de sorvetes (2 unidades).

- Finalização do Pedido: Acionamento do botão de busca por táxi e validação da abertura do modal de busca do motorista.

---

## 🚀 Diferenciais: Funcionalidades e Impacto de Negócio

- Padrão Page Object Model (POM): Arquitetura altamente modular com separação clara entre seletores, ações de página (UrbanRoutesPage) e cenários de teste (TestUrbanRoutes).

- Tratamento Dinâmico de SMS: Automação capaz de interagir com o fluxo de autenticação via telefone, recuperando o código de confirmação diretamente dos logs da aplicação/gerenciador.

- Resiliência e Sync Automático: Utilização estratégica de esperas explícitas (WebDriverWait e expected_conditions) para eliminar flaky tests causados por animações e renderização assíncrona da interface.

- Validação E2E da Tarifa Comfort: Cobertura ponta a ponta dos seletores e comportamentos específicos da tarifa Comfort (manta, lenços, contadores de itens adicionais).

---

## 🛠️ Arquitetura e Tecnologias utilizadas

```
QA-Brazil_Python_Automation/
├── data.py                     # Massas de dados de teste (Enderecos, Telefone, Cartao)
├── helpers.py                  # Funcoes auxiliares (recuperacao de codigo SMS)
├── pages.py                    # Mapeamento do Page Object Model (POM) e Locators
├── main.py                     # Suite de testes automatizados com Pytest
├── .gitignore                  # Arquivos ignorados pelo Git
├── README.md                   # Documentacao principal
└── requirements.txt            # Dependencias do projeto
```
- Linguagem Principal: Python 3.10+

- Automação Web: Selenium WebDriver

- Framework de Testes: Pytest

- Arquitetura: Page Object Model (POM)

---

## 🧪 Validação e Qualidade da Aplicação (QA)

Para assegurar a confiabilidade da automação e a integridade da aplicação durante todo o processo de solicitação, foram adotadas as seguintes práticas de QA:

- Isolamento de Dados de Teste: Centralização de massas de teste em arquivo dedicado (data.py), permitindo a alteração simples de cartões, telefones e rotas.

- Validação das Etapas do Formulário: Verificação de cada sub-etapa do fluxo antes de prosseguir (confirmação do cartão adicionado, validação do contador de sorvetes incrementado para 2).

- Asserção do Estado Final: Checagem rigorosa da exibição do modal de busca de táxi ao finalizar o pedido, garantindo que o fluxo não foi interrompido por erros de contrato ou renderização.

---

## 👩‍💻 Autora e Contato
Isabela Bueno — Psicóloga Escolar | Analista Educacional Sênior | Data & Tech Enabler (QA & Python)

📧 E-mail: isabelabueno.tech@gmail.com

💼 LinkedIn: isabela-bueno-silva

🐱 GitHub: @isabelabuenotech
