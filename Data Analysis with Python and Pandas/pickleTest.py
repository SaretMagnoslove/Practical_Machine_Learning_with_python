import pickle

pickle_in = open('pickle.pickle', 'rb')
data = pickle.load(pickle_in)
print(data)