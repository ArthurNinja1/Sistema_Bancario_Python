class Pessoa:
    def __init__(self, nome, cpf, telefone, email):

        self._verificar_vazio(nome, "nome")
        self._verificar_vazio(cpf, "cpf")
        self._verificar_vazio(telefone, "telefone")
        self._verificar_vazio(email, "email")

        self.nome = nome.strip().title()
        self.cpf =  cpf.strip()
        self.telefone = telefone.strip()
        self.email = email.strip()
    

    def _verificar_vazio(self, valor, campo):
        if not valor.strip():
            raise ValueError(f"O campo {campo} não pode ser vazio")
    
    
    #melhorar depois validação do cpf
    def validar_cpf(self):
        return (len(self.cpf) == 11 and self.cpf.isdigit())

    def alterar_telefone(self, novoTelefone):
        self._verificar_vazio(novoTelefone, "telefone")
        self.telefone = novoTelefone.strip()

    def alterar_email(self, novoEmail):
        self._verificar_vazio(novoEmail, "email")
        self.email = novoEmail.strip()

    def __str__(self):
        return f"Nome {self.nome} | CPF: {self.cpf} | telefone: {self.telefone} | email: {self.email}"






if __name__ == "__main__":

    p = Pessoa("  joão da silva ", "12345678901", "66988884444", "joao@email.com")
    print(p)

    p.alterar_telefone("  66999990000 ")
    print(p)

    try:
        p.alterar_email("   ")
    except ValueError as erro:
        print("Erro:", erro)

    print(p)