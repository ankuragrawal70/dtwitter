# dtwitter

Steps
1) virtualenv -p python3 dtwitter_vir
2) Create a database with appropriate name(eg- dtwitter)
3) Change database values in test_settings.py (db_name, db_user, db_password, db_host) respectively.

4)
----run----
pip install -r requirements.txt


5)
----run---
python manage.py migrate


6) API url is as follow:
https://www.getpostman.com/collections/8232cceebed11a7cc160

7) Way to access the APIs:
Steps:
(i) Register User using resgister API
(ii) GET auth token using token API.
(iii) Access APIs to create tweet, create comment and create likes





