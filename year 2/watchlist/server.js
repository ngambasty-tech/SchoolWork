const express = require('express')
const app = express();
const PORT = 3000;

app.get("/", (req, res) =>{
    res.send('hello class!');
});

app.listen(PORT, () => {
    console.log(`app is running on port ${PORT}`)
})