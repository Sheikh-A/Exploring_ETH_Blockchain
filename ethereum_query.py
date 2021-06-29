from web3 import Web3
from hexbytes import HexBytes

IP_ADDR='18.188.235.196'
PORT='8545'

w3 = Web3(Web3.HTTPProvider('http://' + IP_ADDR + ':' + PORT))

def get_transaction(tx):
    tx = w3.eth.get_transaction(tx)   #YOUR CODE HERE
    return tx

# Return the gas price used by a particular transaction,
#   tx is the transaction
def get_gas_price(tx):
    tx = get_transaction(tx)
    #print(tx)
    gas_price = tx['gasPrice'] #YOUR CODE HERE
    #print(gas_price)
    return gas_price

def get_gas(tx):
    tx = w3.eth.get_transaction_receipt(tx) #YOUR CODE HERE
    #print(tx)
    gas = tx['gasUsed']
    #print(gas)
    return gas

def get_transaction_cost(tx):
    tx_cost = get_gas_price(tx) * get_gas(tx)
    #print(tx_cost)
    return tx_cost

def get_block_cost(block_num):
    block = w3.eth.get_block(block_num)
    #print(block)
    transactions = block['transactions']
    block_cost = 0  #YOUR CODE HERE
    #print(block_cost)
    for items in transactions:
        current_cost = get_transaction_cost(items)
        block_cost = block_cost + current_cost
    return block_cost

# Return the hash of the most expensive transaction
def get_most_expensive_transaction(block_num):
    getBlock = w3.eth.get_block(block_num)
    transactions = getBlock['transactions']
    highestCost = 0
    highestNum = 0
    for transNum in transactions:
        current_cost = get_transaction_cost(transNum)
        if current_cost > highestCost:
            highestCost = current_cost
            highestNum = transNum
    max_tx = HexBytes(highestNum)  #YOUR CODE HERE
    return max_tx

#if w3.isConnected():
#     This line will mess with our autograders, but might be useful when debugging
#    print( "Connected to Ethereum node" )
#else:
#    print( "Failed to connect to Ethereum node!" )
