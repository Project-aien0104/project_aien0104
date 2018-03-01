var PythonShell = require('python-shell');
var options = {
    mode: 'json',
    pythonOptions: ['-u'],
    scriptPath: './',
};
var test =  new PythonShell('messenger.py', options);
test.on('message',function (message) {
    console.log(message);
});
