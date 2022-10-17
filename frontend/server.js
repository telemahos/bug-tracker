const express = require('express')
const serveStatic = require('serve-static')
const path = require('path')

const app = express()

// here we configuring dist to serve app files
app.use('/', serveStatic(path.join(__dirname, '/dist')))

// this * route is to serve project on different page routes except root '/'
app.get('/', (req, res) => {
  res.send('Hello World!')
  res.sendFile(path.join(__dirname, '/dist/index.html'))
})

const port = process.env.PORT || 3001
app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})
