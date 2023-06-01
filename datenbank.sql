CREATE DATABASE  IF NOT EXISTS `library_management` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `library_management`;
-- MySQL dump 10.13  Distrib 8.0.33, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: library_management
-- ------------------------------------------------------
-- Server version	8.0.33

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
-- Table structure for table `books`
--

DROP TABLE IF EXISTS `books`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `books` (
  `bookid` varchar(7) NOT NULL,
  `title` varchar(100) DEFAULT NULL,
  `author` varchar(45) DEFAULT NULL,
  `publisher` varchar(45) DEFAULT NULL,
  `category` varchar(45) DEFAULT NULL,
  `isbn` varchar(100) DEFAULT NULL,
  `stock` int DEFAULT NULL,
  `availability` varchar(4) DEFAULT 'TRUE',
  PRIMARY KEY (`bookid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `books`
--

LOCK TABLES `books` WRITE;
/*!40000 ALTER TABLE `books` DISABLE KEYS */;
INSERT INTO `books` VALUES ('B005','Python','Michael Kofler','Rheinwerk','Programmierung','123456789',10,NULL),('B012','IT - Grundwissen','Michael Kofler','Rheinwerk','IT - Grundlagen','12549875',10,'TRUE'),('B013','Java','Michael Kofler','Rheinwerk','Programmierung','23488791',15,'TRUE'),('B014','C++','Michael Kofler','Rheinwerk','Programmierung','98743212',35,'TRUE'),('B015','WiSo','Hans Wurst','Europa-Lehrmittel','Wirtschaftskunde','6587974123',25,'TRUE'),('B016','Elektrotechnik','Steffen Huber','Europa-Lehrmittel','IT-Grundlagen','236589741',13,'TRUE'),('B017','Netzwerk - Grundlagen','Hans Wurst','Europa-Lehrmittel','IT-Grundlagen','23548101',40,'TRUE'),('B018','Datenbanken - Grundlagen','Michael Kofler','Rheinwerk','IT - Datenbanken','59678971',10,'TRUE'),('B019','Datenbanken - MySQL','Michael Kofler','Rheinwerk','IT - Datenbanken','35897413567',15,'TRUE'),('B020','Python - Erweitert','Michael Kofler','Rheinwerk','Programmierung','1259763578',20,'TRUE'),('B021','Java - Erweitert','Michael Kofler','Rheinwerk','Programmierung','3658974582',50,'TRUE'),('B022','C++ - Erweitert','Michael Kofler','Rheinwerk','Programmierung','32598741',25,'TRUE'),('B023','IT - Grundwissen','Michael Kofler','Rheinwerk','IT - Grundlagen','12549875',10,'TRUE'),('B024','Java','Michael Kofler','Rheinwerk','Programmierung','23488791',15,'TRUE'),('B025','C++','Michael Kofler','Rheinwerk','Programmierung','98743212',35,'TRUE'),('B026','WiSo','Hans Wurst','Europa-Lehrmittel','Wirtschaftskunde','6587974123',25,'TRUE'),('B027','Elektrotechnik','Steffen Huber','Europa-Lehrmittel','IT-Grundlagen','236589741',13,'TRUE'),('B028','Netzwerk - Grundlagen','Hans Wurst','Europa-Lehrmittel','IT-Grundlagen','23548101',40,'TRUE'),('B029','Datenbanken - Grundlagen','Michael Kofler','Rheinwerk','IT - Datenbanken','59678971',10,'TRUE'),('B030','Datenbanken - MySQL','Michael Kofler','Rheinwerk','IT - Datenbanken','35897413567',15,'TRUE'),('B031','Python - Erweitert','Michael Kofler','Rheinwerk','Programmierung','1259763578',20,'TRUE'),('B032','Java - Erweitert','Michael Kofler','Rheinwerk','Programmierung','3658974582',50,'TRUE'),('B033','C++ - Erweitert','Michael Kofler','Rheinwerk','Programmierung','32598741',25,'TRUE'),('B034','IT - Grundwissen','Michael Kofler','Rheinwerk','IT - Grundlagen','12549875',10,'TRUE'),('B035','Java','Michael Kofler','Rheinwerk','Programmierung','23488791',15,'TRUE'),('B036','C++','Michael Kofler','Rheinwerk','Programmierung','98743212',35,'TRUE'),('B037','WiSo','Hans Wurst','Europa-Lehrmittel','Wirtschaftskunde','6587974123',25,'TRUE'),('B038','Elektrotechnik','Steffen Huber','Europa-Lehrmittel','IT-Grundlagen','236589741',13,'TRUE'),('B039','Netzwerk - Grundlagen','Hans Wurst','Europa-Lehrmittel','IT-Grundlagen','23548101',40,'TRUE'),('B040','Datenbanken - Grundlagen','Michael Kofler','Rheinwerk','IT - Datenbanken','59678971',10,'TRUE'),('B041','Datenbanken - MySQL','Michael Kofler','Rheinwerk','IT - Datenbanken','35897413567',15,'TRUE'),('B042','Python - Erweitert','Michael Kofler','Rheinwerk','Programmierung','1259763578',20,'TRUE'),('B043','Java - Erweitert','Michael Kofler','Rheinwerk','Programmierung','3658974582',50,'TRUE'),('B044','C++ - Erweitert','Michael Kofler','Rheinwerk','Programmierung','32598741',25,'TRUE'),('B045','Neue GUI Test','Mario Lausch','Lalalala','Tester','21351323',14,'TRUE'),('B046','TEst123','asdasdasd','asdasdasd','asgasdsd','1245231',12,'TRUE'),('B047','TEst1231','asdasdas123','asda23','asgasdsd','1245231123',13,'TRUE'),('B048','TEst12311','asdasdas123','asda2323213','asgasdsd23','1245231123',132,'TRUE'),('B049','TEst12311','asdasdas123','asda2323213','asgasdsd23','1245231123',132,'TRUE'),('B050','TEst12311','asdasdas123','asda2323213','asgasdsd23','1245231123',132,'TRUE'),('B051','fdasfasda','asdasd','sdasd','sadasd','213123',12,'TRUE'),('B052','fesfsf','sefsefsef','sefsefsf','sefsef','1412341',143,'TRUE'),('B053','fws3fs','dfsdfsdf','gsdsvsdv','dvs3fs','234235232',11,'TRUE'),('B054','TEste1234','ad241e2sad','wda2eaw','adwaadawd','213124142',12,'TRUE');
/*!40000 ALTER TABLE `books` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `tg_books_insert` BEFORE INSERT ON `books` FOR EACH ROW BEGIN
  INSERT INTO books_seq VALUES (NULL);
  SET NEW.bookid = CONCAT('B', LPAD(LAST_INSERT_ID(), 3, '0'));
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `books_seq`
--

DROP TABLE IF EXISTS `books_seq`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `books_seq` (
  `id` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=55 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `books_seq`
--

LOCK TABLES `books_seq` WRITE;
/*!40000 ALTER TABLE `books_seq` DISABLE KEYS */;
INSERT INTO `books_seq` VALUES (5),(12),(13),(14),(15),(16),(17),(18),(19),(20),(21),(22),(23),(24),(25),(26),(27),(28),(29),(30),(31),(32),(33),(34),(35),(36),(37),(38),(39),(40),(41),(42),(43),(44),(45),(46),(47),(48),(49),(50),(51),(52),(53),(54);
/*!40000 ALTER TABLE `books_seq` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lend_books`
--

DROP TABLE IF EXISTS `lend_books`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `lend_books` (
  `lend_id` varchar(7) NOT NULL,
  `userid` int DEFAULT NULL,
  `bookid` int DEFAULT NULL,
  `lenddate` date DEFAULT NULL,
  `returndate` date DEFAULT NULL,
  PRIMARY KEY (`lend_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lend_books`
--

LOCK TABLES `lend_books` WRITE;
/*!40000 ALTER TABLE `lend_books` DISABLE KEYS */;
/*!40000 ALTER TABLE `lend_books` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `tg_lendbooks_insert` BEFORE INSERT ON `lend_books` FOR EACH ROW BEGIN
  INSERT INTO lend_books_seq VALUES (NULL);
  SET NEW.lend_id = CONCAT('L', LPAD(LAST_INSERT_ID(), 3, '0'));
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `lend_books_seq`
--

DROP TABLE IF EXISTS `lend_books_seq`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `lend_books_seq` (
  `id` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lend_books_seq`
--

LOCK TABLES `lend_books_seq` WRITE;
/*!40000 ALTER TABLE `lend_books_seq` DISABLE KEYS */;
/*!40000 ALTER TABLE `lend_books_seq` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `requests`
--

DROP TABLE IF EXISTS `requests`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `requests` (
  `request_id` varchar(7) NOT NULL,
  `userid` int DEFAULT NULL,
  `bookid` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `requests`
--

LOCK TABLES `requests` WRITE;
/*!40000 ALTER TABLE `requests` DISABLE KEYS */;
/*!40000 ALTER TABLE `requests` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `tg_requests_insert` BEFORE INSERT ON `requests` FOR EACH ROW BEGIN
  INSERT INTO requests_seq VALUES (NULL);
  SET NEW.request_id = CONCAT('R', LPAD(LAST_INSERT_ID(), 3, '0'));
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `requests_seq`
--

DROP TABLE IF EXISTS `requests_seq`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `requests_seq` (
  `id` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `requests_seq`
--

LOCK TABLES `requests_seq` WRITE;
/*!40000 ALTER TABLE `requests_seq` DISABLE KEYS */;
/*!40000 ALTER TABLE `requests_seq` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `userid` varchar(7) NOT NULL,
  `firstname` varchar(100) DEFAULT NULL,
  `lastname` varchar(100) DEFAULT NULL,
  `role` varchar(45) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `password` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`userid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES ('U004','Mario','Lausch','Administrator','lauschmario@gmail.com',NULL),('U005','Olaf','Lamm','Administrator','olamm@mail.com','1234');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `tg_users_insert` BEFORE INSERT ON `users` FOR EACH ROW BEGIN
  INSERT INTO users_seq VALUES (NULL);
  SET NEW.userid = CONCAT('U', LPAD(LAST_INSERT_ID(), 3, '0'));
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `users_seq`
--

DROP TABLE IF EXISTS `users_seq`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users_seq` (
  `id` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_seq`
--

LOCK TABLES `users_seq` WRITE;
/*!40000 ALTER TABLE `users_seq` DISABLE KEYS */;
INSERT INTO `users_seq` VALUES (4),(5);
/*!40000 ALTER TABLE `users_seq` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-06-01 22:15:12
