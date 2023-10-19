## Meu Projetos do Santander Dev Week 2023

 Fiz esse repositório para os projetos que foram propostos pela DIO e desenvolvidos por mim durante o Santander Bootcamp 2023 - Ciência de Dados com Python, que ocorreu entre os dias 16/08/2023 até 22/10/2023, no site da Digtal Innovation One (DIO).

 Nesse repositório é possivel encontrar os seguintes projetos:

1. [Explorando IA Generativa em um Pipeline de ETL com Python](Projetos_em_Python/Ia_Generativa_Pipeline_Etl.py)

    Nesse projeto, o objetivo era realizar um Pipeline ETL, isto é, extrair dados de uma API do Banco Santander, transformar os dados gerando uma mensagem personalizada para cada usuário - utilizando a IA Generativa GPT-4 - e carregar os dados transformados para a API do Santander novamente.
        
    ### Passo um: criar usuários no API
    Iniciei o projeto criando 5 usuários na API do Santander, via [Swagger UI](https://sdw-2023-prd.up.railway.app/swagger-ui/index.html#/Users%20Controller/findById), produzido e disponibilizado pela equipe da [DIO](https://www.dio.me/):
        
    | ID   |   Nome   | Número  | Agência | Limite Conta |        Cartão       | Limite Cartão |
    |---:  |----------|-------- |---------|--------------|---------------------|---------------|
    | 5200 |  Marina  | 34200-4 |   0018  |      500     | **** **** **** 5184 |     1000      |
    | 5201 |  Alice   | 36201-4 |   0018  |      500     | **** **** **** 5186 |     1000      |
    | 5202 |  Laura   | 37202-4 |   0018  |      500     | **** **** **** 5618 |     1000      |
        
   ### Passo dois: criar um arquivo .csv com os IDs criados
   Criei um arquivo .csv no meu computador com apenas a coluna ID e salvei com o nome _SDW2023.csv_
   | ID   |
   |---:  |
   | 5200 |
   | 5201 |
   | 5202 |
        
   [Continua (...)](Projetos_em_Python/Ia_Generativa_Pipeline_Etl.py)


2. [Desafios Python: Equilibrando Saldo](<Projetos_em_Python/Equilibrando Saldo.py>)

   Nesse projeto, o desafio era para eu considerar que fui contratada por uma empresa bancária para auxiliar nas implementações e melhorias do sistema empresarial. Em uma análise inicial, foi identificado pela equipe financeira a necessidade de desenvolver uma solução que permita ao cliente equilibrar seu saldo bancário. Dessa forma, o programa deve solicitar uma entrada que representa o saldo atual do funcionário, e após, seja informado o valor de duas transações, sendo elas: _um depósito e um saque_. O programa deve atualizar o saldo com base nas transações e exibir o saldo final.

   **Informação:** As transações de depósito e retirada devem ser tratadas como valores positivos e negativos, respectivamente, para garantir que o cálculo do saldo final seja realizado corretamente.

    ### Entrada

    _saldoAtual_: um número decimal representando o saldo atual da conta bancária.
    _valorDeposito_: um número decimal representando o valor a ser depositado na conta.
    _valorRetirada_: um número decimal representando o valor a ser retirado da conta.

    **Regra de Formatação:** Considere apenas uma casa decimal para esse desafio.

    ### Saída

    Um número decimal que representa o saldo atualizado na conta bancária após o processamento das transações. 

    [Continua(...)](<Projetos_em_Python/Equilibrando Saldo.py>)
    
3. [Desafios Python: Organizando seus ativos](Projetos_em_Python/Organizando_seus_Ativos.py)

    **Descrição do terceiro desafio:** Após uma análise cuidadosa realizada pela equipe de desenvolvimento de uma empresa bancária, foi identificado a necessidade de uma nova funcionalidade para otimizar os processos e melhorias da experiência dos usuários. Agora, sua tarefa é implementar uma solução que organize em ordem alfabética uma lista de ativos que será informada pelos usuários. Os ativos são representados por strings que representam seus tipos, como por exemplo: Reservas de liquidez, Ativos intangiveis e dentre outros.

    ### Entrada

    A primeira entrada consiste em um número inteiro que representa a quantidade de ativos que o usuário possui. Em seguida, o usuário deverá informar, em linhas separadas, os tipos (strings) dos respectivos ativos.

    ### Saída

    Seu programa deve exibir a lista de Ativos organizada em ordem alfabética. Cada ativo deve ser apresentado em uma linha separada.

    [Continua(...)]()Projetos_em_Python/Organizando_seus_Ativos.py

4. [Desafios Python: Condicionalmente rico](Projetos_em_Python/Condicionalmente_Rico.py)

    **Descrição do quarto desafio:** Uma nova feature para um sistema bancário foi analisada pela equipe de desenvolvimento e será uma das tarefas a serem trabalhadas durante a sprint, como desenvolvedor da empresa você recebeu os requisitos para a nova implementação que consiste em uma solução algorítmica que permita aos clientes realizarem saques em caixas eletrônicos. No entanto, existem algumas regras a serem seguidas para garantir que um saque possa ser realizado com sucesso.

    **Regras do saque:**

    - Cada cliente digitará o valor do seu saldoTotal de sua conta bancária e o valorSaque.
    - Um saque só pode ser realizado se o saldoDisponível na conta for igual ou superior ao valor solicitado.
    - Se o saldo for suficiente, o valor solicitado deve ser subtraído do saldo disponível, indicando que o saque foi realizado.
    - Se o saldo for insuficiente, o saque não deve ser realizado e uma mensagem adequada deve ser exibida.

    ### Entrada
    A entrada consiste em dois valores inteiros que representam o total do saldo da conta e o valor do saque.

    ### Saída
    Se o saque for realizado com sucesso, exibir a mensagem "Saque realizado com sucesso! Novo saldo: {saldo}", onde {saldo} é o novo saldo disponível na conta.

    Se o saque não for possível devido a saldo insuficiente, exibir a mensagem "Saldo insuficiente. Saque nao realizado!"

    [Continua (...)](Projetos_em_Python/Condicionalmente_Rico.py)

5. [Desafios Python: Juros compostos](Projetos_em_Python/Juros_Compostos.py)

    **Descrição do quinto desafio:** Imagine que você está desenvolvendo um aplicativo para um banco que deseja calcular os juros compostos de um investimento. Seu objetivo é criar uma função que receba três parâmetros: o valor inicial do investimento, a taxa de juros anual e o período de tempo em anos. A função deve calcular e retornar o valor final do investimento após o período determinado, levando em consideração os juros compostos.

    ### Entrada:
    A função deve receber os seguintes parâmetros:

    *valor_inicial:* um número inteiro ou decimal representando o valor inicial do investimento.
    *taxa_juros:* um número decimal representando a taxa de juros anual. Por exemplo, se a taxa for de 5%, o valor passado será 0.05.
    *periodo:* um número inteiro representando a quantidade de anos do investimento.

    ### Saída:
    A função deve retornar o valor final do investimento após o período determinado, considerando os juros compostos. O valor final deve ser arredondado para duas casas decimais.

    [Continua (...)](Projetos_em_Python/Juros_Compostos.py) 

6. [Desafios Python: O grande depósito](Projetos_em_Python/O_Grande_Dep%C3%B3sito.py)

    **Descrição do sexto desafio:** Você foi contratado por um banco para desenvolver um programa que auxilie seus clientes a realizar depósitos em suas contas. O programa deve solicitar ao cliente o valor do depósito e verificar se o valor é válido. Se o valor for maior do que zero, o programa deve adicionar o valor ao saldo da conta. Caso contrário, o programa deve exibir uma mensagem de erro. O programa deve soliticar apenas uma vez o valor de depósito.

    ### Entrada
    O programa deve utilizar o Scanner para receber o valor de depósito digitado pelo cliente. Os valor pode ser decimal, representando valor em reais.

    ### Saída
    O programa deve exibir uma mensagem de sucesso quando um valor de depósito válido for informado e o saldo da conta for atualizado. Se o valor for "0", deverá imprimir uma mensagem encerrando o programa. Caso um valor inválido seja digitado, o programa deve exibir uma mensagem de erro solicitando um novo valor.

    [Continua (...)](Projetos_em_Python/O_Grande_Dep%C3%B3sito.py)

7. [Criando um relatório de vendas elegante com Power BI](Projetos_em_Power_BI/PowerBi_vendas)
   
    # Desafio Power BI DIO: Criando um Relatório de Vendas Elegante com Power BI

     Este subdiretório é destinado ao meu projeto do primeiro desafio de Power BI da DIO. Neste desafio, eu deveria criar um relatório mais elaborado com base na sample financials do Power BI. 
     Os arquivos de dados estão disponíveis no github: 

     [GitHub da Prof.ª Juliana Zanelatto](https://github.com/julianazanelatto/power_bi_analyst )

    ### Atenções que deveria ter no projeto:

     1. Estrutura definida 
     2. Botões de navegação que fornecem navegabilidade 
     3. Segmentadores utilizados e botões com imagem associado 
     4. Utilize os indicadores e botões para selecionar diferentes visuais sobre um mesmo assunto 

    ### O que eu fiz:

     Baixei o template disponibilizado no GitHub da professora e realizei algumas alterações, de forma a apresentar da maneira que eu queria.

8. [Processando e transformando dados com Power BI](Projetos_em_Power_BI/PoweBI_transformando_dados)
   
    # Desafio Power BI DIO: Processando e Transformando Dados com Power BI

     Esse é meu segundo desafio de Power BI da DIO.
    
     Os arquivos de dados estão disponíveis no github: 

     [GitHub da Prof.ª Juliana Zanelatto](https://github.com/julianazanelatto/power_bi_analyst )

    ### Descrição do desafio:
     1. Criação de uma instância na Azure para MySQL
     2. Criar o Banco de dados com base disponível no github
     3. Integração do Power BI com MySQL no Azure
     4. Verificar problemas na base a fim de realizar a transformação dos dados

    ### Diretrizes para transformação dos dados
     1. Verifique os cabeçalhos e tipos de dados
     2. Modifique os valores monetários para o tipo double preciso
     3. Verifique a existência dos nulos e analise a remoção
     4. Os employees com nulos em Super_ssn podem ser os gerentes. Verifique se há algum colaborador sem gerente
     5. Verifique se há algum departamento sem gerente
     6. Se houver departamento sem gerente, suponha que você possui os dados e preencha as lacunas
     7. Verifique o número de horas dos projetos
     8. Separar colunas complexas
     9. Mesclar consultas employee e departament para criar uma tabela employee com o nome dos departamentos associados aos colaboradores. A mescla terá como base a tabela employee. Fique atento, essa informação influencia no tipo de junção
     10. Neste processo elimine as colunas desnecessárias.
     11. Realize a junção dos colaboradores e respectivos nomes dos gerentes . Isso pode ser feito com consulta SQL ou pela mescla de tabelas com Power BI. Caso utilize SQL, especifique no README a query utilizada no processo.
     12. Mescle as colunas de Nome e Sobrenome para ter apenas uma coluna definindo os nomes dos colaboradores
     13. Mescle os nomes de departamentos e localização. Isso fará que cada combinação departamento-local seja único. Isso irá auxiliar na criação do modelo estrela em um módulo futuro.
     14. Explique por que, neste caso supracitado, podemos apenas utilizar o mesclar e não o atribuir.  
     15. Agrupe os dados a fim de saber quantos colaboradores existem por gerente
     16. Elimine as colunas desnecessárias, que não serão usadas no relatório, de cada tabela

 Neste curso, utilizei a liguagem de programação Python, além de ter explorado SQL e Power BI. Vale resaltar que também aprendi sobre Fundamentos e Técnicas de Machine Learning.