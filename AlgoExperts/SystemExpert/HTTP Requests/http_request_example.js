const httprequest = {
    host: 'localhost',
    port: 8080,
    method: 'POST', // GET, PUT, DELETE, etc
    path: '/payments',
    headers: {
        // type of body 
        'content-type': 'application/json',
        'content-length': 51,
    },
    // data of the request 
    body: '{"data": "This is a piece of data in JSON format."}'
    }

    const httpResponse = {
        statusCode: 200,
        headers: {
            'access-control-allow-origin': 'https://www.algoexpert.io',
            'content-type': 'application/json',
        },
        body: '{}'
    }