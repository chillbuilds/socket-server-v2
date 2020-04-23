const ipCheck = require('./modules/ipCheck')
const http = require('http')
const ws = require('ws')
const port = 7070
var PythonShell = require('python-shell').PythonShell
const scriptPath = '/home/pi/Desktop/temp-test.py'
let piip;

const wss = new ws.Server({noServer: true})

function accept(req, res) {
  if (!req.headers.upgrade || req.headers.upgrade.toLowerCase() != 'websocket') {
    res.end()
    return}
  
  if (!req.headers.connection.match(/\bupgrade\b/i)) {
    res.end()
    return}

  wss.handleUpgrade(req, req.socket, Buffer.alloc(0), onConnect)
}

function onConnect(ws) {
  setInterval(function(){
  var pyshell = new PythonShell(scriptPath)
    pyshell.on('message', function (temp) {
    ws.send(temp)})
  }, 1000)
  ws.on('message', function (message) {
    ws.send(message)
    console.log(message)
    }
)}

if (!module.parent) {
  http.createServer(accept).listen(port);
  console.log(`\nWebSocket server running on port ${port}\n`)
  piip = ipCheck()
  console.log(piip)
} else {
  exports.accept = accept
  console.log('WebSocket server failed')
}