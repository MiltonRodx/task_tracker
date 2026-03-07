#!/usr/bin/env python3
import sys
from genericpath import isfile
import sys
import json
import time
from pathlib import Path

def main():
    if len(sys.argv) <= 1 or len(sys.argv) > 4: # Verifications
        sys.exit("Usage: app.py [arg1] [arg2] | RTFM (read the fking manual)")

    filelocation = Path('userdata.json')
    if not(filelocation.is_file()) or filelocation.stat().st_size == 0:
        with open('userdata.json', 'w') as f:
            json.dump([], f)

    # Modules
    if sys.argv[1] == 'add':
        with open('userdata.json', 'r') as f:
            pylist = json.load(f) # from json to python list
            status = input("Status (done(1), not-done(2), in-progress(3): ")
            createdAt = time.asctime()
            updatedAt = createdAt
            print(f'Updated at: {updatedAt} and createdAt: {createdAt}')

            # counter logic
            if len(pylist) > 0:
                new_id = max(int(task['id']) for task in pylist) + 1
            else:
                new_id = 1

            # little list
            newtask = dict(id=new_id, description=sys.argv[2], status=status, createdAt=createdAt, updatedAt=updatedAt)

            pylist.append(newtask) # add little list to big list (ok)
            
            with open('userdata.json', 'w') as f: # from python list to json again
                json.dump(pylist, f, indent=4)


    elif sys.argv[1] == 'update':
        # open json file as list
        with open('userdata.json', 'r') as f:
            pylist = json.load(f)

        # edit where id = arg2, put arg3 as description
        for object in pylist:
            if str(object['id']) == str(sys.argv[2]):
                object['description'] = sys.argv[3]
                object['updatedAt'] = time.asctime()
                break

        # save list to json
        with open('userdata.json', 'w') as f:
            json.dump(pylist, f, indent=4)

    elif sys.argv[1] == 'delete':
        # delete module
        with open('userdata.json', 'r') as f:
            data = json.load(f)

            # search for id and remove it from the list
            for obj in data:
                if str(obj['id']) == str(sys.argv[2]):
                    data.remove(obj)
                    break

            with open('userdata.json', 'w') as f:
                json.dump(data, f, indent=4)

    elif sys.argv[1] == 'mark-in-progress' or sys.argv[1] == 'mark-done':
        # mark in progress and done module
        with open('userdata.json', 'r') as f:
            data = json.load(f)
            id_found = 0

            for obj in data:
                if str(obj['id']) == str(sys.argv[2]):
                    if sys.argv[1] == 'mark-in-progress':
                        obj['status'] = '1'
                    else:
                        obj['status'] = '3'

                    id_found = str(obj['id'])
                    break

            with open('userdata.json', 'w') as f:
                json.dump(data, f, indent=4)
            print(f'Task Id:{id_found} set to new state')

    elif sys.argv[1] == 'list':
        if len(sys.argv) == 2:
            # list all
            with open('userdata.json', 'r') as f:
                data = json.load(f)
                print('---| All List |---')
                for obj in data:
                    print(f"Id: {obj['id']}:  Description:{obj['description']}  Status:{obj['status']} createdAt:{obj['createdAt']}  updatedAt:{obj['updatedAt']}")
        
        elif sys.argv[2] == 'done' or sys.argv[2] == 'todo' or sys.argv[2] == 'in-progress':
            # list done module
            arr = ['done', 'todo', 'in-progress']

            with open('userdata.json', 'r') as f:
                data = json.load(f)

                print(f'---| {sys.argv[2]} List |---')
                for obj in data:
                    if str(obj['status']) == str(arr.index(f'{sys.argv[2]}') + 1):
                        print(f"Id: {obj['id']}:  Description:{obj['description']}  Status:{obj['status']} createdAt:{obj['createdAt']}  updatedAt:{obj['updatedAt']}")

if __name__ == "__main__":
    main()