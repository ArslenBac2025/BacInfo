function verif() {
  const cin = document.getElementById("cin").value;
  const np = document.getElementById("np").value;
  const adr = document.getElementById("adr").value;
  const postal = document.getElementById("postal").value;

  console.log(cin);

  if (cin.length != 8) {
    alert("cin must be length 8");
    return false;
  }

  if (cin.at(0) != "0" && cin.at(0) != "1") {
    alert("must start with 0 or 1");
    return false;
  }

  if (np.length > 100 || np.length < 10) {
    alert("np can't be larger than 100 and smaller than 10");
  }

  for (let i = 0; i < np.length; i++) {
    if (np.at(i) === " ") continue;
    if (np.at(i).toUpperCase() < "A" || np.at(i).toUpperCase() > "Z") {
      alert("np must be letters or contain spaces");
      return false;
    }
  }

  let espace = 0;
  for (let i = 0; i < adr.length; i++) {
    if (adr.at(i) === " ") espace++;
  }

  if (espace === 0) {
    alert("adresse must have space!");
    return false;
  }

  if (postal < 1000 || postal > 9999) {
    alert("postal code must be between 1000 and 9999");
    return false;
  }

  const fragile = document.getElementById("fragile");
  const nfragile = document.getElementById("nfragile");

  if (!fragile.checked && !nfragile.checked) {
    alert("must check one!");
    return false;
  }

  const transporteur = document.getElementById("transporteur");
  if (transporteur.selectedIndex === 0) {
    alert("please choose a transporteur");
    return false;
  }

  return true;
}
