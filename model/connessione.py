from dataclasses import dataclass
from datetime import datetime


@dataclass
class Connessione:
    id : int
    id_rifugio1 : int
    id_rifugio2 : int
    distanza : float
    difficolta : str
    durata : datetime
    anno : int

    def __hash__(self):
        return hash(self.id)