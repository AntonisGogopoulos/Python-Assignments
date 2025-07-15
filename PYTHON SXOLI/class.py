class animal:
    def __init__(self,name='animal',where='sea',photo='url'):
        self.name=name
        self.where=where
        self.photo=photo

    def displayhero(self):
        print ("onoma",self.name,"to where",self.where,"to photo",self.photo)




onoma=animal('tiger','jungle')
onoma2=animal()
onoma.displayhero()
onoma2.displayhero()




