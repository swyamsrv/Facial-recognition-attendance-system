CREATE DATABASE  IF NOT EXISTS `swym` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `swym`;
-- MySQL dump 10.13  Distrib 8.0.30, for Win64 (x86_64)
--
-- Host: localhost    Database: swym
-- ------------------------------------------------------
-- Server version	8.0.30

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
-- Table structure for table `employee_data`
--

DROP TABLE IF EXISTS `employee_data`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employee_data` (
  `name` varchar(25) DEFAULT NULL,
  `bsalary` varchar(25) DEFAULT NULL,
  `shift` varchar(25) DEFAULT NULL,
  `job` varchar(15) DEFAULT NULL,
  `EId` varchar(15) NOT NULL,
  `Dep` varchar(45) DEFAULT NULL,
  `gender` varchar(10) DEFAULT NULL,
  `addr` varchar(45) DEFAULT NULL,
  `dob` varchar(15) DEFAULT NULL,
  `email` varchar(25) DEFAULT NULL,
  `mob` varchar(45) DEFAULT NULL,
  `hod` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`EId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee_data`
--

LOCK TABLES `employee_data` WRITE;
/*!40000 ALTER TABLE `employee_data` DISABLE KEYS */;
INSERT INTO `employee_data` VALUES ('swyam','<10,000','Morning','intern ','1','IT','Male','RJPM','18/09/2001','SWYAMSRV05@GMAIL.com','9838907453','NA'),('Sir','>10 lacs','Morning','xyz','2','IT','Male','Kapoorthala','01/01/2001','swyam@gmail.com','123456','xyz'),('swyam','<10,000','Morning','intern ','3','IT','Male','RJPM','18/09/2001','SWYAMSRV05@GMAIL.com','9838907453','NA');
/*!40000 ALTER TABLE `employee_data` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-09-12 11:57:36
