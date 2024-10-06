-- MySQL dump 10.13  Distrib 8.0.36, for Linux (x86_64)
--
-- Host: localhost    Database: mydb
-- ------------------------------------------------------
-- Server version	8.0.39-0ubuntu0.24.04.2

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `affectation`
--

DROP TABLE IF EXISTS `affectation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `affectation` (
  `idMem` int NOT NULL,
  `idPar` int NOT NULL,
  `dateDeb` date DEFAULT NULL,
  PRIMARY KEY (`idMem`,`idPar`),
  KEY `fk2` (`idPar`),
  CONSTRAINT `fk1` FOREIGN KEY (`idMem`) REFERENCES `membre` (`idMem`),
  CONSTRAINT `fk2` FOREIGN KEY (`idPar`) REFERENCES `parcelle` (`idPar`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `affectation`
--

LOCK TABLES `affectation` WRITE;
/*!40000 ALTER TABLE `affectation` DISABLE KEYS */;
/*!40000 ALTER TABLE `affectation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `jardin`
--

DROP TABLE IF EXISTS `jardin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `jardin` (
  `idJar` varchar(2) NOT NULL,
  `nomJar` varchar(50) DEFAULT NULL,
  `adresse` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`idJar`),
  CONSTRAINT `jardin_chk_1` CHECK ((length(`idJar`) = 2))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `jardin`
--

LOCK TABLES `jardin` WRITE;
/*!40000 ALTER TABLE `jardin` DISABLE KEYS */;
INSERT INTO `jardin` VALUES ('J1','Residence des Pins','Cité des pins'),('R3','Eden des roses','Rue des Martyres');
/*!40000 ALTER TABLE `jardin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `membre`
--

DROP TABLE IF EXISTS `membre`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `membre` (
  `idMem` int NOT NULL AUTO_INCREMENT,
  `nomMem` varchar(50) DEFAULT NULL,
  `genre` varchar(1) DEFAULT NULL,
  `dateNais` date DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `mdp` varchar(6) DEFAULT NULL,
  PRIMARY KEY (`idMem`),
  UNIQUE KEY `email` (`email`),
  CONSTRAINT `mf` CHECK (((`genre` = _utf8mb4'F') or (`genre` = _utf8mb4'M')))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `membre`
--

LOCK TABLES `membre` WRITE;
/*!40000 ALTER TABLE `membre` DISABLE KEYS */;
/*!40000 ALTER TABLE `membre` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `parcelle`
--

DROP TABLE IF EXISTS `parcelle`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `parcelle` (
  `idPar` int NOT NULL AUTO_INCREMENT,
  `numPar` int DEFAULT NULL,
  `idJar` varchar(2) DEFAULT NULL,
  PRIMARY KEY (`idPar`),
  KEY `fk` (`idJar`),
  CONSTRAINT `fk` FOREIGN KEY (`idJar`) REFERENCES `jardin` (`idJar`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `parcelle`
--

LOCK TABLES `parcelle` WRITE;
/*!40000 ALTER TABLE `parcelle` DISABLE KEYS */;
INSERT INTO `parcelle` VALUES (1,1,'J1'),(2,2,'J1'),(3,3,'J1'),(4,4,'J1'),(5,1,'R3'),(6,2,'R3'),(7,3,'R3'),(8,4,'R3');
/*!40000 ALTER TABLE `parcelle` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-09-28  6:06:15
