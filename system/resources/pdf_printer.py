from fpdf import FPDF

class PDF(FPDF):
    def __init__(self):
        super().__init__()
    def header(self):
        self.set_font('Arial', '', 12)
        self.image("images/images/Banner.png", x=None, y=None, w=180, h=45, type='PNG', link='')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', '', 12)
        self.cell(0, 8, f'Página {self.page_no()}', 0, 0, 'C')

def makeFacturaPDF(fact, cod):
    ch = 10
    factInfo = fact[0]
    ventas = fact[1]
    cliente = factInfo[3]+" "+factInfo[4]+" "+factInfo[5]+" "+factInfo[6]
    cedula = factInfo[0]
    telefono = factInfo[7]
    fecha = str(factInfo[1])
    direccion = factInfo[8]
    vendedor = factInfo[9]+" "+factInfo[10]+" "+factInfo[11]+" "+factInfo[12]
    total = str(factInfo[2])

    # Generate PDF
    pdf = PDF()

    pdf.add_page()
    pdf.set_font("Arial", "B", 24)
    pdf.cell(0, 30, "Factura", 0, 1, "C")

    pdf.set_font("Arial", "B", 14)
    pdf.cell(25, 5, "Cliente: ")
    pdf.set_font("Arial", "", 12)
    pdf.cell(0, 5, cliente, 0, 1, "L")

    pdf.cell(0, 5, "", 0, 1)

    pdf.set_font("Arial", "B", 14)
    pdf.cell(25, 5, "Cedula: ")
    pdf.set_font("Arial", "", 12)
    pdf.cell(75, 5, cedula, 0, 0, "L")

    pdf.set_font("Arial", "B", 14)
    pdf.cell(28, 5, "Fecha: ")
    pdf.set_font("Arial", "", 12)
    pdf.cell(75, 5, fecha, 0, 1, "L")

    pdf.cell(0, 5, "", 0, 1)

    pdf.set_font("Arial", "B", 14)
    pdf.cell(25, 5, "Telefono: ")
    pdf.set_font("Arial", "", 12)
    pdf.cell(75, 5, telefono, 0, 0, "L")

    pdf.set_font("Arial", "B", 14)
    pdf.cell(28, 5, "Direccion: ")
    pdf.set_font("Arial", "", 12)
    pdf.cell(75, 5, direccion, 0, 1, "L")

    pdf.cell(0, 10, "", 0, 1)

    # Table Header
    pdf.set_font('Arial', 'B', 14)
    pdf.cell(120, ch, 'Productos', "B", 0, 'L')
    pdf.cell(20, ch, 'Cant', "B", 0, 'C')
    pdf.cell(20, ch, 'Val', "B", 0, 'C')
    pdf.cell(20, ch, 'Total', "B", 1, 'C')

    # Table contents
    pdf.set_font('Arial', '', 14)
    for i in range(0, len(ventas)):
        pdf.cell(120, ch, str(ventas[i][0]), 0, 0, 'L')
        pdf.cell(20, ch, str(ventas[i][1]), 0, 0, 'C')
        pdf.cell(20, ch, str(ventas[i][2]), 0, 0, 'C')
        pdf.cell(20, ch, str(ventas[i][1]*ventas[i][2]), 0, 1, 'C')

    pdf.cell(0, 10, "", 0, 1)

    pdf.set_font("Arial", "B", 14)
    pdf.cell(28, 5, "Vendedor: ")
    pdf.set_font("Arial", "", 12)
    pdf.cell(110, 5, vendedor, 0, 0, "L")

    pdf.set_font("Arial", "B", 14)
    pdf.cell(15, 5, "Total: ")
    pdf.set_font("Arial", "", 14)
    pdf.cell(25, 5, total, 0, 1, "R")

    pdf.cell(0, 5, "", 0, 1)

    pdf.output(f'./facturas/fac'+str(cod)+'.pdf')