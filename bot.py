try:
	import random
	import requests
	import json
	import time
	import urllib.parse
except:
	import os
	os.system("pip install urllib time json requests random")
	import random
	import requests
	import json
	import time
proxy = {
    "http": "http://0kozAFxxmlLZ5m6:aPuSkAmlDQeYRIi@194.135.30.237:45914",
    "https": "http://0kozAFxxmlLZ5m6:aPuSkAmlDQeYRIi@194.135.30.237:45914"
}
def uuid():
    return f"{random.randint(0, 0xffff):04x}{random.randint(0, 0xffff):04x}-{random.randint(0, 0xffff):04x}-{random.randint(0, 0x0fff) | 0x4000:04x}-{random.randint(0, 0x3fff) | 0x8000:04x}-{random.randint(0, 0xffff):04x}{random.randint(0, 0xffff):04x}{random.randint(0, 0xffff):04x}"
print(uuid())
def useragent():
    tipos_disponiveis = ["Chrome", "Firefox", "Opera", "Explorer"]
    tipo_navegador = random.choice(tipos_disponiveis)
    
    navegadores_chrome = [
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2226.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.4; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2224.3 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.93 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.124 Safari/537.36",
    ]
    
    navegadores_firefox = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1",
        "Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10; rv:33.0) Gecko/20100101 Firefox/33.0",
        "Mozilla/5.0 (X11; Linux i586; rv:31.0) Gecko/20100101 Firefox/31.0",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0",
        "Mozilla/5.0 (Windows NT 5.1; rv:31.0) Gecko/20100101 Firefox/31.0",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:29.0) Gecko/20120101 Firefox/29.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:25.0) Gecko/20100101 Firefox/29.0",
        "Mozilla/5.0 (X11; OpenBSD amd64; rv:28.0) Gecko/20100101 Firefox/28.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:28.0) Gecko/20100101 Firefox/28.0",
    ]
    
    navegadores_opera = [
        "Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14",
        "Opera/9.80 (X11; Linux i686; Ubuntu/14.10) Presto/2.12.388 Version/12.16",
        "Mozilla/5.0 (Windows NT 6.0; rv:2.0) Gecko/20100101 Firefox/4.0 Opera 12.14",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14",
        "Opera/12.80 (Windows NT 5.1; U; en) Presto/2.10.289 Version/12.02",
        "Opera/9.80 (Windows NT 6.1; U; es-ES) Presto/2.9.181 Version/12.00",
        "Opera/9.80 (Windows NT 5.1; U; zh-sg) Presto/2.9.181 Version/12.00",
        "Opera/12.0(Windows NT 5.2;U;en)Presto/22.9.168 Version/12.00",
        "Opera/12.0(Windows NT 5.1;U;en)Presto/22.9.168 Version/12.00",
        "Mozilla/5.0 (Windows NT 5.1) Gecko/20100101 Firefox/14.0 Opera/12.0",
    ]
    
    navegadores_explorer = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko",
        "Mozilla/5.0 (compatible, MSIE 11, Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko",
        "Mozilla/1.22 (compatible; MSIE 10.0; Windows 3.1)",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
        "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 7.0; InfoPath.3; .NET CLR 3.1.40767; Trident/6.0; en-IN)",
    ]
    
    if tipo_navegador == 'Chrome':
        return random.choice(navegadores_chrome)
    elif tipo_navegador == 'Firefox':
        return random.choice(navegadores_firefox)
    elif tipo_navegador == 'Opera':
        return random.choice(navegadores_opera)
    elif tipo_navegador == 'Explorer':
        return random.choice(navegadores_explorer)

token = "1990152924:AAHR3wREHim873af8Do-e-YQypbW6GxPRb0"
id = "435009958"
requests.get(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={id}&text=its work !!!!!!!")
useragent = useragent()
uuid_value = uuid()
name = ''.join(random.sample('abcdefghijklmnopqrstuvwxyz0123456789', 6))

# Create Email
response = requests.post(
    'https://api.internal.temp-mail.io/api/v3/email/new',
    headers={'User-Agent': useragent},
    data={'name': name, 'domain': 'greencafe24.com'}
)
result = response.json()
email = result['email']
print(f"Done Create Email : {email}")

# Check Email
response = requests.post(
    'https://www.instagram.com/accounts/check_email/',
    headers={
        'authority': 'www.instagram.com',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96"',
        'x-ig-app-id': '1217981644879628',
        'x-ig-www-claim': 'hmac.AR3YttfYQWMo4aCfHJfmrEMByM6aqjmE8P-5m67nwiMgJkYH',
        'sec-ch-ua-mobile': '?1',
        'x-instagram-ajax': 'd82a8b39058f',
        'content-type': 'application/x-www-form-urlencoded',
        'accept': '*/*',
        'x-requested-with': 'XMLHttpRequest',
        'x-asbd-id': '198387',
        'user-agent': 'Mozilla/5.0 (Linux; Android 11; SM-A217F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.46 Mobile Safari/537.36',
        'x-csrftoken': 'j96SeMj4NKEfNJKJy90QCVtdzzJoxsW9',
        'sec-ch-ua-platform': '"Android"',
        'origin': 'https://www.instagram.com',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://www.instagram.com/accounts/signup/email',
        'accept-language': 'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7,de-DE;q=0.6,de;q=0.5',
        'cookie': f'mid={uuid_value}; ig_did=BEB7DE0C-FD7B-4ABB-A6C1-8A522CEA34DC; ig_nrcb=1; rur="ODN\\05451273161851\\0541674635965:01f749259149d7fc638b9dbf998ece53c89d114a9b04a016ba9e68aaf8f80789e73c4571"; csrftoken=j96SeMj4NKEfNJKJy90QCVtdzzJoxsW9'
    },
    data={'email': email}
)

if '"invalid_email"' in response.text:
    print("Failed To Register Email\n")
elif '"email_is_taken"' in response.text:
    print("Failed To Register Email\n")
else:
    print("Done Register Email\n")
    
    # Send Verify Email
    response = requests.post(
        'https://i.instagram.com/api/v1/accounts/send_verify_email/',
        headers={
            'authority': 'i.instagram.com',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96"',
            'x-ig-app-id': '1217981644879628',
            'x-ig-www-claim': 'hmac.AR3YttfYQWMo4aCfHJfmrEMByM6aqjmE8P-5m67nwiMgJkYH',
            'sec-ch-ua-mobile': '?1',
            'x-instagram-ajax': 'd82a8b39058f',
            'content-type': 'application/x-www-form-urlencoded',
            'accept': '*/*',
            'user-agent': 'Mozilla/5.0 (Linux; Android 11; SM-A217F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.46 Mobile Safari/537.36',
            'x-asbd-id': '198387',
            'x-csrftoken': 'j96SeMj4NKEfNJKJy90QCVtdzzJoxsW9',
            'sec-ch-ua-platform': '"Android"',
            'origin': 'https://www.instagram.com',
            'sec-fetch-site': 'same-site',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://www.instagram.com/',
            'accept-language': 'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7,de-DE;q=0.6,de;q=0.5',
            'cookie': f'mid={uuid_value}; ig_did=BEB7DE0C-FD7B-4ABB-A6C1-8A522CEA34DC; ig_nrcb=1; rur="ODN\\05451273161851\\0541674635965:01f749259149d7fc638b9dbf998ece53c89d114a9b04a016ba9e68aaf8f80789e73c4571"; csrftoken=j96SeMj4NKEfNJKJy90QCVtdzzJoxsW9'
        },
        data={'device_id': uuid_value, 'email': email}
    )
    
    print("Plz Wait A Few Seconds To Get Code\n")
    
    while True:
        msg = requests.get(f'https://api.internal.temp-mail.io/api/v3/email/{email}/messages').text
        if 'is your Instagram code' not in msg:
            time.sleep(5)  # Wait before retrying
        else:
            msg = json.loads(requests.get(f'https://api.internal.temp-mail.io/api/v3/email/{email}/messages').text)
            subject = msg[0]['subject']
            code = subject.split(' is your Instagram code')[0]
            print(code)
            
            # Check Confirmation Code
            response = requests.post(
                'https://i.instagram.com/api/v1/accounts/check_confirmation_code/',
                headers={
                    'authority': 'i.instagram.com',
                    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96"',
                    'x-ig-app-id': '1217981644879628',
                    'x-ig-www-claim': 'hmac.AR3YttfYQWMo4aCfHJfmrEMByM6aqjmE8P-5m67nwiMgJkYH',
                    'sec-ch-ua-mobile': '?1',
                    'x-instagram-ajax': 'd82a8b39058f',
                    'content-type': 'application/x-www-form-urlencoded',
                    'accept': '*/*',
                    'user-agent': 'Mozilla/5.0 (Linux; Android 11; SM-A217F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.46 Mobile Safari/537.36',
                    'x-asbd-id': '198387',
                    'x-csrftoken': 'j96SeMj4NKEfNJKJy90QCVtdzzJoxsW9',
                    'sec-ch-ua-platform': '"Android"',
                    'origin': 'https://www.instagram.com',
                    'sec-fetch-site': 'same-site',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-dest': 'empty',
                    'referer': 'https://www.instagram.com/',
                    'accept-language': 'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7,de-DE;q=0.6,de;q=0.5',
                    'cookie': f'mid={uuid_value}; ig_did=BEB7DE0C-FD7B-4ABB-A6C1-8A522CEA34DC; ig_nrcb=1; rur="ODN\\05451273161851\\0541674635965:01f749259149d7fc638b9dbf998ece53c89d114a9b04a016ba9e68aaf8f80789e73c4571"; csrftoken=j96SeMj4NKEfNJKJy90QCVtdzzJoxsW9'
                },
                data={'code': int(code), 'device_id': uuid_value, 'email': email}
            )
            #print(response.text)
            if '"invalid_nonce"' in response.text:
                print("Failed To Get Code !\n")
                exit()
            else:
                print(f"Done Get Code : {code}, Plz Wait To Register\n")
                sign_code = json.loads(response.text)
                signup_code = sign_code['signup_code']
                print(signup_code)
                
                # Check Age Eligibility
                response = requests.post(
                    'https://www.instagram.com/web/consent/check_age_eligibility/',
                    headers={
                        'authority': 'www.instagram.com',
                        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96"',
                        'x-ig-app-id': '1217981644879628',
                        'x-ig-www-claim': '0',
                        'sec-ch-ua-mobile': '?1',
                        'x-instagram-ajax': 'd82a8b39058f',
                        'content-type': 'application/x-www-form-urlencoded',
                        'accept': '*/*',
                        'x-requested-with': 'XMLHttpRequest',
                        'x-asbd-id': '198387',
                        'user-agent': 'Mozilla/5.0 (Linux; Android 11; SM-A217F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.46 Mobile Safari/537.36',
                        'x-csrftoken': 'UKmDDrtCDo3XIPWf0PUE2MVHwcokkDat',
                        'sec-ch-ua-platform': '"Android"',
                        'origin': 'https://www.instagram.com',
                        'sec-fetch-site': 'same-origin',
                        'sec-fetch-mode': 'cors',
                        'sec-fetch-dest': 'empty',
                        'referer': 'https://www.instagram.com/accounts/signup/birthday',
                        'accept-language': 'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7,de-DE;q=0.6,de;q=0.5',
                        'cookie': f'mid={uuid_value}; ig_did=BEB7DE0C-FD7B-4ABB-A6C1-8A522CEA34DC; ig_nrcb=1; csrftoken=UKmDDrtCDo3XIPWf0PUE2MVHwcokkDat; ig_gdpr_signup=%7B%22count%22%3A1%2C%22timestamp%22%3A1643112064565%7D'},
                    data = {
                        'day': '20',
                        'month': '11',
                        'year': '1996'}
                 )
                characters = 'abcdefghijklmnopqrstuvwxyz0123456789'
                password = ''.join(random.sample(characters, 8))
                username = ''.join(random.sample(characters, 7))
                first_name = ''.join(random.sample(characters, 6))
                url = 'https://www.instagram.com/accounts/web_create_ajax/'
                headers = {
				    'authority': 'www.instagram.com',
				    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96"',
				    'x-ig-app-id': '1217981644879628',
				    'x-ig-www-claim': 'hmac.AR3v83slgpGfIK_bEpuCItxMgBy1y426AcqAisb9UaZX6nbd',
				    'sec-ch-ua-mobile': '?1',
				    'x-instagram-ajax': '31da6d1b025b',
				    'content-type': 'application/x-www-form-urlencoded',
				    'accept': '*/*',
				    'x-requested-with': 'XMLHttpRequest',
				    'x-asbd-id': '198387',
				    'user-agent': 'Mozilla/5.0 (Linux; Android 11; SM-A217F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.46 Mobile Safari/537.36',
				    'x-csrftoken': 'QCaVNN83zI2xvZvoocMsfHqEJSlsdjfU',
				    'sec-ch-ua-platform': '"Android"',
				    'origin': 'https://www.instagram.com',
				    'sec-fetch-site': 'same-origin',
				    'sec-fetch-mode': 'cors',
				    'sec-fetch-dest': 'empty',
				    'referer': 'https://www.instagram.com/accounts/signup/username',
				    'accept-language': 'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7,de-DE;q=0.6,de;q=0.5',
				    'cookie': f'mid={uuid_value}; ig_did=BEB7DE0C-FD7B-4ABB-A6C1-8A522CEA34DC; ig_nrcb=1; rur="CLN\\05451297125343\\0541674684111:01f7f242288bdab03791a265216076ac9b1703382c58fbe8d76e9186ccfd387e1ae63913"; csrftoken=QCaVNN83zI2xvZvoocMsfHqEJSlsdjfU'
                }
                data = {
				    'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{int(time.time())}:{password}',
				    'email': email,  # استبدل هذا بالإيميل الحقيقي
				    'username': username,
				    'first_name': first_name,
				    'month': '10',
				    'day': '20',
				    'year': '1997',
				    'client_id': uuid_value,  # استبدل هذا بالقيمة المناسبة
				    'seamless_login_enabled': '1',
				    'tos_version': 'row',
				    'force_sign_up_code': signup_code# استبدل هذا بالقيمة المناسبة
                }
                res = requests.post(url, headers=headers, data=data).text
                print("result: ",res)
                result = json.loads(res)
                if result['account_created'] == False:
                    print("Failed To Create ×\n")
                    text = f'''
Failed Create Account ❌.
-----------------------
.+. First Name : {first_name}
.+. Email : {email}
.+. Username : {username}
.+. Password : {password}
-----------------------
~ BY : - @jj8jjj8'''
                    print(text)
                else:
                    user_id = result["user_id"]
                    text = f'''
Failed Create Account ✅.
-----------------------
.+. First Name : {first_name}
.+. Email : {email}
.+. Username : {username}
.+. Password : {password}
.+. User Id : {user_id}
-----------------------
~ BY : - @jj8jjj8'''
                    requests.get(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={id}&text={text}")
                    print(text)
