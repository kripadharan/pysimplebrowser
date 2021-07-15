console.log('In index.js');
// console.clear();

async function main() {
    const registration = await navigator.serviceWorker.register('worker.js');
    console.log(registration);
    for (let i = 1; i <= 10; i++) {
        console.log(`${i}\n`);
    }
}

main();
