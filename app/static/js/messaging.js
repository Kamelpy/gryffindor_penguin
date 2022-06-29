// Import the functions you need from the SDKs you need
import { initializeApp } from "https://www.gstatic.com/firebasejs/9.8.4/firebase-app.js";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyDJGVf7prpOFQglfuoN03aC1HDzB3Q0sIA",
  authDomain: "saigryffindor.firebaseapp.com",
  projectId: "saigryffindor",
  storageBucket: "saigryffindor.appspot.com",
  messagingSenderId: "808675770223",
  appId: "1:808675770223:web:67e52ddfdffcfa651fb29a",
  measurementId: "G-3WMT1RN9XV",
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);

import {
  getMessaging,
  getToken,
  onMessage,
} from "https://www.gstatic.com/firebasejs/9.8.4/firebase-messaging.js";

// Initialize Firebase Cloud Messaging and get a reference to the service
export const messaging = getMessaging(app);

let token;

async function requestPermission() {
  const permission = await Notification.requestPermission();

  if (permission === "granted") {
    console.log("Notification permission granted.");
    token = await getToken(messaging, {
      vapidKey:
        "BFHUvBq-O474KK8haGaxp-1RSGBwoxXSIhAwrJitAebXPfBGgbuR9zOZ5_Wsf3idO6PYpZjymz3ojAEiY6RbOf8",
    });
  }

  console.log(token);
}

document
  .getElementById("request-permission")
  .addEventListener("click", async () => {
    console.log("sii");
    await requestPermission();
  });

function showNotification(notification) {
  // Let's check if the browser supports notifications
  if (!("Notification" in window)) {
    alert("This browser does not support desktop notification");
  }

  // Let's check whether notification permissions have already been granted
  else if (Notification.permission === "granted") {
    // If it's okay let's create a notification
    console.log(notification);
    new Notification(notification.title, {
      body: notification.body,
      icon: notification.image,
    });
  }

  // Otherwise, we need to ask the user for permission
  else if (Notification.permission !== "denied") {
    Notification.requestPermission().then(function (permission) {
      // If the user accepts, let's create a notification
      if (permission === "granted") {
        new Notification(notification);
      }
    });
  }

  // At last, if the user has denied notifications, and you
  // want to be respectful there is no need to bother them anymore.
}

onMessage(messaging, (payload) => {
  console.log("message payload", payload);
  showNotification(payload.notification);
  //   alert(payload.notification.title);
});
