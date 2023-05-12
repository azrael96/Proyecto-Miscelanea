-- --------------------------------------------------------

--
-- Base de datos: `miscelanea`
--

-- --------------------------------------------------------
DROP DATABASE miscelanea;
COMMIT;

CREATE DATABASE miscelanea;
COMMIT;

USE miscelanea;
COMMIT;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `categoria`
--

CREATE TABLE categoria (
  `cat_ID` int NOT NULL,
  `cat_nombre` varchar(50) NOT NULL,
  `cat_descripcion` varchar(100) NOT NULL,
  `cat_activo` boolean NOT NULL
);
ALTER TABLE `categoria` ADD PRIMARY KEY (`cat_ID`);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario`
--

CREATE TABLE usuario (
    `usu_cedula` varchar(20) NOT NULL,
    `usu_nombre1` varchar(50) NOT NULL,
    `usu_nombre2` varchar(50) NOT NULL,
    `usu_apellido1` varchar(50) NOT NULL,
    `usu_apellido2` varchar(50) NOT NULL,
    `usu_direccion` varchar(50) NOT NULL,
    `usu_activo` boolean NOT NULL,
    `usu_telefono` varchar(32) NOT NULL,
    `usu_rol` varchar(50) NOT NULL,
    `usu_alias` varchar(50) NOT NULL,
    `usu_clave` varchar(50) NOT NULL
);
ALTER TABLE `usuario` ADD PRIMARY KEY (`usu_cedula`);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `producto`
--

CREATE TABLE producto (
    `pro_ID` int NOT NULL,
    `pro_nombre` varchar(50) NOT NULL,
    `pro_descripcion` varchar(100) NOT NULL,
    `pro_foto` MEDIUMBLOB NOT NULL,
    `pro_activo` boolean NOT NULL,
    `cat_ID_fk` int NOT NULL
);
ALTER TABLE `producto` ADD PRIMARY KEY (`pro_ID`);
ALTER TABLE `producto` ADD FOREIGN KEY (`cat_ID_fk`) REFERENCES categoria(cat_ID);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `caja`
--

CREATE TABLE caja (
    `caj_ID` int NOT NULL,
    `caj_fecha` date NOT NULL,
    `caj_val_apertura` double NOT NULL,
    `caj_val_cierre` double NOT NULL,
    `usu_cedula_fk` varchar(20) NOT NULL
);
ALTER TABLE `caja` ADD PRIMARY KEY (`caj_ID`);
ALTER TABLE `caja` ADD FOREIGN KEY (`usu_cedula_fk`) REFERENCES usuario(`usu_cedula`);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cliente`
--

CREATE TABLE cliente (
    `cli_cedula` varchar(20) NOT NULL,
    `cli_nombre` varchar(50) NOT NULL,
    `cli_nombre2` varchar(50) NOT NULL,
    `cli_apellido1` varchar(50) NOT NULL,
    `cli_apellido2` varchar(50) NOT NULL,
    `cli_telefono` varchar(32) NOT NULL,
    `cli_direccion` varchar(50) NOT NULL

);
ALTER TABLE `cliente` ADD PRIMARY KEY (`cli_cedula`);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `deuda`
--

CREATE TABLE deuda (
    `deu_ID` int NOT NULL,
    `deu_estado` varchar(50) NOT NULL,
    `deu_abono` double NOT NULL,
    `deu_saldo` double NOT NULL,
    `deu_total` double NOT NULL,
    `cli_cedula_fk` varchar(20) NOT NULL
);
ALTER TABLE `deuda` ADD PRIMARY KEY (`deu_ID`);
ALTER TABLE `deuda` ADD FOREIGN KEY (`cli_cedula_fk`) REFERENCES cliente(cli_cedula);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `gasto`
--

CREATE TABLE gasto (
    `gas_ID` int NOT NULL,
    `gas_descripcion` varchar(100) NOT NULL,
    `gas_valor` double NOT NULL,
    `caj_ID_fk` int NOT NULL
);
ALTER TABLE `gasto` ADD PRIMARY KEY (`gas_ID`);
ALTER TABLE `gasto` ADD FOREIGN KEY (`caj_ID_fk`) REFERENCES caja(caj_ID);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `factura`
--

CREATE TABLE factura (
    `fac_ID` int NOT NULL,
    `fac_tipo` varchar(50) NOT NULL,
    `fac_fecha` date NOT NULL,
    `fac_total` double NOT NULL,
    `caj_ID_fk` int NOT NULL,
    `cli_cedula_fk` varchar(20) NOT NULL
);
ALTER TABLE `factura` ADD PRIMARY KEY (`fac_ID`);
ALTER TABLE `factura` ADD FOREIGN KEY (`caj_ID_fk`) REFERENCES caja(caj_ID);
ALTER TABLE `factura` ADD FOREIGN KEY (`cli_cedula_fk`) REFERENCES cliente(cli_cedula);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `venta`
--

CREATE TABLE venta (
    `ven_ID` int NOT NULL,
    `ven_precio` int NOT NULL,
    `ven_cantidad` int NOT NULL,
    `fac_ID_fk` int NOT NULL,
    `pro_ID_fk` int NOT NULL
);
ALTER TABLE `venta` ADD PRIMARY KEY (`ven_ID`);
ALTER TABLE `venta` ADD FOREIGN KEY (`pro_ID_fk`) REFERENCES producto(pro_ID);
ALTER TABLE `venta` ADD FOREIGN KEY (`fac_ID_fk`) REFERENCES factura(fac_ID);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `abono`
--

CREATE TABLE abono (
    `abo_ID` int NOT NULL,
    `can_abono` double NOT NULL,
    `caj_ID_fk` int NOT NULL,
    `deu_ID_fk` int NOT NULL
);
ALTER TABLE `abono` ADD PRIMARY KEY (`abo_ID`);
ALTER TABLE `abono` ADD FOREIGN KEY (`caj_ID_fk`) REFERENCES caja(caj_ID);
ALTER TABLE `abono` ADD FOREIGN KEY (`deu_ID_fk`) REFERENCES deuda(deu_ID);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `servicio`
--

CREATE TABLE servicio (
    `ser_ID` int NOT NULL,
    `ser_nombre` varchar(50) NOT NULL,
    `ser_unitario` double NOT NULL,
    `ser_veces` int NOT NULL,
    `fac_ID_fk` int NOT NULL
);
ALTER TABLE `servicio` ADD PRIMARY KEY (`ser_ID`);
ALTER TABLE `servicio` ADD FOREIGN KEY (`fac_ID_fk`) REFERENCES factura(fac_ID);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `inventario`
--

CREATE TABLE inventario (
    `inv_ID` int NOT NULL,
    `inv_cantidad` int NOT NULL,
    `inv_costo` double NOT NULL,
    `pro_ID_fk` int NOT NULL
);
ALTER TABLE `inventario` ADD PRIMARY KEY (`inv_ID`);
ALTER TABLE `inventario` ADD FOREIGN KEY (`pro_ID_fk`) REFERENCES producto(pro_ID);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `stock`
--

CREATE TABLE stock (
    `sto_ID` int NOT NULL,
    `sto_cantidad` int NOT NULL,
    `sto_precio` double NOT NULL,
    `pro_ID_fk` int NOT NULL
);
ALTER TABLE `stock` ADD PRIMARY KEY (`sto_ID`);
ALTER TABLE `stock` ADD FOREIGN KEY (`pro_ID_fk`) REFERENCES producto(pro_ID);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pedido`
--

CREATE TABLE pedido (
    `ped_ID` int NOT NULL,
    `ped_unitario` double NOT NULL,
    `ped_cantidad` int NOT NULL,
    `ped_estado` varchar(50) NOT NULL,
    `pro_ID_fk` int NOT NULL
);
ALTER TABLE `pedido` ADD PRIMARY KEY (`ped_ID`);
ALTER TABLE `pedido` ADD FOREIGN KEY (`pro_ID_fk`) REFERENCES producto(pro_ID);

COMMIT;

-- --------------------------------------------------------

--
-- Usuarios iniales de la base de datos
--

INSERT INTO usuario VALUES ('1100121212', 'Jose', 'Andres', 'Santos','Delgado', 'Direccion', True, '1234567890', 'Admin', 'Admin', '1234');
INSERT INTO usuario VALUES ('1100121210', 'Luisa', '', 'Diaz','Perez', 'Direccion', True, '1234567890', 'Vendedor', 'Vendedor', '1234');
INSERT INTO caja VALUES (0, '1998-01-01', 0, 0, '1100121210');

COMMIT;

