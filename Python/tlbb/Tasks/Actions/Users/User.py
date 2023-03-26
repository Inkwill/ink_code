
_accountdic = {}

def getUserAccount(accountstartwith):
    global _accountdic
    if _accountdic.has_key(accountstartwith):
        _accountdic[accountstartwith] = _accountdic[accountstartwith] + 1
    else:
        _accountdic[accountstartwith] = accountstartwith
    return _accountdic[accountstartwith]
