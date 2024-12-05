const voitures = document.getElementById("res");

function verif(){
    const n_mat0 = document.getElementById("n_mat0").value;
    const n_mat1_index = document.getElementById("n_mat1").selectedIndex;
    const n_mat2 = document.getElementById("n_mat2").value;
    const n_mat = n_mat0 + document.getElementById("n_mat1").options[n_mat1_index].value + n_mat2;

    const np = document.getElementById("np").value;
    const adr = document.getElementById("adr").value;
    const cin = document.getElementById("cin").value;
    const marque_index = document.getElementById("marque").selectedIndex;
    const genre_com = document.getElementById("genre_comm").checked;
    const genre_pro = document.getElementById("genre_pro").checked;
    const genre_per = document.getElementById("genre_per").checked;

    const robot = document.getElementById("robot").checked;

    if(np.length === 0 || adr.length === 0 || cin.length === 0 || n_mat.length === 0){
        alert("one input is empty");
        return false;
    }

    if(isNaN(n_mat0) || isNaN(n_mat2)){
        alert("immatric must be int")
        return false;
    }

    if(n_mat0.length !== 3 || n_mat2.length !== 4){
        alert("check mat length");
        return false;
    }

    if(n_mat1_index === -1){
        alert("please select a country");
        return false;
    }

    if(np.indexOf(" ") === -1){
        alert("please enter a space in your name");
        return false;
    }

    for (let i = 0; i < np.length; i++) {
        if (!((np[i] >= 'A' && np[i] <= 'Z') || (np[i] >= 'a' && np[i] <= 'z') || np[i] === ' ')) {
            alert("Name must only contain alphabetic characters and spaces");
            return false;
        }
    }

    if(cin.length !== 8 || isNaN(cin)){
        alert("check your cin");
        return false;
    }

    if(cin[0] !== '0' && cin[0] !== '1'){
        alert("cin must start with 0 or 1");
        return false;
    }

    if(marque_index === -1){
        alert("marque must be selected!");
        return false;
    }

    if(!genre_pro && !genre_com && !genre_per){
        alert("please select a genre");
        return false;
    }

    if(!robot){
        alert("please verify you are not a robot!");
        return false;
    }

    voitures.options[voitures.length] = new Option(n_mat, n_mat);
    return true;

}