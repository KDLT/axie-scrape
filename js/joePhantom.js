var page = require('webpage').create();
var url = 'https://testguild.com/';
page.open(url, function (status) {
console.log(status);
phantom.exit();
});