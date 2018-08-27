# Rasa NLU starter-pack

Looked through the [Rasa NLU documentation](http://rasa.com/docs/nlu/) and ready to build your first chatbot? We have some resources to help you get started! This repository contains the foundations of you first custom bot, clone it to get started:

```
git clone https://github.com/RasaHQ/starter-pack-rasa-nlu.git
```

After you clone the repository, you will have a directory called `starter-pack-rasa-nlu` on your local machine containing all the files of this repo. Let's call this directory our project directory.


## Setup and installation

If you haven’t installed Rasa NLU yet, you can do it by navigating to the project directory and running:
```
pip install -r requirements.txt
```
This will install Rasa NLU and all the dependencies you need to successfully build your first bot.


## What’s in this starter-pack?

This starter-pack contains some training data and the main files which you can use as the basis of your first custom bot. It also resembles the usual structure of Rasa NLU project:

- **data/nlu_data.json** file contains training examples of five simple intents:
	- greet
	- goodbye
	- thanks
	- affirm
	- name (examples of this intent contain an entity called name)
	
- **nlu_cofing.yml** file contains configuration of the pipeline:
```text
language: "en"

pipeline:
- name: "nlp_spacy"                   # loads the spacy language model
- name: "tokenizer_spacy"             # splits the sentence into tokens
- name: "ner_crf"                   # uses the pretrained spacy NER model
- name: "intent_featurizer_spacy"     # transforms the sentence into a vector representation
- name: "intent_classifier_sklearn"   # uses the vector representation to classify using SVM
```	

## How to use it?
Even though this starter-pack have only five and quite generic intents, you can train the Rasa NLU model by running:
```make train-nlu```
This will train the NLU model and store it inside the `/models/current/nlu` folder of your project directory.

To test the model, you can run it as a server using the following command:
```make run-nlu```
This will start the server using port 5000. To get the results of the model, you can pass an input message by making a request:
```curl 'localhost:5000/parse?q=Hello&project=current'```

## What's next?
Five intents and one entity are definitely not enough to build an awesome assistant so here are some ideas for what you can do to take this project to the next level:
- Enrich the `data/nlu_data.md` file with the intents you would like your bot to understand. Retrain the NLU model using the command above and see you assistant improving with every run!
- If you need more inspiration we have a really cool [training data file](https://forum.rasa.com/t/rasa-starter-pack/704) which you can find on Rasa Community Forum. This dataset contains quite a few interesting intents and you can use to build a fun chatbot capable of handling small talk. To use it, append the examples for this dataset to `data/nlu_data.md` file, retrain the NLU model and see how your bot learns new skills.


Make sure to let us know how you are getting on and what have you built. Visit [Rasa Community Forum](https://forum.rasa.com) and share your experience.
