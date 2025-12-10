from model.model import Model

mod = Model()
mod.build_weighted_graph(2000)
print(len(mod.build_weighted_graph(2000).edges()))
print(mod.count_edges_by_threshold(4))
print(mod.cammino_minimo_dfs(4))