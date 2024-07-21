from django.contrib.auth import authenticate

from rest_framework_simplejwt.tokens import RefreshToken

def attempt_login(request, username : str, password : str) -> tuple[dict, int]:
    user = authenticate(request=request, username=username, password=password)

    if user is not None:
        if user.is_active:
            refresh = RefreshToken.for_user(user)
            
            return {"refresh" : str(refresh), 
                    "access" : str(refresh.access_token)
                    }, 200
        
        return {"error" : "User account is disabled."}, 403
    
    return {"error" : "Invalid username or password."}, 401