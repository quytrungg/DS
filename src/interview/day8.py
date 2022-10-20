def find_cycle(graph):
  
  return

graph = {
  'a': {'a2':{}, 'a3':{} },
  'b': {'b2':{}},
  'c': {}
}
# print(find_cycle(graph))
# False
graph['c'] = graph

for i in graph:
    print(i)
    print(graph[i])
# print(find_cycle(graph))
# True