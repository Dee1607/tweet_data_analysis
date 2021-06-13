var mysql = require('mysql');
var conn = mysql.createConnection({
  host: 'db-assignment2.csogz3jhmpaf.us-east-1.rds.amazonaws.com', // assign your host name
  user: 'deep',      //  assign your database username
  password: 'Dee16798p', //  assign your database password
  database: 'nodeapp' // assign database Name
}); 
conn.connect(function(err) {
  if (err) throw err;
  console.log('Database is connected successfully !');
});
module.exports = conn;