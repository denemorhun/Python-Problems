const express = require('express');
const app = express();

app.use(express.json());

app.listen(3000, () => console.log('Listening on port 3000.'));

// curl --get localhost:3000/hello
app.get('/hello', (req, res) => {
    console.log('Headers:', req.headers);
    console.log('Method:', req.method);
    res.send('Recieved GET request!\n');
});

// curl --header 'content-type: application/json' localhost:3000/hello --data '{"foo:"bar"}'
app.post('/hello', (req, res) => {
    console.log('Headers:', req.headers);
    console.log('Method:', req.method);
    console.log('Body', req.body);
    res.send('Recieved Post request!\n');

});