
# Usage

[LINE Developers](https://developers.line.biz/)
1. Create account
2. Create LINE Login channel and get
	- Channel ID -> `client_id`
	- Channel secret -> `client_secret`
3. RUN `python main.py`
4. Set `Callback URL` to http://127.0.0.1:5001/auth/callback
5. Go to http://127.0.0.1:5001 and login
	
	*Note: if website shows BAD REQUEST, it means the client_id and clinet_secret is wrong*
6. Get the LINE user informations

