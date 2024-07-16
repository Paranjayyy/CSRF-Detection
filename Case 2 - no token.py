def detect_csrf_token(request_content):
    csrf_token_string = 'csrf_test_name'
    return csrf_token_string in request_content

request_content = '''
POST /student/personal_details_update HTTP/2
Host: internshala.com
Cookie: ists=0; pdc_new=7607659cf84b9c3a0143bcd2c964d30e; pdcVersion=2; u=1; _gcl_au=1.1.1830611607.1705421426; _ga_XHNTE5RRF4=GS1.1.1707403508.9.1.1707403671.54.0.0; _ga=GA1.2.1961062112.1705421427; __stp=eyJ2aXNpdCI6InJldHVybmluZyIsInV1aWQiOiI2NmU1NWEzZS1jYmEzLTQzMWQtOGVlMi02ZjI1N2FkNWEwZGQiLCJjayI6ImhhY2tlcndvcmxkeDNAZ21haWwuY29tIn0=; _fbp=fb.1.1705421429684.497852820; _clck=r7ul17%7C2%7Cfj3%7C0%7C1476; subscription_cookie=1; subscription_at_bottom_cookie=1; lv=1; is_logged_in=1; unbxd.netcoreId=IjA0YzQ1MDI5MjEzYjU5MTg2NTc5MGU4MzIyMGFkNTIwYzU0YThkMGZjZjdjZGIwNzY5MjA4ZTFjYzU3YzY2ODUi; user_id_cookie=28071291; iso=hbrlhws60xz; nav_bottom_courses_amber_dot=1%7C1707564597; __stdf=MA==; _uetvid=7a6733f0c28a11ee8b36c1c959f90bf9; __stgeo=IjAi; _gid=GA1.2.660961807.1707322671; _clsk=16pe514%7C1707403667712%7C2%7C1%7Cs.clarity.ms%2Fcollect; l=83onpwnqwlr%2F1em01l2to1z; csrf_cookie_name=72d15443f27c6c661e5adb3e4543b4c3; lc=83onpwnqwlr%2F1em01l2to1z; role=student; isc=99fhltgfc0av3g3rp5aieml6mlsahb5q; PHPSESSID=3r2sr1kl4m75prpgluj5794qn90giru6; toUpdatePersistentSession=2; persistentSession=75612a45deb9bb95; persistentSessionDateTimeStamp=1707330600; sessionToken=dcc99009; __sts=eyJzaWQiOjE3MDc0MDM1MDg4MjYsInR4IjoxNzA3NDAzNjY3MTU4LCJ1cmwiOiJodHRwcyUzQSUyRiUyRmludGVybnNoYWxhLmNvbSUyRnN0dWRlbnQlMkZyZXN1bWUlM0ZkZXRhaWxfc291cmNlJTNEcmVzdW1lX2RpcmVjdCIsInBldCI6MTcwNzQwMzY2NzE1OCwic2V0IjoxNzA3NDAzNTA4ODI2LCJwVXJsIjoiaHR0cHMlM0ElMkYlMkZpbnRlcm5zaGFsYS5jb20lMkZzdHVkZW50JTJGZGFzaGJvYXJkIiwicFBldCI6MTcwNzQwMzUwODgyNiwicFR4IjoxNzA3NDAzNTA4ODI2fQ==; __stbpnenable=MA==; _gat_UA-20875335-1=1; AWSALB=owDaZpW+eHHl8gmkTZMBmcCqMlcTluYR1PlF3obr+Zznx0gq3mqwMZa8VGAEo+DHvMmGIutt2k7mXs/0kd7aNz1pZOPIc9tWhFzZAD4lLXJx+I5scPMycMBe0tIk; AWSALBCORS=owDaZpW+eHHl8gmkTZMBmcCqMlcTluYR1PlF3obr+Zznx0gq3mqwMZa8VGAEo+DHvMmGIutt2k7mXs/0kd7aNz1pZOPIc9tWhFzZAD4lLXJx+I5scPMycMBe0tIk
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: /
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://internshala.com/student/resume?detail_source=resume_direct
X-Requested-With: XMLHttpRequest
Content-Type: multipart/form-data; boundary=---------------------------414157090438887265732854618085
Content-Length: 1473
Origin: https://internshala.com
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
'''

csrf_token_present = detect_csrf_token(request_content)
if csrf_token_present:
    print("CSRF token is present in the request.")
else:
    print("CSRF token is not present in the request.")