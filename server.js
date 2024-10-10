var http = require('http')

var port = 80

var server = http.createServer(function (request, response) {
  // Intentionally throwing an error to simulate a 500 Internal Server Error
  response.writeHead(500, {'Content-Type': 'text/plain'})
  response.end('Internal Server Error\n')
})

server.listen(port)

console.log('Server running at http://localhost:' + port)
