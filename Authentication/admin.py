from django.contrib import admin
from django.http import HttpResponse
from Authentication.models import Report
# Register your models here.

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, landscape
from reportlab.platypus import Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.units import inch

def download_pdf(self, request, queryset):
    model_name = self.model.__name__
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename={model_name}.pdf'

    custom_page_size = (landscape(letter)[0], 900)
    pdf = canvas.Canvas(response, pagesize=landscape(letter))
    pdf.setTitle('PDF Report')

    headers = [field.verbose_name for field in self.model._meta.fields]
    data =[headers]

    for obj in queryset:
        data_row = [str(getattr(obj, field.name)) for field in self.model._meta.fields]
        data.append(data_row)

   
    # Adjust column widths to ensure content fits
    col_widths = [1.5 * inch] * len(headers)  # Adjust each column width if necessary
    table = Table(data, colWidths=col_widths)

    table.setStyle(TableStyle(
        [
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 8),  # Smaller font size
            ('BOTTOMPADDING', (0, 0), (-1, 0), 10),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ]
    ))

    # Table placement - start higher on the page to ensure it fits
    canvas_width, canvas_height = landscape(letter)
    table.wrapOn(pdf, canvas_width, canvas_height)
    table_height = table._height  # Actual table height
    y_position = canvas_height - table_height - 250 # Adjust this to fit the table

    table.drawOn(pdf, 10, y_position)
    
    pdf.save()
    return response

download_pdf.short_description = "Download selected items as PDF"

@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = (
        'dept',
        'numStudents',
        'deptAvg',
        'publications',
        'patents',
        'achievements',
        'awards',
        'alumniAchievements',
        'startups'
    )

    actions = [download_pdf]
