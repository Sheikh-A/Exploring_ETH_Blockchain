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
    block_transactions = block['transactions']
    block_cost = 0  #YOUR CODE HERE
    #print(block_cost)
    for items in block_transactions:
        cost = get_transaction_cost(items)
        #print(cost)
        block_cost = cost + block_cost
    #print(block_cost)
    return block_cost

# Return the hash of the most expensive transaction '0xf7f4905225c0fde293e2fd3476e97a9c878649dd96eb02c86b86be5b92d826b6'
def get_most_expensive_transaction(block_num):
    getBlock = w3.eth.get_block(block_num)
    block_transactions = getBlock['transactions']
    #print(block_transactions)
    maxNum = 0
    maxCost = 0
    for items in block_transactions:
        cost = get_transaction_cost(items)
        if cost > maxCost:
            maxCost = cost
            maxNum = items
    max_tx = HexBytes(maxNum)  #YOUR CODE HERE
    #print(max_tx)
    return max_tx

#if w3.isConnected():
#     This line will mess with our autograders, but might be useful when debugging
#    print( "Connected to Ethereum node" )
#else:
#    print( "Failed to connect to Ethereum node!" )
