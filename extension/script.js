const UNSAFE_COLOR = "red";
const UNSAFE_IMAGE = "./images/unsafe.png";
const SAFE_COLOR = "green";
const SAFE_IMAGE = "./images/safe.png";
const LOADING_COLOR = "yellow";
const LOADING_IMAGE = "./images/loading.png";
const ERROR_COLOR = "red";
const ERROR_IMAGE = "./images/error.png";
const API_URL = "http://localhost:5000";

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

const setError = () => {
	setBorderColor(ERROR_COLOR);
	setStatusImage(ERROR_IMAGE);
}

const setLoading = () => {
	setBorderColor(LOADING_COLOR);
	setStatusImage(LOADING_IMAGE);
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
		setLoading();
		const resp = await fetch(`${API_URL}/is-safe?url=${url}`, {
			mode: "cors"
		});
		const data = await resp.json();
		if (data.error) {
			setError();
			return;
		}
		if (!data.safe) {
			setUnSafe();
			return;
		}
		setSafe();
	} catch (error) {
		console.log("[ERROR] ", error);
		setError();
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

if (chrome && chrome.extension) {
	window.addEventListener('DOMContentLoaded', async () => {
		try {
			const tab = await getCurrentTab();
			urlInput.value = tab?.url || "";
			fetchURLInfo(tab?.url);
		} catch (error) {
			console.log("[ERROR] ", error);
			setError();
		}
	})
} else {
	body.style.position = "fixed";
	body.style.top = "50%";
	body.style.left = "50%";
	body.style.transform = "translate(-50%, -50%)";
}
