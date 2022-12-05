const address_mint = document.getElementById('mint-address-input')
const amount_mint = document.getElementById('mint-amount-input')
const mint_btn = document.getElementById('mint-btn')

async function mintTokens() {

    let addressMint = address_mint.value;
    let amountMint = amount_mint.value;

    TuringContract.issueToken(addressMint,amountMint * (2**18)).catch((err) => {
        alert("Error mint tokens" + err.message);
      });
}

mint_btn.addEventListener('click', mintTokens)