#include "ex5.h"

#include <iomanip>

void Program::saisie(int &n) {
    do {
        std::cout << "enter n \n";
        std::cin >> n;
    }while(n > 100);
}
void Program::remplir(std::vector<Eleve>& T, int& n) {
    for(size_t i = 0; i < n ; i++) {
        std::string CIN;
        std::string N_p;
        std::string Section;
        double Moyenne;

        std::cout << "Enter CIN d'eleve: " << i + 1 << '\n';
        std::cin >> CIN;
        std::cin.ignore();
        std::cout << "Enter NP d'eleve: " << i + 1 << '\n';
        std::getline(std::cin ,N_p);
        std::cout << "Enter Section d'eleve: " << i + 1 << '\n';
        std::getline(std::cin ,Section);
        std::cout << "Enter Moyenne Annuelle d'eleve: " << i + 1 << '\n';
        std::cin >> Moyenne;

        Eleve e;
        e.set_num_cin(CIN);
        e.set_section(Section);
        e.set_n_p(N_p);
        e.set_moyen(Moyenne);
        T[i] = e;
    }
}
void Program::stocker(std::string& path,std::vector<Eleve>& T, std::vector<BAC>& T2, int& n){
    std::ofstream F(path);
    if(F.is_open()) {
        for(int i = 0; i < n; i++) {
                double moyenne_bac;
                std::cout << "entrer moyenne de bac d'eleve: " << i + 1 << '\n';
                std::cin >> moyenne_bac;
                T2[i].moyenne_bac = moyenne_bac;
                if(moyenne_bac >= 10) {
                    T2[i].admis = true;
                }
                else {
                    double moyenne_generale = (2 * T2[i].moyenne_bac + T[i].moyen())/3;
                    if(moyenne_generale >= 10) {
                        T2[i].admis = true;
                    }
                    else {
                        T2[i].admis = false;
                    }
                }
        }

        double counter = 0;
        double taux = 0;
        for(int i = 0; i < n; i++) {
            if(T2[i].admis) counter++;
        }
        taux = (counter * 100) / n;
        F << "les nombres des admis:" << counter << '\n';
        F << "le taux des admis:" << std::fixed << std::setprecision(2) << taux << '%' << '\n';
        F.close();

    }
    else {
        std::cerr << "Unable to open file for writing! \n";
    }
}
void Program::afficher(std::string &path) {
    std::fstream F(path);
    if(F.is_open()) {
        std::string line;
        while(std::getline(F, line)) {
            std::cout << line << '\n';
        }
        F.close();
    } else {
        throw std::runtime_error("error opening file to read from");
    }
}



