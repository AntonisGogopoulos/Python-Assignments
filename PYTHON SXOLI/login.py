class player:
    def __init__(self,name="user",password=1234,email="user@user.user"):
        self.name=name
        self.password=password
        self.email=email
    def desplay(self):
        return("%s %s" %(self.name,self.email))
    def newplayer(self):
        onoma=input("dwse to onoma sou:")
        self.name=onoma
        code=int(input("dwse ton kodiko sou:"))
        self.password=code
        mail=input("dwse to email sou:")
        self.email=mail
    def update(self):
        onoma=input("dwse to onoma sou:")
        self.name=onoma
        mail=input("dwse to email sou:")
        self.email=mail
    
        


player1=player()
player1.newplayer()
players=open("players.txt","w",encoding="utf-8")


        
        
