from cStringIO import StringIO
from common import Invoice, repos, inv

repos.add_report(Invoice, 'application/pdf', 'basic.tex',
                 report_name='ConTeXt')
#PDF
if __name__ == '__main__':
    pdf_report, _ = repos.reports[Invoice]['ConTeXt']
    file('bonham_basic.pdf', 'w').write(pdf_report(o=inv).render().getvalue())
