from database.DB_connect import DBConnect
from model.biblioteca_DTO import Biblioteca

"""
    Biblioteca DAO
    Gestisce le operazioni di accesso al database relative alle biblioteche (Effettua le Query).
"""

class BibliotecaDAO:
    def __init__(self):
        pass

    # TODO
    def get_biblioteche(self):
        # Structure
        result = []

        # Connessione DB
        cnx = DBConnect.get_connection()

        # Controls
        if cnx is not None:
            print("Connection established ")
        else:
            print("Connection non established")
            return result

        cursor = cnx.cursor(dictionary=True)
        query = ("""SELECT * 
                 FROM biblioteca AS b 
                 ORDER BY b.id, b.nome""")
        cursor.execute(query)

        # Popolamento della structure
        for row in cursor:
            biblioteca = Biblioteca(*row)
            result.append(biblioteca)

        # Closing...
        cursor.close()
        cnx.close()

        return result

    """row["id"], row["nome"], row["indirizzo"]"""
