import mysql.connector

valEscacez = 5

class DatabaseLink():
    def __init__(self):
        self.cursor = ""
        self.state = ""
        self.database = ""

    def _connect(self):
        self.database = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="safe&SOUND96",
            database="miscelanea"
        )
        self.cursor = self.database.cursor()

    def _disconnect(self):
        self.database.close()

    def _searchMax(self, table, cod, min):
        query = "SELECT MAX("+cod+"_ID) FROM "+table
        self.cursor.execute(query)

        maxCode = self.cursor.fetchone()
        maxCode = maxCode[0]
        if maxCode == None:
            maxCode = min
        else:
            maxCode += 1
        return maxCode

    def conexionStatus(self):
        try:
            self._connect()
            self.state = "Conectado al servidor correctamente"
            self._disconnect()
        except:
            self.state = "No esta conectado al servidor"
        return self.state

    def loginUser(self, username, password):
        self._connect()
        query ="SELECT usu_activo, usu_rol, usu_cedula "\
               "FROM usuario "\
               "WHERE usu_alias = %s AND usu_clave = %s AND usu_activo = True"
        self.cursor.execute(query, (username, password))
        userInfo = self.cursor.fetchone()
        self._disconnect()
        return userInfo

    def getListCategoria(self):
        self._connect()
        query = "SELECT * "\
                "FROM categoria "\
                "WHERE cat_activo = %s"
        self.cursor.execute(query, (True,))
        items = self.cursor.fetchall()
        self._disconnect()
        return items

    def getNamesCategoria(self):
        self._connect()
        query = "SELECT cat_ID, cat_nombre "\
                "FROM categoria "\
                "WHERE cat_activo = %s"
        self.cursor.execute(query, (True,))
        items = self.cursor.fetchall()
        self._disconnect()
        return items

    def getListUsuario(self):
        self._connect()
        query = "SELECT usu_cedula, usu_nombre1, usu_nombre2, usu_apellido1, usu_apellido2, usu_direccion, usu_telefono, usu_rol, usu_alias, usu_clave "\
                "FROM usuario "\
                "WHERE usu_activo = %s"
        self.cursor.execute(query, (True,))
        items = self.cursor.fetchall()
        self._disconnect()
        return items

    def getListProducto(self, cat, nom):
        self._connect()
        para = ()
        query = "SELECT p.pro_ID, p.pro_nombre, p.pro_descripcion, c.cat_nombre "\
                "FROM producto AS p "\
                "INNER JOIN categoria AS c "\
                "ON c.cat_ID = p.cat_ID_fk "\
                "WHERE p.pro_activo = True "

        if cat != "":
            query += "AND c.cat_nombre = %s "
            para = para + (cat,)
        if nom != "":
            query += "AND p.pro_nombre = %s "
            para = para + (nom,)

        self.cursor.execute(query, para)
        items = self.cursor.fetchall()
        self._disconnect()
        return items

    def getOneProducto(self, cod):
        self._connect()
        query = "SELECT p.pro_nombre, p.pro_descripcion, c.cat_nombre "\
                "FROM producto AS p "\
                "INNER JOIN categoria AS c "\
                "ON c.cat_ID = p.cat_ID_fk "\
                "WHERE p.pro_ID = %s "
        self.cursor.execute(query, (cod,))
        item = self.cursor.fetchone()
        self._disconnect()
        return item

    def getListProductoEscacez(self):
        self._connect()

        query = "SELECT p.pro_ID, p.pro_nombre, p.pro_descripcion, c.cat_nombre "\
                "FROM producto AS p "\
                "INNER JOIN categoria AS c "\
                "ON c.cat_ID = p.cat_ID_fk "\
                "WHERE p.pro_activo = True "
        self.cursor.execute(query)

        allItems = self.cursor.fetchall()
        selectedItems = ()
        for i in allItems:
            query = "SELECT SUM(inv_cantidad) " \
                    "FROM inventario " \
                    "WHERE pro_ID_fk = %s "
            self.cursor.execute(query, (i[0],))
            cant = self.cursor.fetchone()

            global valEscacez
            if cant[0] == None or cant[0] < valEscacez:
                selectedItems = selectedItems + (i,)
        self._disconnect()
        return selectedItems

    def getCantTotalInventario(self, cod):
        self._connect()
        query = "SELECT SUM(inv_cantidad) " \
                "FROM inventario " \
                "WHERE pro_ID_fk = %s "
        self.cursor.execute(query, (cod,))
        cant = self.cursor.fetchone()
        self._disconnect()
        if cant[0] == None:
            return 0
        else:
            return cant[0]

    def getListPedido(self):
        self._connect()
        query = "SELECT p.ped_ID, pr.pro_nombre, p.ped_cantidad, p.ped_unitario "\
                "FROM pedido as p " \
                "INNER JOIN producto AS pr "\
                "ON pr.pro_ID = p.pro_ID_fk " \
                "WHERE ped_estado = %s"
        self.cursor.execute(query, ("En Proceso",))
        items = self.cursor.fetchall()
        self._disconnect()
        return items

    def getListInventario(self):
        self._connect()
        query = "SELECT p.pro_nombre, i.inv_cantidad, i.inv_costo, i.pro_ID_fk "\
                "FROM inventario as i " \
                "INNER JOIN producto AS p "\
                "ON p.pro_ID = i.pro_ID_fk "
        self.cursor.execute(query)
        items = self.cursor.fetchall()
        self._disconnect()
        return items

    def addCategoria(self, name, description):
        self._connect()
        cod = self._searchMax("categoria", "cat", 200000)
        query = "INSERT INTO categoria "\
                "VALUES (%s, %s, %s, True)"
        self.cursor.execute(query, (cod, name, description))
        self.database.commit()
        self._disconnect()

    def addUsuario(self, name1, name2, ape1, ape2, ced, dir, tel, rol, nick, con):
        self._connect()
        query = "INSERT INTO usuario "\
                "VALUES (%s, %s, %s, %s, %s, %s, True, %s, %s ,%s, %s)"
        self.cursor.execute(query, (ced, name1, name2, ape1, ape2, dir, tel, rol, nick, con))
        self.database.commit()
        self._disconnect()

    def addProducto(self, name, desc, foto, cat):
        self._connect()
        cod = self._searchMax("producto", "pro", 300000)
        query = "INSERT INTO producto "\
                "VALUES (%s, %s, %s, %s, True, %s)"
        self.cursor.execute(query, (cod, name, desc, foto, cat))

        codStock = self._searchMax("stock", "sto", 600000)
        query = "INSERT INTO stock "\
                "VALUES (%s, %s, %s, %s)"
        self.cursor.execute(query, (codStock, 0, 0, cod))

        self.database.commit()
        self._disconnect()

    def addPedido(self, cost, cant, prod):
        self._connect()
        cod = self._searchMax("pedido", "ped", 400000)
        query = "INSERT INTO pedido "\
                "VALUES (%s, %s, %s, 'En Proceso', %s)"
        self.cursor.execute(query, (cod, cost, cant, prod))
        self.database.commit()
        self._disconnect()

    def addInventario(self, codigoPed):
        self._connect()
        query = "SELECT ped_unitario, ped_cantidad, pro_ID_fk "\
                "FROM pedido " \
                "WHERE ped_ID = %s"
        self.cursor.execute(query, (codigoPed,))
        items = self.cursor.fetchone()

        cod = self._searchMax("inventario", "inv", 500000)
        can = items[0]
        cos = items[1]
        pro = items[2]

        query = "INSERT INTO inventario " \
                "VALUES (%s, %s, %s, %s)"
        self.cursor.execute(query, (cod, cos, can, pro))
        self.database.commit()
        self._disconnect()

    def editCategoria(self, cod, name, description):
        self._connect()
        query = "UPDATE categoria "\
                "SET cat_nombre = %s, cat_descripcion = %s WHERE cat_ID = %s"
        self.cursor.execute(query, (name, description, cod))
        self.database.commit()
        self._disconnect()

    def editUsuario(self, ced, name1, name2, ape1, ape2, dir, tel, rol, nick, con):
        self._connect()
        query = "UPDATE usuario "\
                "SET usu_nombre1 = %s, usu_nombre2 = %s, usu_apellido1 = %s, usu_apellido2 = %s, "\
                "usu_direccion = %s, usu_telefono = %s, usu_rol = %s, usu_alias = %s, usu_clave = %s "\
                "WHERE usu_cedula = %s"
        self.cursor.execute(query, (name1, name2, ape1, ape2, dir, tel, rol, nick, con, ced))
        self.database.commit()
        self._disconnect()

    def editProducto(self, cod, name, desc, foto, cat):
        self._connect()
        query = "UPDATE producto "\
                "SET pro_nombre = %s, pro_descripcion = %s, pro_foto = %s, cat_ID_fk = %s "\
                "WHERE pro_ID = %s"
        self.cursor.execute(query, (name, desc, foto, cat, cod))
        self.database.commit()
        self._disconnect()

    def delCategoria(self, cod):
        self._connect()
        query = "SELECT * "\
                "FROM producto "\
                "WHERE cat_ID_fk = %s"
        self.cursor.execute(query, (cod,))
        children = self.cursor.fetchall()

        if len(children) != 0:
            query = "UPDATE categoria "\
                    "SET cat_activo = %s "\
                    "WHERE cat_ID = %s"
            self.cursor.execute(query, (False, cod))
            self.database.commit()
        else:
            query = "DELETE FROM categoria "\
                    "WHERE cat_ID = %s"
            self.cursor.execute(query, (cod,))
            self.database.commit()
        self._disconnect()

    ##check if need select all
    def delUsuario(self, cod):
        self._connect()
        query = "SELECT * "\
                "FROM caja "\
                "WHERE usu_cedula_fk = %s"
        self.cursor.execute(query, (cod,))
        children = self.cursor.fetchall()

        if len(children) != 0:
            query = "UPDATE usuario "\
                    "SET usu_activo = %s "\
                    "WHERE usu_cedula = %s"
            self.cursor.execute(query, (False, cod))
            self.database.commit()
        else:
            query = "DELETE FROM usuario "\
                    "WHERE usu_cedula = %s"
            self.cursor.execute(query, (cod,))
            self.database.commit()
        self._disconnect()

    def delProducto(self, cod):
        self._connect()
        query = "UPDATE producto "\
                "SET pro_activo = %s "\
                "WHERE pro_ID = %s"
        self.cursor.execute(query, (False, cod))
        self.database.commit()
        self._disconnect()

    def changeEstadoPedido(self, cod, estado):
        self._connect()
        query = "UPDATE pedido " \
                "SET ped_estado = %s " \
                "WHERE ped_ID = %s"
        self.cursor.execute(query, (estado, cod))
        self.database.commit()
        self._disconnect()

    def getFotoProducto(self, cod):
        self._connect()
        query = "SELECT pro_foto "\
                "FROM producto "\
                "WHERE pro_ID = %s"
        self.cursor.execute(query, (cod,))
        item = self.cursor.fetchone()
        self._disconnect()
        return item

    def getListProductoInventario(self, cod):
        self._connect()
        query = "SELECT i.inv_ID, p.pro_nombre, i.inv_cantidad, i.inv_costo "\
                "FROM inventario as i "\
                "INNER JOIN producto AS p " \
                "ON p.pro_ID = i.pro_ID_fk " \
                "WHERE i.pro_ID_fk = %s " \
                "AND i.inv_cantidad != 0 "

        self.cursor.execute(query, (cod,))
        items = self.cursor.fetchall()
        self._disconnect()
        return items

    def getCantStock(self, cod):
        self._connect()
        query = "SELECT sto_cantidad, sto_precio, sto_ID "\
                "FROM stock "\
                "WHERE pro_ID_fk = %s "
        self.cursor.execute(query, (cod,))
        cant = self.cursor.fetchone()
        self._disconnect()

        if cant == None:
            return [0,0,0]
        else:
            return cant

    def editStock(self, cod, can, val, inv):
        self._connect()
        query = "UPDATE stock "\
                "SET sto_cantidad = (sto_cantidad + %s), sto_precio = %s "\
                "WHERE sto_ID = %s"
        self.cursor.execute(query, (can, val, cod))

        query = "UPDATE inventario "\
                "SET inv_cantidad = (inv_cantidad - %s) "\
                "WHERE inv_ID = %s"
        self.cursor.execute(query, (can, inv))
        self.database.commit()

        self._disconnect()

    def getCliente(self, cedula):
        self._connect()
        query = "SELECT cli_nombre, cli_nombre2, cli_apellido1, cli_apellido2, cli_telefono, cli_direccion "\
                "FROM cliente "\
                "WHERE cli_cedula = %s "
        self.cursor.execute(query, (cedula,))
        cant = self.cursor.fetchone()
        self._disconnect()
        return cant

    def addCliente(self, name1, name2, ape1, ape2, ced, dir, tel):
        self._connect()
        query = "INSERT INTO cliente "\
                "VALUES (%s, %s, %s, %s, %s, %s, %s)"
        self.cursor.execute(query, (ced, name1, name2, ape1, ape2, tel, dir))
        self.database.commit()
        self._disconnect()

    def addFactura(self, tip, date, tot, caj, cli):
        self._connect()
        cod = self._searchMax("factura", "fac", 800000)
        query = "INSERT INTO factura "\
                "VALUES (%s, %s, %s, %s, %s, %s)"
        self.cursor.execute(query, (cod, tip, date, tot, caj, cli))
        self.database.commit()
        self._disconnect()
        return cod

    def addDeuda(self, met, abo, sal, tot, cli):
        self._connect()
        cod = self._searchMax("deuda", "deu", 900000)
        query = "INSERT INTO deuda "\
                "VALUES (%s, %s, %s, %s, %s, %s)"
        self.cursor.execute(query, (cod, met, abo, sal, tot, cli))
        self.database.commit()
        self._disconnect()
        return cod

    def addVenta(self, precio, cant, fac, pro, sto):
        self._connect()
        cod = self._searchMax("venta", "ven", 900000)
        query = "INSERT INTO venta "\
                "VALUES (%s, %s, %s, %s, %s)"
        self.cursor.execute(query, (cod, precio, cant, fac, pro))

        query = "UPDATE stock "\
                "SET sto_cantidad = (sto_cantidad - %s) "\
                "WHERE sto_ID = %s"
        self.cursor.execute(query, (cant, sto))

        self.database.commit()
        self._disconnect()

    def cedulaDontExist(self, cod):
        self._connect()
        query = "SELECT usu_cedula "\
                "FROM usuario "\
                "WHERE usu_cedula = %s"
        self.cursor.execute(query, (cod,))
        item = self.cursor.fetchone()
        self._disconnect()
        if item != None:
            return False
        else:
            return True

    def getListDeuda(self):
        self._connect()
        query = "SELECT deu_ID, cli_cedula_fk, deu_saldo, deu_total, deu_abono " \
                "FROM deuda " \
                "WHERE deu_estado = %s "
        self.cursor.execute(query, ("En Deuda",))
        items = self.cursor.fetchall()
        self._disconnect()
        return items

    def editDeuda(self, cod, abono, saldo, caj):
        self._connect()

        estado = "En Deuda"
        if (saldo - abono) == 0:
            estado = "Pagado"

        query = "UPDATE deuda "\
                "SET deu_estado = %s, deu_abono = (deu_abono + %s), deu_saldo = (deu_saldo - %s) "\
                "WHERE deu_ID = %s "
        self.cursor.execute(query, (estado, abono, abono, cod))
        self.database.commit()

        cod_abo = self._searchMax("abono", "abo", 900000)
        query = "INSERT INTO abono " \
                "VALUES (%s, %s, %s, %s)"
        self.cursor.execute(query, (cod_abo, abono, caj, cod))
        self.database.commit()

        self._disconnect()

    def addServicio(self, nom, val, cant, factura):
        self._connect()
        cod = self._searchMax("servicio", "ser", 110000)
        query = "INSERT INTO servicio "\
                "VALUES (%s, %s, %s, %s, %s)"
        self.cursor.execute(query, (cod, nom, val, cant, factura))
        self.database.commit()
        self._disconnect()

    def getListGastos(self, caja):
        self._connect()
        query = "SELECT gas_descripcion, gas_valor "\
                "FROM gasto "\
                "WHERE caj_ID_fk = %s "
        self.cursor.execute(query, (caja, ))
        items = self.cursor.fetchall()
        self._disconnect()
        return items

    def addGastos(self, des, val, caj):
        self._connect()
        cod = self._searchMax("gasto", "gas", 120000)

        query = "INSERT INTO gasto "\
                "VALUES (%s, %s, %s, %s)"
        self.cursor.execute(query, (cod, des, val, caj))
        self.database.commit()
        self._disconnect()

    def getUsuario(self, ced):
        self._connect()
        query = "SELECT usu_cedula, usu_nombre1, usu_nombre2, usu_apellido1, usu_apellido2, usu_direccion, usu_telefono, usu_rol, usu_alias "\
                "FROM usuario "\
                "WHERE usu_cedula = %s"
        self.cursor.execute(query, (ced,))
        items = self.cursor.fetchone()
        self._disconnect()
        return items

    def addCaja(self, date, ced):
        self._connect()
        cod = self._searchMax("caja", "caj", 000000)
        query = "SELECT caj_val_cierre "\
                "FROM caja "\
                "ORDER BY caj_ID "\
                "DESC LIMIT 1; "

        self.cursor.execute(query)
        apertura = self.cursor.fetchone()
        cierre = 0

        query = "INSERT INTO caja "\
                "VALUES (%s, %s, %s, %s, %s)"
        self.cursor.execute(query, (cod, date, apertura[0], cierre, ced))
        self.database.commit()
        self._disconnect()
        return (cod, apertura[0])

    def cerrarCaja(self, caja, apertura):
        self._connect()
        cierre = apertura
        query = "SELECT SUM(gas_valor) FROM gasto WHERE caj_ID_fk = %s"
        self.cursor.execute(query, (caja,))
        totGasto = self.cursor.fetchone()

        query = "SELECT SUM(fac_total) FROM factura WHERE caj_ID_fk = %s AND fac_tipo != %s "
        self.cursor.execute(query, (caja, "Deuda"))
        totFactura = self.cursor.fetchone()

        query = "SELECT SUM(can_abono) FROM abono WHERE caj_ID_fk = %s "
        self.cursor.execute(query, (caja,))
        totAbono = self.cursor.fetchone()

        if totGasto[0] == None:
            totGasto = (0,)
        if totFactura[0] == None:
            totFactura = (0,)
        if totAbono[0] == None:
            totAbono = (0,)

        cierre = cierre - totGasto[0] + totFactura[0] + totAbono[0]

        query = "UPDATE caja "\
                "SET caj_val_cierre = %s "\
                "WHERE caj_ID = %s "
        self.cursor.execute(query, (cierre, caja))
        self.database.commit()
        self._disconnect()

    def cierreActual(self, caja, apertura):
        self._connect()
        cierre = apertura
        query = "SELECT SUM(gas_valor) FROM gasto WHERE caj_ID_fk = %s"
        self.cursor.execute(query, (caja,))
        totGasto = self.cursor.fetchone()

        query = "SELECT SUM(fac_total) FROM factura WHERE caj_ID_fk = %s AND fac_tipo != %s "
        self.cursor.execute(query, (caja, "Deuda"))
        totFactura = self.cursor.fetchone()

        query = "SELECT SUM(can_abono) FROM abono WHERE caj_ID_fk = %s "
        self.cursor.execute(query, (caja,))
        totAbono = self.cursor.fetchone()

        if totGasto[0] == None:
            totGasto = (0, )
        if totFactura[0] == None:
            totFactura = (0, )
        if totAbono[0] == None:
            totAbono = (0, )

        cierre = cierre - totGasto[0] + totFactura[0] + totAbono[0]
        self._disconnect()
        return cierre

    def getInfoFactura(self, facID):
        self._connect()
        query = "SELECT f.cli_cedula_fk, f.fac_fecha, f.fac_total, c.cli_nombre, c.cli_nombre2, c.cli_apellido1, " \
                "c.cli_apellido2, c.cli_telefono, c.cli_direccion, u.usu_nombre1, u.usu_nombre2, u.usu_apellido1, " \
                "u.usu_apellido2 " \
                "FROM factura as f " \
                "INNER JOIN cliente AS c " \
                "ON c.cli_cedula = f.cli_cedula_fk " \
                "INNER JOIN caja AS cj " \
                "ON cj.caj_ID = f.caj_ID_fk " \
                "INNER JOIN usuario AS u " \
                "ON u.usu_cedula = cj.usu_cedula_fk " \
                "WHERE f.fac_ID = %s "
        self.cursor.execute(query, (facID,))
        factInfo = self.cursor.fetchone()

        query = "SELECT p.pro_nombre, v.ven_precio, ven_cantidad " \
                "FROM venta AS v " \
                "INNER JOIN producto AS p " \
                "ON p.pro_ID = v.pro_ID_fk " \
                "WHERE v.fac_ID_fk = %s "
        self.cursor.execute(query, (facID,))
        factVentas = self.cursor.fetchall()

        self._disconnect()
        fact = [factInfo, factVentas]
        return fact

    def getInfoFacturaSer(self, facID):
        self._connect()
        query = "SELECT f.cli_cedula_fk, f.fac_fecha, f.fac_total, c.cli_nombre, c.cli_nombre2, c.cli_apellido1, " \
                "c.cli_apellido2, c.cli_telefono, c.cli_direccion, u.usu_nombre1, u.usu_nombre2, u.usu_apellido1, " \
                "u.usu_apellido2 " \
                "FROM factura as f " \
                "INNER JOIN cliente AS c " \
                "ON c.cli_cedula = f.cli_cedula_fk " \
                "INNER JOIN caja AS cj " \
                "ON cj.caj_ID = f.caj_ID_fk " \
                "INNER JOIN usuario AS u " \
                "ON u.usu_cedula = cj.usu_cedula_fk " \
                "WHERE f.fac_ID = %s "
        self.cursor.execute(query, (facID,))
        factInfo = self.cursor.fetchone()

        query = "SELECT s.ser_nombre, s.ser_unitario, s.ser_veces " \
                "FROM servicio AS s " \
                "WHERE s.fac_ID_fk = %s "
        self.cursor.execute(query, (facID,))
        factVentas = self.cursor.fetchall()

        self._disconnect()
        fact = [factInfo, factVentas]
        return fact