import web
import json
import os
import sys
from numpy import mat

sys.path.append('..')
import common

features = 277 # TODO

def load_model(name):
    model = common.prepare_classifier('./models/' + name, features)
    return {
        'name': name.split('-')[0],
        'model': model
    }

def load_models():
    models = os.listdir('models')
    # ignore hidden files
    models = filter( lambda f: not f.startswith('.'), models)
    if not models:
        raise ValueError('No models found!')
    print 'loading models {}'.format(models)
    models = map(load_model, models)
    print '{} models loaded'.format(len(models))
    return models

def data_to_vector(data):
    # TODO really implement text-to-feature-vector logic here!
    return mat([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.256348108539441,0.24955443375464484,0.0])

models = load_models()

urls = (
    '/categorize', 'categorize'
)
app = web.application(urls, globals())

class categorize:
    def POST(self):
        try:
            input = json.loads(web.data())
        except ValueError:
            web.badrequest()
            return 'Cannot parse incoming JSON'

        print input
        if not 'body' in input:
            web.badrequest()
            return 'Incoming JSON should have "body" field'

        body = input['body']

        vector = data_to_vector(body)

        categories = []
        for model in models:
            if (model['model'].predict(mat(vector))[0] == 1):
                categories.append(model['name'])
        return json.dumps(categories)

if __name__ == "__main__":
    app.run()
