const express = require('express');
const bodyParser = require('body-parser');

const app = express();
const PORT = 3000;

// Middleware
app.use(bodyParser.json());

//students array
const students = [
  { id: 1, name: 'Alice Johnson', major: 'Computer Science' },
  { id: 2, name: 'Bob Smith', major: 'Software Engineering' },
  { id: 3, name: 'Charlie Brown', major: 'Data Science' },
  { id: 4, name: 'Diana Prince', major: 'Cybersecurity' }
];


app.get('/', (req, res) => {
  res.json({ message: 'Welcome to my API', version: '1.0' });
});
app.get('/about', (req, res) => {
  res.json({
    name: 'Muluh Teneng Faith Jr',
    course: 'Advanced Web Development'
  });
});

app.get('/students', (req, res) => {
  res.json(students);
});
app.get('/students/:id', (req, res) => {
  const id = parseInt(req.params.id);
  const student = students.find(s => s.id === id);

  if (student) {
    res.json(student);
  } else {
    res.status(404).json({ error: 'Student not found' });
  }
});

app.post('/students', (req, res) => {
  console.log('Received Student Data:', req.body);
  res.json({ status: 'received' });
});
app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
