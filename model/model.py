import networkx as nx

from database.dao import DAO


class Model:
    def __init__(self):
        """Definire le strutture dati utili"""
        self.G = nx.Graph()
        self.difficolta = { 'facile': 1 ,
                            'media' : 1.5 ,
                            'difficile' : 2 ,
                          }
        self.distanza_cammino_minimo = 10000
        self.cammino_minimo = None

    def build_weighted_graph(self, year: int):
        """
        Costruisce il grafo pesato dei rifugi considerando solo le connessioni con campo `anno` <= year passato
        come argomento.
        Il peso del grafo è dato dal prodotto "distanza * fattore_difficolta"
        """
        lista_connessioni = DAO.ReadConnessioni()
        lista_rifugi = DAO.ReadRifugi()
        for connessione in lista_connessioni:
            if connessione.anno <= year:
                self.G.add_edge(lista_rifugi[connessione.id_rifugio1], lista_rifugi[connessione.id_rifugio2],
                                peso=float(connessione.distanza)*self.difficolta[connessione.difficolta])
        return self.G


    def get_edges_weight_min_max(self):
        """
        Restituisce min e max peso degli archi nel grafo
        :return: il peso minimo degli archi nel grafo
        :return: il peso massimo degli archi nel grafo
        """
        peso_max = 0
        peso_min = 1000
        for _,_,peso in self.G.edges(data=True):
            if peso['peso'] >= peso_max:
                peso_max = peso['peso']
            if peso['peso'] <= peso_min:
                peso_min = peso['peso']
        return peso_min, peso_max


    def count_edges_by_threshold(self, soglia):
        """
        Conta il numero di archi con peso < soglia e > soglia
        :param soglia: soglia da considerare nel conteggio degli archi
        :return minori: archi con peso < soglia
        :return maggiori: archi con peso > soglia
        """
        counter_minori = 0
        counter_maggiori = 0
        for _,_,peso in self.G.edges(data=True):
            if peso['peso'] < soglia:
                counter_minori += 1
            if peso['peso'] > soglia:
                counter_maggiori += 1
        return counter_minori,counter_maggiori

    """Implementare la parte di ricerca del cammino minimo"""
    def cammino_minimo_dfs(self, soglia):
            grafo_filtrato = nx.Graph()
            cammino_migliore = []
            distanza_cammino_migliore = float('inf')
            for u, v, data in self.G.edges(data=True):
                if data['peso'] > soglia:
                    grafo_filtrato.add_edge(u, v, peso =data['peso'])


            for nodo in grafo_filtrato:
                try:
                    distanze, percorsi = nx.single_source_dijkstra(grafo_filtrato,
                                                                   source=nodo,
                                                                   cutoff=self.distanza_cammino_minimo,
                                                                   weight= 'peso')

                    for destinazione,cammino in percorsi.items():
                        if (nodo != destinazione and len(cammino) >= 3 and distanze[destinazione] < distanza_cammino_migliore):
                            cammino_migliore = cammino.copy()
                            distanza_cammino_migliore = distanze[destinazione]
                except nx.NetworkXNoPath:
                    continue
            return cammino_migliore
            print(self.cammino_minimo)
            print(self.distanza_cammino_minimo)











