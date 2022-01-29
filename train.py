from model.initialization import initialization
from config import conf
import argparse
import os


def boolean_string(s):
    if s.upper() not in {'FALSE', 'TRUE'}:
        raise ValueError('Not a valid boolean string')
    return s.upper() == 'TRUE'

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Train')
    parser.add_argument('--cache', default=True, type=boolean_string,
                        help='cache: if set as TRUE all the training data will be loaded at once'
                            ' before the training start. Default: TRUE')
    opt = parser.parse_args()


    m = initialization(conf, train=opt.cache)[0]

    print('主處理程序 ID:', os.getpid())
    print("Training START")
    m.fit()
    print("Training COMPLETE")
