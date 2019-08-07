from rasa_nlu.converters import load_data
from rasa_nlu.config import RasaNLUConfig
from rasa_nlu.model import Trainer
from rasa_nlu.model import Metadata, Interpreter


#builder = ComponentBuilder(use_cache=True)

#with open('./config_tensorflow.json') as conf_file:
#	config_data = json.load(conf_file)
#
# def train_nlu(data, configs, model_dir):
# 	training_data = load_data('./data/data.json')
# 	#trainer = Trainer(RasaNLUModelConfig(configs))
# 	trainer = Trainer(config.load('config_spacy.json'))
# 	trainer.train(training_data)
# 	model_directory = trainer.persist(model_dir, fixed_model_name = 'doctornlu')

def train_nlu(data, config, model_dir):
    training_data = load_data(data)
    trainer = Trainer(RasaNLUConfig(config))
    trainer.train(training_data)
    model_directory = trainer.persist(model_dir, fixed_model_name = 'doctornlu')
#def run_nlu():
#	interpreter = Interpreter.load('./models/nlu/default/doctornlu',RasaNLUModelConfig('config_spacy.yml'))
#	print(interpreter.parse(u"dentist"))
def run_nlu():
    interpreter = Interpreter.load('./models/nlu/default/doctornlu', RasaNLUConfig('config_spacy.json'))


# if __name__ == '__main__':
	# train_nlu('./data/data.json', 'config_spacy.yml', './models/nlu')
	#run_nlu()
if __name__ == '__main__':
    train_nlu('./data/data.json','config_spacy.json', './models/nlu')
    run_nlu()
