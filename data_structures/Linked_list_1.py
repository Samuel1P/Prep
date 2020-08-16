class node:
    __slots__ = 'element', 'reference'
    def __init__(self, data, ref):
        self.element = data
        self.reference = ref

    def __repr__(self):
        return f"node('{self.element}', {self.reference})"

    def node_contents(self):
        print(f" data :{self.element} -- ref: {self.reference.__repr__()}")

node1 = node('data1', None)
node2 = node('data2', None)
node3 = node('data3', None)
node1.reference = node2
node2.reference = node3
node1.node_contents()
node2.node_contents()
node3.node_contents()