from sentence_transformers import SentenceTransformer
from flask import Flask, request, jsonify, json
import pinecone
import pandas as pd

# DB
products = pd.read_csv('flipkart_com-ecommerce_sample.csv')
products = products[:100]

# 
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

# Set pinecone config
config = json.load(open("pinecone_config.json"))

# Set up Pinecone
pinecone.init(api_key=config['api_key'], environment=config['env'])
pinecone_index = pinecone.Index(config['index_name'])

# Setup the Flask App
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return "Server is working..."

# Search for products
@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('q')

    # Encode the search query into a vector
    query_vector = model.encode(query).tolist()

    # Use Pinecone to search the index for similar documents
    results = pinecone_index.query(query_vector, top_k=5)

    # print('res', results)

    # Return the top 10 most similar documents as JSON
    response = []
    
    for result in results.matches:
        product = products.iloc[[result['id']]]
        print(product)

        response.append({
            'name': product['product_name'].iloc[0],
            'description': product['description'].iloc[0],
            'price': product['retail_price'].iloc[0],
            'image': product['image'].iloc[0],
            'rating': product['product_rating'].iloc[0],
            'brand': product['brand'].iloc[0],
            'score': result.score
        })
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
