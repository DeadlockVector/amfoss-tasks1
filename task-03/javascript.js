const n = 10;

for (let i = 1; i < n; i++) {
  let factors = 1;

  for (let j = 2; j <= i; j++) {
    if (i % j === 0) {
      factors += 1;
    }
  }

  if (factors === 2) {
    console.log(`${i} is a prime number`);
  }
}