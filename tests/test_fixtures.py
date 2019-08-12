def test_requests_client(testdir):
    testdir.makepyfile("""
def test_get(requests_client):
    response = requests_client.get('https://httpstat.us/200')
    response.raise_for_status()

def test_get_failed(requests_client):
    response = requests_client.get('https://httpstat.us/404')
    response.raise_for_status()
""")

    result = testdir.runpytest()
    result.assert_outcomes(passed=1, failed=1)
