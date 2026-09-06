<template>
  <div class="min-h-screen bg-white text-primary font-sans">
    <!-- NAVBAR -->
    <nav class="sticky top-0 z-50 w-full bg-white px-8 md:px-12 py-6 flex items-center justify-between shadow-sm">
      <div class="text-3xl font-bold tracking-tight text-primary">
        <span>Fixin</span><span class="text-yellow-400">IT</span>
      </div>
      <div class="flex items-center gap-3">

        <!-- Sudah login -->
        <template v-if="user">
          <span class="text-sm font-bold text-primary">
            {{ user.namaLengkap || user.name || user.email }}
          </span>
          <router-link
            v-if="user.role === 'admin'"
            to="/Admin"
            class="bg-gray-900 text-white font-bold py-2.5 px-5 text-sm hover:bg-gray-700 transition-colors"
          >
            Dashboard
          </router-link>
          <router-link to="/form" class="bg-yellow-400 text-primary font-bold py-2.5 px-6 text-sm hover:bg-yellow-500 transition-colors">
            Laporkan
          </router-link>
          <button @click="logout" class="text-sm font-bold text-gray-400 hover:text-primary transition-colors">
            Keluar
          </button>
        </template>

        <!-- Belum login -->
        <template v-else>
          <router-link to="/login" class="font-bold text-sm text-primary hover:text-gray-500 transition-colors">
            Masuk
          </router-link>
          <router-link to="/form" class="bg-yellow-400 text-primary font-bold py-2.5 px-6 text-sm hover:bg-yellow-500 transition-colors">
            Laporkan
          </router-link>
        </template>

      </div>
    </nav>

    <!-- HERO SECTION -->
    <section class="flex flex-col md:flex-row min-h-[85vh]">
      <div class="w-full md:w-1/2 flex items-center justify-center p-12 md:p-16">
        <div class="max-w-lg">
          <h1 class="text-5xl md:text-6xl font-bold mb-6 leading-tight tracking-tight">
            Jalan Rusak?<br />
            <span class="text-yellow-400">Jangan Diam.</span>
          </h1>
          <p class="text-xl text-gray-500 leading-relaxed mb-8">
            Laporkan kerusakan infrastruktur di sekitar Anda dengan cepat demi keselamatan dan kenyamanan bersama.
          </p>
          <ul class="space-y-4 mb-10">
            <li class="flex items-start gap-3">
              <span class="mt-1 w-2 h-2 bg-yellow-400 rounded-full flex-shrink-0"></span>
              <span class="text-gray-600">Formulir sederhana, laporan langsung terkirim</span>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1 w-2 h-2 bg-yellow-400 rounded-full flex-shrink-0"></span>
              <span class="text-gray-600">Lampirkan foto bukti langsung dari ponsel</span>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1 w-2 h-2 bg-yellow-400 rounded-full flex-shrink-0"></span>
              <span class="text-gray-600">Tandai lokasi tepat dengan peta interaktif</span>
            </li>
          </ul>
          <router-link to="/form" class="inline-block bg-yellow-400 text-primary font-bold py-4 px-10 text-lg hover:bg-yellow-500 transition-colors">
            Laporkan Sekarang
          </router-link>
        </div>
      </div>
      <div class="w-full md:w-1/2 flex items-center justify-center p-12">
        <img src="/src/img/rusak.jpg" alt="Foto jalan rusak" class="jalanrusak rounded-lg" />
      </div>
    </section>

    <!-- FEATURES SECTION -->
    <section class="py-20 px-8 md:px-12 bg-gray-50">
      <div class="max-w-6xl mx-auto">
        <h2 class="text-3xl md:text-4xl font-bold text-center mb-4">Cara Kerja FixinIT</h2>
        <p class="text-gray-500 text-center mb-16 max-w-2xl mx-auto">Tiga langkah sederhana untuk membantu perbaikan infrastruktur di lingkungan Anda.</p>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
          <!-- Feature 1 -->
          <div class="bg-white p-8 text-center">
            <div class="w-16 h-16 bg-yellow-400 flex items-center justify-center mx-auto mb-6">
              <svg class="w-8 h-8 text-primary" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z" />
              </svg>
            </div>
            <h3 class="text-xl font-bold mb-3">Kirim Laporan</h3>
            <p class="text-gray-500">Isi formulir singkat, unggah foto, dan tandai lokasi kerusakan di peta.</p>
          </div>
          <!-- Feature 2 -->
          <div class="bg-white p-8 text-center">
            <div class="w-16 h-16 bg-yellow-400 flex items-center justify-center mx-auto mb-6">
              <svg class="w-8 h-8 text-primary" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
              </svg>
            </div>
            <h3 class="text-xl font-bold mb-3">Verifikasi</h3>
            <p class="text-gray-500">Tim kami memverifikasi setiap laporan untuk memastikan akurasi data.</p>
          </div>
          <!-- Feature 3 -->
          <div class="bg-white p-8 text-center">
            <div class="w-16 h-16 bg-yellow-400 flex items-center justify-center mx-auto mb-6">
              <svg class="w-8 h-8 text-primary" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" d="M9 20l-5.447-2.724A1 1 0 013 16.382V5.618a1 1 0 011.447-.894L9 7m0 13l6-3m-6 3V7m6 10l4.553 2.276A1 1 0 0021 18.382V7.618a1 1 0 00-.553-.894L15 4m0 13V4m0 0L9 7" />
              </svg>
            </div>
            <h3 class="text-xl font-bold mb-3">Pantau Progres</h3>
            <p class="text-gray-500">Lihat status laporan Anda dan pantau proses perbaikan secara transparan.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- CTA SECTION -->
    <section class="py-20 px-8 md:px-12 bg-white text-center">
      <div class="max-w-3xl mx-auto">
        <h2 class="text-3xl md:text-4xl font-bold mb-6">Satu laporan Anda menentukan prioritas perbaikan.</h2>
        <p class="text-gray-500 text-lg mb-10">Jangan tunda lagi. Bersama kita wujudkan infrastruktur yang lebih aman.</p>
        <router-link to="/form" class="inline-block bg-yellow-400 text-primary font-bold py-4 px-12 text-lg hover:bg-yellow-500 transition-colors">
          Laporkan Sekarang
        </router-link>
      </div>
    </section>

    <!-- FOOTER -->
    <footer class="bg-yellow-400 text-black py-16 px-8 md:px-12">
      <div class="max-w-7xl mx-auto">
        <div class="grid grid-cols-1 md:grid-cols-4 gap-12 md:gap-8">
          <div class="md:col-span-2">
            <h6 class="text-sm uppercase tracking-[2px] font-bold mb-5">Tentang FixinIT</h6>
            <p class="text-justify text-sm leading-relaxed max-w-lg text-black/70">
              FixinIT adalah inisiatif untuk membantu masyarakat melaporkan kerusakan infrastruktur dengan cepat demi keselamatan bersama. Kami berfokus pada penyediaan platform yang efisien dan transparan untuk menghubungkan warga dengan otoritas terkait.
            </p>
          </div>
          <div>
            <h6 class="text-sm uppercase tracking-[2px] font-bold mb-5">Layanan</h6>
            <ul class="space-y-3 text-sm text-black/70">
              <li><a href="#" class="hover:text-yellow-400 transition-colors">Pengaduan Jalan</a></li>
              <li><a href="#" class="hover:text-yellow-400 transition-colors">Peta Interaktif</a></li>
              <li><a href="#" class="hover:text-yellow-400 transition-colors">Cek Status Laporan</a></li>
              <li><a href="#" class="hover:text-yellow-400 transition-colors">Statistik Perbaikan</a></li>
            </ul>
          </div>
          <div>
            <h6 class="text-sm uppercase tracking-[2px] font-bold mb-5">Tautan Cepat</h6>
            <ul class="space-y-3 text-sm text-black/70">
              <li><a href="#" class="hover:text-yellow-400 transition-colors">Tentang Kami</a></li>
              <li><a href="#" class="hover:text-yellow-400 transition-colors">Kontak Kami</a></li>
              <li><a href="#" class="hover:text-yellow-400 transition-colors">Pusat Bantuan</a></li>
              <li><a href="#" class="hover:text-yellow-400 transition-colors">Kebijakan Privasi</a></li>
            </ul>
          </div>
        </div>
        <hr class="border-t border-white/20 my-8" />
        <div class="flex flex-col md:flex-row justify-between items-center gap-6">
          <div class="text-sm text-center md:text-left text-black/70">
            Copyright &copy; 2026 Hak Cipta Dilindungi oleh <a href="#" class="text-yellow-400 font-bold hover:text-white transition-colors">FixinIT</a>.
          </div>
          <ul class="flex space-x-4">
            <li>
              <a href="#" class="w-10 h-10 flex items-center justify-center bg-white/10 text-white hover:bg-yellow-400 transition-colors duration-300">
                <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24"><path fill-rule="evenodd" d="M22 12c0-5.523-4.477-10-10-10S2 6.477 2 12c0 4.991 3.657 9.128 8.438 9.878v-6.987h-2.54V12h2.54V9.797c0-2.506 1.492-3.89 3.777-3.89 1.094 0 2.238.195 2.238.195v2.46h-1.26c-1.243 0-1.63.771-1.63 1.562V12h2.773l-.443 2.89h-2.33v6.988C18.343 21.128 22 16.991 22 12z" clip-rule="evenodd" /></svg>
              </a>
            </li>
            <li>
              <a href="#" class="w-10 h-10 flex items-center justify-center bg-white/10 text-white hover:bg-yellow-400 transition-colors duration-300">
                <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24"><path d="M8.29 20.251c7.547 0 11.675-6.253 11.675-11.675 0-.178 0-.355-.012-.53A8.348 8.348 0 0022 5.92a8.19 8.19 0 01-2.357.646 4.118 4.118 0 001.804-2.27 8.224 8.224 0 01-2.605.996 4.107 4.107 0 00-6.993 3.743 11.65 11.65 0 01-8.457-4.287 4.106 4.106 0 001.27 5.477A4.072 4.072 0 012.8 9.713v.052a4.105 4.105 0 003.292 4.022 4.095 4.095 0 01-1.853.07 4.108 4.108 0 003.834 2.85A8.233 8.233 0 012 18.407a11.616 11.616 0 006.29 1.84" /></svg>
              </a>
            </li>
            <li>
              <a href="#" class="w-10 h-10 flex items-center justify-center bg-white/10 text-white hover:bg-yellow-400 transition-colors duration-300">
                <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24"><path fill-rule="evenodd" d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z" clip-rule="evenodd" /></svg>
              </a>
            </li>
          </ul>
        </div>
      </div>
    </footer>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const user = ref(null)

onMounted(() => {
  const stored = localStorage.getItem('user')
  if (stored) user.value = JSON.parse(stored)
})

const logout = () => {
  localStorage.removeItem('token')
  localStorage.removeItem('user')
  user.value = null
  router.push('/')
}
</script>