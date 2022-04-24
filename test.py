from app import app
import unittest


class FlaskTest(unittest.TestCase):

    def test_get_player_by_year(self):
        tester = app.test_client(self)
        res = tester.get('/year/1989')
        sc = res.status_code
        self.assertEqual(sc, 200)
        self.assertEqual(res.content_type, 'application/json')
        self.assertEqual(b'{"player_percentage":"21.2%"}\n', res.data)

    def test_average_age(self):
        tester = app.test_client(self)
        res = tester.get('/avg-age')
        sc = res.status_code
        self.assertEqual(sc, 200)
        self.assertEqual(res.content_type, 'application/json')
        self.assertEqual(
            b'{"Australia":40.03,"Bangladesh":35.8,"England":40.29,"India":36.17,"Netherlands":42.0,"New Zealand":37.77,"Pakistan":41.31,"South Africa":39.33,"Sri Lanka":41.1,"West Indies":37.89,"Zimbabwea":42.5}\n',
            res.data)

    def test_left_hand(self):
        tester = app.test_client(self)
        res = tester.get('/left-hand')
        sc = res.status_code
        self.assertEqual(sc, 200)
        self.assertEqual(res.content_type, 'application/json')
        self.assertEqual(b'{"India":58}\n', res.data)
        # self.assertEqual(, res.data)

    def test_und_player(self):
        tester = app.test_client(self)
        res = tester.get('/und-player')
        sc = res.status_code
        self.assertEqual(sc, 200)
        self.assertEqual(res.content_type, 'application/json')
        self.assertEqual(
            b'["A Choudhary","A Dananjaya","A Hales","A Joseph","A Roy","A Turner","AJ Tye","Ankit Soni","AR Bawne","AS Yadav","Avesh Khan","B Stanlake","BA Stokes","Basil Thampi","C de Grandhomme","C Ingram","CR Woakes","D Shorey","D Short","D Willey","DM Bravo","E Lewis","H Brar","H Gurney","H Klaasen","H Vihari","H Viljoen","Harmeet Singh (2)","I Sodhi","J Archer","J Bairstow","J Behrendorff","J Dala","J Denly","J Searles","JJ Roy","K Ahmed","K Gowtham","K Khejroliya","K Paul","K Rabada","KM Asif","L Ferguson","L Livingstone","L Ngidi","L Plunkett","LH Ferguson","M Ali","M Lomror","M Markande","M Santner","M Ur Rahman","M Wood","MJ Henry","Mohammad Nabi","Mohammed Siraj","N Naik","N Pooran","NB Singh","Niraj Patel","O Thomas","P Chopra","P Krishna","P R Barman","P Raj","P Shaw","R Bhui","R Parag","R Salam","R Singh","RA Tripathi","Rashid Khan","RD Chahar","S Curran","S Dube","S Gill","S Hetmyer","S Kuggeleijn","S Lamichhane","S Mavi","S Midhun","S Rutherford","S Sharma","S Singh","S Warrier","SD Lad","SP Jackson","SS Agarwal","T Curran","T Natarajan","Tejas Baroka","TS Mills","V Chakravarthy","Vishnu Vinod","Washington Sundar"]\n',
            res.data)

    def test_get_player_by_country(self):
        tester = app.test_client(self)
        res = tester.get('/country/England')
        sc = res.status_code
        self.assertEqual(sc, 200)
        self.assertEqual(res.content_type, 'application/json')
        self.assertEqual(
            b'["A Flintoff","AC Thomas","AD Mascarenhas","CJ Jordan","CK Langeveldt","EJG Morgan","GR Napier","JC Buttler","LJ Wright","MJ Lumb","OA Shah","PD Collingwood","RS Bopara","SW Billings"]\n',
            res.data)


if __name__ == '__main__':
    unittest.main()
