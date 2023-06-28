from node import Node

class LinkedList:
    """
        ->   ### Lista Encadeadas:
    """

    def __init__(self):
        self.head = None  # Atributo cabeça que vai ser a cabeça do nó, repesentar o proxima referencia
        self._size = 0  # Atributo não é necessario por que se precisassemos desta informação poderiamos contar os nós

    """
    -> Metodo pra adicionar um elemento no final da lista
    :param elem: recebe o valor para ser adicionado al fim da lista 
    """
    def append(self, elem):
        if self.head:  # Se existe algum na cabeça referenciando outro nó
            pointer = self.head  # Com uma variavel auxiliar ponteiro vamos percorrer os nós
            while(pointer.next):  #Enquanto o ponteiro tiver um proximo
                pointer = pointer.next  # Atribui este proximo ao ponteiro ate o momento que o pointer for "None"
            #  Agora o ponteiro tem o valor do ultimo elemento e vamos atribuir a referencia que ele guarda do proxino nó como o valor do elemento criado
            pointer.next = Node(elem)
        else:  # Senao houver uma referencia entao este e o primeiro elemento
            self.head = Node(elem)  # primeira inserção
        self._size += 1  # Incrementando o tamanho da lista

    #Retorna o tamanho da lista
    def __len__(self):
        return self._size

    # def get(self, index):
        # a = lista.get(0)

    # def set(self, index, elem):
        # a = lista.set(0, 6)

    def _getnode(self, index):
        pointer = self.head  #A variavel auxiliar recebe o valor da cabeça
        for i in range(index):  # como conhecemos o numero de vez que precisaremos percorrer vamos utilizar o for
            if pointer:  # vamos verificar se o pointer nao for None entao a lista nao esta vazia
                pointer = pointer.next
            else:  # se ele for None vamos disparar uma exception IndexError
                raise IndexError("list index out of range")
        return pointer

    #Recuperar um elemento da lista
    def __getitem__(self, index):  # sobrecarga de operadores para utilizarmos os cochetes [] na operação
        # a = lista[0]
        pointer = self._getnode(index)

        if pointer: # se o pointer em que o for terminou nao for vazio
            return pointer.data  # vai ser retornado o dado
        raise IndexError("list index out of range")

    #Alterar algum elemento
    def __setitem__(self, index, elem):
        # lista[0] = 20
        pointer = self._getnode(index)

        if pointer:
            pointer.data = elem
        else:
            raise IndexError("list index out of range")


    #Busca pelo elemento e retorna o index se for encontrado
    def index(self, elem):
        pointer = self.head
        i = 0
        while(pointer):  #Vamos percorrer a lista procurando o elemento enquanto o nó não estiver vazio
            if pointer.data == elem:
                return i
            pointer = pointer.next
            i += 1
        raise ValueError(f'{elem} is not in list')


    def insert(self, index, elem):
        node = Node(elem)  #Criamos um nó
        if index == 0:  #Se a inserção for no inicio da lista
            node.next = self.head  #A cabeça do no passa para o valor da ref erencia do proximo
            self.head = node  #E a cabeça recebe o nó criado
        else:
            pointer = self._getnode(index-1)  #Vamos receber o valor do index do antecessos que nos queremos alterar
            node.next = pointer.next
            pointer.next = node
        self._size += 1

