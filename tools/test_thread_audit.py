"""Regression checks for parsing and audit failure modes, not table certification."""
import hashlib
from pathlib import Path
import tempfile
import unittest
from thread_audit import Audit, H, norm, number, read_html, inches
from thread_html import Extractor, expand

ROOT=Path(__file__).resolve().parents[1]/'data/mechanical-tables'
def cells(*texts):
    return [dict(text=str(text),line=i+1,rowspan=1,colspan=1) for i,text in enumerate(texts)]

class AuditTests(unittest.TestCase):
    def test_spans_and_implicit_cell_closing(self):
        parser=Extractor()
        parser.feed('<table><tr><th rowspan="2">M2<td>0,4<td>1,567<tr><td>0,25<td>1,729</table>')
        grid=expand(parser.tables[0])
        self.assertEqual([[c['text'] for c in row] for row in grid],
                         [['M2','0,4','1,567'],['M2','0,25','1,729']])

    def test_mixed_fractions_do_not_collide(self):
        self.assertNotEqual(norm('1 1/16 - 12 UN 12'),norm('11/16 - 12 UN 12'))
        self.assertEqual(norm('M 7×0,5'),norm('M 7x0,5'))
        self.assertEqual(number('4 1/2'),4.5)
        self.assertAlmostEqual(inches('No. 8'),.164)

    def test_wrong_coarse_pitch_does_not_corrupt_correct_diameters(self):
        audit=Audit(ROOT)
        path=ROOT/'03-ZAVITY/02-Metricke zavity ISO/01-Metricke zavity ISO - pro vseobecne pouziti/example.html'
        audit.inspect(path,[[cells('M 2,2','0,4','1,713','1,908','1,648')]],'')
        self.assertEqual([(f['field'],f['expected']) for f in audit.findings],[('P hrubé řady',.45)])

    def test_metric_root_diameter_uses_17h_over_12(self):
        audit=Audit(ROOT);audit.location='fixture'
        audit.check(cells('26,933'),0,20-17*H*2.5/12,'metric','M20','d3','ISO724')
        self.assertEqual(audit.findings[0]['expected'],16.933)
        self.assertEqual(audit.findings[0]['status'],'confirmed')

    def test_last_digit_difference_is_separate(self):
        audit=Audit(ROOT);audit.location='fixture'
        audit.check(cells('143,506'),0,150-1.25*H*6,'metric','M150','D1','ISO724')
        self.assertEqual(audit.findings[0]['status'],'precision')

    def test_trapezoidal_intentionally_blank_dimensions(self):
        audit=Audit(ROOT)
        path=ROOT/'03-ZAVITY/06-Lichobeznikove zavity/01-Lichobeznikove zavity - zakladni rozmery/example.html'
        row=cells('48','12','','','','','','Tr 48 × 12','12','24','32','48','72','-')
        audit.inspect(path,[[row]],'')
        self.assertEqual(len(audit.findings),1)
        self.assertEqual(audit.findings[0]['expected'],36)
        self.assertEqual(audit.findings[0]['field'],'Ph pro 3 chodů [mm]')

    def test_iso228_uses_standard_rounded_depth(self):
        audit=Audit(ROOT)
        path=ROOT/'03-ZAVITY/05-Trubkove zavity ISO/ISO 228/example.html'
        row=cells('G5/8','14','1,814','22,911','21,749','20,581',
                  '0 -284','0 -142','0 -284','142 0','541 0')
        audit.inspect(path,[[row]],'')
        self.assertEqual([(f['field'],f['expected']) for f in audit.findings],[('D1 [mm]',20.587)])

    def test_overview_does_not_read_11_sixteenths_as_one_and_one(self):
        audit=Audit(ROOT)
        path=ROOT/'03-ZAVITY/03-Palcove zavity ISO/01-Palcove zavity ISO - prehled/example.html'
        row=cells('','11/16','0,6875',*(['']*11))
        audit.headers_and_prose(path.relative_to(ROOT).as_posix(),[[cells('header')]*4+[row]],'')
        self.assertEqual(audit.findings,[])

    def test_full_audit_does_not_modify_inputs(self):
        paths=sorted(p for p in (ROOT/'03-ZAVITY').rglob('*') if p.is_file())
        before={p:hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
        result=Audit(ROOT).run()
        self.assertEqual(len(result['files']),50)
        self.assertEqual(result['rows']['metric_basic'],392)
        self.assertEqual(result['rows']['trapezoidal'],143)
        self.assertEqual(result['rows']['unified'],346)
        self.assertFalse([f for f in result['findings'] if f['field']=='Kontrola řádku'])
        self.assertEqual(before,{p:hashlib.sha256(p.read_bytes()).hexdigest() for p in paths})

    def test_empty_html_is_not_an_invented_table(self):
        with tempfile.TemporaryDirectory() as tmp:
            path=Path(tmp)/'empty.html';path.write_text('',encoding='utf-8')
            self.assertEqual(read_html(path)[2],[])


class RepairedDataTests(unittest.TestCase):
    def test_repaired_library_has_no_actionable_findings(self):
        result=Audit(ROOT).run()
        self.assertEqual(result['findings'],[])
        expected={'metric_basic':392,'metric_optics':314,'unified_overview':71,
                  'unified':346,'whitworth':30,'pipe7':15,'pipe228':24,
                  'trapezoidal':143,'cycle':12,'runouts':24,'undercuts':24}
        for family,count in expected.items():
            self.assertEqual(result['rows'][family],count,family)
        self.assertEqual(result['checks']['export_cells'],12587)

    def test_complete_export_contracts(self):
        from thread_exports import export_spec
        expected_rows=[79,76,78,81,78,392,314,346,30,15,24,143,12,24,24]
        paths=sorted((ROOT/'03-ZAVITY').rglob('*.csv'))
        self.assertEqual(len(paths),15)
        for path,count in zip(paths,expected_rows):
            spec=export_spec(path)
            self.assertEqual(len(spec['rows']),count,str(path))
            self.assertTrue(all(len(row)==len(spec['columns']) for row in spec['rows']))

    def test_optics_copied_m5_diameters_are_not_exempt(self):
        audit=Audit(ROOT)
        path=ROOT/'03-ZAVITY/02-Metricke zavity ISO - pro jemnou mechaniku/example.html'
        audit.inspect(path,[[cells('4,5','0,35','5,000','4,773','4,621','4,571')]],'')
        self.assertEqual(len(audit.findings),4)
        self.assertEqual([f['expected'] for f in audit.findings],[4.5,4.273,4.121,4.071])

    def test_different_undercut_standards_are_not_confused(self):
        audit=Audit(ROOT)
        path=ROOT/'03-ZAVITY/09-Drazky/example.html'
        # ISO 4755 a_min=1.6; DIN type A g1_min=2.1 is a different design.
        row=cells('1','M6; M7','d - 1,6','1,6','3','D + 0,5','4','5,2','2,5','3,7','0,6','0,6')
        audit.inspect(path,[[row]],'')
        self.assertEqual(audit.findings,[])
        row[3]['text']='2,1'
        audit.inspect(path,[[row]],'')
        self.assertEqual(audit.findings[0]['expected'],1.6)

    def test_external_and_internal_radii_are_independent(self):
        audit=Audit(ROOT)
        path=ROOT/'03-ZAVITY/09-Drazky/example.html'
        row=cells('4,5','M42; M45','d - 6,4','8','13,5','D + 0,5','18','23','11','16','2','2')
        audit.inspect(path,[[row]],'')
        self.assertEqual([(f['field'],f['expected']) for f in audit.findings],[('R vnější',2.5)])

    def check_bad_csv(self, transform, field):
        import csv
        from thread_exports import export_spec
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)
            directory=root/'03-ZAVITY/02-Palcove zavity ISO - zakladni rozmery'
            directory.mkdir(parents=True)
            source=next((ROOT/'03-ZAVITY').glob('03-Palcove*/02-Palcove*/0000-index/index_cs.html'))
            (directory/'index_cs.html').write_bytes(source.read_bytes())
            path=directory/'tabulka.csv'
            rows=transform(export_spec(path)['rows'])
            with path.open('w',encoding='utf8',newline='') as stream:
                csv.writer(stream,delimiter='\t',lineterminator='\n').writerows(rows)
            audit=Audit(root);audit.exports([path])
            self.assertIn(field,[f['field'] for f in audit.findings])

    def test_missing_csv_row_is_a_failure(self):
        self.check_bad_csv(lambda rows: rows[:-1], 'Počet řádků CSV')

    def test_extra_csv_column_is_a_failure(self):
        self.check_bad_csv(lambda rows: [rows[0]+['unexpected']]+rows[1:], 'Počet sloupců CSV')

    def test_changed_csv_value_is_a_failure(self):
        def mutate(rows):
            rows[0][6]='999'
            return rows
        self.check_bad_csv(mutate, 'CSV / HTML rozdíl')

if __name__=='__main__':
    unittest.main()