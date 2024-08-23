import json
import os
from langchain_ollama import OllamaLLM
from langchain import ConversationChain
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_core.prompts import PromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage
import import_ipynb



def invoke_demiurge():
    
    data_path = 'jsons/parameters_export.json'
    with open(data_path, 'r') as file:
        sim_data = json.load(file)

    model = OllamaLLM(model='llama3.1', keep_alive='1h')

    intro = f'Instructions: {sim_data['Explanation']} Population data over time: {sim_data['population_data_over_time']}'
    prompt = f'''These are the current parameters which you must adjust: {sim_data['params']}

    Your answer must always be provided in the following format, with no additional text. No exceptions, ever. None of your answers should exceed a value of 15:
    Grass: (Your answer), Rabbits: (Your answer), Wolves: (Your answer)'''


    messages = [
        SystemMessage(content=intro),
        HumanMessage(content=prompt)
    ]

    response = model.invoke(messages)
    print('Parameters updated:', response)
    cleaned_response = response.replace("'", "").strip()
    response_pairs = cleaned_response.split(',')
    response_dict = {}

    for pair in response_pairs:
        if ':' in pair:
            key, value = pair.split(':', 1)
            key = key.strip()
            if key == 'Evaluation':
                response_dict[key] = str(value.strip())
            else:
                try:
                    response_dict[key] = float(value.strip())
                except ValueError:
                    print(f"Skipping invalid value for key {key}: {value.strip()}")
        else:
            print(f"Skipping invalid pair: {pair}")

    return response_dict


