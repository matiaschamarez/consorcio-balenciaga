from django.contrib import admin
from .models import Expensa
# Register your models here.
from .models import Empleado
from applications.gasto_administracion.models import GastoAdministracion
from applications.unidades.models import Unidad
from applications.empleado.models import Empleado
# Register your models here.
from django.urls import reverse
from django.utils.html import format_html
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib import colors

class Modelo_admin(admin.ModelAdmin):
    list_display = ('fecha', 'mi_boton')

    def mi_boton(self, obj):
        url = reverse('expensas')  # Reemplaza 'tu_aplicacion' por el nombre de tu aplicación
        return format_html('<a class="button" href="{}">expensas</a>', url)

    mi_boton.short_description = "Acceder a expensas"
    
    def clean_data_text(text):
        clean_text = re.sub('<.*?>', '', text)
        clean_text = clean_text.replace('&nbsp;', ' ')
        return clean_text
    
    def export_selected_to_pdf(modeladmin, request, queryset):
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="expensas.pdf"'

        doc = SimpleDocTemplate(response, pagesize=letter)
        elements = []

        # Estilo del encabezado
        style = [
            ('BACKGROUND', (0, 0), (-1, 0), colors.lightskyblue),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ]

        # Crear un estilo ParagraphStyle para el encabezado
        header_style = ParagraphStyle(
            'HeaderStyle',
            parent=getSampleStyleSheet()['Normal'],
            fontName='Helvetica-Bold',
            fontSize=16,
            alignment=1,  # 1 corresponde a la alineación centrada (0 izquierda, 2 derecha)
            textColor=colors.black,
            leading=16,
        )

        # Encabezado del PDF
        header_text = ""
        header_paragraph = Paragraph(header_text, header_style)
        elements.append(header_paragraph)

        # Datos de los empleados en una tabla
        data = []
        data.append(["Propietario", "Numero de unidad", "Monto a pagar"])

        # Agregar filas con los datos
        data.append(["Jose Ruiz","1","108.000"])
        data.append(["Mercedes Fernandez",2,"108.000"])
        data.append(["Esteban Rodriguez",3,"108.000"])
        data.append(["Lourdes Rios", "4", "108.000"])
        data.append(["Osvaldo Matesiac",5,"108.000"])

        # Crear una tabla con los datos y aplicar estilos
        table = Table(data)
        table.setStyle(TableStyle(style))

        elements.append(table)

        doc.build(elements)

        return response

    export_selected_to_pdf.short_description = "Exportar expensas seleccionadas a PDF"


    def export_selected_to_pdf_(modeladmin, request, queryset):
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="expensas.pdf"'

        doc = SimpleDocTemplate(response, pagesize=letter)
        elements = []

        # Estilo del encabezado
        style = [
            ('BACKGROUND', (0, 0), (-1, 0), colors.lightskyblue),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ]

        # Crear un estilo ParagraphStyle para el encabezado
        header_style = ParagraphStyle(
            'HeaderStyle',
            parent=getSampleStyleSheet()['Normal'],
            fontName='Helvetica-Bold',
            fontSize=16,
            alignment=1,  # 1 corresponde a la alineación centrada (0 izquierda, 2 derecha)
            textColor=colors.black,
            leading=16,
        )

        # Encabezado del PDF
        header_text = ""
        header_paragraph = Paragraph(header_text, header_style)
        elements.append(header_paragraph)

        # Datos de los empleados en una tabla
        data = []
        data.append(["Propietario", "Numero de unidad", "Monto a pagar"])

        # Agregar filas con los datos
        data.append(["Jose Ruiz","1","90.000"])
        data.append(["Mercedes Fernandez",2,"90.000"])
        data.append(["Esteban Rodriguez",3,"90.000"])
        data.append(["Lourdes Rios", "4", "90.000"])
        data.append(["Osvaldo Matesiac",5,"90.000"])
        data.append(['Pablo Barresi',6,"90.000"])

        # Crear una tabla con los datos y aplicar estilos
        table = Table(data)
        table.setStyle(TableStyle(style))

        elements.append(table)

        doc.build(elements)

        return response

    export_selected_to_pdf_.short_description = "Exportar expensas seleccionadas a archivo PDF"

    
    actions = [export_selected_to_pdf,export_selected_to_pdf_]
    
admin.site.register(Expensa, Modelo_admin)