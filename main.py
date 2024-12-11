in_transaction = False
database = {}
pending = {}


def begin_transaction():
    global in_transaction
    if (in_transaction == False):
        in_transaction = True
        print("transaction initiated")
    else:
        print("transaction already in progress")


def put(key, value):
    global in_transaction
    global pending
    if (in_transaction == True):
        pending[int(key)] = value
    else:
        print("Error: no transaction pending")


def get(key):
    global in_transaction
    global pending

    try:
        return (database[int(key)])
    except KeyError:
        print("database error: key not found")
        return -1



def commit():
    global in_transaction
    global pending
    global database
    if (in_transaction == True):
        database.update(pending)
        pending = {}
        in_transaction = False
        print("commit complete")
    else:
        print("error: no transaction pending")
    # merge pending with database, favoring database commits


def rollback():
    global in_transaction
    global pending
    if (in_transaction):
        pending = {}
        in_transaction = False
        print("transaction cancelled")
    else:
        print("error, no transaction pending")
    # abort all changes, set state back to !intransaction


def run_interface():
    exit = False
    global in_transaction
    global pending
    global database
    while exit == False:
        inp = input('>>')
        if (inp == "exit"):
            exit_prompt = input("are you sure you want to exit? (Y/N")
            if (exit_prompt == "y" or exit_prompt == "Y"):
                exit = True
                print("exiting interface...")
                break
        elif (inp == "start"):
            begin_transaction()
        elif (inp[:3] == "put"):
            parsed = inp.split()
            put(parsed[1], parsed[2])
        elif (inp[:3] == "get"):
            parsed = inp.split()
            print(parsed[1])
            print(get(parsed[1]))
        elif (inp == "commit"):
            commit()
        elif (inp == "rollback"):
            rollback()
        elif (inp == "log"):
            print(database)
        elif (inp == "debug"):
            print(database)
            print(pending)
            print(in_transaction)


run_interface()

