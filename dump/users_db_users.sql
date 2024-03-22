-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: users_db
-- ------------------------------------------------------
-- Server version	8.0.36

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
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(100) NOT NULL,
  `last_name` varchar(100) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'Shane','Nosack','sarus333@yahoo.com','$2b$12$lZGaZ3KuNWXnfuVeGB1OU.OMIojunZEctqOLHPeSi24T20RGTqHLy','2024-03-20 21:45:07','2024-03-20 21:45:07'),(2,'Shane','Nosack','sarus333@yahoo.com','$2b$12$HrALjUY.d2Cuet1CRlVfk.C8SYUPEa3LUIrTR5oPvMn5NqGX3Vjzu','2024-03-20 22:03:01','2024-03-20 22:03:01'),(3,'Shane','Nosack','sarus333@yahoo.com','$2b$12$P3Kr.NBodyDXHC/tHe3VOueAPENAPqqZBtBBf1rmKA4T8gCLaFtra','2024-03-20 22:08:09','2024-03-20 22:08:09'),(4,'Bob','Evans','mashedpotatoman@taters.org','$2b$12$JYnWjG6ylBYqrYA3EMOq/uprIprREaYaK5TZmUJsa94BFR2UJcOjG','2024-03-20 22:29:21','2024-03-20 22:29:21'),(5,'Shane','Nosack','sarus333@yahoo.com','$2b$12$wwvhDsuAKZDHp9SedxNfvuid1YwJrhHjbs/sbD3GhD5.mcvu4exxe','2024-03-21 18:34:46','2024-03-21 18:34:46'),(6,'Brian','Nosack','driftingshade@hotmail.com','$2b$12$opPbCGNS7e5k6rCpJx8K6ulhtx2BllBzIRvfVVqPA7sLA/3ZlVqXG','2024-03-21 18:56:45','2024-03-21 18:56:45'),(7,'Carrie','Nosack','carriescreativetouch@yahoo.com','$2b$12$.stDSMrw.bvqVT9/8QkYs.qRMEjndmVeJoQpSILWJ78l0gYyEgmli','2024-03-21 19:12:23','2024-03-21 19:12:23');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-03-21 19:41:12
