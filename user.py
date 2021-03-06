import re
import hmac
import random
import hashlib

secret = "whatthehell"
USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
PASS_RE = re.compile(r"^.{3,20}$")
EMAIL_RE = re.compile(r"^[\S]+@[\S]+.[\S]+$")

def valid_username(username):
	return USER_RE.match(username)

def valid_password(password):
	return PASS_RE.match(password)

def hash_str(s):
	return hmac.new(secret,s).hexdigest()

def make_secure_val(s):
	return '%s|%s' %(s,hash_str(s))

def check_secure_val(h):
	val = h.split('|')[0]
	if h == make_secure_val(val):
		return val
def make_salt():
	return ''.join(random.choice(string.letters) for x in range(5))

def make_pw_hash(name, pw, salt = None):
	if not salt:
		salt = make_salt()
	h = hashlib.sha256(name + pw + salt).hexdigest()
	return '%s,%s' % (h,salt)

def valid_pw(name, pw, h):
	salt = h.split(',')[1]
	return h == make_pw_hash(name, pw, salt)