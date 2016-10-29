import web
import json
import os
import sys
from numpy import mat

sys.path.append('..')
import common


import dataVector

dV = dataVector.DataVector()
features = len(dV.features_vec(' '))

print 'feature vector length: {}'.format(features)

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
    return mat(dV.features_vec(data))

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
