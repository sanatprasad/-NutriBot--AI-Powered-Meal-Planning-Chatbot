import json
import boto3

boto3_bedrock = boto3.client(service_name='bedrock-runtime')

def extract_slots(interpretations):
    slots = {}
    for interpretation in interpretations:
        current_intent = interpretation.get('intent', {})
        current_slots = current_intent.get('slots', {})
        slots.update(current_slots)
    return slots

def lambda_handler(event, context):
    
    # Extract relevant information from the Lex input event
    user_input = event['inputTranscript']
    intent = event['interpretations'][0]['intent']['name']
    
    # Extract information from all slots
    all_slots = extract_slots(event['interpretations'])
    # Print the entire slots dictionary for debugging
    print("All Slots:", all_slots)
    
    # Extract values for each slot into separate variables
    height = all_slots.get('Height', {}).get('value', {}).get('interpretedValue', None)
    gender = all_slots.get('Gender', {}).get('value', {}).get('interpretedValue', None)
    diettype = all_slots.get('DietType', {}).get('value', {}).get('interpretedValue', None)
    extras = all_slots.get('ExtraIngrediant', {}).get('value', {}).get('interpretedValue', None)
    weight = all_slots.get('Weight', {}).get('value', {}).get('interpretedValue', None)
    
    
    # abc = height + " " + weight + " " + gender + " " + diettype + " " + extras
    # print(abc)
    # print("boto3 version:"+boto3.__version__)
    ask=""
    if gender=="no":
        ask="Provide me a "+diettype+" meal plan for a human weighing "+weight+", measuring "+height+" and also add "+extras+" as ingrediant in 7 day meal plan"
    else:
        ask="Provide me a "+diettype+" meal plan for a "+gender+" weighing "+weight+", measuring "+height+" and also add "+extras+" as ingrediant in 7 day meal plan"
    print(ask)
    
    body = json.dumps({"prompt": "Human:"+ask+"\nAssistant:", "max_tokens_to_sample":512})
    modelId='anthropic.claude-instant-v1'
    accept = 'application/json'
    contentType = 'application/json'
    
    #invoke model
    response = boto3_bedrock.invoke_model(body=body, modelId=modelId, accept=accept, contentType=contentType)
    response_body = json.loads(response.get('body').read())
    print(response_body)
    resp=response_body.get('completion')
    print(resp)

    slots = event['sessionState']['intent']['slots']
    intents = event['sessionState']['intent']['name']
    response = {
        "sessionState": {
            "dialogAction": {
                "type": "Close"
            },
            "intent": {
                'name':intents,
                'slots': slots,
                'state':'Fulfilled'
                
                }
    
        },
        "messages": [
            {
                "contentType": "PlainText",
                "content": resp
            }
        ]
    }
    return response