# nosvotamos
Projeto Nós Votamos para Monitoria do Legislativo Municipal

## Instruções básicas:

- Instale docker, docker-compose e git-core
- clone este repositório
- execute, dentro da pasta: docker-compose up

###### execute o bash dentro do container nosvotamos_web_1:
- docker exec -ti nosvotamos_web_1 bash

###### execute as migrações do banco:
- python manage.py migrate

###### crie um super usuário e responda às perguntas:
- python manage.py createsuperuser

###### Importe as leis de uma cidade, por exemplo:
- python manage.py importa_teofilo_otoni
- python manage.py importa_foz_do_iguacu
- Crie o seu importador com base no comando que fica em: materias/management/commands/importa_teofilo_otoni.py

###### E é isso!

## TODO para o MVP de apresentação

### Modelagem de Matéria
- [ ] Modelagem de Versões propostas vinculadas a uma Matéria
- [ ] Modelagem de campos básicos da matéria
- [ ] Vincular a matéria com o domínio da cidade ex: (teofilootoni.mg.gov.br)

### Modelagem de Legislatura
- [ ] Permitir cadastrar Partidos
- [ ] Permitir cadastrar Vereadores
- [ ] Permitir cadastrar período legislativo ex: Vereador Fulano exerceu do dia 01/01/2015 ao dia 01/06/2015

### Modelagem Usuários
- [ ] Permitir dados básicos do usuário (usuário, senha, etc)
- [ ] Permitir login por rede social (ver: https://simpleisbetterthancomplex.com/tutorial/2016/10/24/how-to-add-social-login-to-django.html)
- [ ] Permitir cadastro de áreas de interesse, que deve ser cruzado com as áreas de impacto da matéria

### Interface básica
- [ ] Usuário visualiza matérias, filtrando por cidade, tipo e tramitação
- [ ] Usuário vê detalhes de uma matéria
- [ ] Usuário comenta em uma matéria
- [ ] Usuário cadastra áreas de interesse
