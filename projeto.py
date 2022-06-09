# iserir dados na tabela

def cadastra():
	nome = input("Digite o Nome: ")
	email = input("Digite o E-mail: ")
	import mysql.connector

	mydb = mysql.connector.connect(
	  host="localhost",
	  user="root",
	  password="",
	  database="consultas"
	)

	mycursor = mydb.cursor()

	sql = "INSERT INTO medicos (nome, email) VALUES (%s, %s)"
	val = (nome, email)
	mycursor.execute(sql, val)

	mydb.commit()

	print(mycursor.rowcount, "record inserted.")


# exibir tabelas presentes em um banco 
def listar():
    print('listar')
    import mysql.connector 

    mydb = mysql.connector.connect( 
        host="localhost", 
        user="root", 
        password="", 
        database="consultas"
    ) 
      
    mycursor = mydb.cursor() 
      
    mycursor.execute("SELECT* FROM medicos;") 
      
    myresult = mycursor.fetchall() 
      
    for x in myresult: 
        print(x)
  # tentar fazer sozinha
  
#uptade
def alterar():
    print('alterar as informaçoes')
    id = int(input(' digite um id: '))
    nome = input("digite o nome: ")
    email = input("digite o endereco: ")
    import mysql.connector

    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="",
      database="consultas"
    )

    mycursor = mydb.cursor()

    sql = "UPDATE medicos SET nome = %s, email = %s WHERE id = %s"
    val = (nome, email, id)
    mycursor.execute(sql,val)

    mydb.commit()

    print(mycursor.rowcount, "record(s) affected")

# deletar
def apagar():
    print('apagar')
    id = int(input(' digite um id: '))
    import mysql.connector

    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="",
      database="consultas"
    )

    mycursor = mydb.cursor()

    sql = "DELETE FROM medicos WHERE id = %s"
    val = (id,)
    mycursor.execute(sql,val)

    mydb.commit()

    print(mycursor.rowcount, "record(s) deleted")
          
#comando de repetição
# menu de opções	
while True:
    print( 'menu de opções' """
    1) cadastra
    2) lista
    3) alterar
    4) apagar
    5) sair
    """)
    print("Digite uma das opções acima ")
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
        print('sair')
        break

