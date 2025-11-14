# Sistema Bancário Simples em Python

Este é um sistema bancário de alto nível implementado em Python, que permite o gerenciamento básico de contas, incluindo cadastro de clientes, login, depósitos, saques, verificação de saldo e emissão de extrato.

## Funcionalidades

- **Saídas Coloridas**: Utilização de funções auxiliares (`print_success`, `print_error`, `print_warning`, `print_info`) para mensagens coloridas e padronizadas no console.
- **Cadastro de Cliente**: Permite cadastrar um novo cliente com CPF e nome. O CPF é único e serve como identificador da conta. Agora, é possível cancelar o cadastro deixando o campo CPF em branco.
- **Status do Usuário**: Novos usuários são cadastrados com o status "Ativo".
- **Login do Cliente**: Autentica o cliente através do CPF. Se o CPF não for reconhecido, o sistema solicita uma nova tentativa ou retorno ao menu principal.
- **Menu Pós-Login**: Após o login, o cliente tem acesso às seguintes opções:
    - **Realizar Depósito**: Adiciona um valor à conta do cliente e registra a transação.
    - **Realizar Saque**: Retira um valor da conta, verificando se há saldo suficiente e permitindo o uso do cheque especial. Registra a transação e o valor utilizado do cheque especial.
    - **Verificar Saldo**: Exibe o saldo atual da conta, o limite do cheque especial e o valor já utilizado do cheque especial.
    - **Emitir Extrato**: Mostra todas as movimentações (depósitos e saques) com data, hora, tipo de operação e valor, além do saldo final.
    - **Solicitar Limite Cheque Especial**: Permite ao cliente solicitar um limite de cheque especial, com aprovação automática para valores até R$ 500 e análise para valores maiores.
    - **Fazer Logout**: Retorna ao menu principal.
- **Menu de Usuários**: Uma nova opção no menu principal que permite:
    - **Listar Usuários**: Exibe o CPF, Nome e Status (Ativo/Inativo) de todos os usuários cadastrados.
    - **Inativar Usuário**: Altera o status de um usuário para "Inativo" e registra a transação.
    - **Reativar Usuário**: Altera o status de um usuário para "Ativo" e registra a transação.

## Estrutura do Projeto

- `bank_system.py`: Contém a lógica principal do sistema bancário, incluindo as funções de menu, cadastro, login e operações bancárias básicas.
- `bank_system_v2.py`: Uma versão aprimorada do sistema bancário que incorpora funcionalidades adicionais, como o gerenciamento do cheque especial e outras melhorias.
- `bank_common.py`: Contém funções comuns e utilitárias utilizadas por ambos os sistemas (`bank_system.py` e `bank_system_v2.py`), como as funções de impressão colorida e a lógica de persistência de dados.
- `data/dataPorConta.json`: Arquivo JSON utilizado para persistir os dados das contas dos clientes, saldos e histórico de transações.
- `transaction_types.json`: Arquivo JSON que define os tipos de transações disponíveis no sistema.

## Como Executar

1. Certifique-se de ter o Python instalado em sua máquina.
2. Navegue até o diretório onde os arquivos `bank_system.py` e `data/dataPorConta.json` estão localizados.
3. Execute o script Python a partir do terminal:
   ```bash
   python bank_system.py
   ```
4. Siga as instruções no console para interagir com o sistema.

## Persistência de Dados

Os dados das contas são armazenados em um arquivo `data/dataPorConta.json`. Cada conta é identificada pelo CPF e contém o nome do cliente, saldo e uma lista de transações. As transações incluem data/hora, tipo (depósito/saque) e valor.

## Testes

O projeto inclui um conjunto de testes unitários para garantir a integridade e o correto funcionamento das funcionalidades implementadas. Os testes são executados utilizando o `pytest`.

Para executar os testes:

1. Certifique-se de ter o `pytest` instalado:
   ```bash
   pip install pytest
   ```
2. Navegue até o diretório raiz do projeto.
3. Execute os testes com o seguinte comando:
   ```bash
   pytest
   ```
   Todos os testes devem passar, indicando que as funcionalidades estão operando conforme o esperado.

## Melhorias Futuras

Esta seção detalha possíveis aprimoramentos e novas funcionalidades para o sistema bancário, visando expandir suas capacidades e melhorar a experiência do usuário.

### 1. Funcionalidades Financeiras Avançadas

*   **Cheque Especial**:
    *   **Adicionar Campo de Limite**: Incluir um campo `limite_cheque_especial` no objeto da conta no `data/dataPorConta.json`.
    *   **Lógica de Aprovação**: Desenvolver uma lógica para aprovar ou negar solicitações de cheque especial, que pode ser baseada em critérios como histórico de transações, tempo de conta, etc.
    *   **Utilização do Limite**: Modificar a função de `sacar` para permitir saques que excedam o `saldo`, utilizando o `limite_cheque_especial`.
    *   **Cálculo de Juros**: Implementar um mecanismo para calcular juros sobre o valor utilizado do cheque especial.
    *   **Interface de Solicitação**: Adicionar uma opção no `menu_pos_login` para o cliente solicitar ou verificar seu `limite_cheque_especial`.
*   **Transferências entre Contas**: Permitir que os usuários transfiram dinheiro para outras contas dentro do sistema, utilizando o CPF do destinatário.
*   **Agendamento de Transações**: Implementar a capacidade de agendar depósitos, saques ou transferências para datas futuras.
*   **Empréstimos Pessoais**: Desenvolver um módulo para solicitação, aprovação e gerenciamento de empréstimos, com cálculo de parcelas e juros.
*   **Pagamento de Contas**: Funcionalidade para pagar contas (água, luz, telefone) diretamente pelo sistema.
*   **Investimentos Automatizados**: Opções para configurar investimentos automáticos com base em regras predefinidas.
*   **Suporte a Múltiplas Moedas**: Permitir transações e saldos em diferentes moedas, com conversão automática.

### 2. Segurança e Autenticação

*   **Autenticação de Dois Fatores (2FA)**: Adicionar uma camada extra de segurança ao processo de login, como envio de código por SMS ou e-mail.
*   **Histórico de Acessos**: Registrar e exibir o histórico de logins do usuário, incluindo data, hora e IP (se aplicável).
*   **Bloqueio de Conta/Cartão**: Funcionalidade para o usuário bloquear temporariamente ou permanentemente sua conta em caso de suspeita de fraude ou perda.
*   **Alertas de Segurança**: Notificações sobre atividades suspeitas na conta (e.g., login de um novo dispositivo, transações incomuns).

### 3. Relatórios e Análises

*   **Geração de Relatórios Financeiros**: Criar relatórios detalhados de movimentações (mensais/anuais), categorizando gastos e receitas.
*   **Categorização de Transações**: Permitir que o usuário categorize suas transações (e.g., alimentação, transporte, lazer) para um melhor controle financeiro.
*   **Orçamentos e Metas Financeiras**: Ferramentas para o usuário definir orçamentos mensais e acompanhar o progresso em relação às suas metas financeiras.

### 4. Gerenciamento de Cartões

*   **Emissão de Cartões Virtuais**: Permitir a criação de cartões de débito/crédito virtuais para compras online.
*   **Controle de Limites de Gastos**: Opção para o usuário definir limites diários/mensais para transações com cartão.

### 5. Usabilidade e Interface

*   **Interface Gráfica (GUI)**: Desenvolver uma interface de usuário mais intuitiva e amigável, utilizando bibliotecas como Tkinter, PyQt ou uma abordagem web-based.
*   **Notificações Personalizadas**: Enviar alertas por e-mail ou SMS para eventos importantes, como saldo baixo, transações de alto valor ou pagamentos agendados.
*   **Integração com Assistentes de Voz**: Adicionar suporte para comandos de voz para operações bancárias básicas.

## Comentários no Código

O código está detalhadamente comentado em português para facilitar a compreensão de cada função e bloco de código.