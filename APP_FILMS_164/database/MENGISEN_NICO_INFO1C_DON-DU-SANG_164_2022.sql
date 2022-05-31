-- OM 2021.02.17
-- FICHIER MYSQL POUR FAIRE FONCTIONNER LES EXEMPLES
-- DE REQUETES MYSQL
-- Database: mengisen_nico_info1c_copie

-- Détection si une autre base de donnée du même nom existe

DROP DATABASE IF EXISTS mengisen_nico_info1c_copie;

-- Création d'un nouvelle base de donnée

CREATE DATABASE IF NOT EXISTS mengisen_nico_info1c_copie;

-- Utilisation de cette base de donnée

USE mengisen_nico_info1c_copie;
-- --------------------------------------------------------


--
-- Table structure for table `t_donneur`
--

CREATE TABLE `t_donneur` (
  `id_donneur` int(11) NOT NULL,
  `prenom` varchar(69) NOT NULL,
  `nom` varchar(69) NOT NULL,
  `adresse` varchar(69) NOT NULL,
  `mail` varchar(69) NOT NULL,
  `num_tel` varchar(69) NOT NULL,
  `date_naissance` date NOT NULL,
  `groupe_sanguin` varchar(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `t_donneur`
--
prenom, nom, adresse, mail, num_tel, date_naissance, groupe_sanguin
INSERT INTO `t_donneur` (`id_donneur`, `prenom`, `nom`, `adresse`, `mail`, `num_tel`, `date_naissance`, `groupe_sanguin`) VALUES
(1, 'Nicolas', 'Mangisson', '1296 Coppet', 'mangissonnnico@gmail.com', '078-894-22-08', '2004-05-25', 'O+'),
(2, 'Kachaw', 'Flash', '3482 Radiator Springs', 'flash.mcqueen@radspri.com', '079-991-11-72', '2006-06-14', 'AB-'),
(3, 'Se', 'Null', '1297 Founex', 'senull@bing.com', '075-637-29-62', '2023-05-25', 'B-'),
(4, 'Suisse', 'Roro', '1442 Montagny-pres-Yverdon', 'suisseroro@yahoo.ch', '079-109-01-02', '1291-08-01', 'A+');

-- --------------------------------------------------------

--
-- Table structure for table `t_donsang`
--

CREATE TABLE `t_donsang` (
  `id_donsang` int(11) NOT NULL,
  `fk_donneur` int(11) NOT NULL,
  `date_don` datetime NOT NULL,
  `quantite` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `t_donsang`
--

INSERT INTO `t_donsang` (`id_donsang`, `fk_donneur`, `date_don`, `quantite`) VALUES
(1, 3, '2022-05-04 00:00:00', 1),
(2, 1, '2022-05-04 00:00:00', 1),
(3, 3, '2022-05-04 00:00:00', 1),
(4, 2, '2022-05-04 00:00:00', 1);

-- --------------------------------------------------------

--
-- Table structure for table `t_pmedical`
--

CREATE TABLE `t_pmedical` (
  `id_pmedical` int(11) NOT NULL,
  `prenom` varchar(69) NOT NULL,
  `nom` varchar(69) NOT NULL,
  `adresse` varchar(69) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `t_pmedical`
--

INSERT INTO `t_pmedical` (`id_pmedical`, `prenom`, `nom`, `adresse`) VALUES
(1, 'Manon', 'Schiff', 'maschiff@chuv.ch'),
(2, 'Evelyn', 'McDonald', 'emcdo@chuv.ch'),
(3, 'Donald', 'Trompe', 'd.trompe@yandex.nk'),
(4, 'Peter', 'Griffin', 'p.griffin@famguy.eu');

-- --------------------------------------------------------

--
-- Table structure for table `t_receveur`
--

CREATE TABLE `t_receveur` (
  `id_receveur` int(11) NOT NULL,
  `prenom` varchar(69) NOT NULL,
  `nom` varchar(69) NOT NULL,
  `adresse` varchar(69) NOT NULL,
  `mail` varchar(69) NOT NULL,
  `numero_telephone` varchar(69) NOT NULL,
  `date_naissance` date NOT NULL,
  `groupe_sanguin` varchar(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `t_receveur`
--

INSERT INTO `t_receveur` (`id_receveur`, `prenom`, `nom`, `adresse`, `mail`, `numero_telephone`, `date_naissance`, `groupe_sanguin`) VALUES
(1, 'Driton', 'Selmanaj', '1860 Aigle', 'driselma@iglou.com', '076-634-93-45', '2008-09-04', 'O-'),
(2, 'Alketa', 'Leclere', '1110 Morges', 'aleclere@gmail.com', '079-294-85-23', '2003-02-24', 'AB+'),
(3, 'Jean-Marc', 'DuLac', '1222 Geneve', 'jmdulac@hotmail.ch', '079-349-29-54', '1960-01-15', 'AB-'),
(4, 'Olivier', 'Maquereau', '1003 Lausanne', 'om@zorba.ru', '078-742-47-94', '0666-01-01', 'O+');

-- --------------------------------------------------------

--
-- Table structure for table `t_transactionsang`
--

CREATE TABLE `t_transactionsang` (
  `id_transactionsang` int(11) NOT NULL,
  `fk_pmedical` int(11) NOT NULL,
  `date_sorti` datetime NOT NULL,
  `quantite` int(11) NOT NULL,
  `fk_receveur` int(11) NOT NULL,
  `groupe_sanguin` varchar(3) NOT NULL,
  `fk_donsang` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `t_transactionsang`
--

INSERT INTO `t_transactionsang` (`id_transactionsang`, `fk_pmedical`, `date_sorti`, `quantite`, `fk_receveur`, `groupe_sanguin`, `fk_donsang`) VALUES
(1, 2, '2022-05-04 00:00:00', 1, 2, 'B-', 3),
(2, 1, '2022-05-04 00:00:00', 1, 1, 'O-', 4),
(3, 3, '2022-05-04 00:00:00', 1, 4, 'AB+', 1),
(4, 4, '2022-05-04 00:00:00', 1, 3, 'AB-', 2);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `t_donneur`
--
ALTER TABLE `t_donneur`
  ADD PRIMARY KEY (`id_donneur`);

--
-- Indexes for table `t_donsang`
--
ALTER TABLE `t_donsang`
  ADD PRIMARY KEY (`id_donsang`),
  ADD KEY `fk_donneur` (`fk_donneur`);

--
-- Indexes for table `t_pmedical`
--
ALTER TABLE `t_pmedical`
  ADD PRIMARY KEY (`id_pmedical`);

--
-- Indexes for table `t_receveur`
--
ALTER TABLE `t_receveur`
  ADD PRIMARY KEY (`id_receveur`);

--
-- Indexes for table `t_transactionsang`
--
ALTER TABLE `t_transactionsang`
  ADD PRIMARY KEY (`id_transactionsang`),
  ADD KEY `fk_pmedical` (`fk_pmedical`,`fk_receveur`,`fk_donsang`),
  ADD KEY `fk_donsang` (`fk_donsang`),
  ADD KEY `t_transactionsang_ibfk_2` (`fk_receveur`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `t_donneur`
--
ALTER TABLE `t_donneur`
  MODIFY `id_donneur` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
--
-- AUTO_INCREMENT for table `t_donsang`
--
ALTER TABLE `t_donsang`
  MODIFY `id_donsang` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
--
-- AUTO_INCREMENT for table `t_pmedical`
--
ALTER TABLE `t_pmedical`
  MODIFY `id_pmedical` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
--
-- AUTO_INCREMENT for table `t_receveur`
--
ALTER TABLE `t_receveur`
  MODIFY `id_receveur` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
--
-- AUTO_INCREMENT for table `t_transactionsang`
--
ALTER TABLE `t_transactionsang`
  MODIFY `id_transactionsang` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
--
-- Constraints for dumped tables
--

--
-- Constraints for table `t_donsang`
--
ALTER TABLE `t_donsang`
  ADD CONSTRAINT `t_donsang_ibfk_1` FOREIGN KEY (`fk_donneur`) REFERENCES `t_donneur` (`id_donneur`);

--
-- Constraints for table `t_transactionsang`
--
ALTER TABLE `t_transactionsang`
  ADD CONSTRAINT `t_transactionsang_ibfk_1` FOREIGN KEY (`fk_pmedical`) REFERENCES `t_pmedical` (`id_pmedical`),
  ADD CONSTRAINT `t_transactionsang_ibfk_2` FOREIGN KEY (`fk_receveur`) REFERENCES `t_receveur` (`id_receveur`),
  ADD CONSTRAINT `t_transactionsang_ibfk_3` FOREIGN KEY (`fk_donsang`) REFERENCES `t_donsang` (`id_donsang`);
