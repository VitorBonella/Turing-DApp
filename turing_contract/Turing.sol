// SPDX-License-Identifier: GPL-3.0

pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";


contract Turing is ERC20{

    struct AddresControl{
        string codename;
        mapping(string => bool) alrearyVotedAdresses;
    }

    mapping(string => address) public addresses;
    mapping(address => AddresControl) public addressesControl;
    address professora;
    bool public PollOpened;


    constructor() ERC20("Turing", "TURI"){
        professora = 0xA5095296F7fF9Bdb01c22e3E0aC974C8963378ad;
        PollOpened = true;

        addresses["Andre"] = 0xD07318971e2C15b4f8d3d28A0AEF8F16B9D8EAb6;
        addresses["Antonio"] = 0x127B963B9918261Ef713cB7950c4AD16d4Fe18c6;
        addresses["Ratonilo"] = 0x5d84D451296908aFA110e6B37b64B1605658283f;
        addresses["eduardo"] = 0x500E357176eE9D56c336e0DC090717a5B1119cC2;
        addresses["Enzo"] = 0x5217A9963846a4fD62d35BB7d58eAB2dF9D9CBb8;
        addresses["Fernando"] = 0xFED450e1300CEe0f69b1F01FA85140646E596567;
        addresses["Juliana"] = 0xFec23E4c9540bfA6BBE39c4728652F2def99bc1e;
        addresses["Altoe"] = 0x6701D0C23d51231E676698446E55F4936F5d99dF;
        addresses["Salgado"] = 0x8321730F4D59c01f5739f1684ABa85f8262f8980;
        addresses["Regata"] = 0x4A35eFD10c4b467508C35f8C309Ebc34ae1e129a;
        addresses["Luis"] = 0xDD551702Dc580B7fDa2ddB7a1Ca63d29E8CDCf33;
        addresses["Nicolas"] = 0x01fe9DdD4916019beC6268724189B2EED8C2D49a;
        addresses["Rauta"] = 0x726150C568f3C7f1BB3C47fd1A224a5C3F706BB1;
        addresses["Silva"] = 0xCAFE34A88dCac60a48e64107A44D3d8651448cd9;
        addresses["Sophie"] = 0xDfb0B8b7530a6444c73bFAda4A2ee3e482dCB1E3;
        addresses["Thiago"] = 0xBeb89bd95dD9624dEd83b12dB782EAE30805ef97;
        addresses["Brito"] = 0xEe4768Af8caEeB042Da5205fcd66fdEBa0F3FD4f;
        addresses["ulopesu"] = 0x89e66f9b31DAd708b4c5B78EF9097b1cf429c8ee;
        addresses["Vinicius"] = 0x48cd1D1478eBD643dba50FB3e99030BE4F84d468;
        addresses["Bonella"] = 0xFADAf046e6Acd9E276940C728f6B3Ac1A043054c;

        addressesControl[0xD07318971e2C15b4f8d3d28A0AEF8F16B9D8EAb6].codename = "Andre";
        addressesControl[0x127B963B9918261Ef713cB7950c4AD16d4Fe18c6].codename = "Antonio";
        addressesControl[0x5d84D451296908aFA110e6B37b64B1605658283f].codename = "Ratonilo";
        addressesControl[0x500E357176eE9D56c336e0DC090717a5B1119cC2].codename = "eduardo";
        addressesControl[0x5217A9963846a4fD62d35BB7d58eAB2dF9D9CBb8].codename = "Enzo";
        addressesControl[0xFED450e1300CEe0f69b1F01FA85140646E596567].codename = "Fernando";
        addressesControl[0xFec23E4c9540bfA6BBE39c4728652F2def99bc1e].codename = "Juliana";
        addressesControl[0x6701D0C23d51231E676698446E55F4936F5d99dF].codename = "Altoe";
        addressesControl[0x8321730F4D59c01f5739f1684ABa85f8262f8980].codename = "Salgado";
        addressesControl[0x4A35eFD10c4b467508C35f8C309Ebc34ae1e129a].codename = "Regata";
        addressesControl[0xDD551702Dc580B7fDa2ddB7a1Ca63d29E8CDCf33].codename = "Luis";
        addressesControl[0x01fe9DdD4916019beC6268724189B2EED8C2D49a].codename = "Nicolas";
        addressesControl[0x726150C568f3C7f1BB3C47fd1A224a5C3F706BB1].codename = "Rauta";
        addressesControl[0xCAFE34A88dCac60a48e64107A44D3d8651448cd9].codename = "Silva";
        addressesControl[0xDfb0B8b7530a6444c73bFAda4A2ee3e482dCB1E3].codename = "Sophie";
        addressesControl[0xBeb89bd95dD9624dEd83b12dB782EAE30805ef97].codename = "Thiago";
        addressesControl[0xEe4768Af8caEeB042Da5205fcd66fdEBa0F3FD4f].codename = "Brito";
        addressesControl[0x89e66f9b31DAd708b4c5B78EF9097b1cf429c8ee].codename = "ulopesu";
        addressesControl[0x48cd1D1478eBD643dba50FB3e99030BE4F84d468].codename = "Vinicius";
        addressesControl[0xFADAf046e6Acd9E276940C728f6B3Ac1A043054c].codename = "Bonella";
        
    }

    modifier onlyTeacher {
        require(msg.sender == professora);
        _;
    }

    modifier VotePermission(string memory codename, uint256 amount){
        require(PollOpened,"You cant vote anymore");
        require(addresses[codename] != address(0x0),"invalid codename"); // se é um voto em alguem que existe
        require(amount <= 2*10**18,"max amount is 2"); // tem que ser no maximo 2
        require(keccak256(abi.encodePacked(addressesControl[msg.sender].codename)) != keccak256(abi.encodePacked("")),"you not allowed to vote"); //tem que ta no mapa de carteiras para votar
        require(keccak256(abi.encodePacked(addressesControl[msg.sender].codename)) != keccak256(abi.encodePacked(codename)),"you should not vote yourself"); // nao pode votar nele mesmo
        require(addressesControl[msg.sender].alrearyVotedAdresses[codename] != true,"you already voted"); // nao pode ser votado no codenome
        _;
    }

    function issueToken(address receiver, uint256 amount) public onlyTeacher{
        _mint(receiver, amount);
    }

    function vote(string memory codename, uint256 amount) public VotePermission(codename, amount){
        
        _mint(addresses[codename],amount);
        _mint(msg.sender,2*10**17);
        addressesControl[msg.sender].alrearyVotedAdresses[codename] = true;

    }

    function endVoting() public onlyTeacher{

        if(PollOpened == true){
            PollOpened = false;
        }else{
            PollOpened = true;
        }

    }

}