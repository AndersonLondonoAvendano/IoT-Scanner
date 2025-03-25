import pdfkit

def html_to_pdf(html_content, output_path, wkhtmltopdf_path=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"):
    """
    Convierte una cadena de HTML o un archivo HTML en un PDF.
    
    :param html_content: Puede ser una cadena con HTML o la ruta de un archivo HTML.
    :param output_path: Ruta donde se guardará el PDF generado.
    :param wkhtmltopdf_path: Ruta personalizada de wkhtmltopdf si no está en PATH.
    """
    options = {
        'page-size': 'A4',
        'encoding': 'UTF-8',
        'enable-local-file-access': ''
    }
    
    config = pdfkit.configuration(wkhtmltopdf=wkhtmltopdf_path) if wkhtmltopdf_path else None
    
    try:
        if html_content.strip().startswith('<'):
            pdfkit.from_string(html_content, output_path, options=options, configuration=config)
        else:
            pdfkit.from_file(html_content, output_path, options=options, configuration=config)
        print(f"PDF generado exitosamente: {output_path}")
    except Exception as e:
        print(f"Error al generar el PDF: {e}")