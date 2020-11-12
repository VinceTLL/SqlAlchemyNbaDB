
class Schema:


    def __init__(self,base,engine,session):
        self.Base = base
        self.engine = engine
        self.session = session

    def create_tables(self):
        self.Base.metadata.create_all(self.engine)


    def add_rows(self,row_data = None):
        try:
            for row in row_data:
                self.session.add_all(row)
        except:
            return "no data provided"


    def commit_rows(self):
        self.session.commit()


    def rollback_rows(self):
        self.session.rollback()



'''
try:
    Teams.__table__.create(engine) # create single table
except Exception as x:
    val = x
if re.search('already exists',str(val)):
    print("table exists")
else :
    print('other')'''
