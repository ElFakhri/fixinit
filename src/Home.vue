<template>
  <div class="min-h-screen bg-white text-primary">
    <!-- NAVBAR -->
    <nav
      class="sticky top-0 z-50 w-full bg-white px-8 md:px-12 py-6 flex items-center justify-between shadow-sm"
    >
      <!-- Kiri: Nama Web -->
      <div class="text-3xl font-bold tracking-tight text-primary">
        <span>Fixin</span><span class="text-yellow-400">IT</span>
      </div>

      <!-- Kanan: Menu Navigasi -->
      <div class="flex items-center space-x-3">
        <router-link
          to="/login"
          class="font-bold text-primary hover:text-gray-500 transition-colors"
        >
          Login
        </router-link>
        <router-link
          to="/form"
          class="text-yellow-400 font-bold py-3 px-8 hover:text-black transition-colors"
        >
          Laporkan
        </router-link>
      </div>
    </nav>

    <!-- SECTION 1: Teks di Kiri, Blok Warna di Kanan -->
    <section class="flex flex-col md:flex-row h-screen max-h-500">
      <div
        class="w-full md:w-1/2 flex items-center justify-center p-12 bg-white"
      >
        <div class="max-w-md">
          <h1
            class="text-5xl md:text-6xl font-bold mb-6 leading tracking-tight"
          >
            Jalan Rusak? <br />
            <span class="text-yellow-400">Jangan Diam.</span>
          </h1>
          <p class="text-xl text-gray-500 leading-relaxed">
            Laporkan kerusakan infrastruktur di sekitar Anda dengan cepat demi
            keselamatan dan kenyamanan bersama.
          </p>
        </div>
      </div>
      <div class="w-full md:w-1/2 flex items-center justify-center">
        <!-- Blok visual sederhana (bisa diganti gambar nanti) -->
        <div class="w-3/4 h-3/4 bg-white/10 rounded-none">
          <img
            src="/src/img/rusak.jpg"
            alt="Foto jalan rusak"
            class="jalanrusak"
          />
        </div>
      </div>
    </section>

    <!-- SECTION 2: 1 Kolom, Teks di Tengah, Tombol di Bawah -->
    <section
      class="flex flex-col items-center justify-center h-screen max-h-500 bg-white p-12"
    >
      <div class="max-w-3xl text-center">
        <h2 class="text-4xl font-bold leading-snug mb-8 text-primary">
          Satu laporan Anda menentukan prioritas perbaikan.
        </h2>

        <button
          class="bg-yellow-400 text-white font-bold py-6 rounded-s px-12 text-xl hover:bg-opacity-90 transition-colors shadow-lg hover:shadow-xl"
        >
          <router-link to="/form"> Laporkan Sekarang </router-link>
        </button>
      </div>
    </section>

    <!-- SECTION 3: Teks di Kiri, Blok Warna di Kanan -->
    <section class="flex flex-col md:flex-row h-screen max-h-500">
      <div
        class="w-full md:w-1/2 flex items-center justify-center p-12 bg-white"
      >
        <div class="max-w-md">
          <h2 class="text-4xl font-bold leading-snug">
            Pantau status laporan secara transparan.
          </h2>
        </div>
      </div>
      <div
        class="w-full md:w-1/2 bg-yellow-50 flex items-center justify-center p-12"
      >
        <!-- Blok visual sederhana -->
        <svg
          class="w-56 h-56 text-yellow-400 hover:-translate-y-2 transition-transform duration-500"
          fill="none"
          stroke="currentColor"
          stroke-width="1"
          viewBox="0 0 24 24"
          xmlns="http://www.w3.org/2000/svg"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            d="M9 12l2 2 4-4M7.835 4.697a3.42 3.42 0 001.946-.806 3.42 3.42 0 014.438 0 3.42 3.42 0 001.946.806 3.42 3.42 0 013.138 3.138 3.42 3.42 0 00.806 1.946 3.42 3.42 0 010 4.438 3.42 3.42 0 00-.806 1.946 3.42 3.42 0 01-3.138 3.138 3.42 3.42 0 00-1.946.806 3.42 3.42 0 01-4.438 0 3.42 3.42 0 00-1.946-.806 3.42 3.42 0 01-3.138-3.138 3.42 3.42 0 00-.806-1.946 3.42 3.42 0 010-4.438 3.42 3.42 0 00.806-1.946 3.42 3.42 0 013.138-3.138z"
          ></path>
        </svg>
      </div>
    </section>

    <!-- SECTION 4: Blok Warna di Kiri, Teks di Kanan -->
    <section class="flex flex-col md:flex-row h-screen max-h-500">
      <div
        class="w-full md:w-1/2 bg-yellow-50 flex items-center justify-center p-12"
      >
        <!-- Vektor Art: Ilustrasi Peta/Map -->
        <svg
          class="w-56 h-56 text-yellow-500 drop-shadow-lg hover:scale-110 transition-transform duration-500"
          fill="none"
          stroke="currentColor"
          stroke-width="1"
          viewBox="0 0 24 24"
          xmlns="http://www.w3.org/2000/svg"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            d="M9 20l-5.447-2.724A1 1 0 013 16.382V5.618a1 1 0 011.447-.894L9 7m0 13l6-3m-6 3V7m6 10l4.553 2.276A1 1 0 0021 18.382V7.618a1 1 0 00-.553-.894L15 4m0 13V4m0 0L9 7"
          ></path>
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            d="M12 11c0 1.657-1.343 3-3 3S6 12.657 6 11s1.343-3 3-3 3 1.343 3 3z"
          ></path>
        </svg>
      </div>
      <div
        class="w-full md:w-1/2 flex items-center justify-center p-12 bg-white"
      >
        <div class="max-w-md">
          <h2 class="text-4xl font-bold leading-snug">
            Peta interaktif sebaran kerusakan jalan.
          </h2>
        </div>
      </div>
    </section>
    <!-- FOOTER BARU -->
    <footer class="bg-yellow-400 text-gray-300 py-16 px-8 md:px-12">
      <div class="max-w-7xl mx-auto">
        <!-- Bagian Atas: Grid Informasi -->
        <div class="grid grid-cols-1 md:grid-cols-4 gap-12 md:gap-8">
          <!-- Tentang (Memakan 2 kolom) -->
          <div class="md:col-span-2">
            <h6
              class="text-white text-sm uppercase tracking-[2px] font-bold mb-5"
            >
              Tentang FixinIT
            </h6>
            <p class="text-justify text-sm leading-relaxed max-w-lg text-white">
              FixinIT adalah inisiatif untuk membantu masyarakat melaporkan
              kerusakan infrastruktur dengan cepat demi keselamatan bersama.
              Kami berfokus pada penyediaan platform yang efisien dan transparan
              untuk menghubungkan warga dengan otoritas terkait.
            </p>
          </div>

          <!-- Kategori / Layanan -->
          <div>
            <h6
              class="text-white text-sm uppercase tracking-[2px] font-bold mb-5"
            >
              Layanan
            </h6>
            <ul class="space-y-3 text-sm text-white">
              <li>
                <a
                  href="#"
                  class="hover:text-yellow-400 hover:pl-1 transition-all duration-300"
                  >Pengaduan Jalan</a
                >
              </li>
              <li>
                <a
                  href="#"
                  class="hover:text-yellow-400 hover:pl-1 transition-all duration-300"
                  >Peta Interaktif</a
                >
              </li>
              <li>
                <a
                  href="#"
                  class="hover:text-yellow-400 hover:pl-1 transition-all duration-300"
                  >Cek Status Laporan</a
                >
              </li>
              <li>
                <a
                  href="#"
                  class="hover:text-yellow-400 hover:pl-1 transition-all duration-300"
                  >Statistik Perbaikan</a
                >
              </li>
            </ul>
          </div>

          <!-- Tautan Cepat -->
          <div>
            <h6
              class="text-white text-sm uppercase tracking-[2px] font-bold mb-5"
            >
              Tautan Cepat
            </h6>
            <ul class="space-y-3 text-sm text-white">
              <li>
                <a
                  href="#"
                  class="hover:text-yellow-400 hover:pl-1 transition-all duration-300"
                  >Tentang Kami</a
                >
              </li>
              <li>
                <a
                  href="#"
                  class="hover:text-yellow-400 hover:pl-1 transition-all duration-300"
                  >Kontak Kami</a
                >
              </li>
              <li>
                <a
                  href="#"
                  class="hover:text-yellow-400 hover:pl-1 transition-all duration-300"
                  >Pusat Bantuan</a
                >
              </li>
              <li>
                <a
                  href="#"
                  class="hover:text-yellow-400 hover:pl-1 transition-all duration-300"
                  >Kebijakan Privasi</a
                >
              </li>
            </ul>
          </div>
        </div>

        <!-- Garis Pemisah -->
        <hr class="border-t border-white/20 my-8" />

        <!-- Bagian Bawah: Copyright & Sosial Media -->
        <div
          class="flex flex-col md:flex-row justify-between items-center gap-6"
        >
          <!-- Copyright -->
          <div class="text-sm text-center md:text-left">
            Copyright &copy; 2026 Hak Cipta Dilindungi oleh
            <a
              href="#"
              class="text-yellow-400 font-bold hover:text-white transition-colors"
              >FixinIT</a
            >.
          </div>

          <!-- Ikon Sosial Media -->
          <ul class="flex space-x-4">
            <!-- Facebook -->
            <li>
              <a
                href="#"
                class="w-10 h-10 flex items-center justify-center rounded-full bg-white/10 text-white hover:bg-[#3b5998] hover:text-white transition-colors duration-300"
              >
                <svg
                  class="w-5 h-5"
                  fill="currentColor"
                  viewBox="0 0 24 24"
                  aria-hidden="true"
                >
                  <path
                    fill-rule="evenodd"
                    d="M22 12c0-5.523-4.477-10-10-10S2 6.477 2 12c0 4.991 3.657 9.128 8.438 9.878v-6.987h-2.54V12h2.54V9.797c0-2.506 1.492-3.89 3.777-3.89 1.094 0 2.238.195 2.238.195v2.46h-1.26c-1.243 0-1.63.771-1.63 1.562V12h2.773l-.443 2.89h-2.33v6.988C18.343 21.128 22 16.991 22 12z"
                    clip-rule="evenodd"
                  />
                </svg>
              </a>
            </li>
            <!-- Twitter/X -->
            <li>
              <a
                href="#"
                class="w-10 h-10 flex items-center justify-center rounded-full bg-white/10 text-white hover:bg-[#00aced] hover:text-white transition-colors duration-300"
              >
                <svg
                  class="w-5 h-5"
                  fill="currentColor"
                  viewBox="0 0 24 24"
                  aria-hidden="true"
                >
                  <path
                    d="M8.29 20.251c7.547 0 11.675-6.253 11.675-11.675 0-.178 0-.355-.012-.53A8.348 8.348 0 0022 5.92a8.19 8.19 0 01-2.357.646 4.118 4.118 0 001.804-2.27 8.224 8.224 0 01-2.605.996 4.107 4.107 0 00-6.993 3.743 11.65 11.65 0 01-8.457-4.287 4.106 4.106 0 001.27 5.477A4.072 4.072 0 012.8 9.713v.052a4.105 4.105 0 003.292 4.022 4.095 4.095 0 01-1.853.07 4.108 4.108 0 003.834 2.85A8.233 8.233 0 012 18.407a11.616 11.616 0 006.29 1.84"
                  />
                </svg>
              </a>
            </li>
            <!-- LinkedIn -->
            <li>
              <a
                href="#"
                class="w-10 h-10 flex items-center justify-center rounded-full bg-white/10 text-white hover:bg-[#007bb6] hover:text-white transition-colors duration-300"
              >
                <svg
                  class="w-5 h-5"
                  fill="currentColor"
                  viewBox="0 0 24 24"
                  aria-hidden="true"
                >
                  <path
                    fill-rule="evenodd"
                    d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"
                    clip-rule="evenodd"
                  />
                </svg>
              </a>
            </li>
          </ul>
        </div>
      </div>
    </footer>
  </div>
</template>

<script>
import { log } from "firebase/firestore/pipelines";
import { auth, storage } from "./JS/firebase.js";
import LoginPage from "./Login.vue";
import RegisterPage from "./Register.vue";

export default {
  name: "App",
  components: {
    LoginPage,
  },
  method: {
    cobaLogin() {
      console.log("test firebase work", auth);
    },
  },
  components: {
    RegisterPage,
  },
  method: {
    TestRegister() {
      console.log("test firebase2 work", auth);
    },
  },
};

// export default {
//   name: 'HomePage',

// }
</script>