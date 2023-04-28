import json

def load_data():
    
    with open('questions.json') as file:
        return json.load(file)
    
def save(data):
    with open('questions.json','w') as file:
        json.dump(data,file)

db=load_data()
