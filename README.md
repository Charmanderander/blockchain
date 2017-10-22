Blockchain in Python
---

A simple skeleton of a blockchain implemented in python!

Credits: http://ecomunsing.com/build-your-own-blockchain

# Components

1. `main.py`

This file initializes the blockchain (making the genesis block), and throws in several random transactions

2. `validate.py`

This file validates the transactions made. It checks on the following things:
* Does the sum of the transactions add up to 0?
* Does the block have the correct hash?

If these two conditions are met, the block is considered valid.

Checking the chain involves checking the validity of each block in the chain.

3. `blockgen.py`

This file generates a block by doing the following:
* Getting the parent block hash
* Making its block number
* Generating its block contents
   * Block number
   * Parents hash
   * Length of transactions
   * A collection of transactions
* Generating a hash of its block contents

4. `hasher.py`

This file does the hashing

5. `update.py`

This file updates the state after the transaction is deemed valid

6. `transaction.py`

This file generates dummy transactions
