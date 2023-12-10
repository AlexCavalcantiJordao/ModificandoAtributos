class Conta:
    def __int__(self, titular, numero, saque, deposita, extrato):
        self.saldo = 0.0
        self.numero = numero
        self.titular = titular

        @property
        def saldo(self):
            return self._saldo

        @saldo.setter
        def saldo(self, saldo):
            if(saldo < 0):
                print("O saldo não pode ser negativo.")
            else:
                self._saldo = saldo

        def saque(self, valor):
            if(self.saldo >= valor):
                self.saldo -= valor
                print("Saque realizado com sucesso.")
            else:
                print("saldo insuficiente.")

        def deposita(self, valor):
            self.saldo += valor

        def extrato(self):
            print("Cliente", self._titular, " Saldo atual: ", self._saldo)