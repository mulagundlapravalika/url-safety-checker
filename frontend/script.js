async function checkURL() {
    const url = document.getElementById("url").value;

    let has_https = url.startsWith("https") ? 1 : 0;
    let has_ip = /\\d+\\.\\d+\\.\\d+\\.\\d+/.test(url) ? 1 : 0;
    let has_at_symbol = url.includes("@") ? 1 : 0;

    const response = await fetch("http://127.0.0.1:5000/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            has_https,
            has_ip,
            has_at_symbol
        })
    });

    const data = await response.json();
    document.getElementById("result").innerText = data.prediction;
}
}