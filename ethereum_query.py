# import web3
# from web3 import Web3
# from hexbytes import HexBytes

# IP_ADDR='18.188.235.196'
# PORT='8545'

# w3 = Web3(Web3.HTTPProvider('http://' + IP_ADDR + ':' + PORT))

# if w3.isConnected():
#     #     This line will mess with our autograders, but might be useful when debugging
#     #     print( "Connected to Ethereum node" )
# else:
#     print( "Failed to connect to Ethereum node!" )

# def get_transaction(tx):
#     tx = w3.eth.get_transaction(tx)
#     print(tx)
#     return tx

# # Return the gas price used by a particular transaction,
# #   tx is the transaction
# def get_gas_price(tx):
#     tx = get_transaction(tx)
#     print(tx)
#     gas_price = tx.gasPrice #YOUR CODE HERE
#     print(gas_price)
#     return gas_price

# def get_gas(tx):
#     tx = w3.eth.get_transaction_receipt(tx)
#     print(tx)
#     #gasUsed
#     gas = tx.gasUsed
#     print(gas)
#     return gas

# def get_transaction_cost(tx):
#     tx_cost = get_gas(tx) * get_gas_price(tx)
#     return tx_cost

# def get_block_cost(block_num):
#     main_block = w3.eth.getBlock(main_block)
#     block_cost = 0
#     for tx in main_block.transactions:
#         block_cost = block_cost + get_transactionCost(tx)
#     return block_cost

# # Return the hash of the most expensive transaction
# def get_most_expensive_transaction(block_num):
#     block = w3.eth.getBlock(block_num)
#     BlockCostMax = 0
#     max_tx = HexBytes('0xf7f4905225c0fde293e2fd3476e97a9c878649dd96eb02c86b86be5b92d826b6')  #YOUR CODE HERE
#     #For Loop for transactions
#     for tx in block.transactions:
#         cost = get_transactionCost(tx)
#         if cost > BlockCostMax:
#             BlockCostMax = cost
#             maxTx = tx
#     return max_tx

import web3
from web3 import Web3
from hexbytes import HexBytes

IP_ADDR='18.188.235.196'
PORT='8545'

w3 = Web3(Web3.HTTPProvider('http://' + IP_ADDR + ':' + PORT))

if w3.isConnected():
#     This line will mess with our autograders, but might be useful when debugging
#     print( "Connected to Ethereum node" )
else:
    print( "Failed to connect to Ethereum node!" )

def get_transaction(tx):
    trans = w3.eth.get_transaction(tx)   #YOUR CODE HERE
    return trans

# Return the gas price used by a particular transaction,
#   tx is the transaction
def get_gas_price(tx):
    gas_price = tx.gasPrice #YOUR CODE HERE
    return gas_price

def get_gas(tx):
    gas =  w3.eth.get_transaction_receipt(tx).gasUsed#YOUR CODE HERE
    return gas

def get_transaction_cost(tx):
    tx_cost = get_gas(tx) * get_gas_price(get_transaction(tx)) #YOUR CODE HERE
    return tx_cost

def get_block_cost(block_num):
    block_cost = 0
    transactions = w3.eth.get_block(block_num).transactions
    for trans in transactions:
        block_cost = block_cost + get_transaction_cost(trans)
    return block_cost

# Return the hash of the most expensive transaction
def get_most_expensive_transaction(block_num):
    max_cost = 0
    max_tx = ''
    transactions = w3.eth.get_block(block_num).transactions
    for trans in transactions:
        if max_cost < get_transaction_cost(trans):
            max_cost = get_transaction_cost(trans)
            max_tx = HexBytes(trans.hash)
    return max_tx
