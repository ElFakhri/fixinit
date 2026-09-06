<template>
  <div class="admin-container">
    <!-- Sidebar -->
    <div class="sidebar">
      <div>
        <div
          class="text-5xl font-extrabold tracking-tighter text-primary mb-6 p-2"
        >
          <span>Fixin</span><span class="text-white drop-shadow-md">IT</span>
          <p class="text-xl font-bold">Ruang Kendali</p>
        </div>
      </div>
      <ul>
        <li><router-link to="/Admin_users" class="block w-full">Data Pengguna</router-link></li>
        <li><router-link to="/Admin" class="block w-full">Data Pengaduan</router-link></li>
      </ul>
    </div>

    <!-- Area Utama -->
    <div class="content">
      <h1 class="text-4xl font-bold text-gray-800 mb-8 mt-4">Daftar Laporan</h1>

      <div v-if="loading" class="py-8">Memuat data...</div>

      <div v-else>
        <div
          v-if="unauthorized"
          class="p-6 bg-yellow-50 border-l-4 border-yellow-400 text-yellow-700"
        >
          <p>{{ unauthMessage }}</p>
          <div class="mt-4">
            <button
              v-if="unauthMessage.includes('login')"
              @click="router.push('/login')"
              class="px-3 py-2 bg-yellow-400 rounded font-bold"
            >
              Ke Halaman Masuk
            </button>
          </div>
        </div>
        <div v-else class="py-8 flex flex-row gap-8">
          <div
            class="border-none border-gray-500 rounded-lg p-4 shadow-sm w-1/4"
          >
            <p class="text-2xl font-semibold">{{ semuaLaporan.length }}</p>
            <p>Laporan Ditemukan</p>
          </div>
          <div
            class="border-none border-gray-500 rounded-lg p-4 shadow-sm w-1/4"
          >
            <p class="text-2xl font-semibold">
              {{
                semuaLaporan.filter((lap) => normalizeStatus(lap.status) === "pending").length
              }}
            </p>
            <p>Laporan Pending</p>
          </div>
          <div
            class="border-none border-gray-500 rounded-lg p-4 shadow-sm w-1/4"
          >
            <p class="text-2xl font-semibold">
              {{ semuaLaporan.filter((lap) => normalizeStatus(lap.status) === "validated").length }}
            </p>
            <p>Laporan Tervalidasi</p>
          </div>

          <div
            class="border-none border-gray-500 rounded-lg p-4 shadow-sm w-1/4"
          >
            <p class="text-2xl font-semibold">
              {{
                semuaLaporan.filter((lap) => normalizeStatus(lap.status) === "rejected").length
              }}
            </p>
            <p>Laporan Ditolak</p>
          </div>
        </div>
        <router-link
          to="/Admin"
          class="px-4 py-2 bg-amber-400 text-white rounded hover:bg-amber-500 mt-4 inline-block"
        >
          Lihat Semua Laporan
        </router-link>
        <router-link
          to="/Admin_selesai"
          class="px-4 py-2 bg-amber-400 text-white rounded hover:bg-amber-500 mt-4 inline-block ml-4"
        >
          Lihat Laporan yang telah Selesai
        </router-link>
        <router-link
          to="/Admin_users"
          class="px-4 py-2 bg-amber-400 text-white rounded hover:bg-amber-500 mt-4 inline-block ml-4"
        >
          Lihat Data Pengguna
        </router-link>

        <table class="data-table">
          <thead>
            <tr>
              <th>ID</th>
              <th>Pelapor</th>
              <th>Deskripsi</th>
              <th>Lokasi</th>
              <th>Gambar</th>
              <th>Tanggal Dibuat</th>
              <th>Status</th>
              <th>Aksi</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="lap in daftarLaporan" :key="lap.id">
              <td>{{ lap.id }}</td>
              <td>{{ lap.author_name || lap.profile_id }}</td>
              <td>{{ lap.description }}</td>
              <td>{{ lap.lokasi }}</td>
              <td>
                <img
                  v-if="lap.pictureUrl"
                  :src="urlGambar(lap.pictureUrl)"
                  :alt="lap.description"
                  class="report-image"
                />
                <span v-else>Tidak ada gambar</span>
              </td>
              <td>{{ formatDate(lap.dibuatPada) }}</td>
              <td>
                <span
                  v-if="normalizeStatus(lap.status) === 'validated'"
                  class="text-green-400 font-bold"
                >
                  Tervalidasi
                </span>
                <span v-else class="text-gray-500 font-bold">-</span>
              </td>
              <td>
                <button
                  @click="hapusLaporan(lap.id)"
                  class="px-3 py-1 bg-red-500 text-white rounded hover:bg-red-600"
                >
                  Hapus
                </button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import api from "./api.js";
import { useRouter } from "vue-router";

const router = useRouter();
const semuaLaporan = ref([]);
const daftarLaporan = ref([]);
const loading = ref(true);
const unauthorized = ref(false);
const unauthMessage = ref("");

const urlGambar = (filename) =>
  `${api.defaults.baseURL}/api/reports/images/${encodeURIComponent(filename)}`;

const normalizeStatus = (status) => {
  const value = String(status || "").trim().toLowerCase();

  if (["validated", "selesai", "done"].includes(value)) return "validated";
  if (["rejected", "ditolak"].includes(value)) return "rejected";
  if (["pending", "proses"].includes(value)) return value === "proses" ? "pending" : value;

  return "pending";
};

const formatDate = (value) => {
  if (!value) return "-";

  const date = new Date(value);
  if (Number.isNaN(date.getTime())) return value;

  return date.toLocaleString("id-ID", {
    day: "2-digit",
    month: "short",
    year: "numeric",
    hour: "2-digit",
    minute: "2-digit",
  });
};

const getAuthHeaders = () => {
  const token = localStorage.getItem("token");
  return {
    Authorization: token ? `Bearer ${token}` : "",
  };
};

const ambilData = async () => {
  loading.value = true;
  try {
    const res = await api.get("/api/admin/reports", {
      headers: getAuthHeaders(),
    });
    semuaLaporan.value = res.data.reports || [];

    daftarLaporan.value = (res.data.reports || []).filter(
      (laporan) => ["validated", "selesai"].includes(normalizeStatus(laporan.status)),
    );
    unauthorized.value = false;
    unauthMessage.value = "";
    console.log("Data laporan berhasil diambil:", daftarLaporan.value);
  } catch (error) {
    console.error("Gagal mengambil data laporan:", error);
    const status = error.response?.status;
    if (status === 401) {
      unauthorized.value = true;
      unauthMessage.value =
        "Anda belum masuk. Silakan login untuk mengakses dashboard admin.";
    } else if (status === 403) {
      unauthorized.value = true;
      unauthMessage.value =
        "Anda tidak memiliki wewenang untuk mengakses dashboard ini.";
    } else {
      unauthorized.value = true;
      unauthMessage.value = "Gagal memuat data. Silakan coba lagi nanti.";
    }
  } finally {
    loading.value = false;
  }
};

const hapusLaporan = async (reportId) => {
  const confirmed = window.confirm("Apakah Anda yakin ingin menghapus laporan ini?");
  if (!confirmed) return;

  try {
    await api.delete(`/api/admin/reports/${reportId}`, {
      headers: getAuthHeaders(),
    });
    await ambilData();
  } catch (error) {
    console.error("Gagal menghapus laporan:", error);
    alert("Gagal menghapus laporan.");
  }
};

onMounted(() => {
  ambilData();
});
</script>

<style scoped>
/* Reset dasar untuk memastikan layout rapi */
.admin-container {
  display: flex;
  min-height: 100vh;
  font-family: Arial, sans-serif;
}

/* Desain Sidebar Kiri */
.sidebar {
  width: 250px;
  background-color: #fbbf24;
  color: white;
  padding: 20px;
}

.sidebar ul {
  list-style-type: none;
  padding: 0;
  margin-top: 20px;
}

.sidebar li {
  padding: 12px 0;
  border-bottom: 1px solid #ffffff;
  cursor: pointer;
}

.sidebar li:hover {
  color: #f5db71;
}

/* Desain Area Kanan */
.content {
  flex: 1;
  padding: 30px;
  background-color: #f8f9fa;
}

/* Desain Tabel Murni */
.data-table {
  width: 100%;
  background-color: white;
  margin-top: 20px;
  box-shadow: 0 1px 4px rgba(0, 0, 0, 0.1);
  border-collapse: separate;
  border-spacing: 0;
  border-radius: 12px;
  overflow: hidden;
}

.data-table th,
.data-table td {
  padding: 15px;
  border: 1px solid #e0e0e0;
  text-align: left;
}

.data-table th {
  background-color: #fbbf24; /* Warna kuning khas FixinIT */
  color: #ffffff;
  font-weight: bold;
  text-align: center;
}

.data-table tr:hover {
  border-radius: 12px;
  border: none;
  background-color: #f9f9f9;
}

.report-image {
  width: 150px;
  height: 100px;
  max-width: 150px;
  max-height: 100px;
  object-fit: cover;
  border-radius: 8px;
}
</style>
