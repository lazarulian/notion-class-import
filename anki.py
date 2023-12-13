import json
import urllib.request

def request(action, **params):
    return {'action': action, 'params': params, 'version': 6}

def invoke(action, **params):
    requestJson = json.dumps(request(action, **params)).encode('utf-8')
    response = json.load(urllib.request.urlopen(urllib.request.Request('http://127.0.0.1:8765', requestJson)))
    if len(response) != 2:
        raise Exception('response has an unexpected number of fields')
    if 'error' not in response:
        raise Exception('response is missing required error field')
    if 'result' not in response:
        raise Exception('response is missing required result field')
    if response['error'] is not None:
        raise Exception(response['error'])
    return response['result']

# Load Flashcards
with open('flashcards.json', 'r') as file:
        flashcards = json.load(file)
        num_flashcards = 0

        for flashcard in flashcards:
            front_content = flashcard['front']
            back_content = flashcard['back']
            
            # Create Flashcards
            num_flashcards += 1
            result = invoke(action='addNote', note={"deckName": "Psych 120A", "modelName": "Basic", "fields": {"Front": front_content, "Back": back_content}})
            print('✅ Successfully Created Card {}: {}'.format(num_flashcards, result))
        
        print('\n ✅ Created {} flashcards.'.format(len(flashcards)))