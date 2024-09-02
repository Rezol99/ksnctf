
s = "EBG KVVV vf n fvzcyr yrggre fhofgvghgvba pvcure gung ercynprf n yrggre jvgu gur yrggre KVVV yrggref nsgre vg va gur nycunorg. EBG KVVV vf na rknzcyr bs gur Pnrfne pvcure, qrirybcrq va napvrag Ebzr. Synt vf SYNTFjmtkOWFNZdjkkNH. Vafreg na haqrefpber vzzrqvngryl nsgre SYNT."


# アスキーコードで文字をずらす

def rot13(s):
    result = ""
    for c in s:
        if c.islower():
            result += chr((ord(c) - ord('a') + 13) % 26 + ord('a'))
        elif c.isupper():
            result += chr((ord(c) - ord('A') + 13) % 26 + ord('A'))
        else:
            result += c
    return result


print(rot13(s))



