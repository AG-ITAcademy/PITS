from llama_index.schema import Document  
from llama_index.text_splitter import TokenTextSplitter 

doc = Document( 
    text="This is sentence 1. This is sentence 2. Sentence 3 here." 
)  

splitter = TokenTextSplitter( 
    chunk_size=11, 
    chunk_overlap=5, 
    separator=" " 
) 

nodes = splitter.get_nodes_from_documents([doc]) 
for node in nodes: 
    print(node.text+"\n"+node.metadata) 