#include <iostream>
#include "objects.h"

bool verif(Objects::Product p) {
    return true;
}
void saisie() {
    std::ofstream ofs("data.bin");
    bool writeMode = true;
    while(writeMode) {
        Objects::Product p;
        do {
            std::string code;
            int qte;
            int annee;
            int mois;

            std::cout << "enter code de votre object \n";
            std::cin >> code;

            std::cout << "enter la quantite \n";
            std::cin >> qte;

            std::cout << "entrer annee";
            std::cin >> annee;

            std::cout << "enter le mois";
            std::cin >> mois;

            Objects::Date d(annee, mois);

            p.set_code(code);
            p.set_stock(qte);
            p.set_DLC(d);

        }while(!verif(p));
        {
            boost::archive::text_oarchive oa(ofs);
            oa << p;
        }

        std::string choice;
        std::cout << "do you want to continue?(O/n) \n";

        std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');

        std::getline(std::cin, choice);

        std::transform(choice.begin(), choice.end(), choice.begin(), [](unsigned char c) {
            return std::toupper(c);
        });

        if(choice.empty() || choice == "O") writeMode = false;
    }
    Objects::Product loaded_product;
    {
        std::ifstream ifs("data.bin");
        boost::archive::text_iarchive ia(ifs);
        ia >> loaded_product;  // Deserialize into loaded_product
    }
}
void transfer() {
    std::vector<Objects::Product> products;
    std::vector<Objects::Result> results;
    int a_rejete = 0;
    //read from data.bin
    {
        std::ifstream ifs("data.bin");

        boost::archive::text_iarchive ifa(ifs);
        try {
            while(true) {
                Objects::Product p;
                ifa >> p;
                products.push_back(p);
            }
        } catch (boost::archive::archive_exception& e) {

        }
    }
    //switch from Product to res.bin
    for(const auto& p: products) {
        Objects::Result r(p, "");
        if(p.stock() == 0) {
            r.decision = "stocké";
        }
        else if(p.DLC().annee() > 2024) {
            r.decision = "nouveau";
        }
        else if(p.DLC().annee() <= 2024 && p.DLC().mois() <= 10) {
            r.decision = "permiée";
            a_rejete++;
        }
        results.push_back(r);
    }
    //print them all
    {
        std::ofstream ofs("res.bin");
        boost::archive::text_oarchive ar(ofs);

        for(const auto& r : results) {
            ar << r;
        }
    }
    {
        std::ofstream ofs("res.txt");
        ofs << "nombre a rejetée: " << a_rejete << '\n';
        for(const auto& r: results) {
            if(r.decision == "permiée") {
                ofs << r.p.code();
            }
        }
    }
}
void afficher() {
    {
        std::ifstream ifs("res.txt");
        std::string line;
        while(std::getline(ifs, line)) {
            std::cout << line << '\n';
        }
    }
}

int main() {
    saisie();
    transfer();
    afficher();
    return 0;
}