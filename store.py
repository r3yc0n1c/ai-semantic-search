from sentence_transformers import SentenceTransformer
import pandas as pd
import pinecone
import json

# Set up SentenceTransformer
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

# Set pinecone config
config = json.load(open("pinecone_config.json"))

# Set up Pinecone
pinecone.init(api_key=config['api_key'], environment=config['env'])

def vectorize(products):
    # Vectorize the documents

    product_data = []

    for i, product in products.iterrows():
        try:
            product_data += [ product['product_name'] + ' ' + product['description'] ]
        except:
            pass

    product_vectors = model.encode(product_data)
    index_dimension = product_vectors.shape[1]
    return index_dimension, product_vectors

    
def pinecone_store(vector_data):
    # Store vectors in Pinecone
    print("Inserting products in Pinecone...")

    index = pinecone.Index(index_name=config['index_name'])
    ids = list(map(str, range(len(products))))
    product_vector_list = [vec.tolist() for vec in vector_data]
    index.upsert(vectors=zip(ids, product_vector_list))

    print(f"{len(products)} new products inserted.")

def create_pinecone_index(index_dim):
    if config['index_name'] not in pinecone.list_indexes():
        print(f"Creating Pinecone Index with dim = {index_dim}")
        pinecone.create_index(
            config['index_name'],
            dimension=index_dim,
            metric=config['metric']
        )

products = pd.read_csv('flipkart_com-ecommerce_sample.csv', usecols=['product_name','description'])
products = products[:100]


index_dim, product_vecs = vectorize(products)
print(index_dim)
create_pinecone_index(index_dim)

# Store products as vector in pinecone
pinecone_store(product_vecs)
