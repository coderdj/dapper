import os

# Let's just use the local mongod instance. Edit as needed.

# Please note that MONGO_HOST and MONGO_PORT could very well be left
# out as they already default to a bare bones local 'mongod' instance.
MONGO_HOST = os.environ["DAX_HOST"]
MONGO_PORT = int(os.environ["DAX_PORT"])
MONGO_USERNAME = os.environ["DAX_USERNAME"]
MONGO_PASSWORD = os.environ["DAX_PASSWORD"]
MONGO_AUTH_SOURCE = 'dax'  # needed if --auth mode is enabled
MONGO_DBNAME = 'dax'

aggregate_schema = {
    "detector": {
        'type': 'string',
        'allowed': ["tpc", "muon_veto", "neutron_veto"],
    },
    "status": {
        "type": "int"
    },
    "update_time": {
        "type": "datetime",
    },
    "rate": {
        "type": "float",
    },
    "diagnosis": {
        "type": "string",
    },
    "mode": {
        "type": "string",
    },
    "buff": {
        "type": "float"        
    },
    "human_readable_status": {
        "type": "string"
    },
    "active": {
        "type": "string"
    },
}
aggregate = {
    # 'title' tag used in item links. Defaults to the resource title minus the final 's'
    'item_title': 'dispatcher_status_doc',

    # by default the standard item entry point is defined as
    # '/aggregate_status/<ObjectId>'. We leave it untouched, and we also enable an
    # additional read-only entry point. This way consumers can also perform
    # GET requests at '/aggregate_status/{detector}'.
    'additional_lookup': {
        'url': 'regex("[\w]+")',
        'field': 'detector',
        'default_sort': [('_id', -1)]
    },

    # We choose to override global cache-control directives for this resource.
    'cache_control': 'max-age=10,must-revalidate',
    'cache_expires': 10,

    # most global settings can be overridden at resource level
    'resource_methods': ['GET'],

    'sorting': True,
    'default_sort': [('_id', -1)],
    'schema': aggregate_schema
}

DOMAIN = {'dispatcher_status': aggregate}
