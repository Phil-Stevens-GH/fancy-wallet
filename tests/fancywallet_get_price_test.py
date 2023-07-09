from click.testing import CliRunner
import unittest
from psfancywallet import psfancywallet 

#adding a comment to test the commit.
class FancyWalletGetPriceTests(unittest.TestCase):

    def test_get_price_tsla_lower(self):
        runner = CliRunner()
        result = runner.invoke(psfancywallet, ['get', 'price', 'tsla'])
        self.assertEqual(result.exit_code, 0)

    def test_get_price_tsla_upper(self):
        runner = CliRunner()
        result = runner.invoke(psfancywallet, ['get', 'price', 'TSLA'])
        self.assertEqual(result.exit_code, 0)
        
    def test_get_price_unknown(self):
        company = 'unknown'
        runner = CliRunner()
        result = runner.invoke(psfancywallet, ['get', 'price', company])
        self.assertNotEqual(result.exit_code, 0)
        self.assertEqual(result.output, f'Company {company} not found!\n')
    
if __name__ == '__main__':
    unittest.main() 