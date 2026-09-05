<script setup>
import { ref, nextTick } from "vue";
import { useRouter } from "vue-router";
import api from './api.js';

const router = useRouter();

// --- Form Data ---
const email = ref("");
const description = ref("");
const lokasi = ref("");
const picture = ref(null);
const picturePreview = ref(null);

// --- Step Control ---
const currentStep = ref(1);
const TOTAL_STEPS = 5;

const nextStep = () => { if (currentStep.value < TOTAL_STEPS) currentStep.value++; };
const prevStep = () => { if (currentStep.value > 1) currentStep.value--; };

// --- File Upload ---
const onFileChange = (e) => {
  const file = e.target.files && e.target.files[0] ? e.target.files[0] : null;
  picture.value = file;
  if (file) {
    const reader = new FileReader();
    reader.onload = (ev) => { picturePreview.value = ev.target.result; };
    reader.readAsDataURL(file);
  } else {
    picturePreview.value = null;
  }
};

// --- Map & Photon ---
const showMap = ref(false);
let mapInstance = null;
let markerInstance = null;
const mapInitialized = ref(false);
const photonQuery = ref("");
const photonResults = ref([]);

const openMap = async () => {
  showMap.value = true;
  await nextTick();
  if (!mapInitialized.value) {
    initMap();
  } else {
    await new Promise((r) => setTimeout(r, 200));
    if (mapInstance && mapInstance.invalidateSize) {
      mapInstance.invalidateSize(true);
      if (markerInstance) {
        mapInstance.setView(markerInstance.getLatLng(), mapInstance.getZoom());
      }
    }
  }
};

const initMap = () => {
  mapInitialized.value = true;
  mapInstance = L.map("photon-map").setView([0, 0], 2);
  L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
    maxZoom: 19,
    attribution: '© OpenStreetMap contributors',
  }).addTo(mapInstance);
  mapInstance.on("click", async (e) => {
    placeMarker(e.latlng.lat, e.latlng.lng);
    await reverseGeocode(e.latlng.lat, e.latlng.lng);
  });
};

const placeMarker = (lat, lon) => {
  if (markerInstance) {
    markerInstance.setLatLng([lat, lon]);
  } else {
    markerInstance = L.marker([lat, lon], { draggable: true }).addTo(mapInstance);
    markerInstance.on("dragend", async (ev) => {
      const p = ev.target.getLatLng();
      await reverseGeocode(p.lat, p.lng);
    });
  }
  mapInstance.setView([lat, lon], 15);
};

const reverseGeocode = async (lat, lon) => {
  try {
    const res = await fetch(`https://photon.komoot.io/reverse?lat=${lat}&lon=${lon}`);
    const data = await res.json();
    if (data && data.features && data.features.length) {
      const props = data.features[0].properties;
      lokasi.value = [props.name || "", props.city || props.state || "", props.country || ""]
        .filter(Boolean).join(", ");
    } else {
      lokasi.value = `${lat.toFixed(6)}, ${lon.toFixed(6)}`;
    }
  } catch {
    lokasi.value = `${lat.toFixed(6)}, ${lon.toFixed(6)}`;
  }
};

const searchPhoton = async () => {
  const q = photonQuery.value.trim();
  if (!q) return;
  try {
    const res = await fetch(`https://photon.komoot.io/api/?q=${encodeURIComponent(q)}&limit=5`);
    const data = await res.json();
    photonResults.value = (data.features || []).map((f) => ({
      label: f.properties.name + (f.properties.city ? ", " + f.properties.city : ""),
      lat: f.geometry.coordinates[1],
      lon: f.geometry.coordinates[0],
      props: f.properties,
    }));
  } catch {
    photonResults.value = [];
  }
};

const selectPhotonResult = (r) => {
  placeMarker(r.lat, r.lon);
  const p = r.props || {};
  const parts = [p.name, p.street, p.city, p.state, p.country].filter(Boolean);
  lokasi.value = parts.length ? parts.join(", ") : r.label || `${r.lat.toFixed(6)}, ${r.lon.toFixed(6)}`;
  photonResults.value = [];
  photonQuery.value = "";
  showMap.value = false;
  setTimeout(() => mapInstance && mapInstance.invalidateSize && mapInstance.invalidateSize(), 100);
};

// --- Auto-fill email ---
const storedUser = localStorage.getItem('user');
let user = storedUser ? JSON.parse(storedUser) : null;
if (user && user.email) email.value = user.email;

// --- Submit ---
const tanganiForm = async () => {
  try {
    if (!user) {
      alert('Silakan login terlebih dahulu.');
      router.push('/login');
      return;
    }
    const token = localStorage.getItem('token');
    const formData = new FormData();
    formData.append('description', description.value);
    formData.append('lokasi', lokasi.value);
    if (picture.value) formData.append('picture', picture.value);

    await api.post('/api/reports/', formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
        Authorization: token ? `Bearer ${token}` : '',
      },
    });

    alert('Laporan berhasil dikirim, menunggu verifikasi!');
    router.push('/');
  } catch (error) {
    console.error('Gagal mengirim laporan:', error);
    alert('Pengiriman gagal: ' + (error.response?.data?.error || error.message));
  }
};
</script>

<template>
  <div class="min-h-screen bg-gray-50 font-sans flex flex-col items-center justify-center py-12 px-4">

    <!-- Back to home -->
    <div class="w-full max-w-md mb-5">
      <router-link to="/" class="text-sm font-bold text-primary hover:text-yellow-400 transition-colors">
        ← Kembali ke Beranda
      </router-link>
    </div>

    <!-- Card -->
    <div class="w-full max-w-md bg-white shadow-sm p-8 md:p-10">

      <!-- Progress Bar: 4 segments for 4 data steps -->
      <div class="flex gap-1.5 mb-8">
        <div
          v-for="i in 4"
          :key="i"
          class="h-1 flex-1 transition-all duration-500"
          :class="currentStep >= i ? 'bg-yellow-400' : 'bg-gray-200'"
        ></div>
      </div>

      <!-- ─────────────── STEP 1: Info Pelapor ─────────────── -->
      <div v-if="currentStep === 1">
        <p class="text-xs font-bold uppercase tracking-[3px] text-yellow-400 mb-2">Langkah 1 dari 4</p>
        <h1 class="text-2xl font-extrabold text-primary mb-1">Formulir Pengaduan</h1>
        <p class="text-sm text-gray-400 mb-8">Masukkan email akun Anda sebagai identitas pelapor.</p>

        <div>
          <label class="block text-xs font-bold uppercase tracking-widest text-gray-500 mb-2">Email</label>
          <input
            type="email"
            v-model="email"
            placeholder="contoh@email.com"
            class="w-full px-4 py-3 border border-gray-200 bg-gray-50 text-primary text-sm focus:outline-none focus:ring-2 focus:ring-yellow-400 focus:bg-white transition-all"
          />
        </div>

        <button
          @click="nextStep"
          :disabled="!email.trim()"
          class="mt-8 w-full bg-yellow-400 text-primary font-extrabold py-3.5 text-sm hover:bg-yellow-500 transition-colors disabled:opacity-40 disabled:cursor-not-allowed"
        >
          Lanjut
        </button>
      </div>

      <!-- ─────────────── STEP 2: Deskripsi ─────────────── -->
      <div v-if="currentStep === 2">
        <p class="text-xs font-bold uppercase tracking-[3px] text-yellow-400 mb-2">Langkah 2 dari 4</p>
        <h1 class="text-2xl font-extrabold text-primary mb-1">Detail Kerusakan</h1>
        <p class="text-sm text-gray-400 mb-8">Jelaskan kondisi kerusakan infrastruktur yang Anda temukan.</p>

        <div>
          <label class="block text-xs font-bold uppercase tracking-widest text-gray-500 mb-2">Deskripsi</label>
          <textarea
            v-model="description"
            placeholder="Contoh: Jalan berlubang dengan diameter sekitar 50cm, sudah ada sejak 2 bulan lalu dan berbahaya bagi pengendara..."
            rows="5"
            class="w-full px-4 py-3 border border-gray-200 bg-gray-50 text-primary text-sm focus:outline-none focus:ring-2 focus:ring-yellow-400 focus:bg-white transition-all resize-none"
          ></textarea>
        </div>

        <div class="flex gap-3 mt-8">
          <button
            @click="prevStep"
            class="flex-1 border border-gray-200 text-primary font-bold py-3.5 text-sm hover:bg-gray-50 transition-colors"
          >
            Kembali
          </button>
          <button
            @click="nextStep"
            :disabled="!description.trim()"
            class="flex-[2] bg-yellow-400 text-primary font-extrabold py-3.5 text-sm hover:bg-yellow-500 transition-colors disabled:opacity-40 disabled:cursor-not-allowed"
          >
            Lanjut
          </button>
        </div>
      </div>

      <!-- ─────────────── STEP 3: Lokasi ─────────────── -->
      <div v-if="currentStep === 3">
        <p class="text-xs font-bold uppercase tracking-[3px] text-yellow-400 mb-2">Langkah 3 dari 4</p>
        <h1 class="text-2xl font-extrabold text-primary mb-1">Lokasi Kerusakan</h1>
        <p class="text-sm text-gray-400 mb-8">Ketik alamat secara manual atau gunakan peta interaktif.</p>

        <div>
          <label class="block text-xs font-bold uppercase tracking-widest text-gray-500 mb-2">Lokasi</label>
          <input
            type="text"
            v-model="lokasi"
            placeholder="Ketik alamat..."
            class="w-full px-4 py-3 border border-gray-200 bg-gray-50 text-primary text-sm focus:outline-none focus:ring-2 focus:ring-yellow-400 focus:bg-white transition-all mb-2"
          />
          <button
            type="button"
            @click="openMap"
            class="w-full py-3 border border-gray-200 text-primary text-sm font-bold hover:bg-gray-50 hover:border-yellow-400 transition-colors flex items-center justify-center gap-2"
          >
            <svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" d="M9 20l-5.447-2.724A1 1 0 013 16.382V5.618a1 1 0 011.447-.894L9 7m0 13l6-3m-6 3V7m6 10l4.553 2.276A1 1 0 0021 18.382V7.618a1 1 0 00-.553-.894L15 4m0 13V4m0 0L9 7" />
            </svg>
            Pilih di Peta
          </button>
          <p v-if="lokasi" class="text-xs text-gray-400 mt-2 truncate">Dipilih: {{ lokasi }}</p>
        </div>

        <div class="flex gap-3 mt-8">
          <button
            @click="prevStep"
            class="flex-1 border border-gray-200 text-primary font-bold py-3.5 text-sm hover:bg-gray-50 transition-colors"
          >
            Kembali
          </button>
          <button
            @click="nextStep"
            :disabled="!lokasi.trim()"
            class="flex-[2] bg-yellow-400 text-primary font-extrabold py-3.5 text-sm hover:bg-yellow-500 transition-colors disabled:opacity-40 disabled:cursor-not-allowed"
          >
            Lanjut
          </button>
        </div>
      </div>

      <!-- ─────────────── STEP 4: Foto Bukti ─────────────── -->
      <div v-if="currentStep === 4">
        <p class="text-xs font-bold uppercase tracking-[3px] text-yellow-400 mb-2">Langkah 4 dari 4</p>
        <h1 class="text-2xl font-extrabold text-primary mb-1">Foto Bukti</h1>
        <p class="text-sm text-gray-400 mb-8">Unggah foto kerusakan sebagai bukti laporan Anda.</p>

        <label for="foto-input" class="block cursor-pointer">
          <div
            class="border-2 border-dashed border-gray-200 p-8 text-center hover:border-yellow-400 transition-colors"
            :class="picturePreview ? 'border-yellow-400' : ''"
          >
            <div v-if="!picturePreview" class="flex flex-col items-center">
              <div class="w-14 h-14 border-2 border-gray-200 flex items-center justify-center mb-3">
                <svg class="w-7 h-7 text-gray-300" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" d="M2.25 15.75l5.159-5.159a2.25 2.25 0 013.182 0l5.159 5.159m-1.5-1.5l1.409-1.409a2.25 2.25 0 013.182 0l2.909 2.909M3 20.25h18M16.5 3.75a.75.75 0 01.75.75v7.5a.75.75 0 01-.75.75h-9a.75.75 0 01-.75-.75v-7.5a.75.75 0 01.75-.75h9z" />
                </svg>
              </div>
              <p class="text-sm font-bold text-gray-400">Masukkan Foto</p>
              <p class="text-xs text-gray-300 mt-1">JPG, PNG, atau WEBP</p>
            </div>
            <div v-else class="flex flex-col items-center">
              <img :src="picturePreview" alt="Preview foto" class="max-h-48 w-full object-contain mb-3" />
              <p class="text-xs text-yellow-500 font-bold">Klik untuk ganti foto</p>
            </div>
          </div>
        </label>
        <input id="foto-input" type="file" accept="image/*" @change="onFileChange" class="hidden" />

        <div class="flex gap-3 mt-8">
          <button
            @click="prevStep"
            class="flex-1 border border-gray-200 text-primary font-bold py-3.5 text-sm hover:bg-gray-50 transition-colors"
          >
            Kembali
          </button>
          <button
            @click="nextStep"
            :disabled="!picture"
            class="flex-[2] bg-yellow-400 text-primary font-extrabold py-3.5 text-sm hover:bg-yellow-500 transition-colors disabled:opacity-40 disabled:cursor-not-allowed"
          >
            Lanjut
          </button>
        </div>
      </div>

      <!-- ─────────────── STEP 5: Konfirmasi ─────────────── -->
      <div v-if="currentStep === 5">

        <!-- Icon -->
        <div class="flex justify-center mb-6">
          <div class="w-16 h-16 bg-yellow-400 flex items-center justify-center">
            <svg class="w-8 h-8 text-primary" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" d="M11.48 3.499a.562.562 0 011.04 0l2.125 5.111a.563.563 0 00.475.345l5.518.442c.499.04.701.663.321.988l-4.204 3.602a.563.563 0 00-.182.557l1.285 5.385a.562.562 0 01-.84.61l-4.725-2.885a.563.563 0 00-.586 0L6.982 20.54a.562.562 0 01-.84-.61l1.285-5.386a.562.562 0 00-.182-.557l-4.204-3.602a.562.562 0 01.321-.988l5.518-.442a.563.563 0 00.475-.345L11.48 3.5z" />
            </svg>
          </div>
        </div>

        <h1 class="text-2xl font-extrabold text-primary mb-1 text-center">Konfirmasi Laporan</h1>
        <p class="text-sm text-gray-400 mb-8 text-center">
          Dengan menekan tombol di bawah, laporan Anda akan dikirimkan dan menunggu verifikasi dari tim kami.
        </p>

        <!-- Summary -->
        <div class="bg-gray-50 border border-gray-100 p-5 space-y-4">
          <div>
            <p class="text-xs font-bold uppercase tracking-widest text-gray-400">Email Pelapor</p>
            <p class="text-sm text-primary font-medium mt-0.5">{{ email }}</p>
          </div>
          <div>
            <p class="text-xs font-bold uppercase tracking-widest text-gray-400">Deskripsi</p>
            <p class="text-sm text-primary font-medium mt-0.5 line-clamp-3">{{ description }}</p>
          </div>
          <div>
            <p class="text-xs font-bold uppercase tracking-widest text-gray-400">Lokasi</p>
            <p class="text-sm text-primary font-medium mt-0.5">{{ lokasi }}</p>
          </div>
          <div v-if="picturePreview">
            <p class="text-xs font-bold uppercase tracking-widest text-gray-400 mb-1.5">Foto Bukti</p>
            <img :src="picturePreview" alt="Foto bukti" class="h-24 object-cover" />
          </div>
        </div>

        <div class="flex gap-3 mt-8">
          <button
            @click="prevStep"
            class="flex-1 border border-gray-200 text-primary font-bold py-3.5 text-sm hover:bg-gray-50 transition-colors"
          >
            Kembali
          </button>
          <button
            @click="tanganiForm"
            class="flex-[2] bg-yellow-400 text-primary font-extrabold py-3.5 text-sm hover:bg-yellow-500 transition-colors"
          >
            Kirim Laporan
          </button>
        </div>
      </div>

    </div>

    <!-- ─────────────── MAP MODAL ─────────────── -->
    <div v-show="showMap" class="fixed inset-0 z-50 flex items-center justify-center bg-black/40">
      <div class="bg-white w-[90%] md:w-2/3 max-w-3xl p-4">
        <div class="flex items-center justify-between mb-3">
          <div class="flex gap-2">
            <input
              v-model="photonQuery"
              @keydown.enter.prevent="searchPhoton"
              placeholder="Cari alamat atau tempat..."
              class="px-3 py-2 border border-gray-200 text-sm w-72 focus:outline-none focus:ring-2 focus:ring-yellow-400"
            />
            <button @click="searchPhoton" class="px-4 py-2 bg-yellow-400 text-primary font-bold text-sm hover:bg-yellow-500 transition-colors">
              Cari
            </button>
          </div>
          <button @click="showMap = false" class="text-sm font-bold text-gray-400 hover:text-primary transition-colors px-2 py-1">
            Tutup ✕
          </button>
        </div>
        <div class="flex gap-4">
          <div class="flex-1">
            <div id="photon-map" style="height: 400px;"></div>
          </div>
          <div class="w-60 overflow-auto max-h-[400px] border-l border-gray-100">
            <ul>
              <li
                v-for="r in photonResults"
                :key="r.lat + '-' + r.lon"
                class="p-3 border-b border-gray-50 text-sm text-primary hover:bg-gray-50 cursor-pointer transition-colors"
                @click="selectPhotonResult(r)"
              >
                {{ r.label }}
              </li>
            </ul>
            <p v-if="!photonResults.length" class="text-xs text-gray-300 p-4 text-center leading-relaxed">
              Cari alamat di atas atau klik langsung pada peta untuk memilih lokasi.
            </p>
          </div>
        </div>
      </div>
    </div>

  </div>
</template>
