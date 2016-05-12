import uuid

def gen_token():
    return str(uuid.uuid4()).replace('-','')