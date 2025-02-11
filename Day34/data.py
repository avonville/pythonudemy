import requests
import html

params = {
    "amount": 10,
    "type": "boolean",
}

trivia_response = requests.get(url="https://opentdb.com/api.php", params=params) 
trivia_response.raise_for_status()

question_data_raw = trivia_response.json()["results"]
question_data = [
    {**q, 'question': html.unescape(q['question'])} for q in question_data_raw
]
