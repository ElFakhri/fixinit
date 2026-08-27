<script setup>
import { ref } from "vue";
import { useRouter } from "vue-router";
import { auth } from "/src/JS/firebase.js";
import { onAuthStateChanged } from "firebase/auth";

import {
  connectDataConnectEmulator,
  getDataConnect,
} from "firebase/data-connect";
import { addNewUser, connectorConfig } from "@dataconnect/generated";
import { mutationRef, executeMutation } from "firebase/data-connect";

const isLocalDev = import.meta.env.DEV && (window.location.hostname === "localhost" || window.location.hostname === "127.0.0.1");

if (isLocalDev) {
  connectDataConnectEmulator(getDataConnect(connectorConfig), "127.0.0.1", 9399);
}

const router = useRouter();
const lokasi = ref("");
const description = ref("");
const namaLengkap = ref("");
const picture = ref(null)
const email = ref("");

// current authenticated user (populated by onAuthStateChanged)
let user = null;

onAuthStateChanged(auth, (u) => {
  user = u;
  if (u && u.email) email.value = u.email;
});

// Simple wrapper to invoke the `addFormPengaduan` mutation on Data Connect
const dcInstance = getDataConnect(connectorConfig);
async function addFormPengaduan(vars) {
  const ref = mutationRef(dcInstance, 'addFormPengaduan', vars);
  return executeMutation(ref);
}

const tanganiForm = async () => {
  try {
    // Pastikan user sudah login
    if (!user) {
      alert("Silakan login terlebih dahulu.");
      router.push("/login");
      return;
    }

    // Simpan Pengaduan ke PostgreSQL Data Connect (Sekarang sudah di-lock ke Lokal!)
    await addFormPengaduan({
      id: user.uid,
      namaLengkap: namaLengkap.value,
      email: user.email || email.value,
      description: description.value,
      pictureUrl: picture.value,
      lokasi: lokasi.value
    });

    alert("Formulir berhasil dilapor, menunggu verifikasi!");
    router.push("/login");
  } catch (error) {
    console.error("Gagal registrasi:", error);
    alert("Pendaftaran gagal: " + error.message);
  }
};
</script>

<template>
  <div class="min-h-screen flex bg-white font-sans text-primary">
    <!-- Bagian Kiri: Visual / Banner (Disembunyikan di HP, Muncul di Desktop) -->
    <div
      class="hidden md:flex md:w-1/2 bg-yellow-400 flex-col justify-center items-center p-12 relative overflow-hidden"
    >
      <!-- Ornamen Dekorasi Sederhana -->
      <div
        class="absolute top-0 left-0 w-full h-full bg-white/10"
        style="clip-path: polygon(0 0, 100% 0, 100% 100%, 0 80%)"
      ></div>

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
          <h1 class="text-3xl font-extrabold mb-2 text-primary">
            Formulir Pengaduan
          </h1>
          <p class="text-gray-500 font-medium">
            Masukkan Nama, Deskripsi, Alamat Lokasi, dan Bukti Foto Anda untuk
            Melengkapi Formulir.
          </p>
        </div>

        <!-- Form -->
        <form @submit.prevent="tanganiForm" class="space-y-6">
          <div>
            <label for="text" class="block text-sm font-bold text-gray-700 mb-2"
              >Nama</label
            >
            <input
              type="text"
              v-model="namaLengkap"
              placeholder="Nama Lengkap"
              class="w-full px-5 py-4 rounded bg-gray-50 border border-gray-200 text-primary focus:bg-white focus:outline-none focus:ring-2 focus:ring-yellow-400 focus:border-transparent transition-all duration-300"
              required
            />
          </div>

          <!-- input Emmail Pengguna -->

          <div>
            <label for="text" class="block text-sm font-bold text-gray-700 mb-2"
              >Email</label
            >
            <input
              type="text"
              v-model="email"
              placeholder="contoh@gmail.com"
              class="w-full px-5 py-4 rounded bg-gray-50 border border-gray-200 text-primary focus:bg-white focus:outline-none focus:ring-2 focus:ring-yellow-400 focus:border-transparent transition-all duration-300"
              required
            />
          </div>


          <!-- Input Deskripsi -->
          <div>
            <label
              for="description"
              class="block text-sm font-bold text-gray-700 mb-2"
              >Deskripsi</label
            >
            <textarea
              type="teks"
              v-model="description"
              placeholder="Isi deskripsi"
              class="w-full px-5 py-4 rounded bg-gray-50 border border-gray-200 text-primary focus:bg-white focus:outline-none focus:ring-2 focus:ring-yellow-400 focus:border-transparent transition-all duration-300"
              required
            />
          </div>

          <!-- Input Lokasi -->
          <div>
            <label
              for="lokasi"
              class="block text-sm font-bold text-gray-700 mb-2"
              >Lokasi</label
            >
            <input
              type="text"
              v-model="lokasi"

              class="w-full px-5 py-4 rounded bg-gray-50 border border-gray-200 text-primary focus:bg-white focus:outline-none focus:ring-2 focus:ring-yellow-400 focus:border-transparent transition-all duration-300"
              required
            />
          </div>
          <div>
            <label
              for="picture"
              class="block text-sm font-bold text-gray-700 mb-2"
              ></label
            >
            <input
              type="file" @change="(e) => picture.value = $event.target.files[0]"
              class="w-full px-5 py-4 rounded bg-gray-50 border border-gray-200 text-primary focus:bg-white focus:outline-none focus:ring-2 focus:ring-yellow-400 focus:border-transparent transition-all duration-300"
              required
            />
          </div>

          <!-- Tombol Lapor -->
          <button
            type="submit"
            class="w-full bg-yellow-400 text-primary font-extrabold py-4 rounded shadow-lg hover:bg-yellow-500 hover:shadow-xl hover:-translate-y-0.5 transition-all duration-300 mt-4"
          >
            Lapor!
          </button>
        </form>
      </div>
    </div>
  </div>
</template>
