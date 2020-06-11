import os
import json
from PIL import Image
import base64
import pickle
import torch
from torch.autograd import Variable
from torchvision import transforms

from model import EncoderCNN, DecoderRNN
from vocabulary import Vocabulary

def clean_sentence(word_idx_list, vocab):
    """Take a list of word ids and a vocabulary from a dataset as inputs
    and return the corresponding sentence (as a single Python string).
    """
    sentence = []
    for i in range(len(word_idx_list)):
        vocab_id = word_idx_list[i]
        word = vocab.idx2word[vocab_id]
        if word == vocab.end_word:
            break
        if word != vocab.start_word:
            sentence.append(word)
    sentence = " ".join(sentence)
    return sentence

def initialize():
    checkpoint = torch.load(os.path.join('./models', 'best-model.pkl'), map_location=torch.device('cpu'))

    embed_size = 256
    hidden_size = 512

    with open('./vocab.pkl', "rb") as f:
        vocab = pickle.load(f)
    vocab_size = len(vocab)

    encoder = EncoderCNN(embed_size)
    decoder = DecoderRNN(embed_size, hidden_size, vocab_size)
    encoder.eval()
    decoder.eval()

    encoder.load_state_dict(checkpoint['encoder'])
    decoder.load_state_dict(checkpoint['decoder'])

    return encoder, decoder, vocab

def image_loader(img):
    transform_test = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize((0.485, 0.456, 0.406),(0.229, 0.224, 0.225))
    ])
    img = transform_test(img).float()
    img = img.unsqueeze_(0)
    img = Variable(img)
    return img