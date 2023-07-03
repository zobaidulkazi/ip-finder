// If you're referring to converting the Python code into another programming language, such as JavaScript, it will require adapting the code to the syntax and libraries of the chosen language. Here's an example of how the IP finder code can be converted to JavaScript:

const dns = require('dns');
const http = require('http');

function getPrivateIP() {
  return new Promise((resolve, reject) => {
    dns.lookup(require('os').hostname(), (err, address) => {
      if (err) {
        reject(err);
      } else {
        resolve(address);
      }
    });
  });
}




console.log(`
\x1b[1m _____       ______ _           _           \x1b[0m
\x1b[1m|_   _|      |  ___(_)         | |          \x1b[0m
\x1b[1m  | | _ __   | |_   _ _ __   __| | ___ _ __ \x1b[0m
\x1b[1m  | || '_ \\  |  _| | | '_ \\ / _\` |/ _ \\ '__|\x1b[0m
\x1b[1m _| || |_) | | |   | | | | | (_| |  __/ |   \x1b[0m
\x1b[1m \\___/ .__/  \\_|   |_|_| |_|\\__,_|\\___|_|   \x1b[0m
\x1b[1m     | |                                    \x1b[0m
\x1b[1m     |_|                                    \x1b[0m

\x1b[1;33m    @@@@@@@ Tool Name ::IP Finder  @@@@@@@\x1b[0m
\x1b[0;36m        Why This tool :: IP Finder is a simple command-line tool written in\x1b[0m
\x1b[0;36m        Python/JavaScript that allows you to retrieve your \x1b[0m
\x1b[0;36m        private and public IP addresses.\x1b[0m
\x1b[0;36m        Contact with Me : \x1b[4;34m[GitHub](https://github.com/zobaidulkazi)\x1b[0m
\x1b[0;31m    @@@ Don't try to copy this project. \x1b[0m
\x1b[0;31m    All rights reserved by @zobaidulkazi.\x1b[0m

\x1b[1m1. Private IP\x1b[0m
\x1b[1m2. Public IP\x1b[0m
\x1b[1m3. Exit\x1b[0m
`);


function getPublicIP() {
  return new Promise((resolve, reject) => {
    http.get('http://ipinfo.io/ip', (res) => {
      let data = '';
      res.on('data', (chunk) => {
        data += chunk;
      });
      res.on('end', () => {
        resolve(data.trim());
      });
    }).on('error', (err) => {
      reject(err);
    });
  });
}

console.log('My IP Finder Boot In JavaScript');

function displayMenu() {
  console.log('\n1. Private IP');
  console.log('2. Public IP');
  console.log('3. Exit');
}

function getUserChoice() {
  return new Promise((resolve) => {
    const readline = require('readline');
    const rl = readline.createInterface({
      input: process.stdin,
      output: process.stdout,
    });
    rl.question('Enter Your Choice Number: ', (choice) => {
      rl.close();
      resolve(choice);
    });
  });
}

async function main() {
  while (true) {
    displayMenu();
    const choice = await getUserChoice();

    if (choice === '1') {
      try {
        const privateIP = await getPrivateIP();
        console.log('Your private IP is:', privateIP);
      } catch (err) {
        console.error('Error retrieving private IP:', err);
      }
    } else if (choice === '2') {
      try {
        const publicIP = await getPublicIP();
        console.log('Your public IP is:', publicIP);
      } catch (err) {
        console.error('Error retrieving public IP:', err);
      }
    } else if (choice === '3') {
      console.log('Exiting the program...');
      break;
    } else {
      console.log('Invalid choice. Please try again.');
    }
  }
}

main().catch((err) => {
  console.error('An error occurred:', err);
});


