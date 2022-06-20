# PRIMEIRA TABELA !!
# tabela de Medicos
# iserir, Listar, Alterar e apagar

import mysql.connector
def conectar():
	mydb = mysql.connector.connect(
	  host="localhost",
	  user="root",
	  password="",
	  database="consultas"
	)
	return mydb
	
def cadastra():

	nome = input(" Digite o Nome do Medico a ser cadastrado: ")
	email = input("Digite o E-mail: ")
	
	mydb = conectar()

	mycursor = mydb.cursor()

	sql = "INSERT INTO medicos (nome, email) VALUES (%s, %s)"
	val = (nome, email)
	mycursor.execute(sql, val)

	mydb.commit()
	mycursor.close()
	mydb.close()
	

	print(mycursor.rowcount, "cadastro adicionado.")


# exibir tabelas presentes em um banco 
def listar():
	print('listar tabela de medicos')

	mydb = conectar()
	
	mycursor = mydb.cursor() 
	  
	mycursor.execute("SELECT * FROM medicos;") 
	  
	myresult = mycursor.fetchall() 
	print('{:^8}|{:^11}|{:^10}'.format('ID', 'NOME','E-MAIL'))	
	for (id, nome, email) in myresult: 
		print('{:^8}|{:^11}|{:^10}'.format(id, nome, email))
		
	mycursor.close()
	mydb.close()
  # tentar fazer sozinha
  
#uptade
def alterar():
	print('alterar as informaçoes')
	id = int(input(' digite um id: '))
	nome = input("digite o nome: ")
	email = input("digite o E-mail: ")
	
	mydb = conectar()

	mycursor = mydb.cursor()

	sql = "UPDATE medicos SET nome = %s, email = %s WHERE id = %s"
	val = (nome, email, id)
	mycursor.execute(sql,val)

	mydb.commit()
	mycursor.close()
	mydb.close()

	print(mycursor.rowcount, "record(s) affected")

# deletar
def apagar():
	print(' selecione o id que sera excluido!')
	id = int(input(' digite um id: '))
	
	mydb = conectar()

	mycursor = mydb.cursor()

	sql = "DELETE FROM medicos WHERE id = %s"
	val = (id,)
	mycursor.execute(sql,val)

	mydb.commit()
	mycursor.close()
	mydb.close()

	print(mycursor.rowcount, "record(s) deleted")
	
# SEGUNDA TABELA
# tabela de especialidade
def cadastra_especialidades():
	print('cadastra especialidade')
	nome = input("Digite o Nome da especialidade: ")
	
	mydb = conectar()

	mycursor = mydb.cursor()

	sql = "INSERT INTO especialidades (nome) VALUES (%s)"
	val = (nome,)
	mycursor.execute(sql, val)

	mydb.commit()
	mycursor.close()
	mydb.close()

	print(mycursor.rowcount, "foi adicionado a especialidade.")

def listar_especialidades():
	print('tabela de especialidades')

	mydb = conectar()
	
	mycursor = mydb.cursor() 
	  
	mycursor.execute("SELECT * FROM especialidades;") 
	  
	myresult = mycursor.fetchall() 
	print('{:^8}|{:^11}'.format('ID', 'NOME'))	
	for (id, nome) in myresult: 
		print('{:^8}|{:^11}'.format(id, nome))
		
	mycursor.close()
	mydb.close()
	
def alterar_especialidades():
	print('alterar as informaçoes de especialidades')
	id = int(input(' digite um id: '))
	nome = input("digite o nome da especialidade: ")
	
	
	mydb = conectar()

	mycursor = mydb.cursor()

	sql = "UPDATE especialidades SET nome = %s WHERE id = %s"
	val = (nome, id)
	mycursor.execute(sql,val)

	mydb.commit()
	mycursor.close()
	mydb.close()

	print(mycursor.rowcount, "record(s) affected")
def apagar_especialidades():
	print('selecione o id que sera excluido!')
	id = int(input(' digite um id: '))
	
	mydb = conectar()

	mycursor = mydb.cursor()

	sql = "DELETE FROM especialidades WHERE id = %s"
	val = (id,)
	mycursor.execute(sql,val)

	mydb.commit()
	mycursor.close()
	mydb.close()

	print(mycursor.rowcount, "record(s) deleted")
	
# TERCEIRA TABELA
# TABELA de Medicos_Tem_Especialidades
def medicos_tem_especialidades():
	print(" id, medico e sua especialidade")
	id_medico = input("Digite o id do medico: ")
	id_especialidade = input("Digite o id da especialidade: ")
		
	mydb = conectar()
	
	mycursor = mydb.cursor() 
	  
	mycursor.execute("SELECT* FROM medicos_tem_especialidades;") 
	  
	myresult = mycursor.fetchall() 
	for x in myresult: 
		print(x)
		
	mycursor.close()
	mydb.close()

#comando de repetição
# menu de opções	
while True:
	print( 'menu de opções' """
	( TABELA de MEDICOS )
	
	1) cadastra
	2) listar
	3) alterar
	4) apagar
	
	( TABELA de ESPECIALIDADES )
	
	5) cadastra_especialidades 
	6) listar_especialidades
	7) alterar_especialidades
	8) apagar_especialidades
	
	( TERCEIRA TABELA )
	9) especialidades que o medico tem
	
	( SAINDO DO SISTEMA )
	10)sair
	""")
	print("Digite uma das opções acima: ")
	opcao = input(": ")

	if opcao == '1': 
		cadastra()
	elif opcao =='2':
		listar()
	elif opcao =='3':
		alterar()
	elif opcao =='4':
		apagar()
	elif opcao =='5':
		cadastra_especialidades()
	elif opcao=='6':
		listar_especialidades()
	elif opcao=='7':
		alterar_especialidades()
	elif opcao =='8':
		apagar_especialidades()
	elif opcao =='9':
		medicos_tem_especialidades()
	elif opcao =='10':
		print('sair')
		break
		

