

todos = ['salsa\n', 'cake\n', 'mango\n']



for t in todos:
    # t = t.strip() to remove charactes from a string
    print(f"Before Strip {t}")

newTodos = [t.strip('\n') for t in todos] # alternative to strip method

for tn in newTodos:
    print(f"After Strip{tn}")