from web3 import HTTPProvider, Web3

def codename_list():

        codename_list = sorted(["Andre",
                "Antonio",
                "Ratonilo",
                "eduardo",
                "Enzo",
                "Fernando",
                "Juliana",
                "Altoe",
                "Salgado",
                "Regata",
                "Luis",
                "Rauta",
                "Silva",
                "Sophie",
                "Thiago",
                "Brito",
                "ulopesu",
                "Vinicius",
                "Bonella"])

        return codename_list

def codename_with_address():

        return [("Andre","0xD07318971e2C15b4f8d3d28A0AEF8F16B9D8EAb6"),
        ("Antonio","0x127B963B9918261Ef713cB7950c4AD16d4Fe18c6"),
        ("Ratonilo","0x5d84D451296908aFA110e6B37b64B1605658283f"),
        ("eduardo","0x500E357176eE9D56c336e0DC090717a5B1119cC2"),
        ("Enzo","0x5217A9963846a4fD62d35BB7d58eAB2dF9D9CBb8"),
        ("Fernando","0xFED450e1300CEe0f69b1F01FA85140646E596567"),
        ("Juliana","0xFec23E4c9540bfA6BBE39c4728652F2def99bc1e"),
        ("Altoe","0x6701D0C23d51231E676698446E55F4936F5d99dF"),
        ("Salgado","0x8321730F4D59c01f5739f1684ABa85f8262f8980"),
        ("Regata","0x4A35eFD10c4b467508C35f8C309Ebc34ae1e129a"),
        ("Luis","0xDD551702Dc580B7fDa2ddB7a1Ca63d29E8CDCf33"),
        ("Nicolas","0x01fe9DdD4916019beC6268724189B2EED8C2D49a"),
        ("Rauta","0x726150C568f3C7f1BB3C47fd1A224a5C3F706BB1"),
        ("Silva","0xCAFE34A88dCac60a48e64107A44D3d8651448cd9"),
        ("Sophie","0xDfb0B8b7530a6444c73bFAda4A2ee3e482dCB1E3"),
        ("Thiago","0xBeb89bd95dD9624dEd83b12dB782EAE30805ef97"),
        ("Brito","0xEe4768Af8caEeB042Da5205fcd66fdEBa0F3FD4f"),
        ("ulopesu","0x89e66f9b31DAd708b4c5B78EF9097b1cf429c8ee"),
        ("Vinicius","0x48cd1D1478eBD643dba50FB3e99030BE4F84d468"),
        ("Bonella","0xFADAf046e6Acd9E276940C728f6B3Ac1A043054c")]

def top_stakers():

        w3 = Web3(HTTPProvider('https://goerli.infura.io/v3/dca275c972ff418ca502afae58202e1c'))

        contract_address = '0x834487ec3b7301EeB63C6cDD9aEB85B5f80A7900'
        
        abi_r = contract_abi()

        contract = w3.eth.contract(
                address= Web3.toChecksumAddress(contract_address),
                abi = abi_r
        )

        list_of_stakers = []
        for c in codename_with_address():
                address = c[1]
                balance = contract.functions.balanceOf(address).call()
                list_of_stakers.append((c[0],balance * (10 ** -18)))

        list_of_stakers.sort(key=lambda a: a[1],reverse = True)

        return list_of_stakers


def contract_abi():

        return [
	{
		"inputs": [],
		"stateMutability": "nonpayable",
		"type": "constructor"
	},
	{
		"anonymous": False,
		"inputs": [
			{
				"indexed": True,
				"internalType": "address",
				"name": "owner",
				"type": "address"
			},
			{
				"indexed": True,
				"internalType": "address",
				"name": "spender",
				"type": "address"
			},
			{
				"indexed": False,
				"internalType": "uint256",
				"name": "value",
				"type": "uint256"
			}
		],
		"name": "Approval",
		"type": "event"
	},
	{
		"anonymous": False,
		"inputs": [
			{
				"indexed": True,
				"internalType": "address",
				"name": "from",
				"type": "address"
			},
			{
				"indexed": True,
				"internalType": "address",
				"name": "to",
				"type": "address"
			},
			{
				"indexed": False,
				"internalType": "uint256",
				"name": "value",
				"type": "uint256"
			}
		],
		"name": "Transfer",
		"type": "event"
	},
	{
		"inputs": [],
		"name": "PollOpened",
		"outputs": [
			{
				"internalType": "bool",
				"name": "",
				"type": "bool"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"name": "addresses",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"name": "addressesControl",
		"outputs": [
			{
				"internalType": "string",
				"name": "codename",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "owner",
				"type": "address"
			},
			{
				"internalType": "address",
				"name": "spender",
				"type": "address"
			}
		],
		"name": "allowance",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "spender",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "amount",
				"type": "uint256"
			}
		],
		"name": "approve",
		"outputs": [
			{
				"internalType": "bool",
				"name": "",
				"type": "bool"
			}
		],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "account",
				"type": "address"
			}
		],
		"name": "balanceOf",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "decimals",
		"outputs": [
			{
				"internalType": "uint8",
				"name": "",
				"type": "uint8"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "spender",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "subtractedValue",
				"type": "uint256"
			}
		],
		"name": "decreaseAllowance",
		"outputs": [
			{
				"internalType": "bool",
				"name": "",
				"type": "bool"
			}
		],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "endVoting",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "spender",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "addedValue",
				"type": "uint256"
			}
		],
		"name": "increaseAllowance",
		"outputs": [
			{
				"internalType": "bool",
				"name": "",
				"type": "bool"
			}
		],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "receiver",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "amount",
				"type": "uint256"
			}
		],
		"name": "issueToken",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "name",
		"outputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "symbol",
		"outputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "totalSupply",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "to",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "amount",
				"type": "uint256"
			}
		],
		"name": "transfer",
		"outputs": [
			{
				"internalType": "bool",
				"name": "",
				"type": "bool"
			}
		],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "from",
				"type": "address"
			},
			{
				"internalType": "address",
				"name": "to",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "amount",
				"type": "uint256"
			}
		],
		"name": "transferFrom",
		"outputs": [
			{
				"internalType": "bool",
				"name": "",
				"type": "bool"
			}
		],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "codename",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "amount",
				"type": "uint256"
			}
		],
		"name": "vote",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	}
]