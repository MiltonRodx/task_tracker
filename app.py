import sys
import json
import time

if len(sys.argv) <= 1 or len(sys.argv) > 3:
    sys.exit("Usage: app.py [arg1] [arg2] | RTFM (read the fking manual)")


if sys.argv[1] == 'add':
    # add module
    with open('userdata.json', 'r') as f:
        print('this is add module')
        print(f"Description: {sys.argv[2]}")        
        status = input("Status (done(1), not-done(2), in-progress(3): ")
        createdAt = time.asctime()
        updatedAt = createdAt
        print(f'Updated at: {updatedAt} and createdAt: {createdAt}')

        pydict = json.load(f) # from json to python dict
        print(pydict)

        # little dict
        newtask = dict(id='3', description=sys.argv[2], status=status, createdAt=createdAt, updatedAt=updatedAt)

        # add little dict to big dict (ok)
        pydict.append(newtask)

        # from python dict to json again
        with open('userdata.json', 'w') as f:
            json.dump(pydict, f, indent=4)

elif sys.argv[1] == 'update':
    # update module
    print('Update')

elif sys.argv[1] == 'delete':
    # delete module
    print('Delete')

elif sys.argv[1] == 'mark-in-progress':
    # mark in progress module
    print('In progress')

elif sys.argv[1] == 'mark-done':
    # mark done module
    print('Mark done')

elif sys.argv[1] == 'list':
    if len(sys.argv) == 2:
        # list all
        print('list all')
        with open('userdata.json', 'r') as f:
            reader = f.read()
            print(reader)
    
    elif sys.argv[2] == 'done':
        # list done module
        print('list done')
        
    elif sys.argv[2] == 'todo':
        # list todo module
        print('list todo')

    elif sys.argv[2] == 'in-progress':
        # list in-progress module
        print('in-progress')