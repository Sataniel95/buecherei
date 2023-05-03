import datetime
datenow = datetime.datetime.now()

class Book():
    def __init__(self,title, author ,isbn,num_copies, category, status=False ):
        self.title= title
        self.author = author
        self.isbn = isbn
        self.num_copies = num_copies
        self.category = category
        self.status = status
        self.lenddate = None
        self.retperiod = datetime.timedelta(days = 14)
        self.retdate = self.lenddate + self.retperiod 
        
        
    def get_status(self):
        if self.num_copies>0:
            self.status = False
        else:
            self.status = True 
        return self.status    
    
    
    def lendbook(self):
        
        if self.status != True:
            self.lenddate = datenow
            
        else:
            print("last Book is already lend")
            return
        
        
        