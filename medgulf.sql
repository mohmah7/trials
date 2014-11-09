-- MySQL dump 10.13  Distrib 5.6.21, for osx10.9 (x86_64)
--
-- Host: localhost    Database: Medgulf
-- ------------------------------------------------------
-- Server version	5.6.21

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
-- Table structure for table `DIAGNOSIS`
--

DROP TABLE IF EXISTS `DIAGNOSIS`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `DIAGNOSIS` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ICDCODE` char(10) DEFAULT NULL,
  `DIAGNOSIS` char(30) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `DIAGNOSIS`
--

LOCK TABLES `DIAGNOSIS` WRITE;
/*!40000 ALTER TABLE `DIAGNOSIS` DISABLE KEYS */;
INSERT INTO `DIAGNOSIS` VALUES (1,NULL,'gastroentritis'),(2,'','Pneumonia'),(3,'','good'),(4,'','good'),(5,'','er'),(6,'','er'),(7,'','fg'),(8,'','TR'),(9,'','fever'),(10,'','jaundice'),(11,'','diarrhea'),(12,'','pneumonia'),(13,'','good'),(14,'','wife'),(15,'','good'),(16,'','hope'),(17,'','true');
/*!40000 ALTER TABLE `DIAGNOSIS` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `HOSPITALNAME`
--

DROP TABLE IF EXISTS `HOSPITALNAME`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `HOSPITALNAME` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `NAME` char(30) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `HOSPITALNAME`
--

LOCK TABLES `HOSPITALNAME` WRITE;
/*!40000 ALTER TABLE `HOSPITALNAME` DISABLE KEYS */;
INSERT INTO `HOSPITALNAME` VALUES (1,'AGH KHOBAR'),(2,'DOSSARY'),(3,'FAKHRY'),(4,'SALAMA'),(5,'AL YOUSEF'),(6,'ASTOON');
/*!40000 ALTER TABLE `HOSPITALNAME` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `PTNAME`
--

DROP TABLE IF EXISTS `PTNAME`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `PTNAME` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `FULL_NAME` char(20) NOT NULL,
  `AGE` int(11) DEFAULT NULL,
  `APPNUMBER` char(20) DEFAULT NULL,
  `VISITDATE` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `PTNAME`
--

LOCK TABLES `PTNAME` WRITE;
/*!40000 ALTER TABLE `PTNAME` DISABLE KEYS */;
INSERT INTO `PTNAME` VALUES (1,'Mohamed',34,NULL,NULL),(2,'sameh',33,NULL,NULL),(3,'shaimaa',223,NULL,NULL);
/*!40000 ALTER TABLE `PTNAME` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `PTNAME_DIAGNOSIS_HOSPITALNAME`
--

DROP TABLE IF EXISTS `PTNAME_DIAGNOSIS_HOSPITALNAME`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `PTNAME_DIAGNOSIS_HOSPITALNAME` (
  `PTNAME_id` int(11) DEFAULT NULL,
  `DIAGNOSIS_id` int(11) DEFAULT NULL,
  `HOSPITALNAME_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `PTNAME_DIAGNOSIS_HOSPITALNAME`
--

LOCK TABLES `PTNAME_DIAGNOSIS_HOSPITALNAME` WRITE;
/*!40000 ALTER TABLE `PTNAME_DIAGNOSIS_HOSPITALNAME` DISABLE KEYS */;
INSERT INTO `PTNAME_DIAGNOSIS_HOSPITALNAME` VALUES (10,0,NULL),(12,10,NULL),(13,11,4),(14,12,1),(15,13,2),(16,14,4),(1,15,1),(2,16,2),(3,17,4);
/*!40000 ALTER TABLE `PTNAME_DIAGNOSIS_HOSPITALNAME` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `date`
--

DROP TABLE IF EXISTS `date`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `date` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `db_name` char(25) DEFAULT NULL,
  `db_date` char(15) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `date`
--

LOCK TABLES `date` WRITE;
/*!40000 ALTER TABLE `date` DISABLE KEYS */;
INSERT INTO `date` VALUES (1,'date:manual date','2010-2-14'),(2,NULL,'2014-11-08');
/*!40000 ALTER TABLE `date` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2014-11-09 21:58:19
