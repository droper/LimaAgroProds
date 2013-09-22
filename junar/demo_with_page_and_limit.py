from junar import ApiClient
auth_key = 'yourauthkey';
junar_api_client = ApiClient(auth_key)
datastream = junar_api_client.datastream('FARM-CROP-PRICE-BY-PARRI')
response = datastream.invoke(params = ['CLARENDON'], output = 'json_array', page = 0, limit = 10)
result = response['result']
for row in result:
    print row
