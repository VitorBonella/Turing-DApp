const selector = document.getElementById('codename-selected')
const amount_input = document.getElementById('vote-amount')
const btn_vote = document.getElementById('vote-btn')

async function vote(){

    let codename = selector.options[selector.selectedIndex].text;
    let amount = amount_input.value * (10**18)
    
    TuringContract.vote(codename,amount).catch((err) => {
        alert("Error end pool" + err.message);
    });


}

btn_vote.addEventListener('click', vote)