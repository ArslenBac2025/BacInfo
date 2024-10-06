function verifnom(nom) {
  if (nom.length > 50) return false;
  if (
    !(nom[0].toUpperCase() <= "Z" && nom[0].toUpperCase() >= "A") ||
    !(
      nom[nom.length - 1].toUpperCase() <= "Z" &&
      nom[nom.length - 1].toUpperCase()
    )
  )
    return false;

  let espace = 0;
  let i = 1;

  while (i < nom.length - 1) {
    if (nom[i] == " ") espace++;
    if (!(nom[i].toUpperCase() <= "Z" && "A" <= nom[i].toUpperCase()))
      return false;
    i++;
  }

  return espace >= 1;
}

function verifemail(email) {
  if (email.length > 50) return false;
  if (!("A" <= email[0].toUpperCase() || email[0].toUpperCase() <= "Z"))
    return false;

  let extension = "";
  const pospt = email.indexOf(".");

  let i = pospt;

  while (i < email.length) {
    extension += email[i];
    i++;
  }

  return extension === ".tn";
}

function verifmdp(mdp) {
  if (mdp.length < 6) return false;

  for (let i = 0; i < mdp.length; i++) {
    if (mdp[i] == " ") return false;
  }

  return true;
}

function inscription() {
  const nom = document.getElementsByName("nom")[0].value;
  const email = document.getElementsByName("email")[0].value;
  const date = document.getElementsByName("date")[0].value;
  const genre = document.getElementsByName("genre")[0].value;
  const mdp = document.getElementsByName("mdp")[0].value;
  const rmdp = document.getElementsByName("rmdp")[0].value;

  if (!verifnom(nom)) {
    return false;
  }
  console.log("hi");

  if (!verifemail(email)) {
    return false;
  }

  const year = parseInt(date.substr(0, 4));
  if (!(1950 < year && year < 2006)) {
    return false;
  }

  if (!genre) {
    return false;
  }

  if (!verifmdp(mdp)) {
    return false;
  }

  if (rmdp != mdp) {
    return false;
  }

  return true;
}
