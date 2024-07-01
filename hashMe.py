import hashlib, json, sys

# Helper function that wraps the hashing algorithm
def hashMe(msg=""):
    # Make sure that the keys are sorted for consistent hashin
    if type(msg) != str:
        msg = json.dumps(msg, sort_keys = True)
    # To handle different Python versions
    if sys.version_info.major == 2:
        return unicode(hashlib.sha256(msg).hexdigest(), 'utf-8')
    else:
        return hashlib.sha256(str(msg).encode('utf-8')).hexdigest()