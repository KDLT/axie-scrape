var page = require('webpage').create(),
system = require('system'),
t, address;

var url = "https://axie.zone/card-tier-list";

if (system.args.length === 1) {
    console.log('Usage: loadspeed.js https://axie.zone/card-tier-list')
    phantom.exit();
}

t = Date.now();
address = system.args[1];
page.open(address, function(status) {
    if (status !== 'success') {
        console.log('FAIL to load the address');
    } else {
        t = Date.now() - t;
        console.log('Loading ' + system.args[1]);
        console.log('Loading time ' + t + ' msec');
        page.render('testload.png'); // render the page
    }
    phantom.exit();
})