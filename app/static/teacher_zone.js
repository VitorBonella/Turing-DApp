const address_mint = document.getElementById('mint-address-input')
const amount_mint = document.getElementById('mint-amount-input')
const mint_btn = document.getElementById('mint-btn')

async function mintTokens() {

    let addressMint = address_mint.value;
    let amountMint = amount_mint.value;

    let value_converted = (amountMint*(10**18)).toString()

    TuringContract.issueToken(addressMint,value_converted).catch((err) => {
        alert("Error mint tokens" + err.message);
      });
}

const pool_btn = document.getElementById('pool-btn')
const pool_status = document.getElementById('pool-status')

async function switchPoll() {

  TuringContract.endVoting().catch((err) => {
      alert("Error end pool" + err.message);
    });

}


var isEndedVote = true;
const EndedVote = async() => {
	try{
		const voting = await TuringContract.PollOpened();
		isEndedVote = voting;
	} catch(e){}
}

function endedVoting(){
	EndedVote();
  if(isEndedVote){
    pool_status.innerText = "Poll Status: Open";
    pool_status.className = "text-success fs-3"
  }
  else{
    pool_status.innerText = "Poll Status: Close";
    pool_status.className = "text-danger fs-3"
  }
}

setInterval(endedVoting, 5000)
mint_btn.addEventListener('click', mintTokens)
pool_btn.addEventListener('click', switchPoll)