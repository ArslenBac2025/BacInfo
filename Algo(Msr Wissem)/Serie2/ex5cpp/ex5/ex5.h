//
// Created by aziz on 10/7/24.
//

#ifndef EX5_H
#define EX5_H

#include <iostream>
#include <vector>
#include <fstream>
#include <iostream>

struct BAC {
    double moyenne_bac;
    bool admis;
};
class Eleve {
public:
    Eleve() : Num_CIN(""), N_p(""), Section(""), Moyen(0.0) {}
    Eleve(const std::string &num_cin, const std::string &n_p, const std::string &section, double moyen)
        : Num_CIN(num_cin),
          N_p(n_p),
          Section(section),
          Moyen(moyen) {
    }

    [[nodiscard]] std::string num_cin() const {
        return Num_CIN;
    }

    void set_num_cin(const std::string &num_cin) {
        if(num_cin.length() != 8) {
            throw std::runtime_error("please enter a cin with 8 characters");
        }
        Num_CIN = num_cin;
    }

    [[nodiscard]] std::string n_p() const {
        return N_p;
    }

    void set_n_p(const std::string &n_p) {
        if(n_p.length() > 20) {
            throw std::runtime_error("your name and last name must be less than 20 chars long");
        }
        N_p = n_p;
    }

    [[nodiscard]] std::string section() const {
        return Section;
    }

    void set_section(const std::string &section) {
        if(Section.length() > 15) {
            throw std::runtime_error("section must be 15 chars");
        }
        Section = section;
    }

    [[nodiscard]] double moyen() const {
        return Moyen;
    }

    void set_moyen(double moyen) {
        if(moyen > 20) {
            throw std::runtime_error("moyen must be equal or less than 20");
        }
        Moyen = moyen;
    }

private:
    std::string Num_CIN;
    std::string N_p;
    std::string Section;
    double Moyen;
};
class Program {
public:
    Program() {
        std::string path = "../ex5/details.txt";
        int n{};
        saisie(n);
        std::vector<Eleve> T(n);
        std::vector<BAC> T2(n);
        remplir(T,n);
        stocker(path, T, T2, n);
        afficher(path);
    }
private:
    void saisie(int& n);
    void remplir(std::vector<Eleve>&T,int& n);
    void stocker(std::string& path,std::vector<Eleve>& T, std::vector<BAC>& T2, int& n);
    void afficher(std::string& path);
};

#endif //EX5_H
