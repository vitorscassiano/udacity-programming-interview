class HashTable(object):
    def __init__(self):
        self.table = [None]*10000

    def store(self, string):
        """Submeta uma string que esteja armazenada na tabela."""
        index = self.calculate_hash_value(string)
        self.table[index] = string

    def lookup(self, string):
        """
        Retorne o valor hash caso a string já esteja na tabela.
        Caso contrário, retorne -1.
        """
        hv = self.calculate_hash_value(string)
        return self.table[hv] if self.table[hv] else -1

    def calculate_hash_value(self, string):
        """Função auxiliar para calcular um valor hash de uma string."""
        address = (ord(string[0]) * 100) + ord(string[1])
        return address


if __name__ == "__main__":
    hash_table = HashTable()
    print(hash_table.calculate_hash_value("UDACITY"))
    print(hash_table.lookup("UDACITY"))
    hash_table.store("UDACITY")

    print(hash_table.lookup("UDACITY"))
    hash_table.store("UDACIOUS")
    print(hash_table.lookup("UDACIOUS"))
