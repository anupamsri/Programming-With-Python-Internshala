class book:
    """ BOOk detaails."""
    def __init__(self,a='Concept of physics',b='R.K Bansal',c='S>L Arorah',d=500,q=600 ):
        self.title=a
        self.author=b
        self.publisher=c
        self.price=d
        self.quan=q
        royal=0
    def get_title(self):
        return self._title
    def set_title(self,a):
        self.title=a
        return
    def get_author(self):
        return self.author
    def set_author(self,b):
        self.author=b
        return
    def get_publisher(self):
        return self.publisher()
    def set_publisher(self,c):
        self.publisher=c
        return
    def get_price(self):
        return self.price
    def set_price(self,d):
        self.price=d
        return
    def get_quan(self):
        return self.quan
    def set_quan(self,e):
        self.quan=e
        return
    def royalty(self):
        if self.quan<=500:
            royal=.1*self.price*self.quan
        elif self.quan>500 and self.quan<=1500:
            royal=.125*self.price*(self.quan-500)+.1*self.price*500
        elif self.quan>1500:
            royal=.1*self.price*500+.125*self.price*1000+.15*self.price*(self.quan-1500)
        return royal

class ebook(book):
    """E-BOOK Detais"""
    def __init(self,aa='PDF'):
        self._fromat=aa
    def get_format(self):
        return self.format
    def set_format(self,b):
        self.format=b
        return
    def royalty(self):
        if self.quan<=500:
            royal=.1*self.price*self.quan
        elif self.quan>500 and self.quan<=1500:
            royal=.125*self.price*(self.quan-500)+.1*self.price*500
        elif self.quan>1000:
            royal=.1*self.price*500+.125*self.price*1000+.15*self.price*(self.quan-1500)
        royal=royal-(.12*royal)
        return royal
a=input(" Enter the title of the book ")
b=input(" Enter the author ofthe book ")
c=input(" Enter the publisher of book ")
d=int(input(" Enter the price of the book "))
e=int(input(" Enter the total number of books sold "))
f=int(input(" Enter 1 for normal book and enter 2 for e book "))
x=book()
x.set_title(a)
x.set_author(b)
x.set_publisher(c)
x.set_price(d)
x.set_quan(e)
y=ebook()
if f==1:
    z=x.royalty()
    print(" Title is {} \n Publisher is {} \n Author is {} \n Price was {} \n Total sold {} \n Royalty is {} \n".format(x.title,x.publisher,x.author,x.price,x.quan,z))

if f==2:
    print("b")
    g=input("Enter the format of ebook")
    z=y.royalty()
    y.set_format(g)
    print(" Title is {} \n Publisher is {} \n Author is {} \n Price was {} \n Total sold {} \n Format is {} \n Royalty is {} \n".format(y.title,y.publisher,y.author,y.price,y.quan,y.format,z))
