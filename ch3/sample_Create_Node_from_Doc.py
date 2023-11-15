from llama_index.schema import Document
from llama_index.node_parser import SimpleNodeParser

doc = Document(text="This is a sample document text")
parser = SimpleNodeParser.from_defaults()
nodes = parser.get_nodes_from_documents([doc])
print (nodes)
