import pickle
todos = {"high": [], "medium": [],"low": []}
with open('todos.pickle', 'wb') as fh :
    pickle.dump(todos, fh)