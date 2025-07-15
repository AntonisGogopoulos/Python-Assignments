class item:
    def __init__(self,name=' ',price=0):
        self.name=name
        self.price=price

    def set_name(self):
        a=input("ti proion thes:")
        self.name=a
    def set_price(self):
        timh=int(input("dvse thn timh:"))
        self.price=timh
    def display(self):
        print("items(%s,%d)"%(self.name,self.price))
    def returns(self):
        return("%s %d"%(self.name,self.price))



print("ti tha htheles:")
print("1.NA ISAGEIS")
print("2.NA EMFANHSW")
x=int(input("dialekse kapoio apo ta duo:"))
item1=item()
if(x==1):
    item1.set_name()
    item1.set_price()
else:
    item1.display()
    item1.set_price()

line=item1.returns()
print(line)
item=open("item.txt","a")
item.write(line+"\n")
item.close()
