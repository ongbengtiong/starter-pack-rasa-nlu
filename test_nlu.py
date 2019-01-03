from rasa_nlu.training_data import load_data
from rasa_nlu.model import Trainer
from rasa_nlu import config


def test_train_and_persist():
    training_data = load_data("data/nlu_data.md")
    trainer = Trainer(config.load("nlu_config.yml"))
    interpreter = trainer.train(training_data)
    test_model_directory = trainer.persist("./models/nlu", fixed_model_name="test")

    parsing = interpreter.parse('hello')

    assert parsing['intent']['name'] == 'greet'
    assert test_model_directory
