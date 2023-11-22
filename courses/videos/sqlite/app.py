import db_utils as db

def main():
    # db.add_one('Laura', 'Smith', 'laura@smith.com')
    # db.delete_one('6') # Must be inputted as String
    # db.add_many([
    #     ('Giacche', 'ro', 'giacchero@gmai.com'),
    #     ('Macche', 'rony', 'maccaroni@gmail.com')
    #     ])
    db.email_lookup('mary@gmail.com')
    # db.show_all()
    
    

if __name__ == '__main__':
    main()