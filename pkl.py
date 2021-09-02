import pickle

with open('data.pkl', 'rb') as f:
    objektas = pickle.load(f)

print(type(objektas))
print(objektas.day)

print(-16**0.5)
