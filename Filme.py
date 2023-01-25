class Filme:
    def __init__(self): #contrutor da classe filme
        self.id = None
        self.nome = None
        self.duracao = None
        self.genero = None

#region gets n sets
    
    # Id do filme  
    def setId(self, idFilme):
        self.id = idFilme
        
    def getId(self):
        return self.idFilme
    
    # Nome do filme
    def setNome(self, nomeFilme):
        self.nome = nomeFilme
        
    def getNome(self):
        return self.nome
    
    # Duração do filme
    def setDuracao(self, duracaoFilme):
        self.duracao = duracaoFilme
        
    def getDuracao(self):
        return self.duracao
    
    # Gênero do filme
    def setGenero(self, generoFilme):
        self.duracao = generoFilme
        
    def getDuracao(self):
        return self.genero
#endregion
