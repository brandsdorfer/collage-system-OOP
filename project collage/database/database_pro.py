import sqlite3

collagemainDB = sqlite3.connect("collage-DB")
curdor = collagemainDB.cursor()

def create_table(instance):

    curdor.execute(f"""
    CREATE TABLE IF IS NOT ACSEST {instance["obj"].name} (
        {instance["PRIMERY"]} PRIMA RY KEY,
        {instance["textforsql"]}
    )
    """)
    collagemainDB.commit()
    collagemainDB.close()

def insart_student(object):
    curdor.execute(f"""
        INSERT INTO Person VALUES
        ({object.name}, {object.id}, {object.age}, {object.phone_nom}, {object.list_of_courses})
)
""")
    collagemainDB.commit()
    collagemainDB.close()
    
def insart_course(object):
    curdor.execute(f"""
    INSERT INTO {object.name} VALUES
        ({object.name}, {object.id}, {object.age}, {object.phone_nom}, {object.list_of_courses})
""")


    collagemainDB.commit()
    collagemainDB.close()