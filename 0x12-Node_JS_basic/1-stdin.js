const readline = require('readline');

const x = readline.createInterface({ input: process.stdin, output: process.stdout });
x.question('Welcome to Holberton School, what is your name?\n', (resp) => {
  console.log(`Your name is: ${resp}`);
  if (!process.stdin.isTTY) {
    console.log('This important software is now closing');
  }
  x.close();
});
