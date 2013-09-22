from junar import ApiClient

if __name__ == '__main__':
    # display dates related to proposed law at Chilean senado
    guid = 'CONGR-DE-LA-PROYE-PUBLI'

    # get an auth_key at www.junar.com/developers/
    auth_key = 'yourauthkeyhere'
    junar_api_client = ApiClient(auth_key)

    # the guid (identificator)
    datastream = junar_api_client.datastream(guid)

    # the parameters are the date in chilean format
    response = datastream.invoke(params = ['01/01/2011', '01/12/2011'], output = 'json_array')
    result = response['result']

    # iterating the response and printing it
    for row in result:
        print '%s -> %s' % (row[4], row[1])
