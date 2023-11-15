from llama_index.schema import Document
from llama_index.node_parser import SentenceWindowNodeParser

doc = Document(text="Lionel Messi is a football player from Argentina. He has won the Ballon d'Or trophy 7 times.")
parser = SentenceWindowNodeParser.from_defaults()
nodes = parser.get_nodes_from_documents([doc])
print(nodes[0])
print(nodes[1])
