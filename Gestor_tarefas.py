# Gestor de tarefas
# Autor Jr-Marins 

tasks = []

def add_task(task):
    tasks.append({"task": task, "completed": False})
    print('#' * 30)
# Função para add uma nova tarefa à minha lista vazia
    
def view_tasks():
    for index, task in enumerate(tasks, start = 1):
        status = "concluída" if task ["completed"] else "pendente"
        print(f"{index}.{task['task']} - {status}")
        print('#' * 30)
# Função para imprimir minhas tarefas, e quando add's automaticamente são marcadas como pendente.
        
def mark_completed(task_index):
    tasks[task_index]["completed"] = True
    print("Tarefa marcada como concluída")
    print('#' * 30)
# Função para marcar tarefa, usando indice como acesso, como conclída
    
while True:
# MAIN
    print("\n1.Adicionar Tarefas")
    print("2.Visualizar Tarefas")
    print("3.Marcar como concluída")
    print("4.Sair")
    print('#' * 30)
    
    choice = int(input("Escolha uma opção: \n"))
    
    if choice == 1:
        task = input("\nDigite a tarefa: ")
        add_task(task)
# Aqui chamo a função add_task 
       
    
    elif choice == 2:
        view_tasks()
# Aqui a função view, como não contem indice, é só para ler mesmo
        
    
    elif choice == 3:
        view_tasks()
        task_index = int(input("Digite o indice da tarefa concluída: ")) - 1
        mark_completed(task_index)
# na opcão 3 chamo a função para marcar uma task como concluida
        
    elif choice == 4:
        print("\nSaindo ... flw ;)")
        print('#' * 30)
        break
    
    else:
        print("\nOpção inválida")
    