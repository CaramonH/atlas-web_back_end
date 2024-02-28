// Connect to redis server and log a message for status

const redis = require('redis');
const client = redis.createClient();
const { promisify } = require('util');

client
  .on('connect', () => {
    console.log('Redis client connected to the server');
  })
  .on('error', (err) => {
    console.log('Redis client not connected to the server: ' + err);
  });

const setNewSchool = async (schoolName, value) => {
  const setAsync = promisify(client.set).bind(client);
  const result = await setAsync(schoolName, value);
  redis.print(null, result);
};

const displaySchoolValue = async (schoolName) => {
  const getAsync = promisify(client.get).bind(client);
  const result = await getAsync(schoolName);
  console.log(result);
};

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
