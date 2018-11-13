CREATE DATABASE  IF NOT EXISTS `solar_dynamics` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `solar_dynamics`;
-- MySQL dump 10.13  Distrib 5.7.24, for Linux (i686)
--
-- Host: localhost    Database: solar_dynamics
-- ------------------------------------------------------
-- Server version	5.7.24-0ubuntu0.16.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `pomiary`
--

DROP TABLE IF EXISTS `pomiary`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `pomiary` (
  `id_pomiaru` int(11) NOT NULL AUTO_INCREMENT,
  `nazwa_pomiaru` varchar(50) NOT NULL,
  `id_obiektu` int(11) NOT NULL,
  PRIMARY KEY (`id_pomiaru`),
  KEY `obiekty_id_obiektu_fk` (`id_obiektu`),
  CONSTRAINT `obiekty_id_obiektu_fk` FOREIGN KEY (`id_obiektu`) REFERENCES `obiekty` (`id_obiektu`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pomiary`
--

LOCK TABLES `pomiary` WRITE;
/*!40000 ALTER TABLE `pomiary` DISABLE KEYS */;
INSERT INTO `pomiary` VALUES (1,'Hamulec postojowy wlaczony',1),(2,'awaria ukladu / niski poziom plynu hamulcowego',1),(3,'Hamowanie',1),(4,'ABS',1),(5,'Temperatura',2),(6,'polaczenie',2),(7,'prad',3),(8,'napiecie',3),(9,'Poziom naladowania akumulatora',4),(10,'Temperatura',4),(11,'Napiecie na kazdym packu ogniw',4),(12,'Prad rozladowania, ladowania, balansowania',4),(13,'Prad pobierany przez falownik 1 z szynie DC',5),(14,'Prad pobierany przez falownik 2 z szynie DC',5),(15,'Napiecie na szynie DC falownka 1',5),(16,'Napiecie na szynie DC falownka 2',5),(17,'Prad pobierany przez silnik 1 w fazie U',5),(18,'Prad pobierany przez silnik 1 w fazie V',5),(19,'Prad pobierany przez silnik 1 w fazie W',5),(20,'Prad pobierany przez silnik 2 w fazie U',5),(21,'Prad pobierany przez silnik 2 w fazie V',5),(22,'Prad pobierany przez silnik 2 w fazie W',5),(23,'Temperatura falownika 1',5),(24,'Temperatura falownika 2',5),(25,'Predkosc walu silnika 1',5),(26,'Predkosc walu silnika 2',5);
/*!40000 ALTER TABLE `pomiary` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-11-13 17:55:17
