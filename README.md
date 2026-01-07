# projeto_facilita
Este é o <ins>__Projeto Facilita__</ins>, que tem como objetivo facilitar o cálculo de compras dos mais diversos tipos, como compras de mercado, por exemplo. Como funções destaques do código, há: Ordenação por Seleção (reordenar listas), Hash (endereçamento de lista) e Notação Big O (tempo de execução).

# 1. Introdução
- Dá boas vindas ao usuário;
- Solicita um nome para ser identificado durante o funcionamento do Projeto;
- Dá início ao Projeto.

# 2. Seção Principal
- Opção de Calcular Compras;
- Opção de Configuração do Usuário;
- Opção de Sair da Conta.

## 2.1 Calcular Compras
- Opção de Compra Livre;
- Opção de Compra Limitada;
- Opção de Dúvidas Frequentes;
- Opção de Encerrar Compra.

### 2.1.1 Compra Livre
- Opção de Adicionar Item à Compra;
- Opção de Ver a Lista de Compras;
- Opção de Remover Item do Carrinho;
- Opção de Finalizar a Compra.

#### • Adicionar Item à Compra
- Solicitar o nome do item, seu preço e sua quantidade ao usuário;
- Se os dados enviados pelo usuário estiverem corretos, serão adicionado à lista de compras;
- Se o nome do item for o mesmo de um item já inserido na lista, o valor antigo será substituído pelo valor novo.

#### • Ver a Lista de Compras
- Só funciona se tiver no mínimo 1 item na lista de compras;
- Opção de Ver do Mais Caro ao Mais Barato;
- Opção de Ver do Mais Barato ao Mais Caro;
- Opção de Ver Item da Lista;
- Opção de Ver Total Atual da Lista;
- Opção de Não Quero Consultar Agora.

##### • Ver do Mais Caro ao Mais Barato
- Vai mostrar a lista de compras começando pelo item mais caro, até chegar no item mais barato.

##### • Ver do Mais Barato ao Mais Caro
- Vai mostrar a lista de compras começando pelo item mais barato, até chegar no item mais caro.

##### • Ver Item da Lista
- Solicitará ao usuário enviar o nome do item que ele deseja consultar (com a lista de compras geral presente para facilitar a consulta);
- Se o nome do item inserido pelo usuário estiver presente na lista, será apresentado ao cliente os aspectos desse item, como o preço e a quantidade;
- Se não estiver na lista de compras o nome do item inserido pelo usuário, será informado que o item solicitado não foi encontrado.

##### • Ver Total Atual da Lista
- Mostrará o total de cada item individualmente, multiplicando o preço pela quantidade;
- Retornará no final o total atual da lista de compra, sendo essa a soma de todos os subtotais de cada item presente na lista de compras.

#####  • Não Quero Consultar Agora
- Retornará para a Seção de Compra Livre.

#### • Remover Item do Carrinho
- Solicitará ao usuário enviar o nome do item que ele deseja que seja removido da lista de compras;
- Se o nome do item enviado pelo usuário estiver presente na lista de compras, o item será removido da lista;
- Se não estiver presente na lista o nome do item enviado pelo usuário, será informado que o item solicitado não foi encontrado.

#### • Finalizar Compra
- Finalizará a compra, mostrando o total de cada item e o total geral da compra;
- Será agradecido o usuário pelo o uso da funcionalidade de calcular compras, e perguntará ao usuário se ele deseja continuar na seção de Calcular Compras;
- Se sim, voltará para a seção de Compra Livre, se não, voltará para a Seção Principal.

### 2.1.2 Compra Limitada
- Será solicitado ao usuário quanto de dinheiro será o limite para aquela compra, e a partir desse limite será decidido se haverá a compra ou não;
- A condição para a compra ser efetuada é não ultrapassar ou chegar ao valor exato do limite estabelecido;
- Opção de Adicionar o Item à Compra;
- Opção de Ver a Lista de Compras;
- Opção de Remover Item do Carrinho
- Opção de Finalizar a Compra.

#### • Adicionar Item à Compra, Ver a Lista de Compras (e suas sub-opções) e Remover Item do Carrinho
- Tais opções têm as mesmas funções que as presentes na Compra Livre.

#### • Finalizar Compra
- Se a compra for finalizada e o total geral ultrapassar o valor limite, a compra será cancelada;
- Caso o valor limite não seja ultrapassado, a compra será finalizada, mostrando o total de cada item e o total geral da compra;
- Mostrará também o troco da compra, subtraindo o valor limite pelo total geral da compra;
- Será agradecido o usuário pelo o uso da funcionalidade de calcular compras, e perguntará ao usuário se ele deseja continuar na seção de Calcular Compras;
- Será exibido o tempo total de uso da funcionalidade de calcular compras;
- Se sim, voltará para a seção de Compra Livre, se não, voltará para a Seção Principal.

### 2.1.3 Dúvidas Frequentes
- Exibe todas as funcionalidades disponível no Cálculo de Compras.

### 2.1.4 Encerrar Compra
- Encerra o cálculo de compras;
- Mostra o tempo que o usuário ficou nessa Seção.

## 2.2 Configuração do Usuário
- Pergunta ao usuário se ele deseja mudar o nome inicialmente inserido;
- Caso sim, será disponibilizado o meio de ser inserido um novo nome;
- Caso não, o usuário retorna à Seção Principal do Projeto.

## 2.3 Sair da Conta
- Agradecimentos ao usuário por ele ter usado o Projeto;
- Informará o tempo total de uso do Projeto;
- Informa o usuário o tempo total que ele usou o Projeto.
