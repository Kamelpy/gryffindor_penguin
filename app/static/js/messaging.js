// Import the functions you need from the SDKs you need
import { initializeApp } from "https://www.gstatic.com/firebasejs/9.8.4/firebase-app.js";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyDrpBOkhzCb0LC2xSEJf45YehgedGb8Hy0",
  authDomain: "gryffindor-ac591.firebaseapp.com",
  projectId: "gryffindor-ac591",
  storageBucket: "gryffindor-ac591.appspot.com",
  messagingSenderId: "316818368677",
  appId: "1:316818368677:web:21e3a322e4cbcb024cc54c",
  measurementId: "G-DVXQ9ZDL5Q"
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
        "BC9ydWNzRYTF-BTt78m0_bQakvC5xYXpQJjWYRWBkwdqrnZrcPpdo7nmlP8uVi14C66-RE3sae8iXg-IHu11YQI",
    });
  }
  return token;
  console.log(token);
}

document
  .getElementById("request-permission")
  .addEventListener("click", async () => {
    console.log("sii");
    token=await requestPermission();
    document.getElementById("token").value = token;
    const data = {token}
    const options = {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    };
    fetch("/recibir",options);;
    } 
  );

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
