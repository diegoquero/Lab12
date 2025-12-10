from database.DB_connect import DBConnect
from model.connessione import Connessione
from model.rifugio import Rifugio


class DAO:
    """
    Implementare tutte le funzioni necessarie a interrogare il database.
    """

    @staticmethod
    def ReadRifugi():
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM rifugio")
        result = {}
        for row in cursor:
            rifugio = Rifugio(**row)
            result[rifugio.id] = rifugio
        conn.close()
        cursor.close()
        return result

    @staticmethod
    def ReadConnessioni():
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM connessione")
        result = []
        for row in cursor:
            connessione = Connessione(**row)
            result.append(connessione)
        conn.close()
        cursor.close()
        return result
