import random
import string


def get_random_string(length):
    # Create random string with the combination of lower and upper case
    letters = string.ascii_letters
    result_str = ''.join(random.choice(letters) for i in range(length))

    return result_str

def generate_api(questionnaire_data):
    youtube_weights = {}

    for user_data in questionnaire_data:
        # youtube
        youtube = user_data["youtube"]
        current_weight = 5 
        for i in range (len(youtube)):
            if youtube[i] in youtube_weights:
                youtube_weights[youtube[i]] += current_weight
            else:
                youtube_weights[youtube[i]] = current_weight
            
            current_weight -= 1
        
    # youtube
    max_weight = max(youtube_weights.values())  # maximum value
    max_keys = [k for k, v in youtube_weights.items() if v == max_weight]  

    return {"youtube": {"videoCategory": max_keys[0]}}

