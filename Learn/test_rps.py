from rps import beats, player, random_player
import random
import pytest


def test_beats():
    assert beats('rock', 'scissors') == True
    assert beats('paper', 'scissors') == False
    assert beats('rock', 'paper') == False

@pytest.mark.parametrize("inputs, expected_output", [
    (['rock'], 'rock'),
    (['quit'], 'quit'),
    (['invalid', 'paper'], 'paper'),
    (['invalid', 'invalid', 'scissors'], 'scissors'),
])
def test_player(inputs, expected_output, monkeypatch):
    #we use the monkeypatch fixture to mock the input function
    def mock_input(prompt):
        return inputs.pop(0)

        monkeypatch.setattr('builtins.input', mock_input)
        #call the fiunction to verify output
        assert player() == expected_output


def test_random_player():
    choices = ['rock', 'paper', 'scissors']

    assert random.choice(choices) in choices
