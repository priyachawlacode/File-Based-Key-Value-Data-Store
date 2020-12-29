# File-Based-Key-Value-Data-Store
It is  file based key value data store that supports basic CRD operations i.e, CREATE , READ , DELETE.

This data store is meant to be used as a local storage for one process on one laptop. The datastore can be exposed to clients as a library that can instantiate a class and work with data store.

FUNCTIONAL REQUIREMENTS:
It can be initialised using an optional file path A new key-value pair can be added to data store using Create operation. Key is a string-capped at 32chars and value is a json object capped at 16kb.
If create is invoked for an existing key , an appropriate error is returned.
Read and Delete operation can be performed by providing the key.
Keys can support Time to Live property when it is created based on user's choice. Once time-to-live for a key expires, no further operations can be performed on that.
All the expected error response are returned.

NON-FUNCTIONAL REQUIREMENTS
The size of file storing data never exceeds 1 GB.
Threading operations are allowed.
