//
// Created by aziz on 10/17/24.
//

#ifndef OBJECTS_H
#define OBJECTS_H

#include <fstream>
#include <iostream>

#include <boost/archive/text_oarchive.hpp>
#include <boost/archive/text_iarchive.hpp>
#include <boost/serialization/access.hpp>


namespace Objects {
    class Date {
    private:
        int m_mois;
        int m_annee;

        friend class boost::serialization::access;

        template<class Archive>
        void serialize(Archive& ar, const unsigned int version) {
            ar & m_annee;
            ar & m_mois;
        }

    public:
        Date(int annee, int mois)
            : m_annee(annee), m_mois(mois)
        {}

        int mois() const {return m_mois;}
        int annee() const {return m_annee;}

        void set_annee(int annee){m_annee = annee;}
        void set_mois(int mois){m_mois = mois;}

    };
    class Product {
    private:
        std::string m_code;
        Date m_DLC;
        int m_qte_stock;

        friend class boost::serialization::access;

        template<class Archive>
        void serialize(Archive& ar, const unsigned int version) {
            ar & m_code;
            ar & m_DLC;
            ar & m_qte_stock;
        }

    public:
        Product(const std::string& code,const Date DLC, int qte_stock)
            :m_code(code), m_DLC(DLC), m_qte_stock(qte_stock)
        {}

        Product()
            : m_code("0"), m_qte_stock(0), m_DLC(Date(1,1))
        {}

        std::string code() const { return m_code; }
        void set_code(const std::string& code) { m_code = code; }

        Date DLC() const { return m_DLC; }
        void set_DLC(const Date& DLC) { m_DLC = DLC; }

        int stock() const { return m_qte_stock; }
        void set_stock(int qte_stock) { m_qte_stock = qte_stock; }

    };

    struct Result {
        Product p;
        std::string decision;
        Result(const Product& p,const std::string& decision)
            :p(p), decision(decision)
        {}

        friend class boost::serialization::access;

        template<class Archive>
        void serialize(Archive& ar, const unsigned int version) {
            ar & p;
            ar & decision;
        }

        Result() = default;
    };
}

#endif //OBJECTS_H
