// storing data in memory (hashmap)

const express = require('express');

const app = express();
app.use(express.json());

// to be used as kv pair db perhaps?
const hashtable = {};

app.listen(3000, () => {
    console.log('Listening on port 3000.');
});

// create key and assign the data from json body
// curl localhost:3000/memory/data --header 'Content-Type: application/json' --data '{"data":"bar"}'


app.post('/memory/:key', (req, res) => {
    console.log('Method:', req.method);
    console.log('Header', req.headers);
    console.log('Body:', req.body);
    // store the request body in the hashmap
    hashtable[req.params.key] = req.body.data;
    res.send("Recieved POST request\n");
});


// curl --get localhost:3000/memory/data
// if key is already in hashtable, send its value as part of response
app.get('/memory/:key', (req, res) => {
    console.log('Method:', req.method);
    // wonder what params does
    const key = req.params.key;
    if (key in hashtable) {
        console.log('Returning value from key: ', key, ", value: ", hashtable[key]);
        res.send(hashtable[key]);
        return;
    }
    // if key is not found
    console.log("Key doesn't exist in the hashmap");
    res.send('null');
});

