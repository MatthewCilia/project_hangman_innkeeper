from project import tea, text_delay, extra_life_q
from unittest.mock import patch

# Tests tea function
@patch("builtins.input", side_effect=["cabbage", "green"])
@patch("project.text_delay")
def test_tea(mock_text_delay, mock_input):
    assert tea("english breakfast tea") == "Oh good, that's all I have! Stay right there and I'll get it for you. Oh, and don't open the black box."
    assert tea("english breakfast") == "Oh good, that's all I have! Stay right there and I'll get it for you. Oh, and don't open the black box."
    assert tea("cab") == "Oh, that sounds delicious! But I only have English Breakfast. Stay right there and I'll get it for you. Oh, and don't open the black box."

# Tests text_delay function
@patch("project.text_delay")
def test_text_delay(mock_text_delay):
    assert text_delay("hello") == "text has been animated"
    assert text_delay("Hello") == "text has been animated"
    assert text_delay("2345sfda") == "text has been animated"

# Test the extra life function when the user inputs the incorrect answer
@patch("project.requests.get")
@patch("project.text_delay")
@patch("project.random.shuffle", side_effect=lambda x: x)
@patch("builtins.input", side_effect=["cabbage", "yes", "z", "d"])
def test_extra_life_q_correct(mock_input, mock_shuffle, mock_text_delay, mock_requests):
    mock_requests.return_value.json.return_value = {
        "results": [{
            "question": "Which one is the dip",
            "correct_answer": "Hummus",
            "incorrect_answers": ["Chicken", "Beef", "Pork"]
        }]
    }
    assert extra_life_q("For sure") == "correct"
    assert extra_life_q("no") == "pass"

    
# Test the extra life function when the user inputs the incorrect answer 
@patch("project.requests.get")
@patch("project.text_delay")
@patch("project.random.shuffle", side_effect=lambda x: x)
@patch("builtins.input", side_effect=["cabbage", "yes", "z", "c"])
def test_extra_life_q_incorrect(mock_input, mock_shuffle, mock_text_delay, mock_requests):
    mock_requests.return_value.json.return_value = {
        "results": [{
            "question": "Which one is the dip",
            "correct_answer": "Hummus",
            "incorrect_answers": ["Chicken", "Beef", "Pork"]
        }]
    }
    assert extra_life_q("For sure") == "incorrect"
    assert extra_life_q("no") == "pass"