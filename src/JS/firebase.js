import { initializeApp } from "firebase/app";
import { getAuth, connectAuthEmulator } from "firebase/auth";
import { getStorage } from "firebase/storage";

const firebaseConfig = {
  apiKey: "AIzaSyAElsvsKz-KaZMzCK4Ckhnw35YnLWNdNV0",
  authDomain: "itechno-3c5fd.firebaseapp.com",
  projectId: "itechno-3c5fd",
  storageBucket: "itechno-3c5fd.firebasestorage.app",
  messagingSenderId: "802198839724",
  appId: "1:802198839724:web:c34394891bfceb08245a09",
  measurementId: "G-QKL586HJEQ"
};

const app = initializeApp(firebaseConfig);

export const auth = getAuth(app);
export const storage = getStorage(app);

const isLocalDev = import.meta.env.DEV && (window.location.hostname === "localhost" || window.location.hostname === "127.0.0.1");

if (isLocalDev) {
  connectAuthEmulator(auth, "http://127.0.0.1:9099");
}