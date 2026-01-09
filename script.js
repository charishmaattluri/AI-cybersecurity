function goToResult() {
    const btn = document.getElementById("analyzeBtn");
    btn.innerText = "Analyzing...";
    btn.disabled = true;

    const scenario = document.getElementById("scenario").value;
    localStorage.setItem("scenario", scenario);

    setTimeout(() => {
        window.location.href = "result.html";
    }, 400);
}


async function loadResult() {
    const scenario = localStorage.getItem("scenario");
    if (!scenario) return;

    try {
        const response = await fetch(`http://127.0.0.1:8000/${scenario}`);
        const data = await response.json();

        document.getElementById("riskLevel").innerText = data.risk_level;
        document.getElementById("riskScore").innerText = data.risk_score;
        document.getElementById("explanation").innerText = data.explanation;
        document.getElementById("action").innerText = data.recommended_action;
        document.getElementById("time").innerText ="Generated on " + new Date().toLocaleString();

    } catch {
        alert("Backend not reachable");
    }
}

function downloadReport() {
    const scenario = localStorage.getItem("scenario");

    const riskLevel = document.getElementById("riskLevel").innerText;
    const riskScore = document.getElementById("riskScore").innerText;
    const explanation = document.getElementById("explanation").innerText;
    const action = document.getElementById("action").innerText;
    const time = new Date().toLocaleString();

    const reportContent =
`AI CYBERSECURITY AGENT – THREAT REPORT

Scenario: ${scenario}
Generated on: ${time}

Risk Level: ${riskLevel}
Risk Score: ${riskScore}

Explanation:
${explanation}

Recommended Action:
${action}
`;

    const blob = new Blob([reportContent], { type: "text/plain" });
    const link = document.createElement("a");

    link.href = URL.createObjectURL(blob);
    link.download = "cybersecurity_report.txt";
    link.click();
}

function goBack() {
    window.location.href = "index.html";
}


window.onload = function () {
    if (document.getElementById("riskLevel")) {
        loadResult();
    }
};

