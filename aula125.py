# Mantendo estados dentro de classes
class Camera:
    def __init__(self, nome, filmando=False, fotografando=False):
        self.nome = nome
        self.filmando = filmando
        self.fotografando = fotografando
    
    def filmar(self):
        if self.fotografando:
            print(f'{self.nome} está fotografando e não pode filmar!')
            return
        
        if self.filmando:
            print(f'{self.nome} já está filmando!')
            return


        print(f'{self.nome} está filmando...')
        self.filmando = True
    
    def parar_filmar(self):
        if self.filmando is False:
            print(f'{self.nome} não está filmando no momento!')
            return
        
        print(f'{self.nome} parou de filmar!')
        self.filmando = False
    
    def fotografar(self):
        if self.filmando:
            print(f'{self.nome} está filmando e não pode fotografar!')
            return

        if self.fotografando:
            print(f'{self.nome} já está fotografando!')
            return

        print(f'{self.nome} está fotografando...')
        self.fotografando = True
    
    def parar_fotografar(self):
        if self.fotografando is False:
            print(f'{self.nome} não está fotografando no momento!')
            return
        
        print(f'{self.nome} parou de fotografar!')
        self.fotografando = False

         
c1 = Camera('Canon')
c2 = Camera('Polaroid')

c1.filmar()
c1.filmar()
c1.fotografar()
c1.parar_filmar()
c1.parar_filmar()
c1.fotografar()
c1.fotografar()
c1.filmar()
c1.parar_fotografar()
c1.parar_fotografar()



