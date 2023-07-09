import click
import requests

#Adding a comment to test commit.

@click.group() 
def fancywallet():
    '''
    Fancy Commands to manage your assets
    '''
    pass

 
@click.group(name='get')
def get_group():
    '''
    Group of commands to get something
    '''
    pass


@click.command(name='price')
@click.argument('stock')
def get_stock_price(stock):
    '''
    Gets the stock price 
    '''
#    print ("https://query1.finance.yahoo.com/v8/finance/chart/" + stock)
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    result = requests.get(
        "https://query1.finance.yahoo.com/v8/finance/chart/" + stock, headers=headers)
    if result.status_code == 404:
        click.echo(f'Company {stock} not found!')
        exit(404)
    if result.status_code == 403:
        click.echo(f'Forbidden')
        exit(403)

    result_dict = result.json()
    click.echo(result_dict['chart']['result'][0]['meta']['regularMarketPrice'])
   

get_group.add_command(get_stock_price)

fancywallet.add_command(get_group)