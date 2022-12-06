const selector = document.getElementById('codename-selected')
const amount_input = document.getElementById('vote-amount')
const btn_vote = document.getElementById('vote-btn')

async function vote(){

    let codename = selector.options[selector.selectedIndex].text;
    let amount = amount_input.value

    let value_converted = (amount*(10**18)).toString()
    
    TuringContract.vote(codename,value_converted).catch((err) => {
        alert("Error vote" + err.message);
    });


}

btn_vote.addEventListener('click', vote)