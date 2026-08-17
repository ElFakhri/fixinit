// 1. Panggil fungsi inisialisasi dari Firebase
import { initializeApp } from "firebase/app";
// Pastikan connectAuthEmulator ikut di-import di sini
import { getAuth, connectAuthEmulator } from "firebase/auth"; 
import { getStorage } from "firebase/storage";

// 2. Tentukan dulu konfigurasi/kuncinya (Ditaruh DI ATAS sebelum dipakai)
const firebaseConfig = {
  apiKey: "AIzaSyAElsvsKz-KaZMzCK4Ckhnw35YnLWNdNV0",
  authDomain: "itechno-3c5fd.firebaseapp.com",
  projectId: "itechno-3c5fd",
  storageBucket: "itechno-3c5fd.firebasestorage.app",
  messagingSenderId: "802198839724",
  appId: "1:802198839724:web:c34394891bfceb08245a09",
  measurementId: "G-QKL586HJEQ"
};

// 3. Nyalakan mesin Firebase-nya menggunakan konfigurasi di atas
const app = initializeApp(firebaseConfig);

// 4. Inisialisasi layanan Auth dan Storage
export const auth = getAuth(app);
export const storage = getStorage(app);

// 5. Sambungkan Auth ke Local Emulator untuk tahap development
connectAuthEmulator(auth, "http://127.0.0.1:9099");