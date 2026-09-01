
<template>
  <div class="min-h-screen flex bg-white font-sans text-primary">
    
    <!-- Bagian Kiri: Visual / Banner (Disembunyikan di HP, Muncul di Desktop) -->
    <div class="hidden md:flex md:w-1/2 bg-yellow-400 flex-col justify-center items-center p-12 relative overflow-hidden">
      <!-- Ornamen Dekorasi Sederhana -->
      <div class="absolute top-0 left-0 w-full h-full bg-white/10" style="clip-path: polygon(0 0, 100% 0, 100% 100%, 0 80%);"></div>
      
      <div class="relative z-10 flex flex-col items-center text-center">
        <!-- Logo -->
        <div class="text-5xl font-extrabold tracking-tighter text-primary mb-6">
          <span>Fixin</span><span class="text-white drop-shadow-md">IT</span>
        </div>
        <h2 class="text-2xl font-bold text-primary mb-4">
          Selamat Datang Kembali!
        </h2>

        
       </div>
    </div>

    <!-- Bagian Kanan: Formulir Login -->
    <div class="w-full md:w-1/2 flex items-center justify-center p-8 md:p-12">
      <div class="w-full max-w-md">
        
        <!-- Header Form -->
        <div class="mb-10 text-center md:text-left">
          <h1 class="text-3xl font-extrabold mb-2 text-primary">Masuk ke Akun</h1>
          <p class="text-gray-500 font-medium">Masukkan email dan *password* Anda untuk melanjutkan.</p>
        </div>

        <!-- Form -->
        <form @submit.prevent="handleLogin" class="space-y-6">
          
          <!-- Input Email -->
          <div>
            <label for="email" class="block text-sm font-bold text-gray-700 mb-2">Alamat Email</label>
            <input 
              type="email" 
              id="email" 
              v-model="email"
              placeholder="contoh@email.com" 
              class="w-full px-5 py-4 rounded bg-gray-50 border border-gray-200 text-primary focus:bg-white focus:outline-none focus:ring-2 focus:ring-yellow-400 focus:border-transparent transition-all duration-300"
              required
            >
          </div>

          <!-- Input Password -->
          <div>
            <div class="flex justify-between items-center mb-2">
              <label for="password" class="block text-sm font-bold text-gray-700">Password</label>
              <a href="#" class="text-sm font-bold text-yellow-500 hover:text-yellow-600 transition-colors">Lupa Password?</a>
            </div>
            <input 
              type="password" 
              id="password" 
              v-model="password"
              placeholder="••••••••" 
              class="w-full px-5 py-4 rounded bg-gray-50 border border-gray-200 text-primary focus:bg-white focus:outline-none focus:ring-2 focus:ring-yellow-400 focus:border-transparent transition-all duration-300"
              required
            >
          </div>

          <!-- Tombol Login -->
          <button 
            type="submit" 
            class="w-full bg-yellow-400 text-primary font-extrabold py-4 rounded shadow-lg hover:bg-yellow-500 hover:shadow-xl hover:-translate-y-0.5 transition-all duration-300 mt-4"
          >
            MASUK
          </button>
          
        </form>

        <!-- Link Daftar -->
        <p class="text-center text-gray-500 font-medium mt-8">
          Belum punya akun? 
          <router-link to="/Register" class="text-primary font-bold hover:text-yellow-500 transition-colors">Daftar sekarang</router-link>
        </p>

      </div>
    </div>

  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { signInWithEmailAndPassword } from 'firebase/auth';
import { auth } from './JS/firebase.js'; 

const router = useRouter();

const email = ref('');
const password = ref('');

const handleLogin = async () => {
  try {
    const kredensialUser = await signInWithEmailAndPassword(auth, email.value, password.value);
    
    console.log("Berhasil login sebagai:", kredensialUser.user.email);
    if (user.value.role == 'admin') {
      router.push('/Admin'); // Sesuaikan dengan rute yang ada
    } else {
      router.push('/');
    }
    // router.push('/')
  } catch (error) {
    console.error("Gagal login:", error);
    
    alert("Login gagal. Pastikan email dan password yang dimasukkan sudah benar.");
  }
};
</script>

