<script setup>
import { ref, nextTick } from "vue";
import { useRouter } from "vue-router";
import api from './api.js';

// Running in local dev is fine; the Vue app will talk to the Flask API at /api/*

const router = useRouter();
const lokasi = ref("");
const description = ref("");
const picture = ref(null)
const email = ref("");

// Map & Photon integration
const showMap = ref(false);
let mapInstance = null;
let markerInstance = null;
const mapInitialized = ref(false);
const photonQuery = ref("");
const photonResults = ref([]);

const onFileChange = (e) => {
  picture.value = e.target.files && e.target.files[0] ? e.target.files[0] : null;
};

const openMap = async () => {
  showMap.value = true;
  // wait until DOM updates
  await nextTick();
  // if map not initialized, create it. Otherwise, the container was hidden; force a redraw
  if (!mapInitialized.value) {
    initMap();
  } else {
    // allow CSS transition / layout to settle then invalidate
    await new Promise((r) => setTimeout(r, 200));
    if (mapInstance && mapInstance.invalidateSize) {
      mapInstance.invalidateSize(true);
      // if marker exists, center on it, otherwise keep world view
      if (markerInstance) {
        mapInstance.setView(markerInstance.getLatLng(), mapInstance.getZoom());
      }
    }
  }
};

const initMap = () => {
  mapInitialized.value = true;
  // global L is provided by Leaflet script added to index.html
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
    const url = `https://photon.komoot.io/reverse?lat=${lat}&lon=${lon}`;
    const res = await fetch(url);
    const data = await res.json();
    if (data && data.features && data.features.length) {
      const props = data.features[0].properties;
      const name = props.name || "";
      const city = props.city || props.state || "";
      const country = props.country || "";
      lokasi.value = [name, city, country].filter(Boolean).join(", ");
    } else {
      lokasi.value = `${lat.toFixed(6)}, ${lon.toFixed(6)}`;
    }
  } catch (err) {
    console.error("Photon reverse geocode failed", err);
    lokasi.value = `${lat.toFixed(6)}, ${lon.toFixed(6)}`;
  }
};

const searchPhoton = async () => {
  const q = photonQuery.value.trim();
  if (!q) return;
  try {
    const url = `https://photon.komoot.io/api/?q=${encodeURIComponent(q)}&limit=5`;
    const res = await fetch(url);
    const data = await res.json();
    photonResults.value = (data.features || []).map((f) => ({
      label: f.properties.name + (f.properties.city ? (", " + f.properties.city) : ""),
      lat: f.geometry.coordinates[1],
      lon: f.geometry.coordinates[0],
      props: f.properties,
    }));
  } catch (err) {
    console.error("Photon search failed", err);
    photonResults.value = [];
  }
};

const selectPhotonResult = async (r) => {
  placeMarker(r.lat, r.lon);
  // Build a robust label from properties when available
  const p = r.props || {};
  const parts = [];
  if (p.name) parts.push(p.name);
  if (p.street) parts.push(p.street);
  if (p.city) parts.push(p.city);
  if (p.state) parts.push(p.state);
  if (p.country) parts.push(p.country);
  lokasi.value = parts.length ? parts.join(", ") : r.label || `${r.lat.toFixed(6)}, ${r.lon.toFixed(6)}`;
  photonResults.value = [];
  photonQuery.value = "";
  // close modal and ensure map redraw
  showMap.value = false;
  setTimeout(() => mapInstance && mapInstance.invalidateSize && mapInstance.invalidateSize(), 100);
};

// Determine logged-in user (stored during login)
const storedUser = localStorage.getItem('user');
let user = storedUser ? JSON.parse(storedUser) : null;
if (user && user.email) email.value = user.email;

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

    const res = await api.post('/api/reports/', formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
        Authorization: token ? `Bearer ${token}` : ''
      }
    });

    alert('Formulir berhasil dilapor, menunggu verifikasi!');
    router.push('/');
  } catch (error) {
    console.error('Gagal mengirim formulir:', error);
    alert('Pengiriman formulir gagal: ' + (error.response?.data?.error || error.message));
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
            Masukkan Deskripsi, Alamat Lokasi, dan Bukti Foto Anda untuk
            Melengkapi Formulir.
          </p>
        </div>

        <!-- Form -->
        <form @submit.prevent="tanganiForm" class="space-y-6">

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
            <div class="flex gap-2">
              <input
                type="text"
                v-model="lokasi"
                class="flex-1 px-5 py-4 rounded bg-gray-50 border border-gray-200 text-primary focus:bg-white focus:outline-none focus:ring-2 focus:ring-yellow-400 focus:border-transparent transition-all duration-300"
                required
              />
              <button type="button" @click="openMap" class="px-4 py-3 bg-yellow-400 rounded font-bold">Pilih di Peta</button>
            </div>
          </div>
          <div>
            <label
              for="picture"
              class="block text-sm font-bold text-gray-700 mb-2"
              ></label
            >
            <input
              type="file" @change="onFileChange"
              class="w-full px-5 py-4 rounded bg-gray-50 border border-gray-200 text-primary focus:bg-white focus:outline-none focus:ring-2 focus:ring-yellow-400 focus:border-transparent transition-all duration-300"
              required
            />
          </div>

          <!-- Map Modal -->
          <div v-show="showMap" class="fixed inset-0 z-50 flex items-center justify-center bg-black/40">
            <div class="bg-white rounded w-[90%] md:w-2/3 max-w-3xl p-4">
              <div class="flex items-center justify-between mb-2">
                <div class="flex gap-2">
                  <input v-model="photonQuery" @keydown.enter.prevent="searchPhoton" placeholder="Cari alamat atau tempat..." class="px-3 py-2 border rounded w-80" />
                  <button @click="searchPhoton" class="px-3 py-2 bg-yellow-400 rounded font-bold">Cari</button>
                </div>
                <div>
                  <button @click="showMap = false" class="px-3 py-2">Tutup</button>
                </div>
              </div>
              <div class="flex gap-4">
                <div class="flex-1">
                  <div id="photon-map" style="height:400px;"></div>
                </div>
                <div class="w-64 overflow-auto">
                  <ul>
                    <li v-for="r in photonResults" :key="r.lat + '-' + r.lon" class="p-2 border-b hover:bg-gray-50 cursor-pointer" @click="selectPhotonResult(r)">
                      {{ r.label }}
                    </li>
                  </ul>
                </div>
              </div>
            </div>
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
