import datetime as dt

            # CLASSE TAREFA ---------------------------------------------------- 
class Tarefa:
                    def __init__(self, nome, descricao, prazo, prioridade, status, id):
                        self.id = id #Gerar um ID único para cada tarefa
                        self.nome = nome
                        self.descricao = descricao
                        self.prazo = prazo
                        self.prioridade = prioridade
                        self.status = status
                        self.concluida = status ==  "Concluída" or False
                    def mostrar_tarefa(self):
                        return (f"ID de Tarefa: {self.id}\n Nome: {self.nome}\n Descrição: {self.descricao}\n Data e hora Limite: {self.prazo}\n Prioridade {self.prioridade}\n Estado da tarefa: *{self.status}\n")
                    def fechar_tarefa(self):
                        if not self.concluida:
                            self.status = 'Concluída'



listaTarefas = []
            
           #LISTA VAZIA BOOL ---------------------------------------------------- 

def listaIsVazia(lista):
  if(len(lista) == 0):
    return True
  else:
       return False

           #LISTA VAZIA RESULT ---------------------------------------------------- 
  
def listaVazia():
  print ("\nA lista de tarefas esta vazia\n")

            #NUM 1 ADICIONAR UMA NOVA TAREFA ----------------------------------------------
  
def adTarefa(dadosTarefa):
   print("\nTarefa adicionada com sucesso!\n")
   return Tarefa (dadosTarefa[0],dadosTarefa[1],dadosTarefa[2],dadosTarefa[3], dadosTarefa[4], dadosTarefa[5])
  
            #NUM 2 LISTAR AS TAREFAS PENDENTES ---------------------------------------------------- 

def tarefasPendentes(listaTarefas):
       listaPendentes = []
       
       if listaIsVazia(listaTarefas):
        print("\nNão há nenhuma tarefa Pendente.\n")
       else:
                for tarefa in listaTarefas:
                    if(tarefa.status=="Pendente"):
                        listaPendentes.append(tarefa)
            
                if(listaIsVazia(listaPendentes) == True):
                    print("\nNão há nenhuma tarefa Pendente.\n")
                
                else:
                    counter = 1
                    for tarefa in listaPendentes:
                     print(f"\n{counter} - Tarefa Pendente: \n {tarefa.mostrar_tarefa()}")
                     counter += 1
                   
                print(f"\nVocê tem {len(listaPendentes)} tarefas pendentes\n")
                    
                return listaPendentes

        #NUM 3 LISTAR AS TAREFAS CONCLUIDAS ---------------------------------------------------- 

def tarefasConcluidas(listaTarefas):
     listaConcluidas = []
     
     if listaIsVazia(listaTarefas):
      print("\nNão há nenhuma tarefa Concluída.\n")
      return
     else:
        for tarefa in listaTarefas:
        
            if(tarefa.status=="Concluída"):
             listaConcluidas.append(tarefa)
            
        if(listaIsVazia(listaConcluidas) == True):
                  print("\nNão há nenhuma tarefa Concluída.\n")
        
        else:
                counter = 1
                for tarefa in listaConcluidas:
                    print(f"\n{counter} - Tarefa Concluida: \n {tarefa.mostrar_tarefa()}")
                    counter = counter + 1
                print(f"\nVocê tem {counter-1} tarefas concluidas\n")
                
     return listaConcluidas

        #NUM 4 LISTAR TODAS AS TAREFAS ---------------------------------------------------- 

def listarTodasAsTarefas(listaTarefas):
     
     if listaIsVazia(listaTarefas):
                listaVazia()
     else:
        count = 1
        for tarefa in listaTarefas:
           print(f"\n{count} - Tarefa: \n {tarefa.mostrar_tarefa()}")
           count = count + 1
        print(f"\nVocê tem {count-1} tarefas na agenda\n")

        #NUM 5 MARCAR CONCLUIDA   ------------------------------------------------------------- 
                
def marcarConcluida(id, listaTarefas):
   if (listaIsVazia(listaTarefas) == False):
       
            for i in range(len(listaTarefas)):
                
                if id not in [tarefa.id for tarefa in listaTarefas]:
                    print(f"\nA tarefa com o ID {id} não está na lista de tarefas.\n")
                    return  
                
                if (listaTarefas[i-1].id == id) and (listaTarefas[i-1].status != 'Concluída') :
                    listaTarefas[id-1].fechar_tarefa()
                    print('\nA tarefa foi marcada como Concluída!')
                               
                elif (listaTarefas[i-1].id != id)  and ((len(listaTarefas)-1) == i) and  (id > (len(listaTarefas)+1)):
                        print("\nNão foi possível marcar a Tarefa como Concluida, pois não existe nenhuma Tarefa com esse ID.\n")
           
                elif (listaTarefas[i-1].id == id) and (listaTarefas[i-1].status == 'Concluída'):
                        print('\nEsta tarefa já  está marcada como Concluída!')              

   elif  (listaIsVazia(listaTarefas)):
           listaVazia()
  
   else:
      print("\nNão existe nenhuma Tarefa com esse ID.\n")

        #NUM 6 APAGAR DA LISTA----------------------------------------------------------------------
      
def apagarTarefa(id, listaTarefas):
      
      if (listaIsVazia(listaTarefas) == False) :

                for i in range(len(listaTarefas)):
                    if (listaTarefas[i-1].id == id):
                        del(listaTarefas[i-1])
                        print("\nTarefa Eliminada com sucesso!\n")
                        break
      
                    elif (listaTarefas[i-1].id != id)  and ((len(listaTarefas)-1) == i) and  (id > (len(listaTarefas)+1)):
                        print("Não foi possível eliminar a Tarefa, pois não existe nenhuma Tarefa com esse ID.\n")
                    
                    elif ((listaTarefas[i-1].id == id) is not True) and ((len(listaTarefas)-1) == i):
                         print("A tarefa com esse ID não existe atualmente na lista de tarefas")  

      elif(listaIsVazia(listaTarefas)):
                    listaVazia()
                 
      else:
                print("\nDigite uma opção valida\n")
    
 #Criando tarefas e adicionando-as a lista de tarefas--------------------------------------------------
def listaMain():
    
    listaDados =[]

    while(True):
      print("Operações:\n")
      print(" 1 - Adicionar Tarefa.\n 2 - Listar Tarefas Pendentes \n 3 - Listar Tarefas Concluídas\n 4 - Listar Todas as Tarefas.\n 5 - Marcar Tarefa como Concluída.\n 6 - Remover Tarefa. \n 0 - Encerrar programa")
      op = input("\nDigite a operação desejada: ")

      if(op == "0"):
            break

#Adicionar tarefa na lista
      if(op =="1"): 
           print ("\nAdicione aqui as informações da tarefa:\n")
           nome = input("Nome:")
           descricao = input("Descrição:")
           data_limite = input("Data Limite (DD/MM/AAAA HH:MM):")

            #Controle de entrada de data e houra 
           while(dt.datetime.now() > dt.datetime.strptime(data_limite,"%d/%m/%Y %H:%M")):
              print("A Data limite deve ser maior que a data atual.")
              data_limite = input("Data Limite (DD/MM/AAAA HH:MM): ")

              if (dt.datetime.now() < dt.datetime.strptime(data_limite,"%d/%m/%Y %H:%M")):
                     break

           prioridade = int(input("Prioridade (1-3) -  1 é alta, 2 é média e 3 é baixa:"))
           status = "Pendente"
           idTarefa = len(listaTarefas)+1

           if (listaIsVazia(listaTarefas) ==False):
              for t in listaTarefas:
                    if (t.id ==  idTarefa):
                          idTarefa +=1
         
           
           listaDados.clear()

           listaDados.append(nome)
           listaDados.append(descricao)
           listaDados.append(data_limite)
           listaDados.append(prioridade)
           listaDados.append(status)  
           listaDados.append(idTarefa)

           listaTarefas.append(adTarefa(listaDados))

      elif(op == "2"):            #Mostrar tarefas Pendentes
         tarefasPendentes(listaTarefas)

      elif(op == "3"):            #Mostrar tarefas Concluidas
            tarefasConcluidas(listaTarefas)
    
      elif(op == "4"):                #Listar todas as tarefas
           listarTodasAsTarefas(listaTarefas)

      elif(op =="5"):                  #Marcar como feita
            id = int(input("\nInforme o ID da tarefa para marcar como concluída: "))
            marcarConcluida(id, listaTarefas)
          
      elif(op =="6"):                  #Eliminar Tarefa
            id = int(input("\nInforme o ID da tarefa a Eliminar: "))
            apagarTarefa(id, listaTarefas)
      else:
       print ("\nOpção Inválida! \n")
       
listaMain()