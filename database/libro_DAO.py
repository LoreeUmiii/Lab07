from database.DB_connect import DBConnect
from model.libro_DTO import Libro

"""
    LIBRO DAO
    Gestisce le operazioni di accesso al database relative ai libri (Effettua le Query).
"""

class LibroDAO:
    def __init__(self):
        pass

    # TODO
    def get_generi(self):
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
        query = ("""SELECT DISTINCT l.genere
                    FROM libro AS l
                    WHERE l.genere IS NOT NULL
                    ORDER BY l.genere""")

        cursor.execute(query)

        # Popolamento della structure
        for row in cursor:
            result.append(row["genere"])

        # Closing...
        cursor.close()
        cnx.close()

        return result

    """row["id"], row["titolo"], row["autore"],
    row["genere"], row["anno_pubblicazione"], row["id_biblioteca"]"""

    def get_libri_filtrati(self, biblioteca, genere):
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
        query = """ select *
                    from biblioteca as b, libro as l
                    where b.id = l.id_biblioteca and
                    l.genere = coalesce(%s, genere) 
                    and b.id = (%s, biblioteca) """

        cursor.execute(query, (genere, biblioteca) )

        for row in cursor:
            result.append(row)

        cursor.close()
        cnx.close()

        return result
