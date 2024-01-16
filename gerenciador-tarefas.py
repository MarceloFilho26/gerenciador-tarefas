class GerenciadorTarefas:
    def __init__(self):
        self.tarefas = []

    def adicionarTarefa(self, tarefa):
        self.tarefas.append(tarefa)
        print(f"A tarefa {tarefa} foi adicionado com sucesso.")

    def removerTarefa(self, tarefa):
        if tarefa not in self.tarefas:
            print(f"Tarefa {tarefa} não encontrada.")
        else:
            self.tarefas.remove(tarefa)
            print(f"Tarefa {tarefa} removida com sucesso.")

    def visualizarTarefa(self):
        c = 1
        if self.tarefas:
            print("tarefas encontradas: ")
            for x in self.tarefas:
                print(f"{c} - {x}")
                c += 1


def main():
    gerenciador = GerenciadorTarefas()

    while True:
        print("====Lista de tarefas===="
              "\n[1] - Adicionar tarefa"
              "\n[2] - Remover tarefa"
              "\n[3] - Visualizar tarefa"
              "\n[4] - Sair")
        option = input("Escolha uma opção: ")

        if option == "1":
            tarefa = input("Digite a tarefa a ser adicionada: ")
            gerenciador.adicionarTarefa(tarefa)

        elif option == "2":
            tarefa = input("Digite a tarefa a ser removida: ")
            gerenciador.removerTarefa(tarefa)

        elif option == "3":
            gerenciador.visualizarTarefa()

        elif option == "4":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida, tente novamente.")


if __name__ == "__main__":
    main()
