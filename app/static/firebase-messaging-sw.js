// [START initialize_firebase_in_sw]
// Give the service worker access to Firebase Messaging.
// Note that you can only use Firebase Messaging here, other Firebase libraries
// are not available in the service worker.
importScripts(
  "https://www.gstatic.com/firebasejs/9.8.4/firebase-app-compat.js"
);
importScripts(
  "https://www.gstatic.com/firebasejs/9.8.4/firebase-messaging-compat.js"
);

// Initialize the Firebase app in the service worker by passing in the
// messagingSenderId.
firebase.initializeApp({
  apiKey: "AIzaSyDJGVf7prpOFQglfuoN03aC1HDzB3Q0sIA",
  authDomain: "saigryffindor.firebaseapp.com",
  projectId: "saigryffindor",
  storageBucket: "saigryffindor.appspot.com",
  messagingSenderId: "808675770223",
  appId: "1:808675770223:web:67e52ddfdffcfa651fb29a",
  measurementId: "G-3WMT1RN9XV",
});

// Retrieve an instance of Firebase Messaging so that it can handle background
// messages.
const messaging = firebase.messaging();
// [END initialize_firebase_in_sw]

// If you would like to customize notifications that are received in the
// background (Web app is closed or not in browser focus) then you should
// implement this optional method.
// [START background_handler]
messaging.onBackgroundMessage(function (payload) {
  console.log(
    "[firebase-messaging-sw.js] Received background message ",
    payload
  );
  // Customize notification here
  const notificationTitle = "Background Message Title";
  const notificationOptions = {
    body: "Background Message body.",
  };

  return self.registration.showNotification(
    notificationTitle,
    notificationOptions
  );
});
// [END background_handler]