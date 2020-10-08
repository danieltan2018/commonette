-- phpMyAdmin SQL Dump
-- version 4.7.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Jan 14, 2019 at 06:42 AM
-- Server version: 5.7.19
-- PHP Version: 7.1.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: 'questionnaire'
--
CREATE DATABASE IF NOT EXISTS `questionnaire` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `questionnaire`;

-- --------------------------------------------------------

--
-- Table structure for table `patient`
--
DROP TABLE IF EXISTS `questionnaire`;
CREATE TABLE IF NOT EXISTS `questionnaire` (
    `user_id` int(64) NOT NULL,
    `youtube_category` int(64) NOT NULL,
    `movie_genre` varchar(64) NOT NULL,
    `book_subject` varchar(64) NOT NULL,
    `artist` varchar(64) NOT NULL,
    `track` varchar(64) NOT NULL,
    `music_genre` varchar(64) NOT NULL,
    PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=100 DEFAULT CHARSET=utf8;