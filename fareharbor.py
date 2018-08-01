"""
    We are implementing a `view` that must consume
    some external service (which we've mocked below). The service returns
    data that needs to be sanitized for client consumption -- in the
    below example it includes sensitive information like SSN. The
    exercises work through simple sanitizations, to slightly more complex
    ones, before asking that the interviewee try to define a general approach
    to solving the problem.
"""
def external_service(project_name):
    # Mock; in real life we use some information
    # about the project to, say, read from a
    # particular URL.
    return {
        'project': 'Sanitization Project',
        'users': [
            {
                'username': 'z',
                'email': 'z@fareharbor.com',
                'ssn': '111223333',
                'api_keys': [
                    {
                        'codename': 'tugboat',
                        'code': 'la8dfh47',
                    },
                    {
                        'codename': 'titanic',
                        'code': 'dg810fj3',
                    },
                ]
            },
            {
                'username': 'bk',
                'email': 'bryan@fareharbor.com',
                'ssn': '888990000',
                'api_keys': [],
            }
        ],
    }


sensitive_information = ['ssn', 'code']

def mask_ssn(dictionary):
    dictionary['ssn'] = '*****%s' % dictionary['ssn'][5:]

def remove_from_dictionary(key):
    def _remove(dictionary):
        dictionary.pop(key, None)
    return _remove
    
key_callback = {
    'ssn': mask_ssn,
    'code': remove_from_dictionary('code')
}

def sanitize(response):
    if isinstance(response, dict):
        for key in sensitive_information:
            if key in response:
                value = response.get(key)
                callback = key_callback.get(key)
                if callback:
                    callback(response)
        for key, value in response.items():
            sanitize(value)
    if isinstance(response, list):
        for i in response:
            sanitize(i)
    return response


def view(project_name):
    response = external_service(project_name)
    result = sanitize(response)
    return result


response = view('part 1')

# Part 2:
#
# Now, we still want to strip the codes, but let's replace the SSN with
# *****3333 (where 3333 is really the last 4).

assert response['users'][0]['ssn'] == '*****3333', 'last 4'
assert 'code' not in response['users'][0]['api_keys'][0], 'stripped first code'
assert 'code' not in response['users'][0]['api_keys'][1], 'stripped second code'
assert response['users'][1]['ssn'] == '*****0000', 'last 4'
