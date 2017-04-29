cordova.define('cordova/plugin_list', function(require, exports, module) {
module.exports = [
    {
        "id": "cz.blocshop.socketsforcordova.Socket",
        "file": "plugins/cz.blocshop.socketsforcordova/socket.js",
        "pluginId": "cz.blocshop.socketsforcordova",
        "clobbers": [
            "window.Socket"
        ]
    },
    {
        "id": "org.apache.cordova.statusbar.statusbar",
        "file": "plugins/org.apache.cordova.statusbar/www/statusbar.js",
        "pluginId": "org.apache.cordova.statusbar",
        "clobbers": [
            "window.StatusBar"
        ]
    }
];
module.exports.metadata = 
// TOP OF METADATA
{
    "cz.blocshop.socketsforcordova": "0.1.0",
    "org.apache.cordova.statusbar": "0.1.8",
    "cordova-plugin-whitelist": "1.3.2",
    "cordova-plugin-console": "1.0.6"
};
// BOTTOM OF METADATA
});