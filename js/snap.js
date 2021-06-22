// console.log('Hello, world!');
// phantom.exit();

var page = require('webpage').create();
page.open('http://axie.zone/card-tier-list', function(status) {
    console.log("Status: " + status);
    if(status === "success") {
        page.render('example.png');
    }
    phantom.exit();
});