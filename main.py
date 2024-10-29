from src.models.store import Store
from src.models.user import User
from src.service.service_user import ServiceUser

store = Store()
# print(store.bd)

name = 'Leonardo'
job = 'TechLead'

user = User(name=name, job=job)

service = ServiceUser()
adicionar = service.add_user(name=name, job=job)
print(adicionar)

nome = 'Matheus'

deletar = service.del_user(name=nome)
print(deletar)

nome = 'Leonardo'

consultar = service.select_user(name=nome)
print(consultar)

nome = 'Leonardo'
newjob = 'Arquiteto'

alterar = service.update_user(name=nome, new_job=newjob)
print(alterar)