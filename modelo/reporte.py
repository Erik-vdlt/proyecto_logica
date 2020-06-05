from reportlab.pdfgen import canvas
from reportlab.platypus.tables import Table
from reportlab.lib.units import mm
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import  green
from conexion.multiple import conjunto
from reportlab.lib import colors
from datetime import datetime as date

class plantilla:
    
    def titulo(self, c):
        c.setFont("Times-Roman",30)
        c.drawString(210,800,"Reporte de Mascota")
    
    def informacion_general(self, c):
        c.setFont("Times-Roman", 15)
        c.drawString(50, 750, "Nombre Clinica: ")
        c.drawString(50, 720, "Nombre Veterinario: ")
        c.drawString(50, 690, "Correo Veterinario: ")
        
    def tabla(self, datos, c):
        encabezados = [["Nombre", "Primer Apellido", "Sergundo Apellido", "Correo", "Nombre Mascota", "Tipo", "Peso"]]
        width,  height = A4
        tabla = Table(encabezados+datos, colWidths=30*mm)
        tabla.setStyle([("VALIGN", (0,0), (-1,-1), "MIDDLE"),
                ("ALIGN", (0,0), (-1,-1), "CENTER"),
                ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black), 
                ('FONT', (0,0), (-1,0), 'Times-Bold'), 
                ('FONTSIZE', (0,0),(-1,-1), 10)])
        tabla.wrapOn(c, width, height)
        tabla.drawOn(c, 0, 520)
        
    def generar_reporte(self, conexion):
        c = canvas.Canvas("reporte.pdf", pagesize = A4)
        c.setLineWidth(1)
        c.setStrokeColor(green)
        c.line(10, 799, 585, 799)
        c.setStrokeColor(green)
        c.line(10, 680, 585, 680)
        width, height = A4
        self.titulo(c)
        self.informacion_general(c)
        #importar informacion para la tabla
        datos = conjunto()
        datos.iniciar_conexion(conexion)
        self.tabla(datos.consulta_reporte(), c)
        fecha = date.today().strftime("%D")
        c.drawString(525, 685, fecha)
        c.showPage()
        c.save()
