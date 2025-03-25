import os
import socket
from lxml import etree
from utils import print_message
from htmlTOpdf import html_to_pdf

def generate_pdf_report(xml_path):
    """
    Convierte un archivo XML de Nmap en un reporte PDF.

    :param xml_path: Ruta del archivo XML generado por Nmap.
    """
    if not os.path.exists(xml_path):
        print_message(f"Error: No se encontró el archivo XML {xml_path}", "red", attrs=["bold"])
        return

    report_name = os.path.splitext(os.path.basename(xml_path))[0]
    html_path = f"./reports/{report_name}_vuln_report.html"
    pdf_path = f"./reports/{report_name}_vuln_report.pdf"
    xslt_path = "./nmap.xsl"

    if not os.path.exists(xslt_path):
        print_message(f"Error: No se encontró el archivo {xslt_path}", "red", attrs=["bold"])
        return

    try:
        xml_tree = etree.parse(xml_path)
        xslt_tree = etree.parse(xslt_path)
        transform = etree.XSLT(xslt_tree)
        html_tree = transform(xml_tree)
        
        with open(html_path, "wb") as html_file:
            html_file.write(etree.tostring(html_tree, pretty_print=True))
        
        print_message(f"Reporte HTML generado: {html_path}", "green", attrs=["bold"])
        
        # Generar PDF y eliminar HTML
        html_to_pdf(html_path, pdf_path)
        os.remove(html_path)
        os.remove(xml_path)
        
        print_message(f"Reporte PDF generado: {pdf_path}", "green", attrs=["bold"])
        return pdf_path
    except Exception as e:
        print_message(f"Error al generar el reporte PDF: {e}", "red", attrs=["bold"])
