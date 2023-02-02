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
-- Table structure for table `login_register`
--

DROP TABLE IF EXISTS `login_register`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `login_register` (
  `fname` varchar(20) NOT NULL,
  `mname` varchar(25) DEFAULT NULL,
  `lname` varchar(25) DEFAULT NULL,
  `mob_number` varchar(25) DEFAULT NULL,
  `age` int NOT NULL,
  `e_mail` varchar(25) NOT NULL,
  `sec_ques` varchar(25) NOT NULL,
  `sec_ans` varchar(25) NOT NULL,
  `password` varchar(25) NOT NULL,
  `gender` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `login_register`
--

LOCK TABLES `login_register` WRITE;
/*!40000 ALTER TABLE `login_register` DISABLE KEYS */;
INSERT INTO `login_register` VALUES ('sss','','','',45,'asddf','Your Best Friend Name','as','   ','Female'),('Prakash ','Chandra ','Sinha','123456',32,'pcs@gmail.com','Your Pet Name','Bunty','123','Male'),('Prakash','Chandra','Sinha','12345',32,'PCS@gmail.com','Your Birth Place','lko','aaa','Male'),('m,','m,','','',22,'jnj','Your Best Friend Name','km',' ','Male'),('kln','mm ','','',22,'srv','Your Best Friend Name','hhh','  ','Male'),('kln','mm ','','',22,'srv','Your Best Friend Name','hhh','  ','Male'),('nb','n ','','',21,'srv','Your Best Friend Name','kkb','  ','Male'),('z','z','','',22,'xx','Your Best Friend Name','ss','ss','Male'),('ss','','','',21,'s','Your Best Friend Name','ss','  ','Male'),('Swyam','','Srivastava','9838907453',20,'swyamsrv05@gmail.com','Your Best Friend Name','Harash','Ssrv@005','Male'),('sWYAM','','','',5454,'SDFGH','Your Pet Name','HH','  ','Other'),('swyam','','srivastava','9838907453',20,'swyamsri013@gmail.com','Your Best Friend Name','Harsh','ssss','Male');
/*!40000 ALTER TABLE `login_register` ENABLE KEYS */;
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
