<template>
  <div class="admin-container">
    <!-- Sidebar -->
    <div class="sidebar">
      <h2>Ruang Kendali</h2>
      <ul>
        <li>Data Pengguna</li>
        <li>Data Pengaduan</li>
      </ul>
    </div>
    
    <!-- Area Utama -->
    <div class="content">
      <h1>Daftar Laporan</h1>

      <div v-if="loading" class="py-8">Memuat data...</div>

      <div v-else>
        <div v-if="unauthorized" class="p-6 bg-yellow-50 border-l-4 border-yellow-400 text-yellow-700">
          <p>{{ unauthMessage }}</p>
          <div class="mt-4">
            <button v-if="unauthMessage.includes('login')" @click="router.push('/login')" class="px-3 py-2 bg-yellow-400 rounded font-bold">Ke Halaman Masuk</button>
          </div>
        </div>

        <table v-else class="data-table">
          <thead>
            <tr>
              <th>ID</th>
              <th>Pelapor</th>
              <th>Deskripsi</th>
              <th>Status</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="lap in daftarLaporan" :key="lap.id">
              <td>{{ lap.id }}</td>
              <td>{{ lap.author_name || lap.profile_id }}</td>
              <td>{{ lap.description }}</td>
              <td>{{ lap.status }}</td>
            </tr>
          </tbody>
        </table>
      </div>
      
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import api from './api.js';
import { useRouter } from 'vue-router';

const router = useRouter();
const daftarLaporan = ref([]);
const loading = ref(true);
const unauthorized = ref(false);
const unauthMessage = ref('');

const ambilData = async () => {
  loading.value = true;
  try {
    const token = localStorage.getItem('token');
    const res = await api.get('/api/admin/reports', {
      headers: {
        Authorization: token ? `Bearer ${token}` : ''
      }
    });
    daftarLaporan.value = res.data.reports || [];
    unauthorized.value = false;
    unauthMessage.value = '';
    console.log('Data laporan berhasil diambil:', daftarLaporan.value);
  } catch (error) {
    console.error('Gagal mengambil data laporan:', error);
    const status = error.response?.status;
    if (status === 401) {
      unauthorized.value = true;
      unauthMessage.value = 'Anda belum masuk. Silakan login untuk mengakses dashboard admin.';
    } else if (status === 403) {
      unauthorized.value = true;
      unauthMessage.value = 'Anda tidak memiliki wewenang untuk mengakses dashboard ini.';
    } else {
      unauthorized.value = true;
      unauthMessage.value = 'Gagal memuat data. Silakan coba lagi nanti.';
    }
  } finally {
    loading.value = false;
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
  background-color: #2c3e50;
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
  border-bottom: 1px solid #3d566e;
  cursor: pointer;
}

.sidebar li:hover {
  color: #f1c40f;
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
  border-collapse: collapse;
  background-color: white;
  margin-top: 20px;
  box-shadow: 0 1px 4px rgba(0,0,0,0.1);
}

.data-table th, .data-table td {
  padding: 15px;
  border: 1px solid #e0e0e0;
  text-align: left;
}

.data-table th {
  background-color: #f1c40f; /* Warna kuning khas FixinIT */
  color: #333;
  font-weight: bold;
}

.data-table tr:hover {
  background-color: #f9f9f9;
}
</style>