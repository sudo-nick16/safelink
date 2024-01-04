const UNSAFE_COLOR = "red";
const UNSAFE_IMAGE = "./images/unsafe.png";
const SAFE_COLOR = "green";
const SAFE_IMAGE = "./images/safe.png";
const API_URL = "http://localhost:3000";

const statusImage = document.getElementById("status-img");
const body = document.getElementsByTagName("body")[0];
const urlInput = document.getElementById("url");
const checkBtn = document.getElementById("check");

const setBorderColor = (color) => {
	body.style.border = "3px solid " + color;
}

const setStatusImage = (imgSrc) => {
	statusImage.src = imgSrc;
}

const setSafe = () => {
	setBorderColor(SAFE_COLOR);
	setStatusImage(SAFE_IMAGE);
}

const setUnSafe = () => {
	setBorderColor(UNSAFE_COLOR);
	setStatusImage(UNSAFE_IMAGE);
}

const fetchURLInfo = async (url) => {
	if (!url) {
		return;
	}
	try {
		const resp = await fetch(`${API_URL}/is-safe?url=${url}`, {
			mode: "cors"
		});
		const data = await resp.json();
		if (data.error || !data.safe) {
			setUnSafe();
			return;
		}
		setSafe();
	} catch (error) {
		console.log("[ERROR] ", error);
	}
}

const getCurrentTab = async () => {
    let queryOptions = { active: true, lastFocusedWindow: true };
    let [tab] = await chrome.tabs.query(queryOptions);
    return tab;
}

checkBtn.addEventListener('click', () => {
	if (!urlInput || !urlInput.value) {
		return;
	}
	fetchURLInfo(urlInput.value);
})

window.addEventListener('DOMContentLoaded', async () => {
	try {
		const tab = await getCurrentTab();
		urlInput.value = tab?.url || "";
		fetchURLInfo(tab?.url);
	} catch (error) {
		console.log("[ERROR] ", error);
	}
})
