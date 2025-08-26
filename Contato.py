class Contato:
    def __init__(self,nome,endereco,idade,numero_de_tel,email):
        self.nome=nome
        self.endereco=endereco
        self.idade=idade
        self.numero_de_tel=numero_de_tel
        self.email=email

    def to_dict(self):
        return {
            'nome':self.nome,
            'endereço':self.endereco,
            'idade':self.idade,
            'numero de telefone':self.numero_de_tel,
            'email':self.email
            }


    def __repr__(self):
        return f"Contato(nome={self.nome},endereço={self.endereco},idade={self.idade},numero de telefone={self.numero_de_tel},email={self.email}"


