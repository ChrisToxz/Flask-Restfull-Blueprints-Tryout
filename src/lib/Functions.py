def return_error(code, msg, http):
    return {
        "code": code,
        "msg": msg
    }, http
