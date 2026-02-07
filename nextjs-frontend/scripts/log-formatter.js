const readline = require('readline');

function getTimestamp() {
  const now = new Date();
  const year = now.getFullYear();
  const month = String(now.getMonth() + 1).padStart(2, '0');
  const day = String(now.getDate()).padStart(2, '0');
  const hours = String(now.getHours()).padStart(2, '0');
  const minutes = String(now.getMinutes()).padStart(2, '0');
  const seconds = String(now.getSeconds()).padStart(2, '0');

  return `${year}-${month}-${day} ${hours}-${minutes}-${seconds}`;
}

const rl = readline.createInterface({
  input: process.stdin,
  terminal: false
});

rl.on('line', (line) => {
  // Prefix every line with the timestamp
  // We use [INFO] as a default level for these system/piped logs
  console.log(`[${getTimestamp()}] [INFO] ${line}`);
});
