import flask
from flask import Flask, request, render_template, jsonify
import json
from PIL import Image
import base64
import pickle
import torch
import io
from torch.autograd import Variable

from utils import clean_sentence, initialize, image_loader
from vocabulary import Vocabulary

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods = ['POST'])
def upload():
    f = request.files['file']
    image = Image.open(f).convert("RGB")
    image.save('img.jpg')

    img_io = io.BytesIO()
    image.save(img_io, 'jpeg', quality=100)
    img_io.seek(0)
    img = base64.b64encode(img_io.getvalue())
    return render_template('index.html', img=img.decode('utf-8'))

@app.route('/predictions', methods = ['POST'])
def predict():
    try:
        # f = request.files['file']  
        image = Image.open('./img.jpg').convert("RGB")
        image = image_loader(image)

        encoder, decoder, vocab = initialize()
        features = encoder(image).unsqueeze(1)
        output = decoder.sample(features)
        sentence = clean_sentence(output, vocab)
        res = {}
        res['pred_1'] = sentence

        outputs = decoder.sample_beam_search(features)
        num_sents = min(len(outputs), 3)
        count = 2
        for output in outputs[:num_sents]:
            sentence = clean_sentence(output, vocab)
            res['pred_{}'.format(count)] = sentence
            count += 1
        # print(res)
        return app.response_class(response=json.dumps(res), status=200, mimetype='application/json')
    except Exception as error:
        err = str(error)
        print(err)
        return app.response_class(response=json.dumps(err), status=500, mimetype='application/json')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=8000, use_reloader=False)
