from llama_hub.wikipedia.base import WikipediaReader

loader = WikipediaReader()
documents = loader.load_data(
pages=[
'Pythagorean theorem', 
'General relativity'
]
)
