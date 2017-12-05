const info = require('../inputs/1.json');
const devices = info.devices;
const bans = info.bans;

const acceptable = devices.filter(device => bans.every(ban => device[ban.key] !== ban.value));
console.log(acceptable.length);
