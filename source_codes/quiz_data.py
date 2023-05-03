import json

a = open("data_final.json","r")
question_data = json.load(a)



"""
Sample Response

[
    {
        'category': 'Sports', 
        'type': 'multiple', 
        'difficulty': 'medium', 
        'question': 'Which Formula One driver was nicknamed &#039;The Professor&#039;?',
        'correct_answer': 'Alain Prost', 
        'incorrect_answers': [
            'Ayrton Senna', 
            'Niki Lauda', 
            'Emerson Fittipaldi'
            ]
    }, 
    {
        'category': 'Entertainment: Music', 
        'type': 'multiple', 
        'difficulty': 'medium', 
        'question': 'In which city did American rap producer DJ Khaled originate from?',
        'correct_answer': 'Miami', 
        'incorrect_answers': [
            'New York', 
            'Detroit', 
            'Atlanta'
            ]
        }
]
"""
