-- MySQL dump 10.13  Distrib 8.0.36, for Linux (x86_64)
--
-- Host: localhost    Database: ep2023
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
-- Table structure for table `colis`
--

DROP TABLE IF EXISTS `colis`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `colis` (
  `idColis` int NOT NULL AUTO_INCREMENT,
  `dateColis` date NOT NULL,
  `nomDest` varchar(100) NOT NULL,
  `adrDest` varchar(100) NOT NULL,
  `codePostal` int NOT NULL,
  `fragile` char(1) DEFAULT NULL,
  `etat` int DEFAULT '0',
  `cinExp` char(8) DEFAULT NULL,
  `idTrans` char(5) DEFAULT NULL,
  PRIMARY KEY (`idColis`),
  CONSTRAINT `ch1` CHECK (((`fragile` = _utf8mb4'F') or (`fragile` = _utf8mb4'V'))),
  CONSTRAINT `ch2` CHECK (((`etat` = 0) or (`etat` = 1)))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `colis`
--

LOCK TABLES `colis` WRITE;
/*!40000 ALTER TABLE `colis` DISABLE KEYS */;
/*!40000 ALTER TABLE `colis` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `expediteur`
--

DROP TABLE IF EXISTS `expediteur`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `expediteur` (
  `cinExp` char(8) NOT NULL,
  `nomExp` varchar(100) NOT NULL,
  `telExp` char(8) NOT NULL,
  PRIMARY KEY (`cinExp`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `expediteur`
--

LOCK TABLES `expediteur` WRITE;
/*!40000 ALTER TABLE `expediteur` DISABLE KEYS */;
/*!40000 ALTER TABLE `expediteur` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `transporteur`
--

DROP TABLE IF EXISTS `transporteur`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `transporteur` (
  `idTrans` char(5) NOT NULL,
  `nomTrans` varchar(100) NOT NULL,
  `telTrans` char(8) NOT NULL,
  PRIMARY KEY (`idTrans`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `transporteur`
--

LOCK TABLES `transporteur` WRITE;
/*!40000 ALTER TABLE `transporteur` DISABLE KEYS */;
/*!40000 ALTER TABLE `transporteur` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-11-03  6:39:19
