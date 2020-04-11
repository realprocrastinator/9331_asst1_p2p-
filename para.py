from enum import Enum, unique

@unique
class header(Enum):
    ACK_PING = 0
    SND_PING = 1
    REQ_FILE = 2
    SND_FILE = 3


class parameters(dict):
    """
    store the basic parameters for later usage
    PORT_BASE = 12000
    PEER_ID
    PING_INTERVAL
    """
    __para = {
        "PORT_BASE" : 12000, # port = base + peer_id
        "HOST_ADDR" : "127.0.0.1",
        "MSG_SIZE" : 1024,  # msg segment size
    }

    def __new__(cls):
        return cls.__para

class uargs(dict):
    """
    store the user input args
    """
    __args = {
        "OPTIONS" : None,   # OPTIONS stored command line options: join|init
        "PEER_ID" : None,
        "FIRST_SUCCESSOR" : None,
        "SECOND_SUCCESSOR" : None,
        "PING_INTERVAL" : None,
        "KNOWN_PEER" : None,
    }

    def __new__(cls):
        return cls.__args


if __name__ == "__main__":
    print(repr(header.ACK_PING))