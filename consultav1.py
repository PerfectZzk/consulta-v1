#!usr/bin/python3
import requests
from time import sleep
import os
#cores
vd='\033[32m'
am='\033[33m'
vm='\033[31m'
az='\033[36m'
ng='\033[1m'
f='\033[m'
lz='\033[34m'   
def ip():  
    n1 = str(input(f'{vm}--={f}{az}[CONSULTA IP]{f}\n\n- {az}[{f}{lz}01{f}{az}]{f} {ng}ipgeolocation{f}\n- {az}[{f}{lz}02{f}{az}]{f} {ng}ip{f}\n- {az}[{f}{lz}03{f}{az}]{f} {ng}ipfind{f}  \n- {am}+=>{f} '))         
    if n1=='1' or n1=='01':
        ip1=input(f'{vm}--=={f}{az}[fonte IPGEOLOCATION]{f} \n{vm}--=={f}{az}[ ip ]{f} {am}+=>{f} ')
        url1 = "https://api.ipgeolocation.io/ipgeo?apiKey=9313e7887bad45cea6d4b5845f085464&ip={}".format(ip1)
        res = requests.get(url1)
        req=res.json()
        br="\n{}[+] CONSULTA REALIZADA PELO SCRIPT DE CONSULTA-V1 \n[+] by: D.security{}{} \n-=[ip]:{}\n-=[código do continente]:{}\n-=[nome do continente]:{}\n-=[código do país 2]:{}\n-=[código do país 3]:{}\n-=[nome do país]:{}\n-=[capital do país]:{}\n-=[prov do estado]:{}\n-=[distrito]:{}\n-=[cidade]:{}\n-=[CEP]:{}\n-=[latitude]:{}\n-=[longitude]:{}\n-=[is_eu]:{}\n-=[código de chamada]:{}\n-=[país tld]:{}\n-=[languages]:{}\n-=[bandeira do país]:{}\n-=[ geoname_id ]:{}\n-=[ isp ]:{}\n-=[continente]:{}\n-=[organização]:{}\n-=[moeda]:{}\n-=[fuso horário]:{}\n\033[m".format(ng,f,vd,req['ip'],req['continent_code'],req['continent_name'],req['country_code2'],req['country_code3'],req['country_name'],req['country_capital'],req['state_prov'],req['district'],req['city'],req['zipcode'],req['latitude'],req['longitude'],req['is_eu'],req['calling_code'],req['country_tld'],req['languages'],req['country_flag'],req['geoname_id'],req['isp'],req['connection_type'],req['organization'],req['currency'],req['time_zone'])
        print(br)


    elif n1=='2' or n1=='02':            
        ip2=input(f'{vm}--=={f}{az}[fonte IP ]{f} \n{vm}--=={f}{az}[ ip ]{f} {am}+=>{f} ')      
        url2='http://ip-api.com/json/{}'.format(ip2)
        res2=requests.get(url2);req1=res2.json()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
        br2="\n{}[+] CONSULTA REALIZADA PELO SCRIPT DE CONSULTA-V1 \n[+] by: D.security{}\n {}-=[status]:{}\n -=[país]:{}\n -=[código do país]:{}\n -=[região]:{}\n -=[nome da região]:{}\n -=[cidade]:{}\n -=[zip]:{}\n -=[lat]:{}\n -=[lon]:{}\n -=[fuso horário]:{}\n -=[isp]:{}\n -=[org]:{}\n -=[as]:{} {}\033[m".format(ng,f,vd,req1['status'],req1['country'],req1['countryCode'],req1['region'],req1['regionName'],req1['city'],req1['zip'],req1['lat'],req1['lon'],req1['timezone'],req1['isp'],req1['org'],req1['as'],req1['query'],f)       
        print(br2)
        exit()
    elif n1=='3' or n1=='03':     
        ip3=input(f'{vm}--=={f}{az}[fonte IPFIND ]{f} \n{vm}--=={f}{az}[ ip ]{f} {am}+=>{f} ')
        url3='https://api.ipfind.com/?ip={}&auth=22e75f18-7853-4227-ac49-3a8a72893210'.format(ip3)
        res3=requests.get(url3);req3=res3.json()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
        br3='\n{}[+] CONSULTA REALIZADA PELO SCRIPT DE CONSULTA-V1 \n[+] by: D.security{}\n{}-=[ip_address]:{}\n-=[country]:{}\n-=[country code]:{}\n-=[continent]:{}\n-=[continente codigo]:{}\n-=[city]:{}\n-=[condado]:{}\n-=[região]:{}\n-=[código da região]:{}\n-=[fuso horário]:{}\n-=[proprietário]:{}\n-=[longitude]:{}\n-=[latitude]:{}\n-=[moeda]:{}\n-=[línguas]:{}\n{}'.format(ng,f,vd,req3['ip_address'],req3['country'],req3['country_code'],req3['continent'],req3['continent_code'],req3['city'],req3['county'],req3['region'],req3['region_code'],req3['timezone'],req3['owner'],req3['longitude'],req3['latitude'],req3['currency'],req3['languages'],f)
        print(br3)
def cpf():
    import requests, os, time, base64, json, re
import platform

def clear():
   if platform.system() == "Windows":
      os.system("cls")
   elif platform.system() == "Linux":
      os.system("clear")
   else:
       os.system("clear")

R='\033[1;31m'; B='\033[1;34m'; C='\033[1;37m'; Y='\033[1;33m'; G='\033[1;32m'; RT='\033[;0m'

code_info = C + '[' + Y + 'i' + C + '] '
code_details = C + '[' + G + '*' + C + '] '
code_result = C + '[' + G + '+' + C + '] '
code_error = C + '[' + R + '!' + C + '] '

a='aHR0cDovL3d3dy5qdXZlbnR1ZGV3ZWIubXRlLmdvdi5ici9wbnBlcGVzcXVpc2FzLmFzcA=='
a=a.encode('ascii')
a=base64.b64decode(a)
a=a.decode('ascii')

def main():
  clear()
  print("\n" + code_info + "CPF.")
  print(f'''
{C}[{G}i{C}] Formas de operação:

[{G}1{C}] Consultar CPF.
[{G}2{C}] Gerar CPF e consultar.
[{G}3{C}] Voltar.
[{G}4{C}] {R}Sair.{C}
''')
tool=input(f'{C}[{G}+{C}] Selecione a forma de operação:{B} ')
  if tool=='1':
    cpf=input(f'{C}[{G}*{C}] Informe o CPF a ser consultado (sem pontos ou traços): {B}')
    consultar(cpf)
  elif tool=='2':
    gerarcpf()
  elif tool=='3':
    clear()
    import consulta
    consulta.main()
  elif tool=='4':
    clear()
    print(f'\n{G}Somos uma comunidade.{C}\n')
    exit()
  else:
    clear()
    print(f'{C}[{R}-{C}] Seleção inválida.')
    time.sleep(0.2)
    main()


def gerarcpf():
  print(f'{C}[{G}*{C}] Gerando CPF...')
  time.sleep(1)
  cpf=requests.request('GET','http://geradorapp.com/api/v1/cpf/generate?token=f01e0024a26baef3cc53a2ac208dd141').json()
  cpf2=cpf['data']['number_formatted']
  cpf=cpf['data']['number']
  print(f'{C}[{Y}i{C}] O CPF gerado foi: {B}'+cpf2)
  time.sleep(1)
  print(f'{C}[{G}*{C}] Consultando CPF gerado...')
  nova=input("\n" + f'{C}[{G}+{C}] Deseja consultar?[{G}s{C}/{R}n{C}]: ').lower()
  if nova=='s' or nova=='sim':
      clear()
      consultar(cpf)
  else:
      print(f'\n{G}Somos uma comunidade.{C}\n')
      exit()
  
def consultar(cpf):
  try:
    h={
    'Content-Type': "text/xml, application/x-www-form-urlencoded;charset=ISO-8859-1, text/xml; charset=ISO-8859-1",
    'Cookie': "ASPSESSIONIDSCCRRTSA=NGOIJMMDEIMAPDACNIEDFBID; FGTServer=2A56DE837DA99704910F47A454B42D1A8CCF150E0874FDE491A399A5EF5657BC0CF03A1EEB1C685B4C118A83F971F6198A78",
    'Host': "www.juventudeweb.mte.gov.br"
    }
    r=requests.post(a, headers=h, data=f'acao=consultar%20cpf&cpf={cpf}&nocache=0.7636039437638835').text
    clear()
    print(f'''
{C}CPF: {B}{re.search('NRCPF="(.*?)"', r).group(1)}
{C}Nome: {B}{re.search('NOPESSOAFISICA="(.*?)"', r).group(1).title()}
{C}Nascimento: {B}{re.search('DTNASCIMENTO="(.*?)"', r).group(1)}
{C}Nome da Mae: {B}{re.search('NOMAE="(.*?)"', r).group(1).title()}
{C}Endereco: {B}{re.search('NOLOGRADOURO="(.*?)"', r).group(1).title()}, {re.search('NRLOGRADOURO="(.*?)"', r).group(1)}
{C}Complemento: {B}{re.search('DSCOMPLEMENTO="(.*?)"', r).group(1).title()}
{C}Bairro: {B}{re.search('NOBAIRRO="(.*?)"', r).group(1).title()}
{C}Cidade: {B}{re.search('NOMUNICIPIO="(.*?)"', r).group(1).title()}-{re.search('SGUF="(.*?)"', r).group(1)}
{C}CEP: {B}{re.search('NRCEP="(.*?)"', r).group(1)}
''')
nova=input(f'{C}[{G}+{C}] Deseja realizar uma nova consulta?[{G}s{C}/{R}n{C}]: ').lower()
    if nova=='s' or nova=='sim':
      clear()
      main()
    else:
      print(f'\n{G}Somos uma comunidade.{C}\n')
      exit()
  except(AttributeError):
    print(f'{R}CPF inexistente{C}' + "\n")
    nova=input(f'{C}[{G}+{C}] Deseja realizar uma nova consulta?[{G}s{C}/{R}n{C}]: ').lower()
    if nova=='s' or nova=='sim':
      clear()
      main()
    else:
      clear()
      print(f'\n{G}Somos uma comunidade.{C}\n')
      exit()
def cep():    
    n1 = str(input(f'{vm}--={f}{az}[CONSULTA CEP]{f}\n\n- {az}[{f}{lz}1{f}{az}]{f} {ng}postmon{f}\n- {az}[{f}{lz}2{f}{az}]{f} {ng}viacep{f}\n- {az}[{f}{lz}3{f}{az}]{f} {ng}apicep{f}  \n- {am}+=>{f} '))
    if n1=='1' or n1=='01':
        cep1=input(f'{vm}--=={f}{az}[fonte POSTMON ]{f} \n{vm}--=={f}{az}[ cep ]{f} {am}+=>{f} ')
        if len(cep1) == 8:
            url1='https://api.postmon.com.br/v1/cep/{}'.format(cep1)
            res1=requests.get(url1);req1=res1.json()
            resl1="\n{}[+] CONSULTA REALIZADA PELO SCRIPT DE CONSULTA-V1 \n[+] by: D.security{} \n{}-=[complemento]:{}\n-=[bairro]:{}\n-=[cidade]:{}\n-=[logradouro]:{}\n-=[estado_info]:{}\n-=[cep]:{}\n-=[cidade_info]:{}\n-=[estado]:{} {}".format(ng,f,vd,req1['complemento'],req1['bairro'],req1['cidade'],req1['logradouro'],req1['estado_info'],req1['cep'],req1['cidade_info'],req1['estado'],f)
            print(resl1)
        else:
            print(f' {vm}[!] valor invalido \n digite apenas numeros \n {f}ex: {ng}01001000 {f}')                                 
    elif n1=='2' or n1=='02':
        cep2=input(f'{vm}--=={f}{az}[fonte VIACEP ]{f} \n{vm}--=={f}{az}[ cep ]{f} {am}+=>{f} ')
        if len(cep2)==8:
            url2='https://viacep.com.br/ws/{}/json/'.format(cep2)
            res2 = requests.get(url2);req2=res2.json()
            resl2="\n{}[+] CONSULTA REALIZADA PELO SCRIPT DE CONSULTA-V1 \n[+] by: D.security{} \n{}-=[cep]:{}\n-=[logradouro]:{}\n-=[complemento]:{}\n-=[bairro]:{}\n-=[localidade]:{}\n-=[uf]:{}\n-=[ibge]:{}\n-=[gia]:{} {}".format(ng,f,vd,req2['cep'],req2['logradouro'],req2['complemento'],req2['bairro'],req2['localidade'],req2['uf'],req2['ibge'],req2['gia'],f)        
            print(resl2)
        else:
            print(f' {vm}[!] valor invalido \n digite apenas numeros \n {f}ex: {ng}01001000 {f}')
    elif n1=='3' or n1=='03':
        cep3=input(f'{vm}--=={f}{az}[fonte APICEP ]{f} \n{vm}--=={f}{az}[ cep ]{f} {am}+=>{f} ')
        if len(cep3) == 8:            
            url3='https://ws.apicep.com/cep/{}.json'.format(cep3) 
            res3 = requests.get(url3);req3=res3.json()
            resl3="\n{}[+] CONSULTA REALIZADA PELO SCRIPT DE CONSULTA-V1 \n[+] by: D.security{} \n{}-=[status]:{}\n-=[ok]:{}\n-=[código]:{}\n-=[estado]:{}\n-=[cidade]:{}\n-=[distrito]:{}\n-=[endereço]:{}\n-=[statusText]:{} {}".format(ng,f,vd,req3['status'],req3['ok'],req3['code'],req3['state'],req3['city'],req3['district'],req3['address'],req3['statusText'],f)
            print(resl3)
        else:
            print(f' {vm}[!] valor invalido \n digite apenas numeros \n {f}ex: {ng}01001000 {f}')            
def cnpj():    
    cpnj1=input(f'{vm}--=={f}{az}[fonte RECEITA FEDERAL ]{f} \n{vm}--=={f}{az}[ cpnj ]{f} {am}+=>{f} ')                           
    url1='https://www.receitaws.com.br/v1/cnpj/{}'.format(cpnj1)
    res=requests.get(url1);req1=res.json()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
    br="\n{}[+] CONSULTA REALIZADA PELO SCRIPT CONSULTA-V1 \n[+]by: D.security {}\n{}-=[data_situacao]:{}\n-=[motivo_situacao]:{}\n-=[complemento]:{}\n-=[tipo]:{}\n-=[nome]:{}\n-=[telefone]:{}\n-=[situacao]:{}\n-=[bairro]:{}\n-=[logradouro]:{}\n-=[numero]:{}\n-=[cep]:{}\n-=[municipio]:{}\n-=[fantasia]:{}\n-=[porte]:{}\n-=[abertura]:{}\n-=[natureza_juridica]:{}\n-=[uf]:{}\n-=[cnpj]:{}\n-=[ultima_atualizacao]:{}\n-=[status]:{}\n-=[email]:{}\n-=[efr]:{}\n-=[situacao_especial]:{}\n-=[data_situacao_especial]:{}\n-=[atividade_principal]:{}\n-=[atividades_secundarias]:{}\n-=[capital_social]:{}\n-=[qsa]:{}\n-=[extra]:{}\n-=[billing]:{} {}".format(ng,f,vd,req1['data_situacao'],req1['motivo_situacao'],req1['complemento'],req1['tipo'],req1['nome'],req1['telefone'],req1['situacao'],req1['bairro'],req1['logradouro'],req1['numero'],req1['cep'],req1['municipio'],req1['fantasia'],req1['porte'],req1['abertura'],req1['natureza_juridica'],req1['uf'],req1['cnpj'],req1['ultima_atualizacao'],req1['status'],req1['email'],req1['efr'],req1['situacao_especial'],req1['data_situacao_especial'],req1['atividade_principal'],req1['atividades_secundarias'],req1['capital_social'],req1['qsa'],req1['extra'],req1['billing'],f)                  
    print(br)
def ban():
    print(f"""
{az}    	
  /﹋\_
 (҂`_´){f} - {vd}By: D.security{f}
 {az}<;︻╦╤─ ҉ - - - - - - - - - - - - -{f}	                            
{vm}--=== >>{f} [  {vd} CONSULTA-V1 {f} ]  
  """)
os.system('clear');
def menu():
    print(f"""
{az}    	
  /﹋\_
 (҂`_´){f} - {vd}By: D.security{f}
 {az}<;︻╦╤─ ҉ - - - - - - - - - - - - -{f}	                            
{vm}--=== >>{f} [  {vd} CONSULTA-V1 {f} ]  
    	 	       
- {az}[{f}{lz}01{f}{az}]{f} {vd}CONSULTAR IP {f}
- {az}[{f}{lz}02{f}{az}]{f} {vd}CONSULTAR CPF {f}
- {az}[{f}{lz}03{f}{az}]{f} {vd}CONSULTAR CEP {f}
- {az}[{f}{lz}04{f}{az}]{f} {vd}CONSULTAR CNPJ {f}
- {az}[{f}{lz}05{f}{az}]{f} {vd}SAIR{f}
    """)
try:
    menu()
    inpu=str(input(f'- {am}=+>{f} '))
except KeyboardInterrupt:
    exit()
except:
    print(f'{vm}- [!] error valor invalido {f}')
try:    
    if inpu=='1' or inpu=='01':   
        os.system('clear');ban();ip()
    elif inpu=='2' or inpu=='02':
        os.system('clear');ban();cep()
         elif inpu=='3' or inpu=='03':
        os.system('clear');ban();cpf()
    elif inpu=='3' or inpu=='04':
        os.system('clear');ban();cnpj()
    elif inpu=='4' or inpu=='05':
        exit()
    else:
        print(f'{vm}- [!] valor invalido !! {f}');exit()                                                                                          
except:
    exit()
       
       
       

  
