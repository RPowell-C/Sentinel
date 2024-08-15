const express = require('express');
const cors = require('cors');
const app = express();
const port = 3000;


app.use(cors());

const sampleData = {
    username: 'Sentinel',
    message: 'Testing'
};

app.get('/get-message', (req, res) => {
    res.json(sampleData);
});
app.listen(port, () => {
    console.log("server is up");
});
