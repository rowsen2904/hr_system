from rest_framework_simplejwt.tokens import AccessToken

def expired_token(token_str):
        try:
            return AccessToken(token_str)
        except:
            return None