const { spawn } = require("child_process");

const py = spawn("python3", ["./accu.py", "https://www.accuweather.com/en/ir/tabriz/207308/current-weather/207308", "https://www.accuweather.com/en/ir/tabriz/207308/air-quality-index/207308"]);

// Read output
py.stdout.on("data", (data) => {
    console.log(`stdout: ${data}`);
});

// Read errors
py.stderr.on("data", (data) => {
    console.error(`stderr: ${data}`);
});

// When done
py.on("close", (code) => {
    console.log(`Python process exited with code ${code}`);
});

