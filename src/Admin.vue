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
      <h1>Daftar Pengguna</h1>
      
      <!-- Tabel Data -->
      <table class="data-table">
        <thead>
          <tr>
            <th>ID</th>
            <th>Email</th>
            <th>Nama Lengkap</th>
            <th>Role</th>
          </tr>
        </thead>
        <tbody>
          <!-- Perulangan v-for untuk mencetak baris sebanyak jumlah data -->
          <tr v-for="user in daftarUser" :key="user.id">
            <td>{{ user.id }}</td>
            <td>{{ user.email }}</td>
            <td>{{ user.namaLengkap }}</td>
            <td>{{ user.role }}</td>
          </tr>
        </tbody>
      </table>
      
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { lihatSemuaUser } from './dataconnect-generated'; // Sesuaikan titik jalurnya jika perlu
import { useRouter } from 'vue-router';

const router = useRouter();
const daftarUser = ref([]);

const ambilData = async () => {
  try {
    const respon = await lihatSemuaUser();
    daftarUser.value = respon.data.profiles; 

    console.log("Data pengguna berhasil diambil:", daftarUser.value);
  } catch (error) {
    console.error("Gagal mengambil data pengguna:", error);
  }
};


// 4. Jalankan fungsi penarikan data tepat saat halaman web pertama kali terbuka
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