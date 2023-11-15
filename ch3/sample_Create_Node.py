from llama_index.schema import Document, TextNode

doc = Document(text="This is a sample document text")
n1 = TextNode(text=doc.text[0:16], doc_id=doc.id_) 
n2 = TextNode(text=doc.text[17:30], doc_id=doc.id_)
print(n1)
print(n2)
